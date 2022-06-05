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

# def show_load_pdf(file_path):
#     base64_pdf = base64.b64encode(file_path.read()).decode('utf-8')
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)    

model = joblib.load('classificator_extra.pkl')

pdf_path = 'Дата-сет для задачи №1\\Разметка\\'

# uploaded_pdf = st.file_uploader("Загрузите PDF file", accept_multiple_files=True, type=['pdf'])

# st.header('Просмотр TAB1')
# Tab1 = pd.read_csv('answer_df.csv')
# clicked1 = st.checkbox("View Tab1")



# if uploaded_pdf:
    # st.write(type(uploaded_pdf[0]))

pdf_files = os.listdir('Дата-сет для задачи №1\\Разметка') # uploaded_pdf

# Обработка pdf
pdf_df = pdf_predict(pdf_files, model, pdf_path)



# Отрисовка таблицы 1
file_names = [i for i in pdf_files]
# if clicked1:
    # st.dataframe(Tab1[Tab1['Наименование_файла_с_описанием'].isin(file_names)])
                                        # col1, col2, col3 = st.columns(3)
                                        # col1.metric("Temperature", "70 °F", "1.2 °F")
                                        # col2.metric("Wind", "9 mph", "-8%")
                                        # col3.metric("Humidity", "86%", "4%") 

# clicked2 = st.checkbox("Показать преобразование")

# Вывод информации по пдф
show_df = []
answ = pd.read_csv('answer_df.csv', index_col=0)
print(answ[answ['Наименование_файла_с_описанием'].isin(pdf_files)])

for file in pdf_files:
    # file = file_.name
    tmp_df = pdf_df[pdf_df.file_name==file][model.classes_]
    tmp_df = tmp_df.sort_values(axis=1, by=tmp_df.index[0], ascending=False).iloc[:, 0:3]
    tmp_df['file_name'] = file
    tmp_df['unit'] = pdf_df[pdf_df.file_name==file]['unit']

    tmp_df = tmp_df.astype(str)
    show_df.append(tmp_df[['file_name', 'unit']])

# print(show_df[0])

# print('2'*50)
for file in show_df:  
    answ.loc[answ['Наименование_файла_с_описанием'] == file.file_name.values[0], 'Единица_измерения_СИ'] = file.unit.values[0]


print(answ[answ['Наименование_файла_с_описанием'].isin([file.file_name.values[0] for file in show_df])])
answ.to_csv('filled_answer.csv')


    # Tab1[Tab1['Наименование_файла_с_описанием']==file]['Единица_измерения_СИ'] = tmp_df['unit'].values
    # st.write(Tab1[Tab1['Наименование_файла_с_описанием']==file])
    # print(Tab1[Tab1['Наименование_файла_с_описанием']==file])
    # cols = st.columns((2,4))
    # if not clicked2:
    #     with cols[0]:
    #         st.dataframe(tmp_df.T)
        
    #     with cols[1]:
    #         st.header("A PDF")
    #         show_load_pdf(file_)   
    
    
    # st.write(tmp_df['unit'].values)
    # Tab2 = Tab1.copy()
    # Tab2[Tab2['Наименование_файла_с_описанием']==file]['Единица_измерения_СИ'] = tmp_df['unit'].values
    # st.dataframe(Tab2[Tab2['Наименование_файла_с_описанием'].isin(file_names)])
    # print(*show_df, sep='\n')

# Занесение информации в базу
# answ = pd.read_csv('answer_df.csv', index_col=0)
# for file_ in pdf_files
# answ