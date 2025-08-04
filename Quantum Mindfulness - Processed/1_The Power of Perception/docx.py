import os
import subprocess

def convert_md_to_docx(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                md_path = os.path.join(dirpath, filename)
                docx_path = os.path.splitext(md_path)[0] + ".docx"
                try:
                    subprocess.run(["pandoc", md_path, "-o", docx_path], check=True)
                    print(f"✔ Converted: {md_path} → {docx_path}")
                except subprocess.CalledProcessError as e:
                    print(f"❌ Error converting {md_path}: {e}")

# Set your root directory here
convert_md_to_docx(".")