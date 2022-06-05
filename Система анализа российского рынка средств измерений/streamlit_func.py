import streamlit as st
import base64
import re

def show_tab1(tab, clicked, uploaded):
    if clicked:
        if uploaded:
            file_names = [i.name for i in uploaded]
            st.dataframe(tab[tab['Наименование_файла_с_описанием'].isin(file_names)])
        else:
            st.dataframe(tab.sample(5))
    else:
        pass

def show_tab2(tab, clicked, uploaded):
    if clicked:
        if uploaded:
            file_names = [i.name for i in uploaded]
            st.dataframe(tab[tab['Наименование_файла_с_описанием'].isin(file_names)])
        else:
            st.dataframe(tab.sample(5))
    else:
        pass

def show_tab1_res(clicked, pdf_files, pdf_df, model, tab1):

    show_df = []
    for file in pdf_files:
        tmp_df = pdf_df[pdf_df.file_name==file][model.classes_]
        tmp_df = tmp_df.sort_values(axis=1, by=tmp_df.index[0], ascending=False).iloc[:, 0:3]
        tmp_df['file_name'] = file
        tmp_df['unit'] = pdf_df[pdf_df.file_name==file]['unit']
        tmp_df = tmp_df.astype(str)
        show_df.append(tmp_df)
    for file in show_df:  
        tab1.loc[tab1['Наименование_файла_с_описанием'] == file.file_name.values[0], 'Единица_измерения_СИ'] = file.unit.values[0]
    
    # tab1.to_csv('csv_files\\filled_answer.csv') 

    if clicked:
        st.dataframe(tab1[tab1['Наименование_файла_с_описанием'].isin(pdf_files)]) 
    return tab1, show_df

def show_tab2_res(clicked, tab1, tab2, pdf_files):
    
    tab2 = tab2.drop(columns='Единица_измерения_СИ').merge(tab1[['Наименование_файла_с_описанием','Номер_в_госреестре', 'Единица_измерения_СИ']],
                        how='left',
                        on=['Наименование_файла_с_описанием', 'Номер_в_госреестре'])
    
    cols = list(tab2.columns)
    cols = cols[:2] + [cols[-1]] + cols[2:-1]
    tab2 = tab2[cols]
    if clicked:
        st.dataframe(tab2[tab2['Наименование_файла_с_описанием'].isin(pdf_files)])

    # tab2.to_csv('csv_files\\sample_data2_full.csv')    
    return tab2

def pdf_show(clicked, show_df, uploaded_pdf):
    if clicked:
        def show_load_pdf(file_path):
            base64_pdf = base64.b64encode(file_path.read()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="400" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)  
            pass
        
        for i, file_ in enumerate(uploaded_pdf):

            cols = st.columns([2, 4])
            with cols[0]:
                st.dataframe(show_df[i].T)
            
            with cols[1]:
                show_load_pdf(file_) 

def anal_show(clicked, tab1, tab2):
    
    if clicked:
        def mother_market_parts(comp_list):
            mother_comps=0
            for comp in comp_list:
                if len(re.findall("([А-я])", comp)) / (len(re.findall("([A-z])", comp)) + 1e-4) > 1:
                    mother_comps += 1
            return mother_comps / len(comp_list)

        full_data = tab2.drop(columns='Единица_измерения_СИ').merge(tab1[['Наименование_файла_с_описанием','Номер_в_госреестре', 'Единица_измерения_СИ']],
                                how='left',
                                on=['Наименование_файла_с_описанием', 'Номер_в_госреестре'])
        
        grouped_data = full_data.groupby('Единица_измерения_СИ').agg({'Производитель_СИ':lambda x: list(x)})

        result = grouped_data['Производитель_СИ'].apply(mother_market_parts)
        st.dataframe(result)
        return(result)
        


            
                                        # col1, col2, col3 = st.columns(3)
                                        # col1.metric("Temperature", "70 °F", "1.2 °F")
                                        # col2.metric("Wind", "9 mph", "-8%")
                                        # col3.metric("Humidity", "86%", "4%") )