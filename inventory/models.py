from django.db import models

##create databse structure 
class Product(models.Model):
    name = models.CharField(max_length=200)                 # Product_Name
    category = models.CharField(max_length=100)             # Category
    supplier_name = models.CharField(max_length=200)        # Supplier_Name
    warehouse_location = models.CharField(max_length=100)   # Warehouse_Location
    status = models.CharField(max_length=50)               # Status
    product_id = models.CharField(max_length=50, unique=True) # Product_ID
    supplier_id = models.CharField(max_length=50)           # Supplier_ID
    date_received = models.DateField()                      # Date_Received
    last_order_date = models.DateField()                    # Last_Order_Date
    expiration_date = models.DateField(null=True, blank=True) # Expiration_Date
    stock_quantity = models.IntegerField()                 # Stock_Quantity
    reorder_level = models.IntegerField()                  # Reorder_Level
    reorder_quantity = models.IntegerField()               # Reorder_Quantity
    unit_price = models.FloatField()                        # Unit_Price
    sales_volume = models.IntegerField()                    # Sales_Volume
    inventory_turnover_rate = models.FloatField()           # Inventory_Turnover_Rate
    percentage = models.FloatField()   
