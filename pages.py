import streamlit as st
import plotly.express as px

categories = {
    "Personal Info": ["Name", "Email", "Billing Name", "Billing Address1", "Billing City", "Billing Phone",
                      "Shipping Name", "Shipping Address1", "Shipping City", "Shipping Phone"],
    "Financial Info": ["Financial Status", "Subtotal", "Shipping", "Total", "Currency", "Payment Method",
                       "Payment Reference", "Payment ID", "Payment References"],
    "Order Info": ["Paid at", "Fulfilled at", "Accepts Marketing", "Created at", "Lineitem name", "Lineitem quantity",
                   "Lineitem price", "Vendor", "Shipping Method"]
}


def overview_page(df):
    st.write("## Overview")
    selected_category = st.selectbox(
        "Select Category", list(categories.keys()))
    existing_columns = [
        col for col in categories[selected_category] if col in df.columns]
    if existing_columns:
        st.write(df[existing_columns])
    else:
        st.write("No columns found for the selected category.")
    st.write("### Data Summary")
    st.write(
        "Below is a summary of the dataset, giving you a quick snapshot of the data.")
    st.write(df.describe())


def histograms_page(df):
    st.write("## Histograms")
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        st.write(f"#### {column}")
        fig = px.histogram(df, x=column, labels={
                           column: column, 'count': 'Frequency'})
        fig.update_layout(
            margin=dict(l=20, r=20, t=30, b=20),
            xaxis_title=column,
            yaxis_title='Frequency',
            xaxis=dict(tickangle=-45),
            bargap=0.2
        )
        st.plotly_chart(fig, use_container_width=True)


def bar_charts_page(df):
    st.write("## Bar Charts")
    columns_to_exclude = ["Name", "Email", "Payment References", "Payment ID", "Payment Reference",
                          "Shipping Phone", "Shipping Address1", "Shipping Name", "Billing Phone",
                          "Billing Address1", "Billing City", "Billing Name", "Lineitem name",
                          "Created at", "Currency", "Fulfilled at", "Paid at", "Shipping City"]
    for column in df.select_dtypes(include=['object']).columns:
        if column in columns_to_exclude:
            continue
        st.write(f"#### {column}")
        bar_data = df[column].value_counts().reset_index()
        bar_data.columns = [column, 'count']
        fig = px.bar(bar_data, x=column, y='count', labels={
                     column: column, 'count': 'Count'})
        fig.update_layout(
            margin=dict(l=20, r=20, t=30, b=20),
            xaxis_title=column,
            yaxis_title='Count',
            xaxis=dict(tickangle=-45),
            bargap=0.2
        )
        st.plotly_chart(fig, use_container_width=True)


def pie_charts_page(df):
    st.write("## Pie Charts")
    columns_to_exclude = ["Name", "Email", "Payment References", "Payment ID", "Payment Reference",
                          "Shipping Phone", "Shipping Address1", "Shipping Name", "Billing Phone",
                          "Billing Address1", "Billing City", "Billing Name", "Lineitem name",
                          "Created at", "Currency", "Fulfilled at", "Paid at", "Shipping City"]
    top_n = st.slider("Number of Top Categories in Pie Charts", 1, 10, 5)
    for column in df.select_dtypes(include=['object']).columns:
        if column in columns_to_exclude:
            continue
        st.write(f"#### {column}")
        pie_data = df[column].value_counts().nlargest(top_n).reset_index()
        pie_data.columns = [column, 'count']
        fig = px.pie(pie_data, values='count', names=column, hole=0.4)
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            'margin': dict(l=0, r=0, t=30, b=0)
        })
        fig.update_traces(marker=dict(line=dict(color='#FFFFFF', width=2)))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("---")