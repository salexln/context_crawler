from bs4 import BeautifulSoup
import urllib2
import re
import sys


class Spider(object):

	def __init__(self, url):
		if not self._validate_ulr(url):
			print 'Input url must be Wiki Category url'
			print 'i.e https://en.wikipedia.org/wiki/Category:New_York'
			quit(-1)

		self._url = url
		self._category_links = []

	def crawl(self):
		self._get_categories()

	def print_category_links(self):
		print 'Category links for %s :' %self._url
		print '\n'
		for category in self._category_links:
			print category

	def _validate_ulr(self, url):
		if not 'wiki/Category:' in url:
			return False
		return True

	def _check_link(self, link):
		if str(link).startswith('/wiki/Category'):
			if not str(link).startswith('/wiki/Category:Wikipedia') and\
			 not str(link).startswith('/wiki/Category:Articles') and\
			  not str(link).startswith('/wiki/Category:All_articles'):		
				return True
		return False


	def _get_categories(self):	
		html_page = urllib2.urlopen(self._url)
		soup = BeautifulSoup(html_page)
		for link in soup.findAll('a'):
			link = link.get('href')
			if self._check_link(link):
				self._category_links.append(link)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'The script must have an input Wiki Category url'
		print 'i.e https://en.wikipedia.org/wiki/Category:New_York'
		quit(-1)		

	url = sys.argv[1]

	print '*'*30
	print '   Context Crawler v0.1'
	print '*'*30
	print '\n\n'

	sp = Spider(url)
	sp.crawl()	
	sp.print_category_links()
