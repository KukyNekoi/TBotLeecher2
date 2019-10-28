#!/bin/python3
'''
File: CrawlerConfig.py
Project: TBotLeecher2
File Created: Sunday, 27th October 2019 7:54:56 pm
Author: Erik Regla (kuky.nekoi@gmail.com)
-----
Last Modified: Monday, 28th October 2019 2:06:38 am
Modified By: Erik Regla (kuky.nekoi@gmail.com)
-----
Licensed under GPLv3,  2019 Erik Regla
'''

import yaml

class CrawlerConfig(object):
    "Configurations for tweet crawling, such as API Keys..."

    def __init__(self, config_file_path:dict):
        try:
            config_file_stream = open(config_file_path, 'r')
            config_file = yaml.load(config_file_stream, Loader=yaml.FullLoader)

            self.consumer_api_key = config_file["credentials"]["CONSUMER_API_KEY"]
            self.consumer_api_key_secret = config_file["credentials"]["CONSUMER_API_KEY_SECRET"]
            self.access_token = config_file["credentials"]["ACCESS_TOKEN"]
            self.access_token_secret = config_file["credentials"]["ACCESS_TOKEN_SECRET"]

        except yaml.YAMLError as exc:
            print("Error in configuration file:", exc)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)