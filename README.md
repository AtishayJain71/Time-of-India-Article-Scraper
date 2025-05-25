# 📰 Times of India Article Scraper

A Python-based web scraper designed specifically to extract news article data from the Times of India (TOI) website. This tool automates the collection of article headlines, full text, and publication dates, and stores the data in a structured CSV file for easy access and analysis.

---

## 🚀 Features

- Scrapes article **headlines** (`<h1>` tag)
- Extracts **publication date** from the byline section
- Captures full **article content** from relevant HTML containers
- Saves scraped data into a CSV file with columns: `head`, `text`, and `date`
- Handles missing data gracefully by assigning 'N/A' if any field is unavailable
- Basic error handling for HTTP request failures

---

## 🧰 Technologies & Libraries Used

- [`requests`](https://pypi.org/project/requests/) — to send HTTP requests
- [`BeautifulSoup`](https://pypi.org/project/beautifulsoup4/) — for parsing HTML content
- [`pandas`](https://pandas.pydata.org/) — to organize and export scraped data as CSV

---

## 🧩 How It Works

1. **Input:** A list of Times of India article URLs.
2. **Scraping:** For each URL, the scraper:
   - Extracts the article title from the `<h1>` tag.
   - Finds the publication date inside a `<div>` with class `_3Mkg- byline`.
   - Collects the main article content from `<div>` elements with class `_s30J clearfix`.
3. **Preprocessing:** Cleans the text by removing extra spaces and unwanted characters.
4. **Output:** Saves the collected data into a CSV file with columns:  
   `head` (headline), `text` (article body), `date` (publication date).

---
