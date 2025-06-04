import json


class QuotesScraperPipeline:
    """Pipeline that stores each scraped item as a JSON line."""

    def open_spider(self, spider):
        self.file = open("quotes.jsonl", "w", encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
