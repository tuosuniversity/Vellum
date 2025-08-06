import os
import re

def remove_front_matter_before_h3(file_path):
    """
    Removes all text from the beginning of the file up to and including
    the first H3 Markdown heading (### Heading).
    This effectively removes YAML front matter and any preceding text.
    Assumes the actual article content starts with an '###' heading.
    """
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the first H3 Markdown heading (### Heading).
    # It captures everything *before* the first H3 heading in group(1)
    # and the H3 heading and everything after it in group(2).
    # We want to keep group(2).
    h3_heading_pattern = re.compile(r'^(.*?)((?:^###\s.*$)(?:[\s\S]*))', re.DOTALL | re.MULTILINE)
    
    match = h3_heading_pattern.match(content)

    if match:
        # new_content starts from the first H3 heading found.
        new_content = match.group(2)
        print(f"  Content trimmed to start from the first '###' heading.")
    else:
        # If no H3 heading is found, it means the file might be just front matter
        # or plain text without a clear H3 heading.
        # In this case, we'll try to remove just the YAML block if it exists,
        # otherwise, the file is unchanged.
        yaml_only_match = re.match(r'---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
        if yaml_only_match:
            new_content = yaml_only_match.group(2) # Keep content after YAML block
            print(f"  Only YAML front matter removed (no '###' heading found).")
        else:
            new_content = content # No front matter or heading found, keep original content
            print(f"  No YAML front matter or '###' heading found. File unchanged.")

    # Write the corrected content back to the file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content.strip()) # .strip() removes leading/trailing whitespace
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

    print(f"\nStarting aggressive front matter removal for files in: {directory_path}")
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(('.md', '.markdown')):
                file_path = os.path.join(root, file_name)
                remove_front_matter_before_h3(file_path)
    print("\nFinished processing all Markdown files.")

# --- How to use the script ---
if __name__ == "__main__":
    # IMPORTANT: You MUST set this variable to the absolute path of the
    # highest-level folder that contains ALL your Markdown files.
    # A single dot '.' means the current directory where the script is run.
    # Use an absolute path for reliability across different execution locations.
    
    # Example for Windows: markdown_files_directory = r"C:\Users\YourUser\Documents\YourRepoName"
    # Example for macOS/Linux: markdown_files_directory = "/home/youruser/your_repo_name"
    
    markdown_files_directory = "." # <--- REPLACE THIS WITH YOUR ABSOLUTE PATH IF NOT RUNNING IN ROOT

    if markdown_files_directory == ".":
        print("Warning: Using '.' as directory. Ensure all target Markdown files are in this directory or its subfolders.")
        print("For best reliability, consider setting an absolute path (e.g., C:\\path\\to\\repo or /home/user/repo).")

    if markdown_files_directory: # Only proceed if the path is set
        if os.path.exists(markdown_files_directory):
            process_directory(markdown_files_directory)
        else:
            print(f"Error: The specified directory '{markdown_files_directory}' does not exist.")
            print("Please ensure the 'markdown_files_directory' variable in the script is set to your actual folder path.")
    else:
        print("Error: 'markdown_files_directory' variable is not set.")
        print("Please update the script with the correct path to your Markdown files.")