import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "supermarket_sales - Sheet1.csv"
data = pd.read_csv(file_path)

# Data Cleaning
data['Date'] = pd.to_datetime(data['Date'])
data['Time'] = pd.to_datetime(data['Time'], format='%H:%M').dt.time
data.rename(columns=lambda x: x.strip().replace(' ', '_').lower(), inplace=True)

# Summary of the dataset
print("Dataset Summary:")
print(data.info())
print("\nDataset Head:")
print(data.head())

# Visualizations
sns.set_theme(style="whitegrid")

# 1. Average Rating by Product Line
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='product_line', y='rating', estimator='mean', ci=None, palette='viridis')
plt.xticks(rotation=45)
plt.title('Average Rating by Product Line')
plt.ylabel('Average Rating')
plt.xlabel('Product Line')
plt.tight_layout()
plt.savefig('average_rating_by_product_line.png')
plt.show()

# 2. Sales by City
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='city', palette='Set2')
plt.title('Number of Sales by City')
plt.xlabel('City')
plt.ylabel('Number of Sales')
plt.tight_layout()
plt.savefig('sales_by_city.png')
plt.show()

# 3. Payment Method Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='payment', palette='muted', order=data['payment'].value_counts().index)
plt.title('Payment Method Distribution')
plt.xlabel('Payment Method')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('payment_method_distribution.png')
plt.show()

# 4. Total Sales by Branch
plt.figure(figsize=(8, 6))
total_sales_branch = data.groupby('branch')['total'].sum().reset_index()
sns.barplot(data=total_sales_branch, x='branch', y='total', palette='coolwarm')
plt.title('Total Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('total_sales_by_branch.png')
plt.show()

# 5. Gross Income vs. Rating
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='rating', y='gross_income', hue='product_line', palette='viridis')
plt.title('Gross Income vs. Rating by Product Line')
plt.xlabel('Rating')
plt.ylabel('Gross Income')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('gross_income_vs_rating.png')
plt.show()
