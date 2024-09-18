import requests
from bs4 import BeautifulSoup
import csv

url = "https://patpat.lk/property/filter/land"


response = requests.get(url)
if(response.status_code == 200):
    soup = BeautifulSoup(response.content, 'html.parser')


    results = soup.find_all('div', class_='result-item')


    csv_file_path = 'land1_data.csv'


    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        #header
        writer.writerow(['Title', 'Image URL', 'Price', 'Lease Rental', 'Down Payment', 'Vehicle Link'])

        # Loop through each result and extract information
        for item in results:
            # vehicle title
            title_tag = item.find('h4', class_='result-title')
            title = title_tag.get_text(strip=True) if title_tag else "N/A"

            #  images url
            img_tag = item.find('img', class_='img-fluid')
            image_url = img_tag['src'] if img_tag else "N/A"

            # price
            price_tag = item.find('label', style=lambda value: value and 'color' in value)
            price = price_tag.get_text(strip=True) if price_tag else "N/A"

            #  lease rental
            lease_rental_tag = item.find('div', class_='result-payments price')
            lease_rental = lease_rental_tag.find('span', class_='money').get_text(strip=True) if lease_rental_tag else "N/A"

            # the down payment
            down_payment_tag = item.find('div', class_='result-payments border-top-0')
            down_payment = down_payment_tag.find('span', class_='money').get_text(strip=True) if down_payment_tag else "N/A"

            #  vehicle link
            link_tag = item.find('a', href=True)
            land_link = link_tag['href'] if link_tag else "N/A"


            writer.writerow([title, image_url, price, lease_rental, down_payment, land_link])

    print(f"Data saved to {csv_file_path}")
