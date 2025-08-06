import os
import re

def fix_yaml_front_matter_pure_text(file_path):
    """
    Reads a Markdown file, fixes YAML front matter using pure text manipulation
    (no PyYAML library), and writes the corrected content back to the file.
    It will:
    1. Replace colons with hyphens in the title.
    2. Quote the title if it contains special characters.
    3. Reformat categories and tags into the 'taxonomy' block.
    4. Rename 'excerpt' to 'post_excerpt'.
    """
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find YAML front matter (between --- lines)
    front_matter_match = re.match(r'---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)

    if not front_matter_match:
        print(f"  No YAML front matter found (or invalid format) in {file_path}. Skipping.")
        return

    original_yaml_block_str = front_matter_match.group(1)
    markdown_content = front_matter_match.group(2) # Rest of the markdown content

    new_yaml_lines = []
    
    # Dictionary to hold parsed data before reformatting
    temp_data = {}
    
    # Regex to parse individual lines of YAML-like key-value pairs
    line_pattern = re.compile(r'^\s*([a-zA-Z0-9_-]+):\s*(.*)$')
    list_item_pattern = re.compile(r'^\s*-\s*(.*)$') # For list items like - item

    current_key = None
    current_list = []

    # First pass: parse the original YAML block into a temp_data dictionary
    for line in original_yaml_block_str.splitlines():
        if line.strip() == '': # Skip empty lines
            continue

        list_match = list_item_pattern.match(line)
        if list_match: # It's a list item
            if current_key:
                current_list.append(list_match.group(1).strip())
            else:
                print(f"  Warning: List item found without a preceding key: '{line}' in {file_path}. Skipping.")
        else: # It's a key-value pair
            key_value_match = line_pattern.match(line)
            if key_value_match:
                key = key_value_match.group(1)
                value = key_value_match.group(2).strip()
                
                if current_key and current_list: # If previous key had list items, save it
                    temp_data[current_key] = current_list
                    current_list = [] # Reset for next list
                
                current_key = key
                if value: # If value is not empty, it's a scalar value
                    temp_data[key] = value
                else: # If value is empty, it might be the start of a list or nested map
                    temp_data[key] = [] # Assume it's a list for now, will be populated by list_match

            else:
                # This handles multi-line string values or malformed lines
                if current_key and isinstance(temp_data.get(current_key), str):
                    temp_data[current_key] += "\n" + line.strip()
                else:
                    print(f"  Warning: Unparseable line in YAML front matter: '{line}' in {file_path}. Skipping.")
    
    # Add any remaining list items
    if current_key and current_list:
        temp_data[current_key] = current_list

    # --- Now, apply transformations based on temp_data ---
    
    # 1. Process 'title': replace colons with hyphens, then quote if needed
    if 'title' in temp_data and isinstance(temp_data['title'], str):
        original_title = temp_data['title']
        processed_title = original_title.replace(':', ' -') # Replace colon with space-hyphen
        
        # Check if the processed title needs quoting (contains special YAML chars, and is not already quoted)
        special_chars = ['[', ']', '{', '}', '#', '&', '*', '!', '|', '>', '<', '%', '@', '`']
        needs_quoting = any(c in processed_title for c in special_chars) and \
                        not (processed_title.startswith("'") and processed_title.endswith("'")) and \
                        not (processed_title.startswith('"') and processed_title.endswith('"'))

        if needs_quoting:
            temp_data['title'] = f'"{processed_title}"'
            print(f"  Title fixed and quoted: '{original_title}' -> '{temp_data['title']}'")
        elif original_title != processed_title: # Only changed colon, no other quoting needed
            temp_data['title'] = processed_title
            print(f"  Title fixed (colon replaced): '{original_title}' -> '{temp_data['title']}'")
        else:
            print(f"  Title found, no changes needed: '{original_title}'")
    else:
        print(f"  No 'title' field or not a string in YAML. Skipping title fix.")

    # 2. Reformat categories and tags into the 'taxonomy' block
    taxonomy_data = {}
    if 'categories' in temp_data:
        current_categories = temp_data.pop('categories')
        if isinstance(current_categories, str):
            taxonomy_data['category'] = [s.strip() for s in current_categories.split(',')]
            print(f"  Converted 'categories' string to list for 'taxonomy: category'.")
        elif isinstance(current_categories, list):
            taxonomy_data['category'] = [str(s).strip() for s in current_categories]
            print(f"  Moved 'categories' list for 'taxonomy: category'.")
        else:
            print(f"  'categories' field has unexpected format. Skipping reformat.")

    if 'tags' in temp_data:
        current_tags = temp_data.pop('tags')
        if isinstance(current_tags, str):
            taxonomy_data['post_tag'] = [s.strip() for s in current_tags.split(',')]
            print(f"  Converted 'tags' string to list for 'taxonomy: post_tag'.")
        elif isinstance(current_tags, list):
            taxonomy_data['post_tag'] = [str(s).strip() for s in current_tags]
            print(f"  Moved 'tags' list for 'taxonomy: post_tag'.")
        else:
            print(f"  'tags' field has unexpected format. Skipping reformat.")
    
    if taxonomy_data:
        temp_data['taxonomy'] = taxonomy_data

    # 3. Rename 'excerpt' to 'post_excerpt'
    if 'excerpt' in temp_data and 'post_excerpt' not in temp_data:
        temp_data['post_excerpt'] = temp_data.pop('excerpt')
        print(f"  Renamed 'excerpt' to 'post_excerpt'.")
    
    # --- Reconstruct the YAML block as a string ---
    final_yaml_lines = []
    for key, value in temp_data.items():
        if key == 'taxonomy' and isinstance(value, dict):
            final_yaml_lines.append(f"taxonomy:")
            for tax_key, tax_value in value.items():
                final_yaml_lines.append(f"    {tax_key}:")
                if isinstance(tax_value, list):
                    for item in tax_value:
                        final_yaml_lines.append(f"        - {item}")
                else: # Should not happen if logic is correct, but for safety
                    final_yaml_lines.append(f"        {tax_value}")
        elif isinstance(value, list): # For other top-level lists if any
            final_yaml_lines.append(f"{key}:")
            for item in value:
                final_yaml_lines.append(f"    - {item}")
        else: # Scalar value (string, number etc.)
            final_yaml_lines.append(f"{key}: {value}")

    final_yaml_block = "\n".join(final_yaml_lines)

    # Reconstruct the file content
    new_content = f"---\n{final_yaml_block.strip()}\n---\n{markdown_content}"

    # Write the corrected content back to the file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  Successfully updated {file_path}")
    except Exception as e:
        print(f"  Error writing to file {file_path}: {e}. File might not be updated.")


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
                fix_yaml_front_matter_pure_text(file_path)
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