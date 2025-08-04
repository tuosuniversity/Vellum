import os
import re

folder_path = "."  # Adjust if needed
md_files = sorted(f for f in os.listdir(folder_path) if f.endswith(".md"))

def extract_h1(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            match = re.match(r'# (.+)', line.strip())
            if match:
                return match.group(1)
    return None

for index, filename in enumerate(md_files, 1):
    filepath = os.path.join(folder_path, filename)
    h1_title = extract_h1(filepath)
    if not h1_title:
        print(f"Skipping (no H1): {filename}")
        continue

    safe_title = re.sub(r'[^\w\s\-]', '', h1_title).strip().replace(' ', '_')
    number = str(index).zfill(2)
    new_filename = f"{number}_{safe_title}.md"
    new_path = os.path.join(folder_path, new_filename)

    os.rename(filepath, new_path)
    print(f"✔ Renamed: {filename} → {new_filename}")