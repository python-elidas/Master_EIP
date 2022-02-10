from bs4 import BeautifulSoup, SoupStrainer
import requests

response = requests.get("http://thehackerway.com") 
if response.status_code not in range(400, 503):
	soup = BeautifulSoup(response.content, "lxml")
	for link in soup.find_all('a', href=True):
		print(link['href'])
