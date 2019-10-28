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

class DataDestination(object):
    "Interface for data destinations for each tweet"

    def __init__(self):
        pass

    def save_object(self, object):
        pass

    def load_object(self, id=None):
        pass
