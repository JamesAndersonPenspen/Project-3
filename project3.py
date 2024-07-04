#importing the scraping libraries and csv to store the data
import requests
from bs4 import BeautifulSoup
import csv

# Doing it in a function so it's easier to mess around with later
def scrape_books(url):
    # Take the data URL
    html_data = requests.get(url)

    # Check if the request was successful so it doesnt throw an error
    if html_data.status_code == 200:
        # interpret the data
        data = BeautifulSoup(html_data.content, 'html.parser')

        # Find all book containers
        chosen_data = data.find_all('div', class_='s-result-item')

        # Open CSV file to store data
        with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Title', 'Author', 'Price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Extract data for every book
            for book in chosen_data:       #Text Text__title1  #BookPageTitleSection__title
                # Extract title based on class
                title = book.find('span', class_='Text Text__title1').text.strip()

                # Extract author based on class
                author = book.find('div', class_='').text.strip()

                # Extract price based on class
                price = book.find('span', class_='BookPage__jumpNav u-sr-only').text.strip()

                # Write data to CSV
                writer.writerow({'Title': title, 'Author': author, 'Price': price})

        print('Scraping and data storage complete.')
    else:
        print(f'Failed to retrieve the webpage: {html_data.status_code}')

#Starts the scrape
if __name__ == '__main__':
    url = 'https://www.goodreads.com/book/show/58587868-black-holes'
    scrape_books(url)  