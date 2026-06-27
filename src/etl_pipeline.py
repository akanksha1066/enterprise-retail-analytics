import os
import pandas as pd

def run_etl(input_file, output_dir):
    print("ETL Pipeline Started using Pandas...")
    
    # 1. Extract: Load CSV Data
    df = pd.read_csv(input_file)
    
    # 2. Transform: Data Cleaning & Feature Engineering
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    df['Total_Revenue'] = round(df['Quantity'] * df['Price_Per_Unit'], 2)
    
    # Filter out invalid values
    df_cleaned = df[(df['Quantity'] > 0) & (df['Price_Per_Unit'] > 0)]
    
    # 3. Aggregations
    # Metric A: Category wise Revenue
    category_metrics = df_cleaned.groupby('Category').agg(
        Category_Revenue=('Total_Revenue', 'sum'),
        Total_Quantity_Sold=('Quantity', 'sum')
    ).reset_index()
        
    # Metric B: City wise Sales Performance
    city_metrics = df_cleaned.groupby('City').agg(
        City_Revenue=('Total_Revenue', 'sum')
    ).reset_index()
    
    # 4. Load: Save processed data to folders
    os.makedirs(f"{output_dir}/cleaned_transactions", exist_ok=True)
    os.makedirs(f"{output_dir}/category_summary", exist_ok=True)
    os.makedirs(f"{output_dir}/city_summary", exist_ok=True)
    
    df_cleaned.to_csv(f"{output_dir}/cleaned_transactions/data.csv", index=False)
    category_metrics.to_csv(f"{output_dir}/category_summary/data.csv", index=False)
    city_metrics.to_csv(f"{output_dir}/city_summary/data.csv", index=False)
    
    print("ETL Job Completed Successfully. Artifacts saved!")

if __name__ == "__main__":
    run_etl("data/raw/transactions.csv", "data/processed")