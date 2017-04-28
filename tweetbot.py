import tweepy
import time
from bs4 import BeautifulSoup
import requests


def scrape_some_data():
	r= requests.urlopen('http://randomtextgenerator.com/').read()
	soup=BeautifulSoup(r,'lxml')
	p = soup.find_all('textarea')[0].get_text()
	op = p[:90]
	return op
	
CONSUMER_KEY = 'jIseBb65iypSqxyjD4Hsy8x8E'
CONSUMER_SECRET = 'VPp4wCLSfCJhOzNcmYT4XiS0DTiUmuCJ9ilK9taOoilxAr3JA4'
ACCESS_KEY = '857465526033031169-S5hLTgVmWyioAwzx6BWrUktOs14gC1w'
ACCESS_SECRET = 'ItCDglOvhhJcy27dYN82fQPOxTvqJ0f2xwvjoCdyC7rO5'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
	tweet = scrape_some_data()
	api.update_status(tweet)
	time.sleep(300)





	