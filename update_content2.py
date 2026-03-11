import re

file_path = "/Users/user/Downloads/Arts Website/index.html"
with open(file_path, "r") as f:
    html_content = f.read()

# The classes of the provided layout vary slightly per section.
# I will define templates exactly matching the classes found in the updated HTML structure,
# and insert the requested content.

template_ug_trending = '''
                        <div class="program-card h-64 flex flex-col p-6 bg-gray-900 rounded-xl group relative border border-gray-800 hover:border-red-500 transition duration-300">
                            <div class="flex items-start mb-4">
                                <div class="w-12 h-12 {{BG_CLASS}} rounded-xl flex items-center justify-center mr-4 flex-shrink-0">
                                    <i class="{{ICON}} text-white text-lg"></i>
                                </div>
                                <div class="flex-1">
                                    <h4 class="font-semibold text-lg text-white leading-tight">{{TITLE}}</h4>
                                    <p class="text-red-400 text-sm mt-1">{{SUBTITLE}}</p>
                                </div>
                            </div>
                            <p class="text-gray-300 text-sm flex-grow mt-2">{{DESC}}</p>
                            <div class="flex justify-start mt-4">
                                <span class="bg-red-600 px-3 py-1 text-white rounded text-xs font-medium">{{DURATION}}</span>
                            </div>
                        </div>'''

template_pg = '''
                        <div class="program-card h-80 flex flex-col p-6 bg-gray-900 rounded-xl group relative border border-gray-800 hover:border-red-500 transition duration-300">
                            <div class="flex items-start justify-between mb-4">
                                <div class="flex items-start flex-1 min-w-0">
                                    <div class="w-12 h-12 {{BG_CLASS}} rounded-xl flex items-center justify-center mr-4 flex-shrink-0">
                                        <i class="{{ICON}} text-white text-lg"></i>
                                    </div>
                                    <div class="flex-1 min-w-0">
                                        <h4 class="font-semibold text-lg text-white leading-tight">{{TITLE}}</h4>
                                        <p class="text-red-400 text-sm mt-1">{{SUBTITLE}}</p>
                                    </div>
                                </div>
                                <span class="text-xs bg-red-600 px-3 py-1.5 rounded-full text-white font-medium flex-shrink-0 ml-2">{{DURATION}}</span>
                            </div>
                            <p class="text-gray-300 text-sm mb-4 flex-grow mt-2">{{DESC}}</p>
                        </div>'''

programs = {
    "trending": [
        {"title": "Artificial Intelligence and Data Science", "sub": "B.Sc. AIDS", "desc": "Artificial Intelligence, Machine Learning, Deep Learning, Data Structures and Algorithms, Big Data Analytics", "icon": "fas fa-brain", "bg": "tech-gradient", "dur": "3 Years"},
        {"title": "Data Science", "sub": "B.Sc. DS", "desc": "Technology and Big Data, Manufacturing and IoT, Healthcare and Medicine, BFSI, E-commerce and Retail", "icon": "fas fa-chart-network", "bg": "gradient-bg", "dur": "3 Years"},
        {"title": "Data Analytics", "sub": "B.Sc. DA", "desc": "Statistical Analysis, Business Intelligence, Data Visualization, Predictive Analytics, Data Mining", "icon": "fas fa-chart-bar", "bg": "tech-gradient", "dur": "3 Years"},
        {"title": "Full Stack Web Development", "sub": "B.Sc. FSD", "desc": "Frontend Development, Backend Development, Databases, API Development, Cloud Deployment", "icon": "fas fa-laptop-code", "bg": "dark-gradient", "dur": "3 Years"},
        {"title": "DevOps and Cloud Computing", "sub": "B.Sc. DevOps", "desc": "Cloud Infrastructure, CI/CD Pipelines, Containerization, Kubernetes, Cloud Security", "icon": "fas fa-cloud", "bg": "tech-gradient", "dur": "3 Years"},
        {"title": "Cyber Security", "sub": "B.Sc. Cyber Security", "desc": "Ethical Hacking, Network Security, Digital Forensics, Cryptography, Security Operations", "icon": "fas fa-shield-alt", "bg": "gradient-bg", "dur": "3 Years"},
        {"title": "Computer Science (AI, ML & DS)", "sub": "B.Sc. CS (AI, ML & DS)", "desc": "Artificial Intelligence, Machine Learning Models, Neural Networks, Data Engineering, AI Applications", "icon": "fas fa-robot", "bg": "dark-gradient", "dur": "3 Years"},
        {"title": "Agentic AI", "sub": "B.Sc. Agentic AI", "desc": "Autonomous AI Systems, AI Agents, Multi-Agent Systems, Decision Intelligence, AI Automation", "icon": "fas fa-microchip", "bg": "tech-gradient", "dur": "3 Years"},
        {"title": "Generative AI", "sub": "B.Sc. GenAI", "desc": "Large Language Models, Prompt Engineering, AI Content Generation, Multimodal AI, AI Product Development", "icon": "fas fa-wand-magic-sparkles", "bg": "gradient-bg", "dur": "3 Years"}
    ],
    "hot": [
        {"title": "Computer Applications", "sub": "BCA", "desc": "Programming Languages, Software Development, Web Technologies, Mobile Applications, Database Management", "icon": "fas fa-code", "bg": "tech-gradient", "dur": "3 Years"},
        {"title": "Digital Marketing and Data Mining", "sub": "B.Com (Digital Marketing & Data Mining)", "desc": "SEO, Social Media Marketing, Data Mining, Digital Advertising, Marketing Analytics", "icon": "fas fa-bullhorn", "bg": "gradient-bg", "dur": "3 Years"},
        {"title": "Information Technology", "sub": "B.Com (IT)", "desc": "Business Information Systems, Data Management, E-Commerce Technologies, IT Infrastructure", "icon": "fas fa-network-wired", "bg": "dark-gradient", "dur": "3 Years"},
        {"title": "Professional Accounting", "sub": "B.Com (Professional Accounting)", "desc": "Financial Accounting, Corporate Accounting, Taxation, Auditing, Financial Management", "icon": "fas fa-file-invoice-dollar", "bg": "tech-gradient", "dur": "3 Years"},
        {"title": "Business Administration", "sub": "BBA", "desc": "Business Management, Entrepreneurship, Marketing Strategy, Human Resource Management", "icon": "fas fa-briefcase", "bg": "gradient-bg", "dur": "3 Years"},
        {"title": "Business Administration (Computer Applications)", "sub": "BBA (CA)", "desc": "Business Analytics, ERP Systems, IT Management, Business Software Tools", "icon": "fas fa-desktop", "bg": "dark-gradient", "dur": "3 Years"}
    ],
    "evergreen": [
        {"title": "Computer Science", "sub": "B.Sc. Computer Science", "desc": "Programming, Operating Systems, Computer Networks, Database Systems, Software Engineering", "icon": "fas fa-server", "bg": "tech-gradient", "dur": "3 Years"},
        {"title": "Commerce", "sub": "B.Com", "desc": "Accounting Principles, Business Law, Finance, Economics, Business Communication", "icon": "fas fa-chart-pie", "bg": "gradient-bg", "dur": "3 Years"},
        {"title": "Commerce (Computer Applications)", "sub": "B.Com (CA)", "desc": "Accounting Software, Database Applications, Programming Basics, Business Analytics", "icon": "fas fa-calculator", "bg": "tech-gradient", "dur": "3 Years"},
        {"title": "Costume Design and Fashion", "sub": "B.Sc. Costume Design & Fashion", "desc": "Fashion Illustration, Textile Science, Apparel Production, Fashion Merchandising", "icon": "fas fa-tshirt", "bg": "dark-gradient", "dur": "3 Years"},
        {"title": "Psychology", "sub": "B.Sc. Psychology", "desc": "Human Behaviour, Cognitive Psychology, Counseling Techniques, Psychological Research", "icon": "fas fa-brain", "bg": "tech-gradient", "dur": "3 Years"}
    ],
    "pg": [
        {"title": "Master of Business Administration", "sub": "MBA", "desc": "Strategic Management, Marketing, Finance, Business Analytics, Entrepreneurship", "icon": "fas fa-user-tie", "bg": "tech-gradient", "dur": "2 Years"},
        {"title": "Master of Computer Applications", "sub": "MCA", "desc": "Advanced Programming, Cloud Computing, Artificial Intelligence, Software Development", "icon": "fas fa-laptop-code", "bg": "gradient-bg", "dur": "2 Years"},
        {"title": "M.Sc. Computer Science", "sub": "", "desc": "Distributed Systems, Data Science, Machine Learning, Software Architecture", "icon": "fas fa-server", "bg": "dark-gradient", "dur": "2 Years"},
        {"title": "M.Sc. Mathematics", "sub": "", "desc": "Applied Mathematics, Statistical Methods, Computational Mathematics", "icon": "fas fa-square-root-variable", "bg": "tech-gradient", "dur": "2 Years"},
        {"title": "M.Com", "sub": "", "desc": "Advanced Accounting, Corporate Finance, Business Analytics", "icon": "fas fa-chart-pie", "bg": "gradient-bg", "dur": "2 Years"},
        {"title": "M.Com (CA)", "sub": "", "desc": "Accounting Systems, Business Applications, Financial Technology", "icon": "fas fa-calculator", "bg": "dark-gradient", "dur": "2 Years"},
        {"title": "M.A. English", "sub": "", "desc": "Literary Studies, Linguistics, Cultural Studies, Academic Writing", "icon": "fas fa-book", "bg": "tech-gradient", "dur": "2 Years"},
        {"title": "Ph.D – Computer Science, Commerce, IT, Management", "sub": "", "desc": "Research Methodology, Advanced Domain Research, Innovation and Publications", "icon": "fas fa-microscope", "bg": "gradient-bg", "dur": "Research"},
        {"title": "Ph.D – Tamil, English, Library Science", "sub": "", "desc": "Language Research, Literary Analysis, Information Science, Knowledge Management", "icon": "fas fa-microscope", "bg": "tech-gradient", "dur": "Research"}
    ]
}

def generate_section(prog_list, template):
    html = ""
    for prog in prog_list:
        card = template.replace('{{TITLE}}', prog['title'])
        card = card.replace('{{SUBTITLE}}', prog['sub'])
        card = card.replace('{{DESC}}', prog['desc'])
        card = card.replace('{{ICON}}', prog['icon'])
        card = card.replace('{{BG_CLASS}}', prog['bg'])
        card = card.replace('{{DURATION}}', prog['dur'])
        html += card + "\n"
    return html

# Generate the block strings
trending_html = generate_section(programs["trending"], template_ug_trending)
hot_html = generate_section(programs["hot"], template_ug_trending) # Using same layout template
evergreen_html = generate_section(programs["evergreen"], template_ug_trending)
pg_html = generate_section(programs["pg"], template_pg)

# Construct full section replacement
full_programs_html = f'''                <!-- UG Programs -->
                <div class="mb-10">
                    <h3 class="font-display text-4xl font-bold text-center mb-12 text-white">
                        <i class="fas fa-graduation-cap text-red-500 mr-4"></i>
                        9 Undergraduate Programs <span class="gradient-text">(Trending/Unique)</span>
                    </h3>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
{trending_html}
                    </div>
                </div>

                <!-- Hot Programs -->
                <div class="mb-10">
                    <h3 class="font-display text-4xl font-bold text-center mb-12 text-white">
                        <i class="fas fa-fire text-red-500 mr-4"></i>
                        6 Undergraduate Programs <span class="gradient-text">(Hot & Fast Moving)</span>
                    </h3>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
{hot_html}
                    </div>
                </div>

                <!-- Evergreen Programs -->
                <div class="mb-10">
                    <h3 class="font-display text-4xl font-bold text-center mb-12 text-white">
                        <i class="fas fa-leaf text-red-500 mr-4"></i>
                        5 Undergraduate Programs <span class="gradient-text">(Evergreen)</span>
                    </h3>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
{evergreen_html}
                    </div>
                </div>

                <!-- PhD Programs -->
                <div>
                    <h3 class="font-display text-4xl font-bold text-center mb-12 text-white">
                        <i class="fas fa-microscope text-red-500 mr-4"></i>
                        9 Postgraduate Programs<span class="gradient-text"> and</span>
                        Research Programs
                    </h3>
                    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
{pg_html}
                    </div>
                </div>'''

# Replace the block
start_tag = '<!-- UG Programs -->'
end_tag = '</div>\n        </section>\n        <!-- <section'

import re
pattern = re.compile(f"{re.escape(start_tag)}.*?</div>\n            </div>\n        </section>", re.DOTALL)

if "<!-- UG Programs -->" in html_content:
    parts = html_content.split("<!-- UG Programs -->", 1)
    before = parts[0]
    after = parts[1].split('</div>\n        </section>\n        <!-- <section', 1)[1]
    
    new_html = before + full_programs_html + '\n            </div>\n        </section>\n        <!-- <section' + after

    with open(file_path, "w") as f:
        f.write(new_html)
    print("Successfully replaced content.")
else:
    print("Could not find delimiters")
