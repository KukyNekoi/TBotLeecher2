#!/bin/python3

class DataDestination(object):
    "Interface for data destinations for each tweet"

    def __init__(self):
        pass

    def save_object(self, object):
        pass

    def load_object(self, id=None):
        pass
