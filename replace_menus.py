import re

with open('/Users/user/Downloads/Arts-landingpage/index.html', 'r') as f:
    index_content = f.read()

with open('/Users/user/Downloads/Arts-landingpage/sports.html', 'r') as f:
    sports_content = f.read()

# Extract nav
nav_pattern = re.compile(r'<nav class="fixed top-0 left-0 right-0 z-50 glass-effect">.*?</nav>', re.DOTALL)
index_nav = nav_pattern.search(index_content).group(0)

# Extract mobile menu
mobile_pattern = re.compile(r'<!-- Mobile Menu -->\s*<div id="mobile-menu".*?</ul>\s*</div>', re.DOTALL)
index_mobile = mobile_pattern.search(index_content).group(0)

# Replace in sports.html
sports_content = nav_pattern.sub(index_nav.replace('\\', '\\\\'), sports_content)
sports_content = mobile_pattern.sub(index_mobile.replace('\\', '\\\\'), sports_content)

with open('/Users/user/Downloads/Arts-landingpage/sports.html', 'w') as f:
    f.write(sports_content)

print("Done")
