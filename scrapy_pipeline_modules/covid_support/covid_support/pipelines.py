from itemadapter import ItemAdapter
from .mongodb import collection

class CovidSupportPipeline:
    def process_item(self, item, spider):
        data = {"title": item["title"], "link": item["link"], "date": item["date"]}
        collection.insert(data)
        return item
