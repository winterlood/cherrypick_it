import requests
from bs4 import BeautifulSoup
import multiprocessing as mp
import traceback
import xmltodict
import json
import pprint
def get_rss_by_target_url(target_url):
    try:
        req = requests.get(target_url, timeout=3)
        if req is not None: 
            if req.ok:
                # 성공 응답 시 액션
                dict_type = xmltodict.parse(req.content)
                json_type = json.dumps(dict_type)
                dict2_type = json.loads(json_type)
                item_list = dict2_type['rss']['channel']['item']
                return item_list

            else:
                return 'ERROR'
    except Exception as e:
        print(e)
        return 'ERROR'


def rss_itdonga(NEWS_DATA):
    print('\n\n')
    print("#"*30)
    print("ITDONGA CRAWL START")
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    rss_url = 'https://it.donga.com/feeds/rss'
    item_list = get_rss_by_target_url(rss_url)
    RESULT_LIST = []

    for idx,item in enumerate(item_list[0:20]):
        post_data_dict = dict()

        headline_text = item['title']
        news_link = item['link']
        author_text = item['author']
        email = author_text.split('(')[0].strip()
        author_text = author_text.split('(')[1].split(')')[0]
        description = item['description']
        soup = BeautifulSoup(description, 'html.parser')
        thumbnail = soup.find('img')['src']

        post_data_dict['source'] = 'https://it.donga.com/'
        post_data_dict['headline'] = headline_text
        post_data_dict['thumbnail_url'] = thumbnail
        post_data_dict['url'] = news_link
        post_data_dict['author'] = author_text
        post_data_dict['type'] = 'TYPE_NEWS'

        # RESULT_LIST.append(post_data_dict)
        NEWS_DATA.append(post_data_dict)
        print('ITDONGA',len(NEWS_DATA))
        # post_data_dict['author_email'] = email
    return RESULT_LIST


def get_soup_obj_by_target_url(target_url):
    try:
        req = requests.get(target_url, timeout=3)
        if req is not None: 
            if req.ok:
                # 성공 응답 시 액션
                req.encoding= None
                html = req.content
                soup = BeautifulSoup(html, 'html.parser')
                return soup
            else:
                return 'ERROR'
    except Exception as e:
        print(e)
        return 'ERROR'

# NEWS
def crawl_TechNiddle(NEWS_DATA):
    print('\n\n')
    print("#"*30)
    print("TECHNIDDLE CRAWL START")
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    target_url = 'https://techneedle.com/archives/category/default'
    soup = get_soup_obj_by_target_url(target_url)
    if soup == 'ERROR':
        print("테크니들 오류발생")
        return []
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

            # GET POST AUTHOR
            cur_target_url = news_link
            cur_soup = get_soup_obj_by_target_url(cur_target_url)
            author_title_tag = cur_soup.find('a',{'class','url'})
            post_data_dict['author'] = author_title_tag.getText()


            # APPEND RESULT LIST
            # RESULT_LIST.append(post_data_dict)
            NEWS_DATA.append(post_data_dict)

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_NEWS'

        except Exception as e:
            print(e)
            print("테크니들 오류발생")

    print(">>> TECHNIDDLE CRAWL DONE")

def crawl_ITWorld(NEWS_DATA):

    print('\n\n')
    print("#"*30)
    print("ITWORLD CRAWL START")
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
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

            # GET POST AUTHOR
            cur_target_url =  f"{post_data_dict['source']}{news_link}"
            cur_soup = get_soup_obj_by_target_url(cur_target_url)
            author_title_tag = cur_soup.find('div',{'class','node_source'})
            post_data_dict['author'] = author_title_tag.getText()

           # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_NEWS'

            # APPEND RESULT LIST
            NEWS_DATA.append(post_data_dict)
            print('ITWORLD',len(NEWS_DATA))

 
        except Exception as e:
            print(e)
            print("ITWORLD 오류발생")
    print(">>> ITWORLD CRAWL DONE")

def crawl_INews24(NEWS_DATA):
    print('\n\n')
    print("#"*30)
    print("iNEWS24 CRAWL START")
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    target_url = 'http://www.inews24.com/list/it'
    
    soup = get_soup_obj_by_target_url(target_url)
    if soup == 'ERROR':
        print("아이뉴스24 오류발생")
        return []
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

            # GET POST AUTHOR
            cur_target_url = f"http://www.inews24.com{news_link}"
            cur_soup = get_soup_obj_by_target_url(cur_target_url)
            if cur_soup == 'ERROR':
                continue
            author_tag = cur_soup.find('author')
            post_data_dict['author'] = author_tag.getText()

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_NEWS'

            # APPEND RESULT LIST
            # RESULT_LIST.append(post_data_dict)
            NEWS_DATA.append(post_data_dict)

        except Exception as e:
            print(e)
            print("INEWS24 오류발생")
            traceback.print_exc()


    print(">>> INEWS24 CRAWL DONE")

def crawl_Itdonga(NEWS_DATA):
    print('\n\n')
    print("#"*30)
    print("IT DONGA CRAWL START")
    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)
    target_url = 'https://it.donga.com/news/'
    
    soup = get_soup_obj_by_target_url(target_url)
    if soup == 'ERROR':
        print("IT동아 오류발생")
        return []
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
            headline_text = str(headline_tag.getText())
            post_data_dict['headline'] = headline_text.strip()

            # GET POST THUMBNIAL
            try:
                img_tag = post_box.find('img')
                img_url = img_tag['data-src']
                post_data_dict['thumbnail_url'] = f"https://it.donga.com{img_url}"
            except Exception:
                post_data_dict['thumbnail_url'] = ''

            # GET POST LINK
            a_tag = post_box.find('a')
            news_link = a_tag['href']
            post_data_dict['url'] = f"https://it.donga.com{news_link}"

            # GET POST AUTHOR
            author_tag = post_box.find('strong',{'class':'reporter'})
            print(author_tag.getText())
            news_author = author_tag.getText()
            post_data_dict['author'] = news_author

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_NEWS'

        except Exception as e:
            print(e)
            print("IT DONGA 오류발생")

    print(">>> IT DONGA CRAWL DONE")



# COLUMN
def crawl_Woowabros(COLUMN_DATA):
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

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_COLUMN'

            # APPEND RESULT LIST
            COLUMN_DATA.append(post_data_dict)


        except Exception as e:
            print(e)
            print("WOOWA BROS 오류발생")

    print(">>> WOOWABROS CRAWL DONE")

def crawl_Kakao(COLUMN_DATA):
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

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_COLUMN'

            # APPEND RESULT LIST
            COLUMN_DATA.append(post_data_dict)
        except Exception as e:
            print(e)
            print("KAKAO 오류발생")

    print(">>> KAKAO CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST

def crawl_Velog(COLUMN_DATA):
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

            # APPEND ARTICLE TYPE
            post_data_dict['type'] = 'TYPE_COLUMN'

            # APPEND RESULT LIST
            COLUMN_DATA.append(post_data_dict)

        except Exception as e:
            print(e)
            print("Velog 오류발생")

    print(">>> Velog CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST

# crawl_INews24()