import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from main import file_process_csv, file_process_pdf
from excel2csv import convert_excel_to_csv
st.title("My first Streamlit app")
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx","pdf"])
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", uploaded_file.size, "bytes")
    file_name = uploaded_file.name
    file_path = f"data/{file_name}"
    file_extension = file_name.split(".")[-1].lower()
    if file_extension == "csv":
        st.write("Processing CSV file...")
        # save this file in the data directory
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("File saved successfully!")
        button = st.button("Process CSV file", key="process_csv")
        if button:
            result = file_process_csv(file_path)
            if result:
                st.write(result["result"])
                 
    elif file_extension == "xlsx":
        st.write("Processing Excel file...")
        # save this file in the data directory
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("File saved successfully!")
        button = st.button("Convert Excel to CSV and process", key="convert_excel")
        if button:
            csv_file = convert_excel_to_csv(file_path)
            if csv_file:
                result = file_process_csv(csv_file[0])  # Process the first CSV file generated
                if result:
                    st.write(result["result"])

        # Add your Excel processing code here
    elif file_extension == "pdf":
        st.write("Processing PDF file...")
        # save this file in the data directory
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("File saved successfully!")
        # display the content of the uploaded PDF File in the Streamlit app
        button = st.button("Process PDF file", key="process_pdf")
        if button:
            result = file_process_pdf(file_path)
            if result:
                st.write(result["result"])

        
        # Add your PDF processing code here
    else:
        st.write("Unsupported file type.")
