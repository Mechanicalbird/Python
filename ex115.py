import random
import urllib2

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name)+ ".jpg"
    proxies = {url}
    opener = urllib2.FancyURLopener(proxies)
    download = opener.urlretrieve(URL, file_name)



download_web_image("http://ejocurionline.net/data/wallpapers/4/DDW_813569.jpg")
