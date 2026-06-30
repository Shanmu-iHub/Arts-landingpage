import sys

file_path = '/Users/user/Downloads/Arts-landingpage/about.html'
with open(file_path, 'r') as f:
    content = f.read()

replacements = {
    "Bachelor of Technology": "Bachelor of Arts/Science",
    "SNS_College_of_Technology": "SNS_College_of_Arts_and_Science",
    "#/technology": "#/arts"
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w') as f:
    f.write(content)

print("Done secondary replacements")
