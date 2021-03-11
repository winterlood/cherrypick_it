import requests
from bs4 import BeautifulSoup
import traceback


def get_soup_obj_by_target_url(target_url):
    req = requests.get(target_url)
    req.encoding= None
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# NEWS
def crawl_TechNiddle():
    print('\n\n')
    print("#"*30)
    print("TECHNIDDLE CRAWL START")

    target_url = 'https://techneedle.com/archives/category/default'
    soup = get_soup_obj_by_target_url(target_url)

    # RESULT LIST INIT
    RESULT_LIST = []

    # GET POST ITEMS 
    post_box_list = soup.find_all('div',{'class':'post-inside'})

    # GET POST DATAS
    for post_box in post_box_list:  
        try:
            post_data_dict = dict()
            post_data_dict['source'] = 'https://techneedle.com'

            # GET POST THUMBNIAL
            img_tag = post_box.find('img')
            img_url = img_tag['src']
            post_data_dict['thumbnail_url'] = img_url

            # GET POST HEADLINE
            headline_tag = post_box.find('h2',{'class':'entry-title'})
            headline_text = headline_tag.getText()
            post_data_dict['headline'] = headline_text

            # GET POST LINK
            a_tag = headline_tag.find('a')
            news_link = a_tag['href']
            post_data_dict['url'] = news_link

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_NEWS'

        except Exception as e:
            print(e)
            print("테크니들 오류발생")

    print(">>> TECHNIDDLE CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST

def crawl_ITWorld():
    print('\n\n')
    print("#"*30)
    print("ITWORLD CRAWL START")

    target_url = 'https://www.itworld.co.kr/news'
    soup = get_soup_obj_by_target_url(target_url)

    # RESULT LIST INIT
    RESULT_LIST = []

    # GET POST ITEMS 
    post_box_list = soup.find_all('div',{'class':'news_list_'})

    # GET POST DATAS
    for post_box in post_box_list:
        try:
            post_data_dict = dict()
            post_data_dict['source'] = 'https://www.itworld.co.kr'

            # GET POST THUMBNIAL
            try:
                img_tag = post_box.find('img')
                img_url = img_tag['src']
                post_data_dict['thumbnail_url'] = f"https://www.itworld.co.kr{img_url}"
            except Exception:
                post_data_dict['thumbnail_url'] = ''

            # GET POST HEADLINE
            headline_tag = post_box.find('h4')
            headline_text = headline_tag.getText()
            post_data_dict['headline'] = headline_text

            # GET POST LINK
            a_tag = post_box.find('a')
            news_link = a_tag['href']
            post_data_dict['url'] = f"{post_data_dict['source']}{news_link}"

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_NEWS'

        except Exception as e:
            print(e)
            print("ITWORLD 오류발생")
    print(">>> ITWORLD CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST

def crawl_INews24():
    print('\n\n')
    print("#"*30)
    print("iNEWS24 CRAWL START")
    target_url = 'http://www.inews24.com/list/it'
    
    soup = get_soup_obj_by_target_url(target_url)

    # RESULT LIST INIT
    RESULT_LIST = []

    # GET POST ITEMS 
    post_box_list = soup.find_all('li',{'class','list'})

    # GET POST DATAS
    for idx,post_box in enumerate(post_box_list):
        try:
            post_data_dict = dict()
            post_data_dict['source'] = 'http://www.inews24.com/'

            # GET POST HEADLINE
            try:
                headline_section = post_box.find('div',{'class','thumb'})
                headline_tag = headline_section.find('a')
                headline_text = headline_tag.getText()
                post_data_dict['headline'] = headline_text
            except Exception as e:
                continue

            # GET POST THUMBNIAL
            try:
                img_tag = post_box.find('img')
                img_url = img_tag['src']
                post_data_dict['thumbnail_url'] = img_url
            except Exception:
                post_data_dict['thumbnail_url'] = ''

            # GET POST LINK
            a_tag = headline_section.find('a')
            news_link = a_tag['href']
            post_data_dict['url'] = f"http://www.inews24.com{news_link}"

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_NEWS'

        except Exception as e:
            print(e)
            print("INEWS24 오류발생")
            traceback.print_exc()


    print(">>> INEWS24 CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST


def crawl_Itdonga():
    print('\n\n')
    print("#"*30)
    print("IT DONGA CRAWL START")
    target_url = 'https://it.donga.com/news/'
    
    soup = get_soup_obj_by_target_url(target_url)

    # RESULT LIST INIT
    RESULT_LIST = []

    # GET POST ITEMS 
    post_box_list = soup.find_all('li',{'class','media'})

    # GET POST DATAS
    for idx,post_box in enumerate(post_box_list):
        try:
            post_data_dict = dict()
            post_data_dict['source'] = 'https://it.donga.com'

            # GET POST HEADLINE
            headline_tag = post_box.find('h5')
            headline_text = headline_tag.getText()
            post_data_dict['headline'] = headline_text

            # GET POST THUMBNIAL
            try:
                img_tag = post_box.find('img')
                img_url = img_tag['src']
                post_data_dict['thumbnail_url'] = img_url
            except Exception:
                post_data_dict['thumbnail_url'] = ''

            # GET POST LINK
            a_tag = post_box.find('a')
            news_link = a_tag['href']
            post_data_dict['url'] = f"https://it.donga.com{news_link}"

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_NEWS'

        except Exception as e:
            print(e)
            print("IT DONGA 오류발생")

    print(">>> IT DONGA CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST


# COLUMN
def crawl_Woowabros():
    print('\n\n')
    print("#"*30)
    print("WOOWABROS CRAWL START")
    target_url = 'https://woowabros.github.io'
    soup = get_soup_obj_by_target_url(target_url)

    # RESULT LIST INIT
    RESULT_LIST = []

    # GET POST ITEMS 
    post_box_list = soup.find_all('div',{'class':'list-module'})[:10]

    # GET POST DATAS
    for idx,post_box in enumerate(post_box_list):
        try:
            post_data_dict = dict()
            post_data_dict['source'] = 'https://woowabros.github.io'

            # GET POST HEADLINE
            headline_tag = post_box.find('h2')
            headline_text = headline_tag.getText()
            post_data_dict['headline'] = headline_text

            # GET POST LINK
            a_tag = post_box.find('a')
            news_link = a_tag['href']
            post_data_dict['url'] = f"{post_data_dict['source']}{news_link}"

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_COLUMN'

        except Exception as e:
            print(e)
            print("ITWORLD 오류발생")

    print(">>> WOOWABROS CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST

def crawl_Kakao():
    print('\n\n')
    print("#"*30)
    print("KAKAO CRAWL START")
    target_url = 'https://tech.kakao.com/blog/'
    
    soup = get_soup_obj_by_target_url(target_url)

    # RESULT LIST INIT
    RESULT_LIST = []

    # GET POST SECTION
    post_section = soup.find('ul',{'class':'list_post'})

    # GET POST ITEMS 
    post_box_list = post_section.find_all('li')

    # GET POST DATAS
    for idx,post_box in enumerate(post_box_list):
        try:
            post_data_dict = dict()
            post_data_dict['source'] = 'https://tech.kakao.com/blog/'

            # GET POST HEADLINE
            headline_tag = post_box.find('strong')
            headline_text = headline_tag.getText()
            post_data_dict['headline'] = headline_text

            # GET POST THUMBNIAL
            try:
                img_tag = post_box.find('img')
                img_url = img_tag['src']
                post_data_dict['thumbnail_url'] = img_url
            except Exception:
                post_data_dict['thumbnail_url'] = ''

            # GET POST LINK
            a_tag = post_box.find('a')
            news_link = a_tag['href']
            post_data_dict['url'] = f"{news_link}"

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_COLUMN'

        except Exception as e:
            print(e)
            print("KAKAO 오류발생")

    print(">>> KAKAO CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST

def crawl_Velog():
    print('\n\n')
    print("#"*30)
    print("Velog CRAWL START")
    target_url = 'https://velog.io/'
    
    soup = get_soup_obj_by_target_url(target_url)

    # RESULT LIST INIT
    RESULT_LIST = []

    # GET POST ITEMS 
    post_box_list = soup.find_all('div',{'class','sc-hzDkRC'})

    # GET POST DATAS
    for idx,post_box in enumerate(post_box_list):
        try:
            post_data_dict = dict()
            post_data_dict['source'] = 'https://velog.io/'

            # GET POST HEADLINE
            headline_tag = post_box.find('h4')
            headline_text = headline_tag.getText()
            post_data_dict['headline'] = headline_text

            # GET POST THUMBNIAL
            try:
                img_tag = post_box.find('img')
                img_url = img_tag['src']
                post_data_dict['thumbnail_url'] = img_url
            except Exception:
                post_data_dict['thumbnail_url'] = ''

            # GET POST LINK
            a_tag = post_box.find('a')
            news_link = a_tag['href']
            post_data_dict['url'] = f"https://velog.io{news_link}"

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_COLUMN'

        except Exception as e:
            print(e)
            print("Velog 오류발생")

    print(">>> Velog CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST


