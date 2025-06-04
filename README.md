# ScrapyDemo

This project demonstrates a simple Scrapy spider that collects quotes from [quotes.toscrape.com](http://quotes.toscrape.com/).

## Setup

Run the provided script to create a virtual environment and install dependencies:

```bash
./setup_env.sh
```

## Running the spider

Use the helper script to execute the spider and save results to `quotes.jsonl`:

```bash
python run_spider.py
```

The scraped data will be written as JSON lines.

