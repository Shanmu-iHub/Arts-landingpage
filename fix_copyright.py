import glob
import sys

for file_path in glob.glob("*.html"):
    with open(file_path, 'r') as f:
        content = f.read()

    # The string might have leading whitespace or not. We'll just replace the exact text.
    old_text = "2026 Dr. SNS Rajalakshmi College of Arts and Science. All rights reserved. |"
    new_text = "&copy; 2026 Dr. SNS Rajalakshmi College of Arts and Science. All rights reserved. |"

    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated {file_path}")
    else:
        print(f"No match in {file_path}")

print("Done fixing copyright")
