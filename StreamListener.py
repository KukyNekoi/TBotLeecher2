#!/bin/python3
'''
File: StreamListener.py
Project: TBotLeecher2
File Created: Monday, 28th October 2019 11:59:17 pm
Author: Erik Regla (kuky.nekoi@gmail.com)
-----
Last Modified: Monday, 28th October 2019 11:59:26 pm
Modified By: Erik Regla (kuky.nekoi@gmail.com)
-----
Licensed under GPLv3,  2019 Erik Regla
'''
import tweepy
import sys
from DataDestination import DataDestination

class StreamListener(tweepy.StreamListener):

    def __init__(self, destination:DataDestination ):
        tweepy.StreamListener.__init__(self)
        self.destination = destination

    def on_status(self, status: tweepy.Status):
        self.destination.save_objects([status])

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:', status_code)
        return True # Don't kill the stream

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        return True # Don't kill the stream


    def on_event(self, event):
        print(sys.stderr, 'Event...', event)
        return True # Don't kill the stream

