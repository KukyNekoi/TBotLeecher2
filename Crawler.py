#!/bin/python3
'''
File: Crawler.py
Project: TBotLeecher2
File Created: Sunday, 27th October 2019 10:37:02 pm
Author: Erik Regla (kuky.nekoi@gmail.com)
-----
Last Modified: Monday, 28th October 2019 2:06:31 am
Modified By: Erik Regla (kuky.nekoi@gmail.com)
-----
Licensed under GPLv3,  2019 Erik Regla
'''

from QueryConfig import QueryConfig
from CrawlerConfig import CrawlerConfig
from StreamListener import StreamListener
import tweepy
import pprint
import time
import pymongo
class Crawler(object):
    """
    Base class for crawlers.

    Each crawler uses their own API credentials, given that you can use multiple
    API keys to different crawling purposes. As such, you must give this configuration
    beforehand.
    """

    def __init__(self, config:CrawlerConfig, query: QueryConfig, tweepy_api:tweepy.API, destination:pymongo.MongoClient):
        self.tweepy_api = tweepy_api
        self.query_config = query
        self.destination = destination

    def run(self):
        if self.query_config.query_type == "streaming":
            self.engage_stream()
        elif self.query_config.query_type == "query":
            self.get_tweets()

    def get_tweets(self):
        tweepy_cursor = tweepy.Cursor(self.tweepy_api.search, q=self.query_config.query, count=self.query_config.page_size, tweet_mode='extended')
        tweets = [tweet for tweet in tweepy_cursor.items(self.query_config.stride)]
        return tweets

    def engage_stream(self):
        self.stream_listener = StreamListener(destination = self.destination)
        self.bounded_stream = tweepy.Stream(auth = self.tweepy_api.auth, listener=self.stream_listener, tweet_mode='extended')
        self.bounded_stream.filter( locations=self.query_config.locations, track=self.query_config.track , is_async=True)
        while True:
            #print("Threaded status: " + str(self.bounded_stream.running))
            time.sleep(5)