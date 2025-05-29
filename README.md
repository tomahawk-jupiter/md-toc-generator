# Markdown Table of Contents Generator

## `md-toc-gen.py`

Improved version, takes command line arguments.

```bash
python3 md-toc-gen.py --help # get help

# Example:
python3 md-toc-gen.py filename.md --depth 2 --no-overwrite
```

## Old Version: It prompts user for each argument

Run the script in the terminal and it will prompt for:

1. The markdown file name/path.
2. How many levels of headers you want to include in the contents.
3. Whether or not to continue if there is already a 'Table of Contents'. It will delete the original and add the new one.

## How to make it executable from anywhere

1. Add this to the top of the script: `#!/usr/bin/env python3`
2. Make it executable: `chmod +x md-toc-gen.py`

   - or copy it then change the permission if you don't want them both to be executable.

3. Copy it to bin folder: `sudo cp md-toc-gen.py /usr/local/bin`

   - running this command again will overwrite, ie. to update it with any changes.

4. Rename without file extension: `sudo mv /usr/local/bin/md-toc-gen.py /usr/local/bin/md-toc-gen`

   - executable scripts don't usually have file extensions

## New Feature Ideas

### Sort Feature

Include an option that will sort sections into alphabetical (or number) order. With or without creating a TOC.

This would be useful if you have glossary/reference style notes that you've been writing in no particular order and have become unwieldy. Re-ordering would be useful.
