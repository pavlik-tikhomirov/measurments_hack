import os
import numpy as np
import pandas as pd
import fitz
from tqdm import tqdm
import re
import joblib
import streamlit as st
import base64
from functions import pdf_predict

def show_load_pdf(file_path):
    base64_pdf = base64.b64encode(file_path.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)    

model = joblib.load('classificator_extra.pkl')

pdf_path = 'Дата-сет для задачи №1\\Разметка\\'

uploaded_pdf = st.file_uploader("Загрузите PDF file", accept_multiple_files=True, type=['pdf'])
if uploaded_pdf:
    # st.write(type(uploaded_pdf[0]))

    pdf_files = uploaded_pdf # os.listdir('Дата-сет для задачи №1\\Разметка')[:5]

    # Обработка pdf
    pdf_df = pdf_predict(pdf_files, model, pdf_path)
    
    # Вывод информации по пдф
    show_df = []
    for file_ in pdf_files:
        file = file_.name
        tmp_df = pdf_df[pdf_df.file_name==file][model.classes_]
        tmp_df = tmp_df.sort_values(axis=1, by=tmp_df.index[0], ascending=False).iloc[:, 0:3]
        tmp_df['file_name'] = file
        tmp_df['unit'] = pdf_df[pdf_df.file_name==file]['unit']
        cols = tmp_df.columns[:3]
        # style_dict = {col: '{:,.2f%}.format' for col in cols}
        # tmp_df = tmp_df.style.format(style_dict)     

        cols = st.columns(([2,5]))
        with cols[0]:
            #show_df.append(tmp_df)
            st.dataframe(tmp_df)

        with cols[1]:
            st.header("A PDF")
            show_load_pdf(file_)     

    # print(*show_df, sep='\n')

# Занесение информации в базу