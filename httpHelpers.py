import urllib
import urllib2


def openUrl(url, data = None, headers = None):
	encodedData = data
	if headers:
		req = urllib2.Request(url, encodedData, headers)
	else:
		req = urllib2.Request(url, encodedData)
	f = urllib2.urlopen(req)
	return f