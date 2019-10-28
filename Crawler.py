#!/bin/python3
from QueryConfig import QueryConfig
from CrawlerConfig import CrawlerConfig
import tweepy
import pprint

class Crawler(object):
    """
    Base class for crawlers.

    Each crawler uses their own API credentials, given that you can use multiple
    API keys to different crawling purposes. As such, you must give this configuration
    beforehand.
    """

    def __init__(self, config:CrawlerConfig, query: QueryConfig, tweepy_api:tweepy.API):
        self.tweepy_api = tweepy_api
        self.query_config = query

    def build_query(self, query_structure):
        pass

    def get_tweets(self):
        tweepy_cursor = tweepy.Cursor(self.tweepy_api.search, q=self.query_config.query, count=self.query_config.page_size)

        tweets = [tweet for tweet in tweepy_cursor.items(self.query_config.stride)]

        print("number of tweets: ", len(tweets))
        pprint.pprint(tweets[0]._json)

    
