from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import kagglehub
import os

def descargar_dataset(request):
    try:
        # Descargar dataset desde Kaggle
        dataset_path = kagglehub.dataset_download("willianoliveiragibin/grocery-inventory")
        # kagglehub devuelve la carpeta donde se descargó el dataset
        csv_file = os.path.join(dataset_path, "Grocery_Inventory new v1.csv")

        # Leer CSV con pandas
        df = pd.read_csv(csv_file)

        # Columnas que quieres devolver
        columns = ['Product_Name','Catagory','Supplier_Name','Warehouse_Location','Status',
                   'Product_ID','Supplier_ID','Date_Received','Last_Order_Date','Expiration_Date',
                   'Stock_Quantity','Reorder_Level','Reorder_Quantity','Unit_Price',
                   'Sales_Volume','Inventory_Turnover_Rate','percentage']

        df_filtrado = df[columns]
        data = df_filtrado.to_dict(orient='records')

        return JsonResponse(data, safe=False)

    except FileNotFoundError:
        return JsonResponse({'error': 'Archivo no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def log_in_interface(request):
    return render(request, 'log_in/log_in.html')
