
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("data/clean_books.csv")

# Create output folder
os.makedirs("output", exist_ok=True)

# Graph 1: Price Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=20)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("output/price_distribution.png")
plt.show()

# Graph 2: Rating Distribution
rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index, rating_counts.values)
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig("output/rating_distribution.png")
plt.show()

# Graph 3: Availability
availability = df["Availability"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(availability.index, availability.values)
plt.title("Book Availability")
plt.xlabel("Availability")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("output/availability.png")
plt.show()

# Graph 4: Top 10 Expensive Books
top_books = df.sort_values(
    by="Price",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_books["Title"], top_books["Price"])
plt.title("Top 10 Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")
plt.tight_layout()
plt.savefig("output/top_10_expensive.png")
plt.show()


# Graph 5 – Price Outlier Detection
plt.figure(figsize=(8, 5))

plt.boxplot(df["Price"])

plt.title("Book Price Outlier Analysis")
plt.ylabel("Price (£)")

plt.tight_layout()
plt.savefig("output/price_outliers.png")
plt.show()

# Graph 6 – Average Price by Rating
rating_price = df.groupby("Rating")["Price"].mean()

plt.figure(figsize=(8, 5))

plt.bar(rating_price.index, rating_price.values)

plt.title("Average Price by Book Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")

plt.xticks([1, 2, 3, 4, 5])

plt.tight_layout()
plt.savefig("output/average_price_by_rating.png")
plt.show()

# Graph 7 – Price vs Rating Relationship
plt.figure(figsize=(8, 5))

plt.scatter(df["Rating"], df["Price"])

plt.title("Relationship Between Price and Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.tight_layout()
plt.savefig("output/price_vs_rating.png")
plt.show()

print("All visualizations created successfully!")
