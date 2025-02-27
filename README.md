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
For BeautifulSoup-based scraping: `web_scrapper/scrap.py`\
For Scraper API (recommended for large-scale scraping): `web_scrapper/scrap_alt.py`\
Once scraping is complete, run the final text processing/formatting functions: `web_scrapper/finalized_cleanup.py`\
Finally, insert the data into our database with: `web_scrapper/mysql_insertion.py`

### Setting up the Database
We step up the database by running: `mysql -u root -p < queries/setup.sql` 
The Database is structured as follows:\
![Screenshot of the application](https://github.com/Thehashhobo/Recipe-Data-Analysis/blob/main/queries/structure.PNG)

## Data Analysis using SQL
The data can be analyzed with quuries with in `analysis.sql`, these analysis include:
- Count number of recipes
- Show complete recipe details
- Top 10 recipes by rating
- Top 10 recipes by cooking time and ratings (prefer faster recipes)
- Most Common Ingredients
- Recipes with the Most Ingredients
- Fastest Cooking Recipes
- Most Complex Recipes (most steps)
- Distribution of Ratings

## Exploratory  Data Analysis With Juypter notebook
This section explores the recipe dataset to uncover insights about ingredient usage, cooking times, and ratings. Using Jupyter Notebook, we apply various statistical and visualization techniques to understand the structure of the data and identify patterns.
### The Exploratory Data Analysis (EDA) follows these steps:
- Load and Clean Data → Retrieve structured recipe data from the MySQL database.
- Handle Missing Values → Identify and address missing or inconsistent entries.
- Feature Engineering → Create new variables such as number of ingredients, instructions, and cooking time in minutes.
- Data Distribution Analysis → Visualize how features like ratings, ingredient counts, and cooking times are distributed.
- Correlation Analysis → Identify relationships between ingredients, cooking times, and ratings.
- Outlier Detection → Detect anomalies in cooking time and ingredient counts.
### Technologies Used
- Jupyter Notebook → Interactive environment for EDA.
- Pandas → Data manipulation and processing.
- Seaborn & Matplotlib → Data visualization.
- SQLAlchemy → connect to our database for better integrations with Pandas.




