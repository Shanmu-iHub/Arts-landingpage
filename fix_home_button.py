import glob
import re

old_str = '''class="flex flex-col items-center justify-center w-1/5 pb-1 text-[#b0cb1f]"'''
new_str = '''class="flex flex-col items-center justify-center w-1/5 pb-1" style="color: #b0cb1f;"'''

for file_path in glob.glob("*.html"):
    with open(file_path, 'r') as f:
        content = f.read()

    new_content = content.replace(old_str, new_str)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Skipped {file_path}")

