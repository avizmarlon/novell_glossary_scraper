### Novell Glosary Scraping

import re
import requests
import urllib
from lxml import etree


def URL(category_num):
	category_num_width = 6 - len(str(category_num))
	url_suffix = character_category_base.ljust(category_num_width, "0") + str(category_num)
	URL = "https://www.novell.com/documentation/glossary/glossenu/data/" + url_suffix + ".html"
	return URL

def connect(category_num):
	url = URL(category_num)
	print("Connecting to %s" % (url))
	request = urllib.request.Request(url)
	data = urllib.request.urlopen(request)
	print("Connected.")
	return data

def parse():
	print("Parsing...", end="")
	parser = etree.HTMLParser()
	print(" Done.\n")
	return parser

def xpath(category_num, path):
	root = etree.parse(connect(category_num), parse())
	return root.xpath(path)


def scrap(n):
	pass

glossary = {}

character_category_range = range(0, 26)
character_category_base = "ch00"
for category_num in character_category_range:
	path = """//*[@id="DocNavEntry%d"]""" % (category_num + 1)
	glossary_data = ['word', 'definition']
	xpath_root = xpath(category_num, path)
	print(xpath_root)
	