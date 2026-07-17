# Read the data

import pandas as pd
import numpy as np

df= pd.read_excel(r"C:\Users\hp\Desktop\Projects\Retail Superstore data\Ecommerce_Messy_Dataset.xlsx")

# Understand the data

print(df.head())
print(df.info()) 
print(df.shape)
print(df.describe())
print(df.isnull().sum())

# Count duplicates records, print duplicates records and then remove duplicate records

print("Exact Duplicate Rows:", df.duplicated().sum())
duplicate_orders = df[df["Order_ID"].duplicated(keep=False)]

print(duplicate_orders.sort_values("Order_ID"))

# Analyze missing values

print("Missing Percentage:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage.sort_values(ascending=False))

# Convert the date column

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    format="mixed",
    errors="coerce",
    dayfirst=True
)

# Standardize text columns

print("Customer Name")
df["Customer_Name"] = df["Customer_Name"].str.strip()

print("\nGender")
df["Gender"] = df["Gender"].replace({
    "male": "Male",
    "M": "Male",
    "F": "Female"
})

print("\nCity")
df["City"] = df["City"].str.strip().str.title()

print("\nPayment Mode")
df["Payment_Mode"] = df["Payment_Mode"].str.strip().str.title()

# Validate Age, Quantity and Customer Rating

df.loc[
    (df["Age"] < 18) | (df["Age"] > 100),
    "Age"
] = np.nan

df.loc[
    (df["Customer_Rating"] <1) | (df["Customer_Rating"] >5), 
       "Customer_Rating"
] = np.nan

df.loc[df["Quantity"] < 0, "Quantity"] = np.nan

# Handling missing values in age, Gender, city, state, customer_id, Quantity, unit_price

median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)

df["Gender"] = df["Gender"].fillna("Unknown")

df["City"] = df["City"].fillna("Unknown")

df["State"] = df["State"].fillna("Unknown")

df["Customer_ID"] = df["Customer_ID"].fillna("Unknown")

median_qty = df["Quantity"].median()
df["Quantity"] = df["Quantity"].fillna(median_qty)

median_rating = df["Customer_Rating"].median()
df["Customer_Rating"] = df["Customer_Rating"].fillna(median_rating)

df["Unit_Price"] = df.groupby("Product")["Unit_Price"].transform(
    lambda x: x.fillna(x.median())
)
# Export the cleaned dataset

df.to_excel(
    r"C:\Users\hp\Desktop\Projects\Retail Superstore data\Ecommerce_Cleaned_Dataset.xlsx",
    index=False
)

print("Dataset exported successfully!")