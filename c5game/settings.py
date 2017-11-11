# -*- coding: utf-8 -*-
# https://www.c5game.com/dota/1143-S.html
# https://www.c5game.com/dota/661-S.html
# https://www.c5game.com/dota/553443749-S.html
# https://www.c5game.com/dota/56-P.html
# https://www.c5game.com/dota/18841-S.html
# https://www.c5game.com/dota/511105035-S.html
# //*[@id="center"]/div[2]/div/div[2]/ul/li[1]/div[3]/span[2]/span
# //*[@id="center"]/div[2]/div/div[2]/ul/li[1]/div[3]/span[2]/text()
# Scrapy settings for c5game project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'c5game'

SPIDER_MODULES = ['c5game.spiders']
NEWSPIDER_MODULE = 'c5game.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'c5game (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    "c5game.middlewares.UserAgentMiddleware":401,
}
DOWNLOAD_DELAY = 2.5
