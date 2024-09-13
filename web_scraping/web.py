#import reqiered libs
import requests

#url for the page of scrap
url = 'https://example.com/'
#send a get request to the server
response = requests.get(url)
#print the scrap data
if response.status_code==200:
    print(response.text)
else :
    print("error")
