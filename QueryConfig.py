#!/bin/python3
'''
File: QueryConfig.py
Project: TBotLeecher2
File Created: Sunday, 27th October 2019 11:50:27 pm
Author: Erik Regla (kuky.nekoi@gmail.com)
-----
Last Modified: Monday, 28th October 2019 2:07:00 am
Modified By: Erik Regla (kuky.nekoi@gmail.com)
-----
Licensed under GPLv3,  2019 Erik Regla
'''

import yaml
import tweepy

class QueryConfig(object):
    """
    Configurations for queries used on crawling.

    Configurations are developed on a way that all attributes are concatenated
    by an "and" operator. In this way, you can develop custom and specific crawlers
    dedicated to grab all information from a single source of parameters.

    Given this, it's expected that each element to be concatenated is to be developed on
    a diffent file unless stated other in the parameter file
    """

    def __init__(self, config_file_path:dict, tweepy_api:tweepy.API):
        try:
            query_file_stream = open(config_file_path, 'r')
            query_file = yaml.load(query_file_stream, Loader=yaml.FullLoader)

            query_terms = query_file["query"]
            parameters = query_file["parameters"]

            self.tweepy_api = tweepy_api

            # build parameters    
            self.language = parameters["language"]
            self.locale = parameters["locale"]
            self.since_id = parameters["since_id"]
            self.geocode = parameters["geocode"]
            self.show_user = parameters["show_user"]
            self.parameter_operator = parameters["parameter_operator"]
            self.query_operator = parameters["query_operator"]
            self.page_size = parameters["page_size"]
            self.stride = parameters["stride"]

            self.hashtags_query = self.build_query_string(query_terms["hashtags"], self.query_operator)
            self.terms_query = self.build_query_string(query_terms["terms"], self.query_operator)
            self.countries_query = self.build_country_parameters(query_terms["countries"], "place", self.query_operator)

            self.query = self.join_queries([self.hashtags_query, self.terms_query, self.countries_query], self.parameter_operator)

        except yaml.YAMLError as exc:
            print("Error in configuration file:", exc)


    def join_queries(self, queries_array: list, operator):
        _queries_array = filter(lambda x: x != '', queries_array)
        if queries_array:
            return self.build_query_string(_queries_array, operator)
        else:
            return "*"

    def evenly_space_operator(self, operator:str):
        return " " + operator.strip() + " "

    def build_query_string(self, array:list, operator:str = "OR"):
        "Concatenates the parameters in a single query"
        if not array:
            return ""
        return self.evenly_space_operator(operator).join(array)

    def build_country_parameters(self, array:list, parameter:str, operator:str = "OR"):
        "Concatenates the parameters in a single query"
        if not array:
            return ""

        _ids_array = []
        for x in array:
            places = self.tweepy_api.geo_search(query=x, granularity="country")
            place_id = places[0].id
            _ids_array.append(place_id)

        return self.evenly_space_operator(operator).join([parameter + ":" + x for x in _ids_array])

    def test_variable_or_default(self, variable:str, file:dict, default=None):
        if file[variable] is None:
            return default
        return file[variable]
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)