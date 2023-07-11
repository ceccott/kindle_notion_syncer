## What does this app do?

Forked from [lg08/kindle_notion_syncer](https://github.com/lg08/kindle_notion_syncer)

**TLDR:**

It automatically syncs all of the highlights and notes that you make on the kindle app right to a Notion database at any interval of your choosing! It’s completely free, set it up once and never worry about your notes being out of sync again!

### My Clippings Extension
Personal Documents are not currently supported by the kindle online reader app.
Highlights and notes for such non-amazon ebooks can be imported to Notion by supplying the `My Clippings.txt` file found in the kindle `Documents` folder.
Usage of the clippings file extension:
```
./kindle_notion_syncer.py --clip_file <path to My Clippings.txt>
```

## Environment

The following environmental variables should be set in the environment.

* CHROMEDRIVER_PATH
* GOOGLE_CHROME_BIN
* AMAZON_EMAIL
* AMAZON_PASSWORD
* database_ID
* secret_Key





