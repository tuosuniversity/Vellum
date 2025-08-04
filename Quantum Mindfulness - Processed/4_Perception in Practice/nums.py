import os
import re

# Set this to the path where your Markdown files are
FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))  # This folder

def update_markdown_chapter_numbers(folder_path):
    for filename in os.listdir(folder_path):
        if not filename.endswith(".md"):
            continue

        match = re.match(r"(\d+)_.*\.md$", filename)
        if not match:
            continue

        chapter_num = str(int(match.group(1)))  # Remove leading zeros like 01 → 1
        filepath = os.path.join(folder_path, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            original_content = file.read()
            content = original_content

        # Replace chapter header (e.g., "# Chapter 40:") with new number
        content, chapter_subs = re.subn(r"(?<=# Chapter )\d+", chapter_num, content)

        # Replace outline numbers (e.g., **40.2:**) to new chapter (e.g., **6.2:**)
        content, outline_subs = re.subn(r"\*\*\d+\.(\d+):\*\*", rf"**{chapter_num}.\1:**", content)

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"✅ {filename}: Updated chapter → {chapter_num}, {chapter_subs} headers, {outline_subs} outlines.")
        else:
            print(f"⚠️  {filename}: No changes made.")

# Auto-run on script start
if __name__ == "__main__":
    update_markdown_chapter_numbers(FOLDER_PATH)