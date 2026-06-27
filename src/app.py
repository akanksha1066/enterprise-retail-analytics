import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Enterprise Retail Analytics", layout="wide")

st.title("📊 Enterprise Retail Analytics Platform")
st.markdown("Real-time executive insights dashboard powered by ETL Pipeline.")

# Direct paths to the processed data files
clean_path = "data/processed/cleaned_transactions/data.csv"
category_path = "data/processed/category_summary/data.csv"
city_path = "data/processed/city_summary/data.csv"

if os.path.exists(clean_path) and os.path.exists(category_path) and os.path.exists(city_path):
    df_clean = pd.read_csv(clean_path)
    df_category = pd.read_csv(category_path)
    df_city = pd.read_csv(city_path)
    
    # --- KPI METRICS ---
    total_rev = df_clean['Total_Revenue'].sum()
    total_sales = df_clean['Quantity'].sum()
    avg_ticket = df_clean['Total_Revenue'].mean()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Revenue", f"${total_rev:,.2f}")
    col2.metric("📦 Units Sold", f"{total_sales:,}")
    col3.metric("💳 Avg Transaction Value", f"${avg_ticket:.2f}")
    
    st.markdown("---")
    
    # --- CHARTS SECTION ---
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.subheader("Category-wise Revenue Performance")
        fig_cat = px.bar(df_category, x='Category', y='Category_Revenue', 
                         text_auto='.2s', color='Category')
        st.plotly_chart(fig_cat, use_container_width=True)
        
    with right_col:
        st.subheader("Geographical Sales Distribution")
        fig_city = px.pie(df_city, values='City_Revenue', names='City', hole=0.4)
        st.plotly_chart(fig_city, use_container_width=True)
        
    # --- DATA VIEW ---
    st.subheader("📋 Sample Processed Enterprise Transactions")
    st.dataframe(df_clean.head(100), use_container_width=True)
else:
    st.error("Data files missing! Please make sure you ran python src/etl_pipeline.py successfully.")