#!/usr/bin/env python
__author__ = 'Ghiat Mira'

import os
import json
import re
import sys


sys.path.append('/documents/coding-challenge-master/')


def average_degree(hashtags, curenttime, prevtime):

    
	for i in range(len(hashtags)):
	    if (curenttime - prevtime < 0):    
	        hashtag_window.append[hashtag[i]]
	dict = counter(hashtag_window)
	average_degree = len(dict)/len(hashtags)
	   
	return average_degree

def parser_jtweet(line):
    
	# Read line tweet of the file 
	tweet = json.loads(line)
	date = tweet["created_at"]
	unixtime = tweet['timestamp_ms']
	hashtags =(tweet["entities"]["hashtags"]["text"])
	timestamp = [unixtime[i]/1000 for i in range(len(unixtime))]      #from milliseconde to sconde
	return [date, hashtags, timestamp]
     
def clean_hashtags(hashtags, date, timestamp):

    for i in range(len(hashtags)):
	    hashatgs[i] = hashtags[i].encode('ascii', 'ignore')
	    hashtags[i] = hashtags[i].lower.strip()
	    if hashatgs[i] == '':
                hashtags.remove(hashtags[i])
                date.remove(date[i])
                timestamp.remove(timestamp[i])
                continue
    for i in range [len(hashtags)]:   
        print('{0:2} == {0:10}' .format(date[i], hashtags[i]))	
    return [date, hashtags, timestamp]	
		
def filter_hashtags(keyword_list, hashtags, date, timestamps):

	for i in range(len(hashtags)):
		if re.search( hashtags[i], keyword_list):
			continue	
		else:
			hashtags.remove(hashtags[i])
			date.remove(date[i])
			timestamp.remove(timestamp[i])
	return [date, hashtags, timestamp]
			
 
def manipulat_tweet():
 
	average_degree = 0;
	with open('jtweets.json', 'r') as tweets_file:
		for line in tweets_file:
			try:
				[date, hashtags, timestamp] = parser_jtweet(line)
				[date, hashtags, timestamp] = clean_hashtags((hashtags, date, timestamp))
				[date, hashtags, timestamp] = filter_hashtags(keyword_list, hashtags, date, timestamps)
				curenttime = timestamp
				prevtime = currenttime - 60
				if len(hashtags) < 1:
					return 0
				else: 
					average_degree += average_degree(hashtag, curenttime, prevtim)
					sys.stdout.write(str(average_degree(hashtag, curenttime, prevtime)) + "\n")
			
			except IOError:
				print('no data to process', jtweets.json)
				pass 
 

if __name__ == '__main__':

 dname = os.path.dirname('/tweet_output')
 os.chdir(dname)

 sys.stdout = open('output.txt', 'w')
 
 manipulat_tweet()
 
         
 
 


	
		
		
