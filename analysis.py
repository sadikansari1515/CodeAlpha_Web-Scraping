
import pandas as pd

# Load dataset
df = pd.read_csv("data/clean_books.csv")

print("\n========== 1. DATASET OVERVIEW ==========")

print("Dataset Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())


print("\n========== 2. PRICE ANALYSIS ==========")

print("Average Price:", df["Price"].mean())
print("Median Price:", df["Price"].median())
print("Minimum Price:", df["Price"].min())
print("Maximum Price:", df["Price"].max())

print("\nPrice Statistics:")
print(df["Price"].describe())


print("\n========== 3. RATING ANALYSIS ==========")

print("Rating Distribution:")
print(df["Rating"].value_counts().sort_index())

print("Average Rating:", df["Rating"].mean())
print("Most Common Rating:", df["Rating"].mode()[0])


print("\n========== 4. RESEARCH QUESTION ==========")

# Compare high-rated and lower-rated books
high_rated = df[df["Rating"] >= 4]
low_rated = df[df["Rating"] < 4]

print("High Rated Average Price:",
      high_rated["Price"].mean())

print("Low Rated Average Price:",
      low_rated["Price"].mean())


print("\n========== 5. CORRELATION ==========")

correlation = df["Price"].corr(df["Rating"])

print("Price-Rating Correlation:", correlation)

if pd.isna(correlation):
    print("Correlation could not be calculated.")
elif correlation > 0:
    print("Positive relationship between price and rating.")
elif correlation < 0:
    print("Negative relationship between price and rating.")
else:
    print("No linear relationship between price and rating.")


print("\n========== 6. OUTLIER DETECTION ==========")

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Price"] < lower_limit) |
    (df["Price"] > upper_limit)
]

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Outliers Found:", len(outliers))

print("\nOutlier Books:")
print(outliers[["Title", "Price"]])


print("\n========== 7. AVAILABILITY ==========")

print(df["Availability"].value_counts())

from scipy.stats import ttest_ind

high_rated = df[df["Rating"] >= 4]["Price"]
low_rated = df[df["Rating"] < 4]["Price"]

t_stat, p_value = ttest_ind(
    high_rated,
    low_rated,
    equal_var=False
)

print("\n========== HYPOTHESIS TEST ==========")

print("T-Statistic:", t_stat)
print("P-Value:", p_value)

if p_value < 0.05:
    print("Significant difference in average prices.")
else:
    print("No statistically significant difference found.")

print("\n========== EDA COMPLETED ==========")
