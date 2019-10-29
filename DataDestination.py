#!/bin/python3
'''
File: DataDestination.py
Project: TBotLeecher2
File Created: Sunday, 27th October 2019 8:00:18 pm
Author: Erik Regla (kuky.nekoi@gmail.com)
-----
Last Modified: Monday, 28th October 2019 2:06:46 am
Modified By: Erik Regla (kuky.nekoi@gmail.com)
-----
Licensed under GPLv3,  2019 Erik Regla
'''

import wget
import tweepy
from CrawlerConfig import CrawlerConfig
from QueryConfig import QueryConfig
import os

class DataDestination(object):
    "Interface for data destinations for each tweet"

    def __init__(self, query: QueryConfig):
        self.__query = query

    @property
    def query(self):  
        return self.__query

    def save_objects(self, objects):
        pass

    def load_objects(self, id=None):
        pass

    def save_media(self, target_tweet):
        tweet_id = target_tweet["id"]
        if("extended_entities" in target_tweet):
            entities = target_tweet["extended_entities"]
            if("media" in entities):
                media_array = entities["media"]
                for media_object in media_array:
                    self.download_media(media_object, tweet_id)
                    if "video" in media_object["type"]:
                        self.download_media(media_object, tweet_id, video=True)
            
    def download_media(self, media_object:dict, tweet_id:str, video:bool = False):
        media_type = ""
        media_url = ""
        if video:
            media_type = media_object["type"]
            media_url = media_object["video_info"]["variants"][-1]["url"]
        else: 
            media_type = media_object["type"]
            media_url = media_object["media_url"]

        ## download                
        destination_directory = self.query.download_media+ "/" + str(tweet_id) + "/" + media_type
        destination_file = os.path.basename(media_url)
        final_destination = destination_directory + "/" + destination_file

        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        if not os.path.exists(final_destination):
            wget.download(media_url, final_destination)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)