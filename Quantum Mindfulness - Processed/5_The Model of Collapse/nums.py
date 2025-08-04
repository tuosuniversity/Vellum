import os
import re

FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

def update_chapter_numbers(folder_path):
    for filename in os.listdir(folder_path):
        if not filename.endswith(".md"):
            continue

        match = re.match(r"(\d+)_.*\.md$", filename)
        if not match:
            continue

        chapter_num = str(int(match.group(1)))
        filepath = os.path.join(folder_path, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Fix Chapter Heading (e.g. "# Chapter 43:" -> "# Chapter 60:")
        content, chapter_subs = re.subn(
            r"# Chapter\s+\d+\s*:", f"# Chapter {chapter_num}:", content
        )

        # Fix Outline Numbering (e.g. "**43.1:**" -> "**60.1:**")
        content, outline_subs = re.subn(
            r"\*\*(\d+)\.(\d+):\*\*", lambda m: f"**{chapter_num}.{m.group(2)}:**", content
        )

        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"✅ {filename}: Chapter heading and {outline_subs} outline numbers updated.")

if __name__ == "__main__":
    update_chapter_numbers(FOLDER_PATH)