# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import houses_db


class QuotesJsScraperPipeline:
    def process_item(self, item, spider):
        properties = item["properties"]
        db = houses_db.db_handler()
        db.create_table()
        for i in properties:
            db.insert(i[0], i[1], i[2])
        
        return item
