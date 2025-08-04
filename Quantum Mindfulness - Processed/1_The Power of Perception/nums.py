import os
import re

input_dir = "."  # <-- Replace with your actual folder path

def fix_headers_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix missing space after hash marks
    content = re.sub(r'(^|\n)(#{1,6})([^\s#])', r'\1\2 \3', content)

    # Move inline headers to new line
    content = re.sub(r'([^\n])\s+(#{1,6} .+)', r'\1\n\n\2', content)

    # Ensure blank line before all headers
    content = re.sub(r'([^\n])\n(#{1,6} )', r'\1\n\n\2', content)

    # Ensure blank line between stacked headers (e.g., H2 followed by H3)
    content = re.sub(r'(#{1,6} .+)\n(#{1,6} )', r'\1\n\n\2', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith(".md"):
            fix_headers_in_file(os.path.join(root, filename))