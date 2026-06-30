import glob
import re

old_str = '''        .floating-chat-container {
            position: fixed;
            bottom: 0.5rem;
            right: 1rem;
            display: flex;
            flex-direction: column-reverse;
            align-items: flex-end;
            z-index: 50;
        }'''

new_str = '''        .floating-chat-container {
            position: fixed;
            bottom: 5.5rem;
            right: 1rem;
            display: flex;
            flex-direction: column-reverse;
            align-items: flex-end;
            z-index: 50;
        }'''

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

