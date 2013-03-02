# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
"""
class DoubanbookPipeline(object):
    def process_item(self, item, spider):
        return item
"""

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class DoubanbookPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print '#' * 100
        for image_url in item['image_urls']:
            print image_url
            yield Request(image_url)
        print '$' * 100
    def item_completed(self, results, item, info):
        print 'TT' * 30
        image_path = [x['path'] for ok, x in results if ok][0]
        print image_path
        if not image_path:
            raise DropItem("Item contains no images")
        item['image_path'] = image_path
        return item
"""
class ImageDownloaderPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
"""
