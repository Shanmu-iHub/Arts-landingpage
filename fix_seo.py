import glob
import re

new_block = """<title>Dr. SNS Rajalakshmi College of Arts &amp; Science | NAAC A+ | Coimbatore</title>
\t<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="keywords" content="Dr SNS Rajalakshmi College of Arts and Science, DRSNSRCAS, best arts and science college in Coimbatore, NAAC A+ college Coimbatore, autonomous college Coimbatore, B.Sc AI Data Science Coimbatore, BCA college Coimbatore, BBA college Coimbatore, MBA co" />
<meta name="description" content="Dr. SNS Rajalakshmi College of Arts & Science — Autonomous, NAAC A+, NIRF Ranked (101–150). B.Sc, B.Com, BCA, BBA, MBA, MCA with AI, Data Science & Design Thinking curriculum. 9 LPA highest package. Admissions 2026 open. College Code 326. Coimbatore, Tamil Nadu." />"""

for file_path in glob.glob("*.html"):
    with open(file_path, 'r') as f:
        content = f.read()

    head_match = re.search(r'(<head.*?>)(.*?)(</head>)', content, flags=re.DOTALL | re.IGNORECASE)
    if head_match:
        head_start = head_match.group(1)
        head_content = head_match.group(2)
        head_end = head_match.group(3)

        # Remove existing meta tags (keywords, description, content-type)
        head_content = re.sub(r'<meta\s+name=["\'](?:keywords|description)["\'][^>]*>', '', head_content, flags=re.IGNORECASE)
        head_content = re.sub(r'<meta\s+http-equiv=["\']Content-Type["\'][^>]*>', '', head_content, flags=re.IGNORECASE)
        
        # Replace the first title tag with the new block
        head_content = re.sub(r'<title>.*?</title>', new_block, head_content, count=1, flags=re.DOTALL | re.IGNORECASE)

        # Also cleanup some blank lines left by removing the meta tags
        head_content = re.sub(r'\n\s*\n\s*\n', '\n\n', head_content)

        new_head = head_start + head_content + head_end
        content = content[:head_match.start()] + new_head + content[head_match.end():]

        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Updated {file_path}")

print("Done fixing SEO")
