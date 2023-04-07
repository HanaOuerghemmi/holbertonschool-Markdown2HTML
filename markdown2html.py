"""
markdown
"""
#!/usr/bin/python3

"""
a script markdown2html.py that takes an argument 2 strings:
First argument is the name of the Markdown file
Second argument is the output file name
"""


import sys
import os
import markdown
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

    with open(input_file, 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    with open(output_file, 'w') as f:
        f.write(html)

else:
    sys.exit(0)
