#!/bin/python

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
