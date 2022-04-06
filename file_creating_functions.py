import json
import csv
import requests
import os.path


def get_page(page_name, url, header_s):
    """
    Формирует html страницу в подкаталоге pages.
    :param page_name: Имя для сохраняемой страницы, без разширения.
    :param url: Ссылка на веб-страницу хабра со статьями.
    :param header_s: Заголовки для передачи на сайт, чтобы походить на реального пользователя.
    :return: Строка с относительной ссылкой на html страницу в подкаталоге html_pages
    """
    response = requests.get(url=url, headers=header_s)
    src = response.text

    if not os.path.exists('./html_pages'):
        os.mkdir('./html_pages')

    page_path = f'./html_pages/{page_name}.html'
    if not os.path.exists(page_path):
        with open(page_path, 'w', encoding='utf-8') as file:
            file.write(src)
    else:
        print('Файл с таким именем уже существует.')

    return page_path


def write_data_to_json(file_name, data):
    """
    Записывает собранные данные в файл формата json и помещает его в каталог json_data
    :param file_name: Желаемое имя файла без разширения.
    :param data: Список собранных данных.
    :return: Строка с относительной ссылкой на json файл в подкаталоге json_data.
    """

    if not os.path.exists('./json_data'):
        os.mkdir('./json_data')

    file_path = f'./json_data/{file_name}.json'
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
        print('Файл с таким именем уже существует.')

    return file_path


def write_data_to_csv(file_name, data):
    """
    Записывает собранные данные в файл формата csv и помещает его в каталог csv_data
    :param file_name: Желаемое имя файла без разширения.
    :param data: Список собранных данных.
    :return: Строка с относительной ссылкой на csv файл в подкаталоге csv_data.
    """

    if not os.path.exists('./csv_data'):
        os.mkdir('./csv_data')

    file_path = f'./csv_data/{file_name}.csv'
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    else:
        print('Файл с таким именем уже существует.')

    return file_path
