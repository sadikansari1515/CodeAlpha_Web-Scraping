import pandas as pd
import os

def test_csv_exists():
    assert os.path.exists("data/clean_books.csv")

def test_csv_not_empty():
    df = pd.read_csv("data/clean_books.csv")
    assert len(df) > 0

def test_required_columns():
    df = pd.read_csv("data/clean_books.csv")

    required = [
        "Title",
        "Price",
        "Rating",
        "Availability",
        "Product_URL"
    ]

    for column in required:
        assert column in df.columns

def test_price_is_numeric():
    df = pd.read_csv("data/clean_books.csv")
    assert pd.api.types.is_numeric_dtype(df["Price"])

def test_rating_range():
    df = pd.read_csv("data/clean_books.csv")
    assert df["Rating"].between(1, 5).all()