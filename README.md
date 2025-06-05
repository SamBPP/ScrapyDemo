# Scrapy Teaching Project: Quote Scraper

This project demonstrates how to use [Scrapy](https://scrapy.org/) to crawl and collect quotes from [http://quotes.toscrape.com](http://quotes.toscrape.com). It includes a functional spider, logging, a simple data pipeline, and the ability to run Scrapy from a standalone Python script.

---

## 📁 Project Structure

```
quotes_scraper/
├── scrapy.cfg
├── run_spider.py
└── quotes_scraper/
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders/
        ├── __init__.py
        └── quotes_spider.py
README.md
requirements.txt
run_spider.py
setup_env.sh
```

---

## 🧪 Requirements

You’ll need Python 3.7+ and `scrapy` installed:

```bash
pip install scrapy
```

---

## ▶️ How to Run the Spider

You can run the spider programmatically using:

```bash
python run_spider.py
```

This will start crawling quotes from the site and print logs in the terminal.

---

## 🕷️ What the Spider Does

Located in `quotes_project/spiders/quotes_spider.py`, the spider:

- Starts at: `http://quotes.toscrape.com`
- Extracts:
  - `text`: The quote text
  - `author`: The person who said it
  - `tags`: Tags for the quote
- Follows pagination links to scrape all pages

### Key Code:

```python
yield {
    'text': quote.css('span.text::text').get(),
    'author': quote.css('span small.author::text').get(),
    'tags': quote.css('div.tags a.tag::text').getall()
}
```

---

## ⚙️ Logging

In `settings.py`, we’ve enabled Scrapy logging:

```python
LOG_LEVEL = "INFO"
```

This shows each request and basic status messages as the spider runs.

---

## 🧼 Pipeline

In `pipelines.py`, a simple pipeline removes any surrounding quote characters:

```python
item['text'] = item['text'].strip('“”')
```

Enabled in `settings.py`:

```python
ITEM_PIPELINES = {
    "quotes_project.pipelines.QuotesProjectPipeline": 300,
}
```

---

## 💡 Teaching Tips

- Try editing the spider to scrape only certain authors.
- Try exporting results using `scrapy crawl quotes -o quotes.json`.
- Modify the pipeline to remove HTML or filter by tag.

---

## 📄 Output

To export scraped data:

```bash
scrapy crawl quotes -o quotes.json
```

Or use the programmatic run and build on it.

---

Happy scraping!