# Markdown Table of Contents Generator

The script will generate the table of contents and add it to the file beneath the main header. You can choose the level of header to include.

NOTE: I haven't fully tested or made it work for all use cases. Its mainly for my own personal use.

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
