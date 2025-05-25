import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_toi_article(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.find('h1').text.strip() if soup.find('h1') else 'N/A'
    
    date = soup.find('div', {'class': '_3Mkg- byline'}).text.strip() if soup.find('div', {'class': '_3Mkg- byline'}) else 'N/A'
    
    article_body = soup.find_all('div', {'class': '_s30J clearfix'})
    article_text = ' '.join([paragraph.text.strip() for paragraph in article_body])
    
    return {
        'head': title,
        'text': article_text,
        'date': date
    }

def save_to_csv(data, filename='toi_articles.csv'):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    urls = [
        'https://timesofindia.indiatimes.com/world/us/joe-biden-bids-farewell-with-a-selfie-before-trumps-swearing-in/articleshow/117402546.cms',
        'https://timesofindia.indiatimes.com/technology/tech-news/why-shark-tank-judge-anupam-mittal-has-tagged-maharashtra-cm-over-these-traffic-challans/articleshow/113622328.cms',
        'https://timesofindia.indiatimes.com/city/kolkata/kolkata-horror-bjp-leader-dilip-ghosh-accuses-tmc-of-bribing-victims-parents-to-shut-their-mouths/articleshow/113619230.cms'
    ]
    
    articles_data = []
    
    for url in urls:
        print(f"Scraping: {url}")
        article_data = scrape_toi_article(url)
        articles_data.append(article_data)
    
    save_to_csv(articles_data)

if __name__ == "__main__":
    main()