import os
import re
import yaml

def quote_yaml_value(value_str):
    """
    Quotes a string value if it contains special YAML characters or needs to be quoted.
    This is a pre-processing step before parsing with PyYAML.
    """
    if not isinstance(value_str, str):
        return value_str # Return non-string values as is

    # Check for characters that require quoting in YAML, or if it looks like a number/boolean
    # that should be a string, or if it contains a colon (unless it's already quoted).
    # This is a more comprehensive check.
    special_chars_regex = r'[:#\-\[\]{}!|><%@`\'"]'
    
    # Check if it's already quoted
    is_quoted = (value_str.startswith("'") and value_str.endswith("'")) or \
                (value_str.startswith('"') and value_str.endswith('"'))

    # Check if it looks like a boolean or null
    looks_like_boolean_or_null = value_str.lower() in ['true', 'false', 'null', '~']

    # Check if it looks like a number (integer or float)
    looks_like_number = re.fullmatch(r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?', value_str) is not None

    if (re.search(special_chars_regex, value_str) and not is_quoted) or \
       looks_like_boolean_or_null or \
       looks_like_number: # Always quote if it could be misinterpreted as non-string
        
        # Use double quotes, escaping any existing double quotes
        return f'"{value_str.replace('"', '\\"')}"'
    
    return value_str

def fix_yaml_front_matter(file_path):
    """
    Reads a Markdown file, robustly fixes YAML front matter by:
    1. Pre-quoting problematic string values in the raw YAML.
    2. Replacing colons with hyphens in the title.
    3. Reformatting categories and tags into the 'taxonomy' block.
    4. Renaming 'excerpt' to 'post_excerpt'.
    Then writes the corrected content back to the file.
    """
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Robust regex to find YAML front matter (allowing for more flexible whitespace)
    front_matter_match = re.match(r'---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)

    if not front_matter_match:
        print(f"  No YAML front matter found (or invalid format) in {file_path}. Skipping.")
        return

    original_yaml_block_str = front_matter_match.group(1)
    markdown_content = front_matter_match.group(2)

    # --- Step 1: Aggressive Pre-quoting of all simple key-value pairs in the raw YAML string ---
    # This is crucial to prevent yaml.safe_load from failing on initial parse errors.
    pre_quoted_yaml_lines = []
    lines = original_yaml_block_str.splitlines()
    
    key_value_pattern = re.compile(r'^\s*([a-zA-Z0-9_-]+):\s*(.*)$')
    
    for line in lines:
        match = key_value_pattern.match(line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            
            # Apply quoting to the value part
            quoted_value = quote_yaml_value(value)
            pre_quoted_yaml_lines.append(f"{match.group(1)}: {quoted_value}")
            if quoted_value != value:
                print(f"  Pre-quoted line: '{line}' -> '{match.group(1)}: {quoted_value}'")
        else:
            pre_quoted_yaml_lines.append(line) # Add original line if not a simple key-value pair

    pre_fixed_yaml_block_str = "\n".join(pre_quoted_yaml_lines)

    # --- Step 2: Now, attempt to parse the (aggressively pre-quoted) YAML string ---
    parsed_yaml = {}
    try:
        parsed_yaml = yaml.safe_load(pre_fixed_yaml_block_str)
        if not isinstance(parsed_yaml, dict):
            print(f"  YAML parsed but is not a dictionary in {file_path}. Skipping reformat.")
            return
    except yaml.YAMLError as e:
        print(f"  Error parsing YAML in {file_path} even after aggressive pre-quoting: {e}. Skipping file.")
        print(f"  Problematic YAML block:\n---\n{pre_fixed_yaml_block_str}\n---")
        return
    except Exception as e:
        print(f"  An unexpected error occurred during YAML parsing for {file_path}: {e}. Skipping file.")
        return

    # --- Step 3: Apply transformations to the parsed Python dictionary ---
    
    # 3.1 Process 'title': replace colons with hyphens
    if 'title' in parsed_yaml and isinstance(parsed_yaml['title'], str):
        original_title = parsed_yaml['title']
        if ':' in original_title:
            parsed_yaml['title'] = original_title.replace(':', ' -') # Replace colon with space-hyphen
            print(f"  Replaced colon in title: '{original_title}' -> '{parsed_yaml['title']}'")
    
    # 3.2 Reformat categories and tags into the 'taxonomy' block
    taxonomy_data = {}
    if 'categories' in parsed_yaml:
        current_categories = parsed_yaml.pop('categories')
        if isinstance(current_categories, str):
            taxonomy_data['category'] = [s.strip() for s in current_categories.split(',')]
            print(f"  Converted 'categories' string to list for 'taxonomy: category'.")
        elif isinstance(current_categories, list):
            taxonomy_data['category'] = [str(s).strip() for s in current_categories]
            print(f"  Moved 'categories' list for 'taxonomy: category'.")
        else:
            print(f"  'categories' field has unexpected format ({type(current_categories)}). Skipping reformat.")

    if 'tags' in parsed_yaml:
        current_tags = parsed_yaml.pop('tags')
        if isinstance(current_tags, str):
            taxonomy_data['post_tag'] = [s.strip() for s in current_tags.split(',')]
            print(f"  Converted 'tags' string to list for 'taxonomy: post_tag'.")
        elif isinstance(current_tags, list):
            taxonomy_data['post_tag'] = [str(s).strip() for s in current_tags]
            print(f"  Moved 'tags' list for 'taxonomy: post_tag'.")
        else:
            print(f"  'tags' field has unexpected format ({type(current_tags)}). Skipping reformat.")
    
    if taxonomy_data:
        # Merge new taxonomy data with any existing taxonomy data
        if 'taxonomy' in parsed_yaml and isinstance(parsed_yaml['taxonomy'], dict):
            parsed_yaml['taxonomy'].update(taxonomy_data)
        else:
            parsed_yaml['taxonomy'] = taxonomy_data

    # 3.3 Rename 'excerpt' to 'post_excerpt'
    if 'excerpt' in parsed_yaml and 'post_excerpt' not in parsed_yaml:
        parsed_yaml['post_excerpt'] = parsed_yaml.pop('excerpt')
        print(f"  Renamed 'excerpt' to 'post_excerpt' for {file_path}.")

    # --- Step 4: Re-dump the corrected Python dictionary back to YAML string ---
    # PyYAML's dump function will correctly handle quoting and formatting.
    final_yaml_block = yaml.dump(parsed_yaml, sort_keys=False, default_flow_style=False, allow_unicode=True)

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