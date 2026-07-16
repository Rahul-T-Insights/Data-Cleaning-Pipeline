# 🧹 E-Commerce Data Cleaning Pipeline using Python

## 📌 Project Overview

This project demonstrates an end-to-end data cleaning process on a messy e-commerce dataset using **Python**, **Pandas**, and **NumPy**. The goal is to transform raw, inconsistent data into a clean dataset suitable for analysis.

The project covers common real-world data quality issues such as missing values, duplicate records, inconsistent text formatting, invalid data, and incorrect data types.

---

## 🛠️ Tools & Libraries

* Python
* Pandas
* NumPy
* Microsoft Excel

---

## 📂 Dataset

The dataset contains customer order information with the following fields:

* Order ID
* Order Date
* Customer ID
* Customer Name
* Gender
* Age
* City
* State
* Product
* Category
* Quantity
* Unit Price
* Payment Mode
* Sales Representative
* Customer Rating

---

## 🔍 Data Cleaning Process

### 1. Data Inspection

Performed an initial assessment of the dataset using:

* `head()`
* `info()`
* `shape`
* `describe()`
* Missing value analysis

---

### 2. Duplicate Analysis

* Identified duplicate records
* Checked duplicate Order IDs

---

### 3. Missing Value Analysis

Calculated the percentage of missing values for every column to understand data quality before cleaning.

---

### 4. Date Conversion

Converted the **Order_Date** column into the datetime format using:

* `pd.to_datetime()`
* `errors="coerce"`

Invalid dates were automatically converted into missing values (`NaT`).

---

### 5. Text Standardization

Cleaned inconsistent text values by:

* Removing leading and trailing spaces
* Standardizing Gender values
* Standardizing City names
* Standardizing Payment Mode values

---

### 6. Data Validation

Validated business rules by identifying and correcting invalid values.

Examples:

* Age less than 18 or greater than 100
* Negative Quantity values
* Customer Rating outside the 1–5 range

Invalid values were replaced with missing values before further processing.

---

### 7. Missing Value Handling

Applied appropriate strategies for different data types.

**Numerical Columns**

* Age → Median
* Quantity → Median
* Customer Rating → Median
* Unit Price → Filled using the median Unit Price of the corresponding Product

**Categorical Columns**

* Gender → Unknown
* City → Unknown
* State → Unknown
* Customer ID → Unknown

---

## 📁 Output

The cleaned dataset is exported as:

```text
Ecommerce_Cleaned_Dataset.xlsx
```

---

## 📚 Skills Demonstrated

* Data Cleaning
* Data Validation
* Missing Value Treatment
* Duplicate Detection
* Date Conversion
* Text Standardization
* Feature Preparation
* Pandas Data Manipulation
* Data Quality Assessment

---

## 📷 Project Workflow

```text
Raw Excel Dataset
        │
        ▼
Data Inspection
        │
        ▼
Duplicate Analysis
        │
        ▼
Missing Value Analysis
        │
        ▼
Date Conversion
        │
        ▼
Text Standardization
        │
        ▼
Data Validation
        │
        ▼
Missing Value Handling
        │
        ▼
Cleaned Excel Dataset
```

---

## 🎯 Learning Outcome

This project helped strengthen practical skills in:

* Working with messy real-world datasets
* Cleaning and validating data using Pandas
* Choosing appropriate techniques for handling missing values
* Preparing datasets for further analysis

---

## 👤 Author

**Your Name**

Aspiring Data Analyst | Python | SQL | Excel | Power BI
