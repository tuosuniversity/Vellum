import os
import re
import yaml

def fix_yaml_front_matter(file_path):
    """
    Reads a Markdown file, fixes YAML front matter by quoting the 'title' field,
    and writes the corrected content back to the file.
    """
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find YAML front matter (between --- lines)
    front_matter_match = re.match(r'---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)

    if not front_matter_match:
        print(f"  No YAML front matter found in {file_path}. Skipping.")
        return

    original_yaml_block_str = front_matter_match.group(1)
    markdown_content = content[front_matter_match.end():]

    corrected_yaml_block_str = original_yaml_block_str
    parsed_yaml = {} # Initialize parsed_yaml outside the try block

    try:
        # Step 1: Attempt to fix the 'title' line in the raw YAML string first
        # This handles cases where unquoted colons prevent initial parsing
        title_line_match = re.search(r'^(title:\s*)(.*)$', original_yaml_block_str, re.MULTILINE)
        if title_line_match:
            key_part = title_line_match.group(1) # "title: "
            value_part = title_line_match.group(2).strip() # "Beyond Meditation: The Ancient Roots..."

            # Check if the value needs quoting (contains colon and is not already quoted)
            if ':' in value_part and \
               not (value_part.startswith("'") and value_part.endswith("'")) and \
               not (value_part.startswith('"') and value_part.endswith('"')):
                
                # Replace the original title line with a quoted one
                corrected_value_part = f'"{value_part}"'
                corrected_yaml_block_str = original_yaml_block_str.replace(
                    f"{key_part}{value_part}",
                    f"{key_part}{corrected_value_part}",
                    1 # Only replace the first occurrence
                )
                print(f"  Pre-quoting title: '{value_part}' -> '{corrected_value_part}'")
            else:
                print(f"  Title line found but does not need pre-quoting: '{value_part}'")
        else:
            print(f"  No 'title' line found in YAML block. Skipping pre-quoting.")

        # Step 2: Now, attempt to parse the (potentially corrected) YAML string
        parsed_yaml = yaml.safe_load(corrected_yaml_block_str)
        
        # Step 3: Re-dump the YAML with corrections (this ensures proper formatting)
        # This also handles any other quoting needs that PyYAML's dump function applies
        final_yaml_block = yaml.dump(parsed_yaml, sort_keys=False, default_flow_style=False, allow_unicode=True)

        # Reconstruct the file content
        new_content = f"---\n{final_yaml_block.strip()}\n---\n{markdown_content}"

        # Write the corrected content back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Successfully updated {file_path}")

    except yaml.YAMLError as e:
        print(f"  Error parsing YAML in {file_path} AFTER pre-quoting: {e}. Skipping file.")
        print(f"  Problematic YAML block:\n---\n{corrected_yaml_block_str}\n---")
    except Exception as e:
        print(f"  An unexpected error occurred with {file_path}: {e}. Skipping file.")


def process_directory(directory_path):
    """
    Walks through a directory and processes all Markdown files.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found: {directory_path}")
        return

    print(f"\nStarting YAML front matter fix for files in: {directory_path}")
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(('.md', '.markdown')):
                file_path = os.path.join(root, file_name)
                fix_yaml_front_matter(file_path)
    print("\nFinished processing all Markdown files.")

# --- How to use the script ---
if __name__ == "__main__":
    # IMPORTANT: You MUST set this variable to the actual path of your Markdown files.
    # A single dot '.' means the current directory where the script is run.
    markdown_files_directory = "." 

    if markdown_files_directory: # Only proceed if the path is set
        if os.path.exists(markdown_files_directory):
            process_directory(markdown_files_directory)
        else:
            print(f"Error: The specified directory '{markdown_files_directory}' does not exist.")
            print("Please ensure the 'markdown_files_directory' variable in the script is set to your actual folder path.")
    else:
        print("Error: 'markdown_files_directory' variable is not set.")
        print("Please update the script with the correct path to your Markdown files.")