import urllib2

goog_url = 'http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv'

def download_stock_data(csv_url):
    responce = urllib2.urlopen(csv_url)
    csv = responce.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


download_stock_data(goog_url)
