import requests
from bs4 import BeautifulSoup
import csv
import logging

# Set up logging
logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_data(url):
    """
    Fetches article titles from a given URL.
    
    Args:
        url (str): The URL to scrape data from.
        
    Returns:
        list: A list of article titles.
    """
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})
        response.raise_for_status()  # Raise an exception for bad status codes
        
        soup = BeautifulSoup(response.content, 'html.parser')
        article_titles = []
        articles = soup.find_all('h3', class_='gs-c-promo-heading__title')
        for article in articles:
            article_titles.append(article.get_text().strip())  # Clean up whitespace
            
        return article_titles
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return []

def save_to_csv(data):
    """
    Saves data to a CSV file.
    
    Args:
        data (list): The data to be saved to the CSV file.
    """
    with open('news_articles.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Article Title'])
        writer.writerows(zip(data))
    logging.info('Data saved to news_articles.csv')

if __name__ == '__main__':
    url = 'https://www.bbc.com/news'
    
    scraped_data = scrape_data(url)
    if scraped_data:
        save_to_csv(scraped_data)
