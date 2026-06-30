import glob

old_link = 'href="https://snsrcas.org/old/Placement_cell.html" target="_blank"'
new_link = 'href="https://iipc.snsgroups.com/" target="_blank"'

for file_path in glob.glob("*.html"):
    with open(file_path, 'r') as f:
        content = f.read()

    new_content = content.replace(old_link, new_link)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Skipped {file_path}")

