import re

file_path = "/Users/user/Downloads/Arts Website/index.html"
with open(file_path, "r") as f:
    html_content = f.read()

# Define the new courses based on the image
ug_cs_courses = [
    "BCA", "Full Stack Web Development", "AI and Data Science", "Data Analytics",
    "Data Science & Visualization", "DevOps & Cloud", "Cyber Security",
    "Computer Science (AI, ML & DS) *", "Agentic AI*", "Generative AI*",
    "Information Technology"
]

ug_commerce_courses = [
    "B.Com", "B.Com Professional Accounting", "B.Com (CA)", "B.Com (IT)",
    "B.Com Digital Marketing and Data Mining", "BBA", "BBA (Computer Applications)"
]

ug_specialized_courses = [
    "B.Sc. Costume Design & Fashion", "B.Sc. Psychology"
]

pg_courses = [
    "MBA", "MCA", "M.Sc. Computer Science", "M.Sc. Mathematics", "M.Com",
    "M.Com (CA)", "M.A. English", "Ph.D - CS, Commerce, IT, Management",
    "Ph.D - Tamil, English, Library Science"
]

def generate_card(title, tag, icon, gradient):
    return f"""
            <div class="program-card h-64 flex flex-col p-6 bg-gray-900 rounded-xl group relative border border-gray-800 hover:border-[#b0cb1f] transition duration-300">
                <div class="flex items-start mb-4">
                    <div class="w-12 h-12 {gradient} rounded-xl flex items-center justify-center mr-4 flex-shrink-0">
                        <i class="fas {icon} text-white text-lg"></i>
                    </div>
                    <div class="flex-1 relative">
                        <h4 class="font-semibold text-lg text-white leading-tight">{title}</h4>
                        <p class="text-[#b0cb1f] text-sm mt-1">{tag}</p>
                    </div>
                </div>
                <p class="text-gray-400 text-sm flex-grow mt-2">Specialized curriculum focused on modern industry practices and advanced theoretical concepts.</p>
                <div class="flex justify-start mt-4">
                    <span class="text-xs bg-[#8ca218] px-3 py-1.5 rounded text-white font-medium">3 Years</span>
                </div>
            </div>"""

def generate_pg_card(title, tag, icon, gradient):
    return f"""
            <div class="program-card h-64 flex flex-col p-6 bg-gray-900 rounded-xl group relative border border-gray-800 hover:border-[#b0cb1f] transition duration-300">
                <div class="flex items-start mb-4">
                    <div class="w-12 h-12 {gradient} rounded-xl flex items-center justify-center mr-4 flex-shrink-0">
                        <i class="fas {icon} text-white text-lg"></i>
                    </div>
                    <div class="flex-1 relative">
                        <h4 class="font-semibold text-lg text-white leading-tight">{title}</h4>
                        <p class="text-[#b0cb1f] text-sm mt-1">{tag}</p>
                    </div>
                </div>
                <p class="text-gray-400 text-sm flex-grow mt-2">Advanced studies and research opportunities focusing on specialized knowledge and practical application.</p>
                <div class="flex justify-start mt-4">
                    <span class="text-xs bg-[#8ca218] px-3 py-1.5 rounded text-white font-medium">2 Years / Research</span>
                </div>
            </div>"""

def build_section(title, subtitle, icon, cards_html):
    return f"""
        <div class="mb-16">
            <h3 class="font-display text-4xl font-bold text-center mb-12 text-white">
                <i class="fas {icon} text-[#b0cb1f] mr-4"></i>
                {title} <span class="gradient-text">({subtitle})</span>
            </h3>
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                {cards_html}
            </div>
        </div>"""

# Build HTML
cs_cards = "".join([generate_card(c, "B.Sc. CS", "fa-laptop-code", "tech-gradient") for c in ug_cs_courses])
com_cards = "".join([generate_card(c, "Commerce", "fa-chart-pie", "gradient-bg") for c in ug_commerce_courses])
spec_cards = "".join([generate_card(c, "Specialized", "fa-palette", "dark-gradient") for c in ug_specialized_courses])
pg_cards_html = "".join([generate_pg_card(c, "PG / Ph.D", "fa-microscope", "tech-gradient") for c in pg_courses])

section1 = build_section("B.Sc. Computer Science", "UG Programs", "fa-code", cs_cards)
section2 = build_section("Commerce Programs", "UG Programs", "fa-calculator", com_cards)
section3 = build_section("Specialized B.Sc.", "UG Programs", "fa-star", spec_cards)
section4 = build_section("PG & Research", "Masters & Ph.D", "fa-user-graduate", pg_cards_html)

new_programs_html = section1 + section2 + section3 + section4

# Cut out old programs part 
# The old HTML has an <!-- UG Programs --> and ends with the end of the academic section div.
start_marker = "<!-- UG Programs -->"
end_marker = "<!-- End Academic Programs Section -->" # We will need to locate the end of the sections container.
# In the original HTML snippet, the last section is "<!-- PhD Programs -->" up to line 2500 and ends appropriately. 
# We'll use regex to replace from <!-- UG Programs --> to the closing </section> of Academic Programs.

pattern = re.compile(r"<!-- UG Programs -->.*?</div>\s*</div>\s*</section>", re.DOTALL)
replacement = f"""<!-- UG Programs -->
{new_programs_html}
            </div>
        </section>"""

if pattern.search(html_content):
    new_html = pattern.sub(replacement, html_content)
    with open(file_path, "w") as f:
        f.write(new_html)
    print("Successfully replaced Academic Programs section.")
else:
    print("Could not find the target HTML block to replace.")

