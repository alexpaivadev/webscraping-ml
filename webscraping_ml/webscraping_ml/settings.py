# Scrapy settings for webscraping_ml project

BOT_NAME = "webscraping_ml"

SPIDER_MODULES = ["webscraping_ml.spiders"]
NEWSPIDER_MODULE = "webscraping_ml.spiders"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"

ROBOTSTXT_OBEY = False

COOKIES_ENABLED = True

DOWNLOAD_DELAY = 2  # Atraso de 2 segundos entre as requisições

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com",
    "Connection": "keep-alive"
}

# Enable or disable downloader middlewares
# Uncomment and configure if using proxies
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#     'myproject.middlewares.MyProxyMiddleware': 100,
# }

HTTPCACHE_IGNORE_HTTP_CODES = [403, 404]

# Other settings, extensions, pipelines, etc.
# SPIDER_MIDDLEWARES = {}
# ITEM_PIPELINES = {}
# AUTOTHROTTLE_ENABLED = True

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"