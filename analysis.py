import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')
df['basket_date'] = pd.to_datetime(df['basket_date'])
df['month'] = df['basket_date'].dt.month
df['year'] = df['basket_date'].dt.year

# Chart 1 - Top 10 products
top_products = df.groupby('product_id')['basket_count'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
top_products.plot(kind='bar')
plt.title('Top 10 Products by Quantity')
plt.xlabel('Product ID')
plt.ylabel('Total Quantity')
plt.tight_layout()
plt.savefig('top_products.png')
plt.show()

# Chart 2 - Monthly orders
monthly = df.groupby(['year', 'month'])['basket_count'].sum()
plt.figure(figsize=(8, 5))
monthly.plot(kind='bar')
plt.title('Monthly Orders')
plt.xlabel('Year - Month')
plt.ylabel('Total Orders')
plt.tight_layout()
plt.savefig('monthly_orders.png')
plt.show()

# Chart 3 - Top 10 active customers
top_customers = df.groupby('customer_id')['basket_count'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 5))
top_customers.plot(kind='bar')
plt.title('Top 10 Active Customers')
plt.xlabel('Customer ID')
plt.ylabel('Total Orders')
plt.tight_layout()
plt.savefig('top_customers.png')
plt.show()