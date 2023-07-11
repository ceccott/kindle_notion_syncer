#! /usr/bin/python3
from kindle_scraper import get_highlights
from query_notion_database import get_pageid_for_title, get_list_of_paragraphs_for_page_with_title, append_items_to_page, create_page
from kindle_parser import parse_clippings

import argparse
import os

email = os.environ.get("AMAZON_EMAIL")
password = os.environ.get("AMAZON_PASSWORD")

parser=argparse.ArgumentParser(
        prog='kindle notion syncer',
        description='syncs kindle highlights and notes to notion',
        )
parser.add_argument('-c', '--clip_file',
                    help='Parse content from provided My Clippings.txt',
                    default= ''
                    )
args = parser.parse_args()

book_highlights = None

if (os.path.exists(args.clip_file)):
    book_highlights = parse_clippings(args.clip_file)
else:
    book_highlights = get_highlights(email, password)

print(book_highlights)

if book_highlights != None:
    for title in book_highlights:
        pageid = get_pageid_for_title(title)
        data = book_highlights[title]
        author = data['author']
        highlights = data['highlights']

        if pageid is None:
            create_page(title, author, highlights)
        else:
            notes = get_list_of_paragraphs_for_page_with_title(title)
            new_notes = []
            for note in highlights:
                if note not in notes:
                    new_notes.append(note)
            append_items_to_page(title, new_notes)
