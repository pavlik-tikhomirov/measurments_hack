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
from streamlit_func import show_tab1, show_tab2, show_tab1_res, show_tab2_res, pdf_show, anal_show
import matplotlib.pyplot as plt


# def show_load_pdf(file_path):
#     base64_pdf = base64.b64encode(file_path.read()).decode('utf-8')
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)    


tab1 = pd.read_csv('csv_files\\answer_df.csv') # кусок незаполненной базы 'Дата-сет_Задача 1.csv'

tab2 = pd.read_csv('csv_files\\sample_data2_full.csv', index_col=0)
tab2.reset_index(drop=True, inplace=True)
cols = set(tab2.columns) - {'Дата_поверки_СИ'}
tab2 = tab2.sort_values(by='Дата_поверки_СИ').drop_duplicates(cols)

model = joblib.load('classificator_extra.pkl')

pdf_path = 'test_files\\'

# ИНТЕРФЕЙС streamlit

st.title('СКАДСИ')
st.title('Команда Test123')
st.write('--'*30)

# pdf загрузчик
uploaded_pdf = st.file_uploader("Загрузите PDF file", accept_multiple_files=True, type=['pdf'])

clicked1 = st.checkbox("View Tab1 fragment")
show_tab1(tab1, clicked1, uploaded_pdf)
clicked2 = st.checkbox("View Tab2 fragment")
show_tab2(tab2, clicked2, uploaded_pdf)

if uploaded_pdf:

    # обработка пдф
    pdf_files = [i.name for i in uploaded_pdf] # uploaded_pdf
    pdf_df = pdf_predict(pdf_files, model, pdf_path)

    # вывод итоговых таблиц
    clicked1_result = st.checkbox("View Tab1 filled fragment")
    tab1, show_df = show_tab1_res(clicked1_result, pdf_files, pdf_df, model, tab1)
    clicked2_result  = st.checkbox("View Tab2 filled fragment")
    tab2 = show_tab2_res(clicked2_result, tab1, tab2, pdf_files)
 
    # вывод результатов обработки pdf    
    clicked_pdf = st.checkbox("View pdf preprocessing result")
    pdf_show(clicked_pdf, show_df, uploaded_pdf)

    # вывод аналитики по долям отечественным
    clicked_anal = st.checkbox("View base2 analitics")
    anal_show(clicked_anal, tab1, tab2)

