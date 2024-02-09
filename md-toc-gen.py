#!/usr/bin/env python3

import re

#################################################################################
# This script will generate a contents section for a markdown file
# You can choose the level of header to include
# It will remove the existing contents section before adding a new one
#
# Author: Jupiter Tomahawk with help from ChatGPT
##################################################################################


def generate_toc(file_content, num_levels):
    toc = f"## Table of Contents\n\n"
    headers = re.findall(r'^(#{2,6})\s+(.+)$', file_content, re.MULTILINE)

    for level, header_text in headers:
        # Remove special characters and spaces
        # Keep & character, this is removed after to leave --
        # this is to format the link correctly so it works.

        anchor = re.sub(r'[^a-zA-Z0-9&]+', '-', header_text.lower())
        anchor = anchor.replace('&', '')

        # remove trailing "-" otherwise link won't work
        if anchor.endswith("-"):
            anchor = anchor[:-1]

        # Determine the indentation based on header level
        indentation = " " * ((len(level) - 2) * 2) if len(level) > 2 else ""

        # Check if the header level is within the specified number of levels
        if len(level) - 1 <= num_levels:
            toc += f"{indentation}- [{header_text}](#{anchor})\n"

    return toc


def main():
    filename = input(
        "Enter the name of the Markdown file (including extension): ")
    num_levels = int(
        input("Enter the number of header levels to include in the Table of Contents: "))

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # Find the line '## Table of Contents'
        toc_match = re.search(
            r'^##\s*Table of Contents.*$', content, re.MULTILINE)

        if toc_match:
            replace_toc = input(
                "Table of Contents already exists. Do you want to replace it? (y/n): ").lower()
            if replace_toc == 'y':
                # Find the position of the first empty line after '## Table of Contents'
                toc_start = toc_match.end() + \
                    content[toc_match.end():].find('\n') + 1

                # Iterate over lines after the first empty line after '## Table of Contents'
                iteration = 0
                toc_end = toc_start
                while toc_end < len(content):
                    line = content[toc_end:].split('\n', 1)[0]
                    if iteration > 2:
                        if not line or not line.lstrip().startswith('-'):
                            break
                        # Include the newline character
                        toc_end += len(line) + 1
                    else:
                        # Include the newline character
                        toc_end += len(line) + 1
                        iteration += 1

                # Remove the lines between '## Table of Contents' and the first empty line
                content = content[:toc_match.start()] + content[toc_end + 1:]

        # Find the position after the main header
        main_header_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if main_header_match:
            main_header_end = main_header_match.end()
        else:
            main_header_end = 0

        # Generate TOC
        toc_content = generate_toc(content, num_levels)

        # Append TOC below the main header
        updated_content = content[:main_header_end] + \
            '\n\n' + toc_content + content[main_header_end:]

        # Write the updated content back to the file
        with open(filename, 'w', encoding='utf-8') as updated_file:
            updated_file.write(updated_content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Please enter a valid number for the header levels.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
