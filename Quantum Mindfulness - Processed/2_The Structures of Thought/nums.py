import os
import re

def remove_tables_and_descriptions(root_folder):
    table_pattern = re.compile(r'(^\|.*?\|\s*\n)+', re.MULTILINE)
    description_pattern = re.compile(r'^Table:.*\n?', re.MULTILINE)

    for foldername, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".md"):
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Remove table and "Table:" description lines
                content = re.sub(table_pattern, '', content)
                content = re.sub(description_pattern, '', content)

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)

# Replace with your actual folder path
remove_tables_and_descriptions("PATH/TO/YOUR/CHAPTERS")