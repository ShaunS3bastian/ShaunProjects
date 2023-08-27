# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape news article titles
def scrape_data():
    # Send a request to the BBC News website
    response = requests.get('https://www.bbc.com/news')

    # Create a "soup" object to work with the webpage's content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Initialize an empty list to store news article titles
    article_titles = []

    # Find and process news article elements
    articles = soup.find_all('div', class_='gs-c-promo')
    for article in articles:
        # Look for the title element inside each article
        title_element = article.find('h3', class_='gs-c-promo-heading__title')
        
        # If a title is found, extract and add it to the list
        if title_element:
            article_titles.append(title_element.get_text())

    # Return the list of news article titles
    return article_titles

# Function to save data to a CSV file
def save_to_csv(data):
    # Open a CSV file in write mode
    with open('news_articles.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(['Article Title'])

        # Write the article titles into the CSV
        writer.writerows(zip(data))

    # Print a message to confirm data saving
    print('Data saved to news_articles.csv')

# Entry point of the script
if __name__ == '__main__':
    # Call the scraping function to get news article titles
    scraped_data = scrape_data()

    # Call the function to save data to a CSV file
    save_to_csv(scraped_data)
