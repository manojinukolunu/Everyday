import urllib2,base64
req=urllib2.Request("https://api.del.icio.us/v1/posts/all")
username="zerocool1989"
password="mangdang123.bits"
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
req.add_header("Authorization", "Basic %s" % base64string) 
response=urllib2.urlopen(req)
print response.read()
