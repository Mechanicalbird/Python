import urllib2
opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')]
response = opener.open('http://google.com')
htmlData = response.read()
f = open('file.txt','w')
f.write(htmlData )
f.close()
