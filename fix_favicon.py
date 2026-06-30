import glob

for file_path in glob.glob("*.html"):
    with open(file_path, 'r') as f:
        content = f.read()
    
    modified = False
    
    if 'href="./Assets/favicon.png"' in content:
        content = content.replace('href="./Assets/favicon.png"', 'href="Dr.SNSRCAS.png"')
        modified = True
        
    if 'href="/favicon.ico"' in content:
        content = content.replace('href="/favicon.ico"', 'href="Dr.SNSRCAS.png"')
        modified = True

    if modified:
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated {file_path}")

print("Done fixing favicon")
