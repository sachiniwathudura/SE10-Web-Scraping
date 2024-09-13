# image download

import requests
from bs4 import BeautifulSoup
import os

# URL to scrape
url = "https://www.geeksforgeeks.org/fundamentals-of-algorithms/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    # Create a directory to save images
    if not os.path.exists('images'):
        os.makedirs('images')

    # Download each image
    for img in img_tags:
        img_url = img.get('src')
        if img_url:
            # Handle relative URLs
            if img_url.startswith('/'):
                img_url = url + img_url

            # Get the image content
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                # Extract the image file name
                img_name = os.path.join('images', os.path.basename(img_url))

                # Save the image
                with open(img_name, 'wb') as f:
                    f.write(img_response.content)
                print(f"Downloaded {img_name}")
else:
    print("Failed to retrieve the page")