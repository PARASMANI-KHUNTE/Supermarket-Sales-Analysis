Supermarket Sales Analysis
This repository contains a Python script to analyze and visualize supermarket sales data. The dataset includes information on customer purchases, ratings, payment methods, and more. The script provides insights through visualizations and statistics, helping to understand sales trends and customer behavior.

Dataset Overview
The dataset file is named supermarket_sales - Sheet1.csv and contains the following columns:

Column Name	Description
Invoice ID	Unique identifier for each transaction
Branch	Store branch (A, B, C)
City	City where the store is located
Customer type	Membership status of the customer (Member/Normal)
Gender	Gender of the customer
Product line	Category of the product purchased
Unit price	Price per unit of the product
Quantity	Quantity of the product purchased
Tax 5%	Tax applied to the transaction
Total	Total transaction amount
Date	Date of purchase
Time	Time of purchase
Payment	Payment method used (Cash, Credit card, Ewallet)
COGS	Cost of goods sold
Gross margin percentage	Gross margin percentage
Gross income	Gross income generated
Rating	Customer rating for the transaction
Script Features
The Python script analyze_supermarket_sales.py performs the following tasks:

Data Loading and Cleaning:

Reads the CSV file and formats columns for consistency.
Converts Date and Time columns into appropriate data types.
Exploratory Data Analysis (EDA):

Prints a summary of the dataset.
Displays the first few rows of the data.
Data Visualizations:

Average Rating by Product Line: Bar chart of average ratings per product line.
Sales by City: Count plot showing the number of sales per city.
Payment Method Distribution: Frequency of payment methods.
Total Sales by Branch: Total sales across different branches.
Gross Income vs. Rating: Scatter plot comparing gross income and ratings, categorized by product line.
Saved Outputs:

All visualizations are saved as .png files for easy reference.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/PARASMANI-KHUNTE/Supermarket-Sales-Analysis.git
cd supermarket-sales-analysis
Install required libraries:

bash
Copy code
pip install pandas matplotlib seaborn
Add the dataset file:

Place the supermarket_sales - Sheet1.csv file in the same directory as the script.
Usage
Run the script to analyze and visualize the data:

bash
Copy code
python analyze_supermarket_sales.py
The script will generate visualizations and save them as PNG files in the working directory.

Visualizations
Average Rating by Product Line:

Sales by City:

Payment Method Distribution:

Total Sales by Branch:

Gross Income vs. Rating:
