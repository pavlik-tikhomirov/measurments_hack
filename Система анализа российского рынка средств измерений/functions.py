
import pandas as pd
import fitz
from tqdm import tqdm


def pdf_predict(pdf_files, model, pdf_path):
    data_dict = {}
    for file in tqdm(pdf_files):
        file_name = file.name
        text=''
        
        doc = fitz.open(pdf_path+file_name)  #  ('Дата-сет для задачи №1\\Разметка\\'+file_name)
        page_count = doc.page_count
        for n in range(page_count):
                page = doc.load_page(n)
                text += page.get_text()
        data_dict[file_name] = text

    pdf_df = {i: list(item) for i, item in enumerate(data_dict.items())}
    pdf_df = pd.DataFrame.from_dict(pdf_df, orient='index', columns=['file_name', 'text'])
    pdf_df[model.classes_]=model.predict_proba(pdf_df.text)
    pdf_df['unit']=model.predict(pdf_df.text)
    return pdf_df