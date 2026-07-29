import csv
import datetime

# create a dictionary for mapping
products = {
    'P001': {'name': 'Wireless Headphones', 'price': 100},
    'P002': {'name': 'Laptop Backpack', 'price': 60},
    'P003': {'name': 'Bluetooth Speaker', 'price': 50},
    'P004': {'name': 'USB Flash Drive', 'price': 20},
    'P005': {'name': 'Mobile Phone Case', 'price': 15},
    'P006': {'name': 'Wireless Mouse', 'price': 30},
    'P007': {'name': 'Laptop Stand', 'price': 40},
    'P008': {'name': 'HDMI Cable', 'price': 15},
    'P009': {'name': 'Smartphone', 'price': 600},
    'P010': {'name': 'External Hard Drive', 'price': 100},
}

def get_product_details(id):
    return products.get(id)

product_sales_data = []
with open('product_sales.txt', 'r') as sales_file:
    sales_items = sales_file.readlines()
    for index, product in enumerate(sales_items):
        product_id = str(product.strip())
        product_detail_dict = get_product_details(product_id)

        # prepare data to put
        current_date = datetime.datetime.now().strftime("%#m/%#d/%Y")
        sequence_id = index + 1
        product_name = product_detail_dict['name']
        product_price = product_detail_dict['price']

        # add data to list
        product_sales_data.append([current_date, sequence_id, product_id, product_name, product_price])

with open('product_sales.csv', 'w', newline='') as product_sales_file:
    csv_writer = csv.writer(product_sales_file)
    csv_writer.writerow(['current_date', 'sale_id', 'product_id', 'name', 'price'])
    csv_writer.writerows(product_sales_data)