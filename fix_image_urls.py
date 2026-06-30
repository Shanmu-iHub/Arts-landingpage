import sys

file_path = '/Users/user/Downloads/Arts-landingpage/about.html'
with open(file_path, 'r') as f:
    content = f.read()

content = content.replace("snsrcas.snscourseware.org", "snsct.snscourseware.org")

with open(file_path, 'w') as f:
    f.write(content)

print("Done fixing image URLs")
