import re

def parse_clippings(file_path):
    clippings = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into individual clipping entries
    entries = content.strip().split('==========')

    def parse_title_author(book_string):
        pattern = r'^(.*?)\((.*?)\)(?:\s*\((.*?)\))?$'
        match = re.match(pattern, book_string.strip())

        if match:
            title = match.group(1).strip()
            author = match.group(2).strip() if match.group(2) else match.group(3).strip()
            return title, author
        else:
            return book_string, ''

    for entry in entries:
        entry_lines = entry.strip().split('\n')

        if len(entry_lines) >= 3:
            book_title, author = parse_title_author(entry_lines[0].strip())
            metadata = entry_lines[1].strip()
            clipping_text = '\n'.join(entry_lines[3:]).strip()

            if book_title in clippings:
                clippings[book_title]['highlights'].append((clipping_text,'highlight'))
            else:
                clippings[book_title] ={
                     'highlights':[(clipping_text,'highlight')],
                     'author': author
                     }

    return clippings
