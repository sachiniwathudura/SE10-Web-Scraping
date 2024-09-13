import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = 'https://example.com/'

# Send a GET request to the server
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.get_text())

    tags = soup.find_all(['h1','p'])
    for tag in tags :
        print(tag.text.strip())

# Extract text content, stripping out HTML tags
# text = soup.get_text(separator=' ', strip=True)

# Print the extracted text
# print(text)
else:
    print("Error: Unable to fetch the webpage")
