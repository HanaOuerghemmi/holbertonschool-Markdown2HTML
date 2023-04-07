#!/usr/bin/python3
"""a script markdown2html.py"""

import sys
import os
import markdown

if __name__ == '__main__':
    """a script markdown2html.py"""
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        exit(1)

        with open(input_file, 'r') as f:
            text = f.read()
            html = markdown.markdown(text)

        with open(output_file, 'w') as f:
            f.write(html)
    else:
        sys.exit(0)
