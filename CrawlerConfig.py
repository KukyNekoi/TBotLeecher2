#!/bin/python3
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