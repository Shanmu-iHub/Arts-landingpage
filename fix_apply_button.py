import glob
import re

# We want to find: bg-[#b0cb1f] inside the Mobile Bottom Navigation Apply button
old_str = '''class="absolute bottom-6 flex items-center justify-center bg-[#b0cb1f] w-14 h-14 rounded-full text-white shadow-lg border-4 border-white transform transition hover:scale-105 active:scale-95 z-10"'''
new_str = '''class="absolute bottom-6 flex items-center justify-center w-14 h-14 rounded-full text-white shadow-lg border-4 border-white transform transition hover:scale-105 active:scale-95 z-10" style="background-color: #b0cb1f;"'''

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

