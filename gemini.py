import vertexai
from vertexai.generative_models import GenerativeModel, Part

# --- Configuration ---
# Use your actual project ID
PROJECT_ID = "arched-curve-464100-c9"
LOCATION = "us-central1" # Or your desired region

# --- Initialize Vertex AI ---
print(f"Initializing Vertex AI for project: {PROJECT_ID} in location: {LOCATION}")

# Add quota_project_id to explicitly tell Vertex AI which project to use for quotas/billing
vertexai.init(project=PROJECT_ID, location=LOCATION)

# --- Load a Generative Model ---
# You can use "gemini-pro" for text, or "gemini-pro-vision" for multimodal input
model_name = "gemini-2.5-flash"
model = GenerativeModel(model_name)
print(f"Loaded generative model: {model_name}")

# --- Define a prompt ---
prompt = "Tell me a short, inspiring story about a programmer and their first open-source contribution."
print(f"\nSending prompt:\n'{prompt}'\n")

# --- Generate content ---
try:
    response = model.generate_content(prompt)

    # --- Print the response ---
    print("Generated content:")
    print(response.text)

except Exception as e:
    print(f"An error occurred: {e}")
    # Update troubleshooting tips based on latest error
    print("Please check: ")
    print("1. **Vertex AI Gemini API (or Generative Language API)** is enabled in your Google Cloud Project's API Library.")
    print("2. Your project ID and location are correct and match the API region (us-central1 is common for Gemini-pro).")
    print("3. Billing is enabled for your Google Cloud Project.")
    print("4. Your account has the necessary IAM permissions (e.g., Project 'Owner' or 'Vertex AI User').")

