import streamlit as st
st.title("My first Streamlit app")
st.write("It contains some sample code.")
if st.button("Click me!"):
    st.write("Show me Your Data!")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt"])
    if uploaded_file is not None:
        st.write("File name:", uploaded_file.name)
        st.write("File type:", uploaded_file.type)
        st.write("File size:", uploaded_file.size, "bytes")
