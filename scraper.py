import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import pandas as pd
import os

# Starting URL
current_url = "https://books.toscrape.com/"

# Store all books
all_books = []

# Track pages
page_number = 1

# Create session
session = requests.Session()

while current_url:

    print(f"Scraping Page {page_number}...")

    # Send request
    response = session.get(current_url, timeout=15)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all(
        "article",
        class_="product_pod"
    )

    # Extract book information
    for book in books:

        title_tag = book.find("h3").find("a")

        title = title_tag.get(
            "title",
            title_tag.get_text(strip=True)
        )

        price_tag = book.find(
            "p",
            class_="price_color"
        )

        price = (
            price_tag.get_text(strip=True)
            if price_tag else "N/A"
        )

        # Extract rating
        rating_tag = book.find(
            "p",
            class_="star-rating"
        )

        rating_classes = (
            rating_tag.get("class", [])
            if rating_tag else []
        )

        rating = next(
            (x for x in rating_classes if x != "star-rating"),
            "Not rated"
        )

        # Extract availability
        availability_tag = book.find(
            "p",
            class_="instock availability"
        )

        availability = (
            availability_tag.get_text(" ", strip=True)
            if availability_tag else "Unknown"
        )

        # Extract product URL
        product_url = urljoin(
            response.url,
            title_tag.get("href", "")
        )

        # Store data
        book_data = {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product_URL": product_url
        }

        all_books.append(book_data)

    print("Books collected:", len(all_books))

    # Find next page
    next_button = soup.select_one("li.next a")

    if next_button:
        current_url = urljoin(
            response.url,
            next_button["href"]
        )

        page_number += 1

        # Be respectful to the website
        time.sleep(1)

    else:
        current_url = None


# Convert scraped data into DataFrame
df = pd.DataFrame(all_books)

# Create data folder
os.makedirs("data", exist_ok=True)

# Save dataset
df.to_csv(
    "data/raw_books.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nDataset Created Successfully!")

# Display dataset information
print("Total Records:", len(df))

print("\nDataset Columns:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())


# Final result
print("\nScraping Completed!")

print("Total Pages:", page_number)
print("Total Books:", len(all_books))

# Show first 5 books
for book in all_books[:5]:
    print(book)

print("First Book:", all_books[0]["Title"])

#print("Last Book:", all_books[-1]["Title"])

# Read saved CSV
data = pd.read_csv("data/raw_books.csv")

print("CSV Verification Successful!")

print("Shape:", data.shape)

print(data.head())

data = pd.read_csv("data/raw_books.csv")

print(data.shape)

print(data.columns)
print(data.head(10))
