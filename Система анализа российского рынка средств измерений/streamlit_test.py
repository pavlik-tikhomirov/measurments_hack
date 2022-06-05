import streamlit as st
import os
import pandas as pd
import numpy as np
import base64
from PIL import Image

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def show_load_pdf(file_path):
    base64_pdf = base64.b64encode(file_path.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)    

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

def st_display_pdf(pdf_file):
    with open(pdf_file,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<embed src=”data:application/pdf;base64,{base64_pdf}” width=”700″ height=”1000″ type=”application/pdf”>'
    st.markdown(pdf_display, unsafe_allow_html=True)


st.title(""" 
СКАДСИ
""")
st.write('project by Test123')

st.header("Загрузка\n")
load = st.selectbox(
     'Что будем загружать?',
     ('PDF Документ', 'CSV файл', 'Ничего'))

if(load=='CSV файл'):
    uploaded_csv = st.file_uploader("Загрузите CSV файл",type=['csv'])
    if uploaded_csv:
        file_details = {"FileName":uploaded_csv.name ,"FileType":uploaded_csv.type,"FileSize":uploaded_csv.size}
        st.write(file_details)
        clicked1 = st.checkbox("View CSV file")
        df = pd.read_csv(uploaded_csv, delimiter=';', encoding='windows-1251')
        if clicked1:
            st.dataframe(df)

if(load=='PDF Документ'):
    uploaded_pdf = st.file_uploader("Загрузите PDF file", accept_multiple_files=True)
    if uploaded_pdf:
        st.write(type(uploaded_pdf[0]))
        col1, col2 = st.columns(2)
        with col1:
            st.header("New Data")
            st.image("https://static.streamlit.io/examples/cat.jpg")

        with col2:
            st.header("A PDF")
            show_load_pdf(uploaded_pdf[0])           

st.header('Просмотр TAB1')
Tab1 = pd.read_csv('C:/Users/Danya_Laptop/Desktop/Хакатон/cистема_анализа_российского_рынка_средств_измерений/Tab1.csv', delimiter=';', encoding='windows-1251')
clicked = st.checkbox("View Tab1")
if clicked:
    st.dataframe(Tab1)
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

camera = st.camera_input("Take a picture")
if camera is not None:
    image = Image.open(camera)
    st.image(image, caption='Результат сканирования')  


uploaded_png = st.file_uploader("Choose a PNG file", accept_multiple_files=True)
if uploaded_png:
    for i in range(len(uploaded_png)):
        st.image(uploaded_png[i], caption='Sunrise by the mountains')


col1, col2 = st.columns(2)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A PDF")
    show_pdf("C:/Users/Danya_Laptop/Desktop/Хакатон/cистема_анализа_российского_рынка_средств_измерений/Разметка/2005-30815-05.pdf")   

