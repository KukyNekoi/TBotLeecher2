#!/bin/python
'''
File: main.py
Project: TBotLeecher2
File Created: Sunday, 27th October 2019 9:37:08 pm
Author: Erik Regla (kuky.nekoi@gmail.com)
-----
Last Modified: Monday, 28th October 2019 2:06:53 am
Modified By: Erik Regla (kuky.nekoi@gmail.com)
-----
Licensed under GPLv3,  2019 Erik Regla
'''

import argparse
from CrawlerConfig import CrawlerConfig
from QueryConfig import QueryConfig
from Crawler import Crawler
import tweepy


parser = argparse.ArgumentParser()

#parser.add_argument('name')
parser.add_argument('--config-file-path', default='./config.prod.yml')
parser.add_argument('--query-file-path', default='./queries/chile_geocoded.yml')

if __name__ == '__main__':
    args = parser.parse_args()
    config = CrawlerConfig(config_file_path = args.config_file_path)

    tweepy_api = tweepy.API()
    auth = tweepy.OAuthHandler(config.consumer_api_key,config.consumer_api_key_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    tweepy_api = tweepy.API(auth)


    query = QueryConfig(config_file_path = args.query_file_path, tweepy_api=tweepy_api)

    print(config)
    print(query)

    crawler = Crawler(config=config, query=query, tweepy_api=tweepy_api)

    crawler.get_tweets()
