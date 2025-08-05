import os
import re

def sanitize_filename(title):
    """
    Sanitizes a string to be a valid filename.
    Strips the words "article" and "articulo" and removes invalid characters.
    """
    # Strip the words "article" and "articulo" from the title, case-insensitively
    filename = re.sub(r'\b(article|articulo)\b', '', title, flags=re.IGNORECASE)
    # Replace spaces with hyphens and clean up extra spaces left by the replacement
    filename = re.sub(r'\s+', '-', filename.strip())
    # Remove any characters that are not alphanumeric, hyphens, or underscores
    filename = re.sub(r'[^a-zA-Z0-9-]', '', filename)
    # Ensure the filename isn't empty
    if not filename:
        return "untitled-article"
    return filename.lower()

def process_markdown_file(file_path, destination_dir):
    """
    Reads a markdown file, splits it into articles based on '### Title',
    and saves each as a new file with the '### Title' as the filename.
    Removes '## ARTICLES', '## Article N', '## Articulo N' headers and any initial intro text.
    """
    print(f"  -> Found file: {os.path.basename(file_path)}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split the content by the `### Title` heading pattern.
    # The first element (index 0) will contain everything before the first '### Title'.
    articles_raw_split = re.split(r'^(### .*)', content, flags=re.MULTILINE)
    
    # If there are no '### Title' headings, or only one with no content, skip.
    if len(articles_raw_split) < 2:
        print("Warning: No '### Title' headings found or insufficient content. Skipping file.")
        return

    # Iterate through the split parts, starting from the first actual title.
    # The first element (articles_raw_split[0]) contains the intro and '## ARTICLES' section, which we want to discard.
    for i in range(1, len(articles_raw_split), 2):
        title_line = articles_raw_split[i].strip()
        
        # Ensure there is content following the title.
        if i + 1 >= len(articles_raw_split):
            print(f"Warning: Title '{title_line}' found at end of file with no content. Skipping.")
            continue
            
        article_content = articles_raw_split[i+1].strip()

        # Remove various article-related headers from the content.
        cleaned_content = re.sub(r'^(## (ARTICLES|Article \d+|Articulo \d+)\n)', '', article_content, flags=re.MULTILINE, count=1).strip()
        
        # Construct the new article content, starting with its title.
        new_file_content = f"{title_line}\n{cleaned_content}"

        # Sanitize the title to create a valid filename
        title_for_filename = title_line.replace('### ', '')
        filename = sanitize_filename(title_for_filename) + '.md'
        
        output_path = os.path.join(destination_dir, filename)
        
        try:
            with open(output_path, 'w', encoding='utf-8') as outfile:
                outfile.write(new_file_content)
            print(f"  -> Saved article: {output_path}")
        except OSError as e:
            print(f"  -> Error saving file {output_path}: {e}")

def main(source_dir, destination_dir):
    """
    Main function to orchestrate the recursive file processing.
    """
    for root, dirs, files in os.walk(source_dir):
        # Calculate the relative path from the source_dir to the current subdirectory
        relative_path = os.path.relpath(root, source_dir)
        
        # Construct the new destination directory path
        current_destination_dir = os.path.join(destination_dir, relative_path)

        # Create the destination directory if it doesn't exist
        if not os.path.exists(current_destination_dir):
            os.makedirs(current_destination_dir)
            print(f"Created destination directory: {current_destination_dir}")

        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_markdown_file(file_path, current_destination_dir)

if __name__ == "__main__":
    # --- CONFIGURATION ---
    # This is the name of the folder that contains your 'EN' and 'ES' directories.
    articles_base_folder_name = 'Output'
    # ---------------------
    
    # The language folders to process
    language_folders = ['EN', 'ES']
    
    print("Starting article splitting script...")
    
    for lang in language_folders:
        # The base path is just the name of the folder, as the script is run from root.
        source_dir = os.path.join(articles_base_folder_name, lang)
        destination_dir = os.path.join(source_dir, 'output_articles')
        
        print(f"\nAttempting to process articles in: {source_dir}")
        if os.path.exists(source_dir):
            main(source_dir, destination_dir)
        else:
            print(f"Warning: The source directory '{source_dir}' does not exist. Skipping.")

    print("\nScript finished.")
    print("New articles have been saved to the 'output_articles' subfolders within each language directory.")
