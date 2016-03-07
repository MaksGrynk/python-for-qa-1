import urllib2
import re

url = 'https://www.facebook.com/'
website = urllib2.urlopen(url)
html = website.read()
links = re.findall('"((http|ftp)s?://.*?)"', html)

print(links)
