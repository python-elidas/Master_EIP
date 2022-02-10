import mechanize 
import http.cookiejar 
br = mechanize.Browser() 
cj = http.cookiejar.LWPCookieJar() 
br.set_cookiejar(cj) 

br.set_handle_equiv(True) 
br.set_handle_gzip(True) 
br.set_handle_redirect(True) 
br.set_handle_referer(True) 
br.set_handle_robots(False) 
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')] 

br.open('http://thehackerway.com') 
for link in br.links(): 
	if "Contact" in  link.text: 
		new_link = br.click_link(link) 
		br.open(new_link) 
		print(br.response().read())
