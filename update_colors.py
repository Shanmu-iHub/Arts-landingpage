import re

file_path = "/Users/user/Downloads/Arts Website/index.html"
with open(file_path, "r") as f:
    content = f.read()

# 1. Update CSS Vars
content = re.sub(r"--primary:\s*#[a-fA-F0-9]+", "--primary: #b0cb1f", content)
content = re.sub(r"hsl\(73\.33,\s*53%,", "hsl(69.4, 73.5%,", content)
content = re.sub(r"hsl\(73\.33,\s*20%,", "hsl(69.4, 20%,", content)
content = re.sub(r"165,\s*195,\s*60", "176, 203, 31", content)
content = re.sub(r"--brand-red:\s*#[a-fA-F0-9]+;", "--brand-red: #b0cb1f;", content)
content = re.sub(r"(?i)#a5c33c", "#b0cb1f", content)

# 2. Update the Gradient colors globally
content = re.sub(r"(?i)#dc2626", "#b0cb1f", content)
content = re.sub(r"(?i)#b91c1c", "#8ca218", content)
content = re.sub(r"(?i)#ef4444", "#c2d645", content)
content = re.sub(r"(?i)#f87171", "#d4e375", content)
content = re.sub(r"(?i)#7f1d1d", "#6a7b11", content)
content = re.sub(r"(?i)#991b1b", "#7b8f14", content)

# 3. Inject Tailwind overrides into </head>
tailwind_overrides = """
  <style>
    /* Theme Overrides to #b0cb1f entirely */
    .text-red-300, .text-red-400, .text-red-500, .text-red-600, .text-red-700, .text-red-800, .text-orange-400 { color: #b0cb1f !important; }
    .bg-red-500, .bg-red-600, .bg-red-700 { background-color: #b0cb1f !important; }
    .border-red-500, .border-red-600, .border-red-700 { border-color: #b0cb1f !important; }
    .hover\\:bg-red-500:hover, .hover\\:bg-red-600:hover, .hover\\:bg-red-700:hover { background-color: #8ca218 !important; }
    .hover\\:text-red-300:hover, .hover\\:text-red-400:hover, .hover\\:text-red-500:hover, .hover\\:text-red-600:hover { color: #8ca218 !important; }
  </style>
</head>"""
if "/* Theme Overrides" not in content:
    content = content.replace("</head>", tailwind_overrides)

with open(file_path, "w") as f:
    f.write(content)

print("Modification complete.")
