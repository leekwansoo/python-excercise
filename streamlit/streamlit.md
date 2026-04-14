## What is Streamlit

Streamlit the most powerful way to build data apps, including the ability to display and style data, draw charts and maps, add interactive widgets, customize app layouts, cache computation, and define themes.


##  Setting up a local development environment

1.  create virtual environment .venv 

python -m venv .venv # 아래의 Terminal에서 실행

2.  activate the virtual environment

.venv/Script/activate   # 아래의 Terminal에서 실행

3. Install necessary dependencies

pip install streamlit

4. change directory to "streamlit" with

cd streamlit

5. Create a app.py file with following content 

import streamlit as st 
st.title("My first Streamlit app")
 ------
 streamlit and python codes
 ------

6.  run the file with following command at the terminal

streamlit run app.py

load iris_data.csv in the file_upload menu

then hit the Process CSV file