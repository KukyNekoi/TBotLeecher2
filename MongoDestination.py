#!/bin/python3
'''
File: MongoDestination.py
Project: TBotLeecher2
File Created: Sunday, 27th October 2019 8:00:18 pm
Author: Erik Regla (kuky.nekoi@gmail.com)
-----
Last Modified: Monday, 28th October 2019 2:06:46 am
Modified By: Erik Regla (kuky.nekoi@gmail.com)
-----
Licensed under GPLv3,  2019 Erik Regla
'''

from DataDestination import DataDestination
from CrawlerConfig import CrawlerConfig
import pymongo

class MongoDestination(DataDestination):
    "Interface for data destinations for each tweet"

    def __init__(self, config: CrawlerConfig):
        self.client = pymongo.MongoClient(config.database_config_object["connection_string"])
        self.database = self.client[config.database_config_object["database_name"]]
        
        # checks collection, otherwise, creates a new one if not present
        collections = self.database.list_collection_names()
        if config.database_config_object["collection_name"] in collections:
            print("The collection exists. Nothing to do.")
        else:
            print("Collection doesn't exist. Must be created.")
        
        self.collection = self.database[config.database_config_object["collection_name"]]

    def save_objects(self, objects):
        pass

    def load_objects(self, id=None):
        pass
