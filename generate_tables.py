import pandas as pd

df = pd.read_csv('data.csv')
product = df[['Product ID', 'Category', 'Unit Price', 'Region']]
order = df[['Order ID', 'Product ID', 'Quantity Sold', 'Discount','Shipping Cost','Date of Sale']]
customer = df[['Order ID','Customer Name', 'Customer Email', 'Customer Address']]

product.to_csv('product.csv', index=False) 
order.to_csv('order.csv', index=False) 
customer.to_csv('customer.csv', index=False) 