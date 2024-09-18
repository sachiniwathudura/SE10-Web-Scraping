import requests
from bs4 import BeautifulSoup
import csv

# Base URL with placeholder for page number
base_url = "https://patpat.lk/property/filter/land?page={}"

# Create or overwrite the CSV file to store the data
csv_file_path = 'land_data100.csv'
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Header
    writer.writerow(['Title', 'Image URL', 'Price', 'Lease Rental', 'Down Payment', 'Vehicle Link'])

    # Loop through multiple pages
    page_number = 1
    while page_number <= 100:  # Stop when page_number exceeds 200
        url = base_url.format(page_number)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to retrieve page {page_number}. Status code: {response.status_code}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all result items on the current page
        results = soup.find_all('div', class_='result-item')

        # If no results found, stop the loop (indicating no more pages)
        if not results:
            print(f"No more results found on page {page_number}.")
            break

        # Extract data from each result item
        for item in results:
            # Vehicle title
            title_tag = item.find('h4', class_='result-title')
            title = title_tag.get_text(strip=True) if title_tag else "N/A"

            # Image URL
            img_tag = item.find('img', class_='img-fluid')
            image_url = img_tag['src'] if img_tag else "N/A"

            # Price
            price_tag = item.find('label', style=lambda value: value and 'color' in value)
            price = price_tag.get_text(strip=True) if price_tag else "N/A"

            # Lease rental
            lease_rental_tag = item.find('div', class_='result-payments price')
            lease_rental = lease_rental_tag.find('span', class_='money').get_text(strip=True) if lease_rental_tag else "N/A"

            # Down payment
            down_payment_tag = item.find('div', class_='result-payments border-top-0')
            down_payment = down_payment_tag.find('span', class_='money').get_text(strip=True) if down_payment_tag else "N/A"

            # Vehicle link
            link_tag = item.find('a', href=True)
            land_link = link_tag['href'] if link_tag else "N/A"

            # Write the row to the CSV file
            writer.writerow([title, image_url, price, lease_rental, down_payment, land_link])

        print(f"Page {page_number} scraped successfully.")
        page_number += 1  # Move to the next page

print(f"Data saved to {csv_file_path}")
