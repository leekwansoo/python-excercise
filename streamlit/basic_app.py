import streamlit as st

# Basic use case: draw Markdown-formatted text
st.write("Hello, *World!* :sunglasses:")

# You can also display other content
st.write("Here are some more examples:")

# Display a simple dataframe
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})
st.write(df)

# Display a chart
st.line_chart(df.set_index('Name'))