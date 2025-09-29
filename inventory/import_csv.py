import os
import sys
import django
import pandas as pd

# Configurar Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inventory_Apis.settings")
django.setup()

from inventory.models import Product

# Ruta  CSV (point to the folder where is manage.py)
csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Grocery_Inventory_new_v1.csv')

# read CSV
df = pd.read_csv(csv_path)
#clean names 

df.columns = df.columns.str.strip()

# clean dates
for col in ['Date_Received', 'Last_Order_Date', 'Expiration_Date']:
    df[col] = pd.to_datetime(df[col], errors='coerce')  # convierte o pone NaT si hay error

#clean price:  $ y comas, change to a float
df['Unit_Price'] = df['Unit_Price'].replace('[\$,]', '', regex=True).astype(float)

# clean percentaje:  % y change to a float
df['percentage'] = df['percentage'].replace('%', '', regex=True).astype(float)

# Insertar datos en la base de datos
for _, row in df.iterrows():
    Product.objects.create(
        name=row['Product_Name'],
        category=row['Catagory'],
        supplier_name=row['Supplier_Name'],
        warehouse_location=row['Warehouse_Location'],
        status=row['Status'],
        product_id=row['Product_ID'],
        supplier_id=row['Supplier_ID'],
        date_received=row['Date_Received'],
        last_order_date=row['Last_Order_Date'],
        expiration_date=row['Expiration_Date'],
        stock_quantity=row['Stock_Quantity'],
        reorder_level=row['Reorder_Level'],
        reorder_quantity=row['Reorder_Quantity'],
        unit_price=row['Unit_Price'],
        sales_volume=row['Sales_Volume'],
        inventory_turnover_rate=row['Inventory_Turnover_Rate'],
        percentage=row['percentage']
    )

print("Successfully imported!")
