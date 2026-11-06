
import pandas as pd
import os

# 1. Load raw dataset
df = pd.read_csv("data/raw_books.csv")

print("Original Dataset Shape:", df.shape)

# 2. Remove duplicate books
df = df.drop_duplicates(subset=["Product_URL"])

# 3. Clean Price
df["Price"] = (
    df["Price"]
    .astype("string")
    .str.replace(r"[^0-9.]", "", regex=True)
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

# 4. Convert Rating into numbers
rating_mapping = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_mapping)

# 5. Clean text columns
df["Title"] = df["Title"].astype("string").str.strip()

df["Availability"] = (
    df["Availability"]
    .astype("string")
    .str.strip()
)

# 6. Remove rows with missing essential values
df = df.dropna(
    subset=["Title", "Price", "Rating"]
)

# 7. Check remaining missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 8. Check duplicates
print("\nDuplicate Records:", df.duplicated().sum())

# 9. Dataset statistics
print("\nDataset Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nDataset Preview:")
print(df.head())

# 10. Save cleaned dataset
os.makedirs("data", exist_ok=True)

df.to_csv(
    "data/clean_books.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nClean Dataset Saved Successfully!")
