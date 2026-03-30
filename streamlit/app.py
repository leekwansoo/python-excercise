import streamlit as st 
st.title("My first Streamlit app")
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx","pdf"])
if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("Filename:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", uploaded_file.size, "bytes")
    file_name = uploaded_file.name
    file_extension = file_name.split(".")[-1].lower()
    if file_extension == "csv":
        st.write("Processing CSV file...")
        # save this file in the csv directory
        with open(f"csv/{file_name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("File saved successfully!")

        # Add your CSV processing code here
                 
    elif file_extension == "xlsx":
        st.write("Processing Excel file...")
        # save this file in the excel directory
        with open(f"excel/{file_name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("File saved successfully!")
        # Add your Excel processing code here
    elif file_extension == "pdf":
        st.write("Processing PDF file...")
        # save this file in the pdf directory
        with open(f"pdf/{file_name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.write("File saved successfully!")
        # display the content of the uploaded PDF File in the Streamlit app
        st.write("Displaying PDF file...")
        with open(f"pdf/{file_name}", "rb") as f:
            pdf_data = f.read()
        # display data in the Streamlit app
        st.write(pdf_data)
        
        # Add your PDF processing code here
    else:
        st.write("Unsupported file type.")
