import glob
import re

old_pattern = r'''<h4 class="font-display font-semibold text-lg mb-6 gradient-text">\s*DIFFERENTIATORS\s*</h4>\s*<ul class="space-y-3">.*?</ul>'''

new_block = '''<h4 class="font-display font-semibold text-lg mb-6 gradient-text">
                            DIFFERENTIATORS
                        </h4>
                        <ul class="space-y-3">
                            <li>
                                <span class="text-gray-400">Design Thinking Based Curriculum</span>
                            </li>
                            <li>
                                <span class="text-gray-400">Center for Learning and Teaching</span>
                            </li>
                            <li>
                                <span class="text-gray-400">Skill and Career Development</span>
                            </li>
                            <li>
                                <span class="text-gray-400">Industry Institute Partnership Cell</span>
                            </li>
                            <li>
                                <span class="text-gray-400">Centre for Creativity</span>
                            </li>
                            <li>
                                <span class="text-gray-400">Social Responsibility Initiative</span>
                            </li>
                        </ul>'''

for file_path in glob.glob("*.html"):
    with open(file_path, 'r') as f:
        content = f.read()

    new_content = re.sub(old_pattern, new_block, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Skipped {file_path} (no match)")
