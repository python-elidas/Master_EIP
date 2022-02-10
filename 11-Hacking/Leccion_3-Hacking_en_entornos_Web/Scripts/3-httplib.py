import http.client 
conn = http.client.HTTPConnection("www.google.com") 
headers = {} 
params = {} 
conn.request("GET", "", params, headers)  
response = conn.getresponse()
print(response.status)
print(response.headers)
print(response.info())
print(response.read())

