# Markdown Table of Contents Generator

A nice simple interactive tool to generate a table of contents for your markdown file.

The script will generate the table of contents and add it to the file beneath the main header. You can choose the level of header to include. The toc will be nested accordingly.

Its interactive, it prompts you for options on how you want to generate your TOC.

NOTE: I haven't fully tested or made it work for all use cases. Its primarily for my own personal use for which it works well. I used to manually write a toc for my notes and it was time consuming!

## Usage

Run the script in the terminal and it will prompt for:

1. The markdown file name/path.
2. How many levels of headers you want to include in the contents.
3. Whether or not to continue if there is already a 'Table of Contents'. It will delete the original and add the new one.

## How to make it executable from anywhere

1. Add this to the top of the script: `#!/usr/bin/env python3`
2. Make it executable: `chmod +x md-toc-gen.py`
3. Copy it to bin folder: `sudo cp md-toc-gen.py /usr/local/bin`

   NOTE: running this command again will overwrite, ie. to update it with any changes.

## Author

Jupiter Tomahawk

## Bugs

### Hypen after hash

This `- [$PATH](#-path)` should be `- [$PATH](#path)`. The special character is replaced with `-` but this should be removed when its directly after the `#`.

This means the link won't work if you click it. The toc entry will still be generated.

### Extra empty lines

An extra empty line is added after the TOC. This is a problem if the script is run multiple times, it will add an extra empty line each time.

When I save my md file in vscode it removes the extra space for me.

## New Feature Ideas

### Sort Feature

Include an option that will sort sections into alphabetical (or number) order. With or without creating a TOC.

This would be useful if you have glossary/reference style notes that you've been writing in no particular order and have become unwieldy. Re-ordering would be useful.

### Non-interactive mode with CLI arguments

Make it so it can take command line arguments for the file name, options etc.

So interactive mode doesn't have to be used. This will make it faster to use. Eg:

`md-toc-gen.py [filename] [header-depth] [-f]`

- `-f` for force, ie. overwrite without warning
