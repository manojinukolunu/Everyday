import sys
from mechanize import ParseResponse,urlopen,urljoin,Request,Browser

if len(sys.argv)==1:
    uri="http://imdb.com"
else:
    uri=sys.argv[1]

req=Request(uri)
req.set_proxy("208.232.182.74:80","http")
response=urlopen(req)
forms=ParseResponse(response,backwards_compat=False)
form=forms[0]
form["q"]="fatih akin"
br=Browser()
br.open(form.click())

print br.title()

for link in br.links():
    if str(link.text).count('Fatih')>0:
        print link.absolute_url +":" +link.text
        
        
    
