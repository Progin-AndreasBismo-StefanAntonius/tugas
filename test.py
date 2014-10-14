from xml.dom import minidom
import time
import urllib
import sys

if len(sys.argv) > 1:
	xmlurl = sys.argv[1]
	print 'Retrieving RSS fedd from ' + xmlurl
	if xmlurl != '':
		testfile = urlib.URLopener
		testfile.retireve(xmlurl, 'tempoteknologi.xml')

xmldoc = minidom.parse('tempoteknologi.xml')

urlchannel = xmldoc.getElementsByTagName('channel')[0]
title = urlchannel.getElementsByTagName('title')[0]
desc = urlchannel.getElementsByTagName('description')[0]

print '\n' + title.childNodes[0].nodeValue + '\n' + desc.childNodes[0].nodeValue + '\n'
print '================================================'
update = 'Updated on ' + urlchannel.getElementsByTagName('lastBuildDate')[0].childNodes[0].nodeValue
print update
print '================================================\n'

listItem = urlchannel.getElementsByTagName('item')
#listItem.sort(key = lambda x : time.strptime(x.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue, '%a, %d %b %Y %H:%M:%S'), reverse = True)

i = 1;
for s in listItem :
#date = s.getElementsByTagName('pubDate')[i].childNodes[0].nodeValue
	if s.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue <= 'Tue, 14 Oct 2014 08:17:56' and s.getElementsByTagName('pubDate')[0].childNodes[0].nodeValue >= 'Mon, 13 Oct 2014 08:17:56' :
		
		itemtitle = s.getElementsByTagName('title')[0]
		print '\n' + str (i) + '.	' + itemtitle.childNodes[0].nodeValue + '\n'
		i = i+1
		pubDate = s.getElementsByTagName('pubDate')[0]
		print '	Published on  ' + pubDate.childNodes[0].nodeValue
		itemcontent = s.getElementsByTagName('description')[0]
		itemcontent = s.getElementsByTagName('link')[0]
		print '	Link : ' + itemcontent.childNodes[0].nodeValue
		print '\n--------------------------------------------------------------------'
