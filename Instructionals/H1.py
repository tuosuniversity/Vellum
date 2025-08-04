import os
import re

# Path to your folder
folder_path = "."

# Loop through each Markdown file
for filename in os.listdir(folder_path):
    if filename.endswith(".md") and re.match(r"^\d{2}_.+\.md$", filename):
        filepath = os.path.join(folder_path, filename)

        # Extract the clean title from the filename
        basename = os.path.splitext(filename)[0]
        parts = basename.split("_", 1)
        if len(parts) != 2:
            continue
        new_title = parts[1].replace("_", " ")

        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Replace the first H1 with the new title
        for i, line in enumerate(lines):
            if line.strip().startswith("# "):
                lines[i] = f"# {new_title}\n"
                break

        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(lines)

print("H1 headings updated based on filenames.")