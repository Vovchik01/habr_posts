

def get_article_id(article_soup_block):
    """
    :param article_soup_block: Блок объекта BeautifulSoup в котором должны находиться необходимые данные.
    :return: Строка с id статьи
    """
    try:
        return article_soup_block.get('id')
    except Exception as ex:
        print(ex)
        return 'Ничего не нашлось'


def get_article_datetime(article_soup_block):
    """
    :param article_soup_block: Блок объекта BeautifulSoup в котором должны находиться необходимые данные.
    :return: Строка с датой и временем публикации статьи в формате 'yyyy-mm-dd, hh:mm'
    """
    try:
        return article_soup_block.find('span', class_='tm-article-snippet__datetime-published')\
            .find('time').get('title')
    except Exception as ex:
        print(ex)
        return 'Ничего не нашлось'


def get_article_title(article_soup_block):
    """
    :param article_soup_block: Блок объекта BeautifulSoup в котором должны находиться необходимые данные.
    :return: Строка с названием статьи.
    """
    try:
        return article_soup_block.find('a', class_='tm-article-snippet__title-link').text.strip()
    except Exception as ex:
        print(ex)
        return 'Ничего не нашлось'


def get_article_url(article_soup_block):
    """
    :param article_soup_block: Блок объекта BeautifulSoup в котором должны находиться необходимые данные.
    :return: Строка с url адресом статьи.
    """
    try:
        return f"https://habr.com{article_soup_block.find('a', class_='tm-article-snippet__title-link').get('href')}"
    except Exception as ex:
        print(ex)
        return 'Ничего не нашлось'


def get_article_mark(article_soup_block):
    """
    :param article_soup_block: Блок объекта BeautifulSoup в котором должны находиться необходимые данные.
    :return: Строка с оценкой статьи.
    """
    try:
        return article_soup_block.find('div', class_='tm-votes-meter').find('span', class_='tm-votes-meter__value').text
    except Exception as ex:
        print(ex)
        return 'Ничего не нашлось'


def get_article_tags(article_soup_block):
    """
    :param article_soup_block: Блок объекта BeautifulSoup в котором должны находиться необходимые данные.
    :return: Кортеж со строками. Теги относящиеся к статье.
    """
    try:
        tag_block_list = article_soup_block.find('div', class_='tm-article-snippet')\
            .find('div', class_='tm-article-snippet__hubs') \
            .find_all('span', class_='tm-article-snippet__hubs-item')
        tag_list = []
        for block in tag_block_list:
            tag = block.find('span').text
            tag_list.append(tag)
        return tag_list
    except Exception as ex:
        print(ex)
        return 'Ничего не нашлось'
