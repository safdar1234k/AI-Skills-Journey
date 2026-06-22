import os
import shutil

file_path = input("Enter the file path: ").strip('"')
if not os.path.isdir(file_path):
    raise SystemExit(f"Path not found: {file_path}")

list_of_files = os.listdir(file_path)
for items in list_of_files:
    source = os.path.join(file_path, items)
    if not os.path.isfile(source):
        continue

    lower = items.lower()
    if lower.endswith('.txt'):
        dest_dir = os.path.join(file_path, "text_files")
    elif lower.endswith('.jpg') or lower.endswith('.jpeg') or lower.endswith('.png'):
        dest_dir = os.path.join(file_path, "images")
    elif lower.endswith('.pdf'):
        dest_dir = os.path.join(file_path, "pdf_files")
    elif lower.endswith('.docx') or lower.endswith('.doc'):
        dest_dir = os.path.join(file_path, "documents")
    elif lower.endswith('.xlsx') or lower.endswith('.xls'):
        dest_dir = os.path.join(file_path, "excel_files")
    else:
        dest_dir = os.path.join(file_path, "Others")

    os.makedirs(dest_dir, exist_ok=True)
    shutil.move(source, dest_dir)

print("Files are organized")