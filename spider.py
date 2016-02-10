from bs4 import BeautifulSoup
import urllib2
import re
import sys

def getLinks(url):
	# html_page = urllib2.urlopen("http://www.yourwebsite.com")
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)
	for link in soup.findAll('a'):
	    print link.get('href')



if __name__ == '__main__':
	url = sys.argv[1]
	getLinks(url)