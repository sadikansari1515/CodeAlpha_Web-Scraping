# Books Data Scraper 📚

## Project Overview
A Python web scraping project that collects book information from [Books to Scrape](https://books.toscrape.com/).

The scraped data is cleaned, analyzed, tested, and visualized using Python libraries.

## Features
- Scrapes book titles, prices, ratings, and availability.
- Supports pagination.
- Exports data to CSV.
- Cleans and processes scraped data.
- Performs Exploratory Data Analysis (EDA).
- Creates visualizations using Matplotlib.
- Includes automated tests using Pytest.

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- Pytest

## Project Structure
- `scraper.py` – Collects book data.
- `data_cleaning.py` – Cleans the dataset.
- `analysis.py` – Performs data analysis.
- `visualization.py` – Generates charts.
- `test_scraper.py` – Tests dataset requirements.

## Installation

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Web-Scraping-Project

python -m venv venv
```

Activate the environment:

Windows:
```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python scraper.py
python data_cleaning.py
python analysis.py
python visualization.py
pytest -v
```

## Data Source
Books to Scrape – https://books.toscrape.com/

## Data Analysis & Key Findings

The Books Data Scraper project collected and analyzed 1,000 book records from Books to Scrape.

### Key Findings

1. The average book rating is approximately 2.92 out of 5.
2. High-rated books have an average price of approximately £35.72.
3. Lower-rated books have an average price of approximately £34.68.
4. Price and rating have a very weak positive correlation of approximately 0.028.
5. IQR-based outlier detection found no price outliers.
6. All 1,000 scraped books were listed as In stock.
7. Welch's independent t-test returned a p-value of approximately 0.281, so there is insufficient evidence of a statistically significant difference in average prices between the two rating groups.

### Conclusion

The analysis suggests that book price does not have a meaningful linear relationship with customer rating in this dataset. The project demonstrates a complete workflow involving web scraping, data cleaning, exploratory analysis, statistical testing, and visualization.

## Author
Sadik Ansari