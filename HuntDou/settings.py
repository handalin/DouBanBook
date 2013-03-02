# Scrapy settings for DouBanBook project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'DouBanBook'

SPIDER_MODULES = ['DouBanBook.spiders']
NEWSPIDER_MODULE = 'DouBanBook.spiders'

DOWNLOAD_DELAY =2.0

IMAGES_STORE = 'pic/'
DOWNLOAD_TIMEOUT = 1100
ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline',
                  'DouBanBook.pipelines.DoubanbookPipeline']#

#IMAGES_EXPIRES = 90

IMAGES_THUMBS = {
    'big': (140, 193),
}

IMAGES_MIN_HEIGHT = 144
IMAGES_MIN_WIDTH = 103


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DouBanBook (+http://www.yourdomain.com)'

"""
IMAGES_MIN_HEIGHT = 50
IMAGES_MIN_WIDTH = 50
IMAGES_STORE = 'image-downloaded/'
DOWNLOAD_TIMEOUT = 1200
ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline',
                  'image_downloader.pipelines.ImageDownloaderPipeline']
"""
