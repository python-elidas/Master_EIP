from bs4 import BeautifulSoup 
import urllib.request, urllib.parse, urllib.error 
import urllib.request, urllib.error, urllib.parse 

url = urllib.request.urlopen("http://thehackerway.com") 
contents = url.read() 
soup = BeautifulSoup(contents, "lxml") 

print(soup.title) 
print(soup.head) 
print(soup.body) 
print(soup.title .text)
