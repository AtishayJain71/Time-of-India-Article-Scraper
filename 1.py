import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape a single news article with error handling
import requests
from bs4 import BeautifulSoup

# Function to scrape a single news article with error handling
def scrape_news_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Debugging: Print the HTML structure of the page
    print(soup.prettify())  # This will print the entire page's HTML structure
    
    # Example for title (adjust based on actual tag)
    title_tag = soup.find('h1')
    title = title_tag.text if title_tag else 'Title not found'

    # Example for publication date (adjust based on actual tag)
    date_tag = soup.find('time')
    date = date_tag.text if date_tag else 'Date not found'

    # Example for news content (adjust based on actual tag)
    content_tag = soup.find('div', class_='article-body')
    content = content_tag.text if content_tag else 'Content not found'

    return {'title': title, 'date': date, 'content': content, 'url': url}

# Test scraping a single article
article_url = 'https://example.com/news-article'
news_data = scrape_news_article(article_url)
print(news_data)

# Function to save data to CSV
def save_to_csv(news_list, filename='news_articles.csv'):
    df = pd.DataFrame(news_list)
    df.to_csv(filename, index=False)

# Example of saving a list of scraped articles
news_articles = [scrape_news_article(article_url)]
save_to_csv(news_articles)