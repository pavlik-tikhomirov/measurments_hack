# Система анализа российского рынка средств измерений

## Команда test123

Основные файлы В папке "Система анализа российского рынка средств измерений":

 + [*main.py*](https://github.com/pavlik-tikhomirov/measurments_hack/blob/main/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%20%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D1%80%D1%8B%D0%BD%D0%BA%D0%B0%20%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%20%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D0%B9/main.py) – запускается через streamlit. Предсавляет собой пользовательский интерфейс со всем доступным функционалом
 + *functions.py* и *streamlit_func.py* – побочные функции для работы программы
 + *experiments.ipynb* – черновик и исследовательский блокнот (лучше не запускать)
 + *classificator_extra.pkl* – модель, обученная определять единицы измерения в документе
 + *file_small_names.txt* – технический файл (стало жалко удалять)
 
В папке "csv_files" находятся выборки из баз данных для удобной демонстрации возможностей системы

В папке ["test_files"](https://github.com/pavlik-tikhomirov/measurments_hack/tree/main/%D0%A1%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%20%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%20%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D1%80%D1%8B%D0%BD%D0%BA%D0%B0%20%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%20%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D0%B9/test_files) находятся pdf файлы, на которых можно испытать сервис

[Блокнот с обучением модели](https://colab.research.google.com/drive/14VYptm2d2_DPi3inHqrqQbUrZAGndwHX?usp=sharing)

## Инструкция

После клонирования репозитория (скачивания его архива) необходимо установить requirements.txt:

`pip install -r requirements.txt`

Далее необходимо запустить streamlit:

`streamlit run main.py`

Приложение откроется в браузере. После небольшой загрузки интерфейс будет готов

[Демнострация](https://drive.google.com/file/d/1sZECX3LwPNKj_rWs5X-OfESGcKNdVK9P/view?usp=sharing)

