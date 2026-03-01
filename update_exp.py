import re
import os

with open('planar.html', 'r', encoding='utf-8') as f:
    planar = f.read()

# Extract the <section class="project-content section"> ... </section> before </main>
match = re.search(r'(<section class="project-content section">.*?</section>)\s*</main>', planar, re.DOTALL)
if match:
    content = match.group(1)
    
    files = ['roboto-ai.html', 'pricol.html', 'crl-purdue.html', 'ta-purdue.html']
    for filename in files:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            # Use a function for replace to avoid processing backslashes in content
            def repl(m):
                return content + "\n    </main>"
                
            new_content = re.sub(r'<section class="project-content section">.*?</section>\s*</main>', repl, file_content, flags=re.DOTALL)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
else:
    print("Could not find section in planar.html")
