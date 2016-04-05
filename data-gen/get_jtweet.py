#!/usr/bin/env python
__author__ = 'Ghiat Mira'

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
from pprint import pprint
import tweepy
import time
import json
import os
import io
import sys

os.path.join("c:", "foo")
# loads Twitter credentials from .twitter file that is in the same directory as this script
file_dir = os.path.dirname(os.path.realpath(__file__)) 
with open(file_dir + '/.twitter-example') as twitter_file:  
    twitter_cred = json.load(twitter_file)

# authentication from the credentials file above
access_token = twitter_cred["access_token"]
access_token_secret = twitter_cred["access_token_secret"]
consumer_key = twitter_cred["consumer_key"]
consumer_secret = twitter_cred["consumer_secret"]

now = time.time()
tm = time.localtime(now)
start_time = time.mktime(tm)         #grabs the system time
print (time.ctime(start_time))

class StdOutListener(StreamListener):
 
	def __init__(self, start_time):
 
		self.time = start_time
		self.tweet_data = []
 
	def on_data(self, data):
	    
		
		now = time.time()
		tm = time.localtime(now)
 
		while (time.mktime(tm) - self.time) < 60*10:   #10 minutes allowed
 
			try:
 				self.tweet_data.append(data)
 				return True
  
			except BaseException as e:
				print ('failed appending,', str(e))
				time.sleep(5)
				pass
 
		
		save_to_File = io.open('jtweets.json', 'w', encoding='utf-8')
		save_to_File.write(u'[\n')
		save_to_File.write(','.join(self.tweet_data))
		save_to_File.write(u'\n]')
		save_to_File.close()
		now = time.time()
		tm = time.localtime(now)
		current_time = time.mktime(tm)
		print(time.ctime(current_time))
				
		exit()
 
	def on_error(self, status):
 
		print(statuses)
		
		
if __name__ == '__main__':
		
 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 auth.set_access_token(access_token, access_token_secret)
 
 keyword_list = ['#apache', '#hadoop', '#spark', '#storm', '#flink', '#hbase', '#kafka']   
 twitterStream = Stream(auth, StdOutListener(start_time)) 
 twitterStream.filter(track=keyword_list, languages=['en'])  
 