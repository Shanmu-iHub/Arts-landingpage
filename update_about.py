import sys

file_path = '/Users/user/Downloads/Arts-landingpage/about.html'
with open(file_path, 'r') as f:
    content = f.read()

replacements = {
    "SNS College of Technology": "Dr. SNS Rajalakshmi College of Arts and Science",
    "SNSCT": "SNSRCAS",
    "snsct": "snsrcas",
    "Engineering Innovation": "Arts and Science Innovation",
    "Engineering education": "Arts and Science education",
    "AI Engineering": "Arts and Science",
    "engineering college": "arts and science college",
    "Engineering programs": "Arts and Science programs",
    "Engineering admissions": "Arts and Science admissions",
    "best engineering college": "best arts and science college",
    "engineering colleges": "arts and science colleges",
    "list of engineering college": "list of arts and science college",
    "engineering solutions": "arts and science solutions",
    "TNEA 2726": "Autonomous College",
    "TNEA code 2726": "Autonomous College",
    "TNEA Code 2726": "Autonomous College",
    "TNEA Code: 2726": "Autonomous College",
    "TNEA counselling": "counselling",
    "TNEA Admissions": "Admissions",
    "B.Tech": "Undergraduate",
    "B.E.": "Undergraduate",
    "Engineering": "Arts and Science",
    "engineering": "arts and science",
    "Technology.": "Arts and Science.",
    "Technology,": "Arts and Science,",
    "technology,": "arts and science,"
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Fix prompt engineering
content = content.replace("Prompt Arts and Science", "Prompt Engineering")

with open(file_path, 'w') as f:
    f.write(content)

print("Done replacements")
