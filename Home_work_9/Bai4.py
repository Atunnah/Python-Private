import pandas as pd
import numpy as np

file_path = "D:\HIT Python\Home_work_9\Car_sales.csv"
df = pd.read_csv(file_path)
print("Data Frame: \n", df)

num_rows, num_columns = df.shape
print(f"So hang: {num_rows} \nSo cot: {num_columns}")

print("Vi tri thieu du lieu: ", df.isnull())
df['Sales_in_thousands'].fillna(0.0, inplace=True)
mean_resale_price = df['__year_resale_value'].mean()
df['__year_resale_value'].fillna(mean_resale_price, inplace=True)
median_car_price = df['Price_in_thousands'].median()
df['Price_in_thousands'].fillna(median_car_price, inplace=True)
print("Vi tri thieu du lieu: \n", df.isnull())
print("Data Frame: \n", df)

print(df.columns)
numeric_cols = ['Sales_in_thousands', '__year_resale_value', 'Price_in_thousands', 'Engine_size', 'Horsepower', 'Wheelbase', 'Width', 'Length', 'Curb_weight', 'Fuel_capacity', 'Fuel_efficiency', 'Power_perf_factor']
string_cols = ['Manufacturer', 'Model', 'Vehicle_type']
date_cols = ['Latest_Launch']
violations = {}

for col in numeric_cols:
    try:
        df[col] = pd.to_numeric(df[col], errors='raise', downcast='float')
    except pd.errors.OverflowError as e:
        print(f"Overflow error in column {col}: ", e)
    except pd.errors.InvalidIndexError as e:
        print(f"Invalid index error in column {col}: ", e)
    except pd.errors.ParserError as e:
        violations[col] = df[df[col].apply(lambda x : not pd.to_numeric(x, errors='coerce')).index.tolist()]

for col in date_cols:
    try:
        df[col] = pd.to_datetime(df[col], errors='raise', format='%Y-%m-%d')
    except pd.errors.OverflowError as e:
        print(f"Overflow error in column {col}: ", e)
    except pd.errors.ParserError as e:
        violations[col] = df[df[df[col].apply(lambda x : not pd.to_datetime(x, errors='coerce')).index.tolist()]]

for col in string_cols:
    df[col] = df[col].astype(str)

print("Row with incorrect data types: \n", violations)
