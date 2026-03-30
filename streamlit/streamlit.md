## What is Streamlit

Streamlit the most powerful way to build data apps, including the ability to display and style data, draw charts and maps, add interactive widgets, customize app layouts, cache computation, and define themes.


##  Setting up a local development environment

1.  create virtual environment .venv 

python -m venv .venv # 아래의 Terminal에서 실행

2.  activate the virtual environment

.venv/Script/activate   # 아래의 Terminal에서 실행

3. Install necessary dependencies

pip install streamlit

4. Create a app.py file with following content 

import streamlit as st 
st.title("My first Streamlit app")

5.  run the file with following command at the terminal

streamlit run app.py