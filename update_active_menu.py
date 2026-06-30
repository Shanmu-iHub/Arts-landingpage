import glob
import re
import os

for file_path in glob.glob("*.html"):
    with open(file_path, 'r') as f:
        content = f.read()

    # Base classes
    active_style = 'style="color: #b0cb1f;"'
    inactive_class = 'text-gray-400 hover:text-[#b0cb1f] transition-colors'

    # Determine which is active
    basename = os.path.basename(file_path)
    
    home_is_active = (basename == 'index.html')
    about_is_active = (basename == 'about.html')
    contact_is_active = (basename == 'contact.html')

    # Fix Home
    # Currently Home might be `style="color: #b0cb1f;"` or `text-[#b0cb1f]`
    home_pattern = re.compile(r'(<a href="index\.html" class="flex flex-col items-center justify-center w-1/5 pb-1)[^>]*>')
    if home_is_active:
        content = home_pattern.sub(rf'\1" {active_style}>', content)
    else:
        content = home_pattern.sub(rf'\1 {inactive_class}">', content)

    # Fix About
    about_pattern = re.compile(r'(<a href="about\.html"\s+class="flex flex-col items-center justify-center w-1/5 pb-1)[^>]*>')
    if about_is_active:
        content = about_pattern.sub(rf'\1" {active_style}>', content)
    else:
        content = about_pattern.sub(rf'\1 {inactive_class}">', content)

    # Fix Contact
    contact_pattern = re.compile(r'(<a href="contact\.html"\s+class="flex flex-col items-center justify-center w-1/5 pb-1)[^>]*>')
    if contact_is_active:
        content = contact_pattern.sub(rf'\1" {active_style}>', content)
    else:
        content = contact_pattern.sub(rf'\1 {inactive_class}">', content)
        
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Updated {file_path}")

