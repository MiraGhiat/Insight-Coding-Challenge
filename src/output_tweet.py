#!/usr/bin/env python
__author__ = 'Ghiat Mira'

import os
import json
import re
import sys
from average_degree import parser_jtweet
from average_degree import clean_hashtags
from average_degree import filter_hashtags


if __name__ == '__main__':

	sys.stdout = open('output.txt', 'w')
 
	with open('jtweets.json', 'r') as tweets_file:
			try:
				for line in tweets_file:
					[date, hashtags, timestamp] = parser_jtweet(line)
					[date, hashtags, timestamp] = clean_hashtags(hashtags, date, timestamp)
					[date, hashtags, timestamp] = filter_hashtags(keyword_list, hashtags, date, timestamps)
					sys.stdout.write(str(filter_hashtags(hashtags, date, timestamp)) + "\n")	
    
			except IOError:
				print('cannot open jason file')