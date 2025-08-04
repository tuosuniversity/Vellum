import os
import traceback
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig, Part

# --- CRITICAL AUTHENTICATION NOTE ---
# Your authentication for local development is handled by running:
# `gcloud auth application-default login`
# in your system terminal, and setting the
# `GOOGLE_CLOUD_QUOTA_PROJECT` environment variable in your run configuration.
# ------------------------------------

# --- Configuration ---
PROJECT_ID = "arched-curve-464100-c9"  # Ensure this is your correct Google Cloud Project ID
LOCATION = "us-central1"               # Ensure this is the correct region for your model
MODEL_NAME = "gemini-2.5-flash"        # Recommended for larger contexts, or "gemini-pro" for smaller.

INPUT_ROOT_FOLDER = "Input/ES"  # TODO: SET THIS, e.g., "input_documents"
OUTPUT_ROOT_FOLDER = "Output/ES"    # TODO: SET THIS, e.g., "processed_documents"
PROMPT_FILENAME = "prompt.txt"                         # File containing your main instructions template
FILE_CONTENT_PLACEHOLDER = "{file_content_placeholder}" # Placeholder in prompt.txt for file content

print("[*] Script started.")
print(f"[*] Using Project ID: {PROJECT_ID}, Location: {LOCATION}, Model: {MODEL_NAME}")
print(f"[*] Input Folder: {INPUT_ROOT_FOLDER}")
print(f"[*] Output Folder: {OUTPUT_ROOT_FOLDER}")
print(f"[*] Instructions Template: {PROMPT_FILENAME}")

# --- Load Main Prompt Instructions (Template) ---
main_prompt_instructions = ""
try:
    with open(PROMPT_FILENAME, "r", encoding="utf-8") as f_prompt_template:
        main_prompt_instructions = f_prompt_template.read()
    if not main_prompt_instructions.strip() or FILE_CONTENT_PLACEHOLDER not in main_prompt_instructions:
        print(f"[ERROR] Prompt instruction file '{PROMPT_FILENAME}' is empty or does not contain the placeholder '{FILE_CONTENT_PLACEHOLDER}'.")
        print(f"[*] Please ensure '{PROMPT_FILENAME}' contains instructions and the exact string '{FILE_CONTENT_PLACEHOLDER}'.")
        exit()

    print(f"[*] Prompt instructions loaded successfully from '{PROMPT_FILENAME}'.")
except FileNotFoundError:
    print(f"[ERROR] Prompt instruction file not found: {PROMPT_FILENAME}")
    print(f"[*] Please create '{PROMPT_FILENAME}' or check the filename.")
    exit()
except IOError as e:
    print(f"[ERROR] Failed to read prompt instruction file '{PROMPT_FILENAME}': {e}")
    exit()
# --- End of Main Prompt Loading ---

# --- Main Processing Logic ---
try:
    # 1. Initialize Vertex AI (once)
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    print(f"[*] Vertex AI initialized successfully.")

    # 2. Define the generation configuration (once)
    generation_config = GenerationConfig(
        temperature=0.7,
        top_p=1.0,
        top_k=32.0,
        # max_output_tokens=4096 # Potentially needed for longer responses
    )

    # 3. Initialize the Generative Model (once)
    print(f"[*] Initializing model: {MODEL_NAME}...")
    model = GenerativeModel(MODEL_NAME)
    print(f"[*] Model {MODEL_NAME} initialized successfully.")

    # --- Create the main output folder if it doesn't exist ---
    if not os.path.exists(OUTPUT_ROOT_FOLDER):
        os.makedirs(OUTPUT_ROOT_FOLDER)
        print(f"[*] Created output root folder: {OUTPUT_ROOT_FOLDER}")

    # --- Iterate through files in the INPUT_ROOT_FOLDER ---
    file_counter = 0
    processed_success_count = 0
    processed_fail_count = 0

    if not os.path.exists(INPUT_ROOT_FOLDER):
        print(f"[ERROR] Input folder '{INPUT_ROOT_FOLDER}' not found. Please create it and place your files there.")
        exit()

    for dirpath, _, filenames in os.walk(INPUT_ROOT_FOLDER):
        for filename in filenames:
            if filename == ".DS_Store":
                print(f"[INFO] Skipping macOS metadata file: {os.path.join(dirpath, filename)}")
                continue

            if not (filename.lower().endswith((".txt", ".md"))):
                print(f"[INFO] Skipping file with unhandled extension: {os.path.join(dirpath, filename)}")
                continue

            input_filepath = os.path.join(dirpath, filename)
            file_counter += 1
            print(f"\n--- Processing file {file_counter}: {input_filepath} ---")

            try:
                with open(input_filepath, "r", encoding="utf-8") as f_input_content:
                    current_file_content = f_input_content.read()

                if not current_file_content.strip():
                    print(f"[INFO] File '{input_filepath}' is empty. Skipping.")
                    continue

                # Prepare the current prompt by injecting the file content
                current_prompt_text = main_prompt_instructions.replace(FILE_CONTENT_PLACEHOLDER, current_file_content)

                print(f"[*] Calling model.generate_content() for '{filename}'...")
                response = model.generate_content(
                    current_prompt_text,
                    generation_config=generation_config
                )
                print(f"[*] model.generate_content() call completed for '{filename}'.")

                generated_text_to_save = None
                if response and response.candidates:
                    first_candidate = response.candidates[0]
                    all_text_parts = []
                    if first_candidate.content and first_candidate.content.parts:
                        for part_object in first_candidate.content.parts:
                            if hasattr(part_object, "text") and part_object.text:
                                all_text_parts.append(part_object.text)

                        if all_text_parts:
                            generated_text_to_save = "".join(all_text_parts)

                            relative_path_from_input_root = os.path.relpath(input_filepath, INPUT_ROOT_FOLDER)
                            output_filepath = os.path.join(OUTPUT_ROOT_FOLDER, relative_path_from_input_root)

                            output_file_dir = os.path.dirname(output_filepath)
                            if not os.path.exists(output_file_dir):
                                os.makedirs(output_file_dir)
                                print(f"[*] Created output subdirectory: {output_file_dir}")

                            try:
                                with open(output_filepath, "w", encoding="utf-8") as f_out:
                                    f_out.write(generated_text_to_save)
                                print(f"[SUCCESS] Output for '{filename}' saved to: {output_filepath}")
                                processed_success_count += 1
                            except IOError as e_save:
                                print(f"[ERROR] Failed to write output to file {output_filepath}: {e_save}")
                                processed_fail_count += 1
                        else:
                            print(f"[INFO] No text found in response parts for '{filename}'.")
                            processed_fail_count += 1
                    else:
                        print(f"[INFO] Response candidate has no content or parts for '{filename}'.")
                        processed_fail_count += 1

                else:
                    if response and hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
                        print(f"[INFO] Response for '{filename}' was blocked. Reason: {response.prompt_feedback.block_reason_message}. Blocked part: {response.prompt_feedback.blocked_part}")
                    else:
                        print(f"[INFO] No response or no candidates received for '{filename}'.")
                    processed_fail_count += 1

            except Exception as e_file_proc:
                print(f"[ERROR] An unexpected error occurred while processing file {input_filepath}: {e_file_proc}")
                traceback.print_exc()
                processed_fail_count += 1


except AttributeError as attr_error:
    print(f"\n[FATAL ERROR] AttributeError occurred: {attr_error}")
    traceback.print_exc()
except Exception as e_global:
    print(f"\n[FATAL ERROR] An unexpected error occurred during global setup or file iteration: {e_global}")
    traceback.print_exc()

print(f"\n[*] Script finished. Total files scanned: {file_counter}.")
print(f"[*] Successfully processed: {processed_success_count}")
print(f"[*] Failed to process: {processed_fail_count}")
