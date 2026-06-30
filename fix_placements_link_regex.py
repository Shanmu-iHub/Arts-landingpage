import glob
import re

pattern = re.compile(r'<!-- Placements -->\s*<a href="[^"]*"\s*target="_blank"\s*class="flex flex-col items-center justify-center w-1/5 pb-1 text-gray-400 hover:text-\[#b0cb1f\] transition-colors">')

replacement = '''<!-- Placements -->
        <a href="https://iipc.snsgroups.com/" target="_blank"
            class="flex flex-col items-center justify-center w-1/5 pb-1 text-gray-400 hover:text-[#b0cb1f] transition-colors">'''

for file_path in glob.glob("*.html"):
    with open(file_path, 'r') as f:
        content = f.read()

    new_content = pattern.sub(replacement, content)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Skipped {file_path}")

