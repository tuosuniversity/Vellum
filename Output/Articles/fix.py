import os
import re
import shutil # For potential backup/moving if needed, not directly used in rename

def sanitize_filename(title_text):
    """
    Sanitizes a string to be used as a valid, human-readable filename.
    Replaces common invalid characters with hyphens or removes them,
    but keeps spaces.
    """
    # Replace colons with hyphens (as per your specific request)
    sanitized_name = title_text.replace(':', ' -')
    
    # Remove other characters that are invalid in Windows/Linux filenames
    # This regex matches any character that is NOT a letter, number, space, hyphen, or dot.
    # We allow spaces because you want human-readable names.
    sanitized_name = re.sub(r'[^\w\s\-\.]', '', sanitized_name)
    
    # Replace multiple spaces with a single space
    sanitized_name = re.sub(r'\s+', ' ', sanitized_name).strip()
    
    return sanitized_name

def rename_markdown_file_from_h3(file_path):
    """
    Reads a Markdown file, extracts the title from the first H3 heading,
    sanitizes it, and renames the file.
    """
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find the first H3 Markdown heading (### Heading).
        # It captures the text of the H3 heading in group(1).
        h3_heading_pattern = re.compile(r'^###\s*(.*)$', re.MULTILINE)
        
        match = h3_heading_pattern.search(content)

        if match:
            extracted_title = match.group(1).strip()
            
            if not extracted_title:
                print(f"  Warning: H3 heading found but is empty in {file_path}. Skipping rename.")
                return

            new_base_name = sanitize_filename(extracted_title)
            
            # Get the directory and current filename components
            directory = os.path.dirname(file_path)
            current_file_name = os.path.basename(file_path)
            
            new_file_name = f"{new_base_name}.md"
            new_file_path = os.path.join(directory, new_file_name)

            if current_file_name == new_file_name:
                print(f"  Filename already matches H3 title: {current_file_name}. Skipping rename.")
                return

            if os.path.exists(new_file_path):
                print(f"  Error: Target filename '{new_file_name}' already exists in {directory}. Skipping rename to prevent overwrite.")
                return

            os.rename(file_path, new_file_path)
            print(f"  Renamed '{current_file_name}' to '{new_file_name}'")

        else:
            print(f"  No H3 heading found in {file_path}. Skipping rename.")

    except Exception as e:
        print(f"  Error processing {file_path}: {e}. Skipping file.")


def process_directory_for_rename(directory_path):
    """
    Walks through a directory and processes all Markdown files for renaming.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found: {directory_path}")
        return

    print(f"\nStarting file renaming based on H3 headings in: {directory_path}")
    for root, _, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith(('.md', '.markdown')):
                file_path = os.path.join(root, file_name)
                rename_markdown_file_from_h3(file_path)
    print("\nFinished renaming all Markdown files.")

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
            process_directory_for_rename(markdown_files_directory)
        else:
            print(f"Error: The specified directory '{markdown_files_directory}' does not exist.")
            print("Please ensure the 'markdown_files_directory' variable in the script is set to your actual folder path.")
    else:
        print("Error: 'markdown_files_directory' variable is not set.")
        print("Please update the script with the correct path to your Markdown files.")