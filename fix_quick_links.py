import glob
import re

old_links = r'''<ul class="space-y-3">\s*<li>\s*<a href="#home" class="text-gray-400 hover:text-white transition-colors">Home</a>\s*</li>\s*<li>\s*<a href="#programs"\s*class="text-gray-400 hover:text-white transition-colors">Programs</a>\s*</li>\s*<li>\s*<a href="#innovation"\s*class="text-gray-400 hover:text-white transition-colors">Innovation Ecosystem</a>\s*</li>\s*<li>\s*<a href="https://iipc\.snsgroups\.com/"\s*class="text-gray-400 hover:text-white transition-colors">Placement</a>\s*</li>\s*<li>\s*<a href="#campus-life" class="text-gray-400 hover:text-white transition-colors">Campus\s*Life</a>\s*</li>\s*</ul>'''

new_links = '''<ul class="space-y-3">
                            <li>
                                <a href="index.html#home" class="text-gray-400 hover:text-white transition-colors">Home</a>
                            </li>
                            <li>
                                <a href="index.html#programs"
                                    class="text-gray-400 hover:text-white transition-colors">Programs</a>
                            </li>
                            <li>
                                <a href="index.html#innovation"
                                    class="text-gray-400 hover:text-white transition-colors">Innovation Ecosystem</a>
                            </li>
                            <li>
                                <a href="https://iipc.snsgroups.com/"
                                    class="text-gray-400 hover:text-white transition-colors">Placement</a>
                            </li>
                            <li>
                                <a href="index.html#campus-life" class="text-gray-400 hover:text-white transition-colors">Campus Life</a>
                            </li>
                        </ul>'''

for file_path in glob.glob("*.html"):
    with open(file_path, 'r') as f:
        content = f.read()

    new_content = re.sub(old_links, new_links, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Skipped {file_path} (no match)")

