import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    file_path = './TKM Orders.xlsx'
    df = pd.read_excel(file_path)

    # Convert object type columns to string
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str)

    # Define the columns to be visualized
    columns_to_visualize = [
        "Name", "Email", "Financial Status", "Paid at", "Fulfilled at", "Accepts Marketing", "Currency",
        "Subtotal", "Shipping", "Total", "Shipping Method", "Created at", "Lineitem name", "Lineitem quantity",
        "Lineitem price", "Billing Name", "Billing Address1", "Billing City", "Billing Phone",
        "Shipping Name", "Shipping Address1", "Shipping City", "Shipping Phone", "Payment Method",
        "Payment Reference", "Vendor", "Payment ID", "Payment References"
    ]

    # Filter dataframe to include only specified columns
    df = df[columns_to_visualize]
    return df