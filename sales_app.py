import streamlit as st
import pandas as pd

st.title("📊 Sales Dashboard App")
st.subheader("Filter and visualize product sales by category")

data = {
    "Product": ["Laptop", "Shirt", "Mobile", "Jeans", "Tablet"],
    "Category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "Sales": [50000, 15000, 30000, 20000, 25000]
}

df = pd.DataFrame(data)

st.sidebar.header("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

filtered_df = df[df["Category"] == category]

st.write(f"### Showing data for: {category}")
st.dataframe(filtered_df)

st.write("### Sales Trend")
st.line_chart(filtered_df.set_index("Product")["Sales"])
