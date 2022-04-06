from bs4 import BeautifulSoup
from config import *
from habr_search_functions import *
from file_creating_functions import *


def get_posts_info(path_to_page):
    """
    Формирует список необходимых данных о статье (id, дата и время публикации, название, ссылка, оценка, теги).
    :param path_to_page: Путь к сохранённой странице из которой будут браться данные.
    :return: Список с кортежами полученных данных.
    """
    with open(path_to_page, encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    all_articles_blocks = soup.find_all('article', class_='tm-articles-list__item')
    clear_info = []
    for block in all_articles_blocks:
        article_id = get_article_id(article_soup_block=block)
        article_time = get_article_datetime(article_soup_block=block)
        article_title = get_article_title(article_soup_block=block)
        article_url = get_article_url(article_soup_block=block)
        article_mark = get_article_mark(article_soup_block=block)
        article_tags = get_article_tags(article_soup_block=block)
        clear_info.append((article_id, article_time, article_title, article_url, article_tags, article_mark))

    return clear_info


def main():
    # path_to_page = get_page('index', habr_url, headers)
    path_to_page = get_page('study_first_page', habr_study_url, headers)
    posts_data = get_posts_info(path_to_page=path_to_page)
    # write_data_to_json('test', posts_data)
    write_data_to_csv('test2', posts_data)


if __name__ == '__main__':
    main()
