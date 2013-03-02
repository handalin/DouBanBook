# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DoubanbookItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title = Field()
    author = Field()
    publisher = Field()
    numOfPages = Field()
    ISBN = Field()
    intro = Field()
    rating = Field()
    image_urls = Field()
    images = Field()
    image_path = Field()
