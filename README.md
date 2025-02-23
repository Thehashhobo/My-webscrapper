# Recipe Data SQL Analysis
This project extracts, cleans, and analyzes a dataset of 4,000 recipes. The data is extracted using web scraping, and SQL is used to extract insights about ratings, cooking times, and ingredient popularity. It demonstrates data extraction, cleaning, and complex SQL queries.

## Data Extraction and Storage
The web scraper is written in Python 3 using the following technologies:
- BeautifulSoup (Used in scrap.py): Extracts structured data from HTML.
- Scraper API (Used in scrap_alt.py): Enables large-scale scraping by handling rotating proxies and avoiding IP-based request limitations.
- spaCy: Cleans scraped text by removing unnecessary details and descriptions, resulting in concise final data.

### Running the Web Scraper
Install dependencies: `pip install -r requirements.txt`

Choose your scraping method:
For BeautifulSoup-based scraping: `web_scrapper/scrap.py`
For Scraper API (recommended for large-scale scraping): `web_scrapper/scrap_alt.py`
Once scraping is complete, run the final text processing/formatting functions: `web_scrapper/finalized_cleanup.py`
Finally, insert the data into our database with: `web_scrapper/mysql_insertion.py`

### Setting up the Database
We step up the database by running: `mysql -u root -p < queries/setup.sql`