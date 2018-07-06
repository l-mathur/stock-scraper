# stock-scraper

This project scrapes [Bloomberg Markets](https://www.bloomberg.com/markets) for current security prices, appends prices and their corresponding times to a csv file, and sends an email with current security performances to desired recipients.

I made this to practice web scraping and using SMTP.

### Prerequisites

Make sure you have installed BeautifulSoup4 using pip

```
easy_install pip
pip install BeautifulSoup4
```

### Installing

clone stock-scraper into a local directory

### Notes
* scrape_bloomberg.py scrapes for S&P 500 and Vanguarg VTI
* add Bloomberg Markets indices to page_urls to be scraped
* replace the sender and destination email information for personal use

### Bloomberg Markets Performance Warning
* overusing the scraper may flag as a violation of Bloomberg's Terms of Agreement
* this will prevent any further information retrieval

### Built With

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/?) - for web scraping
* [SMTP protocol client](https://docs.python.org/2/library/smtplib.html) - send emails