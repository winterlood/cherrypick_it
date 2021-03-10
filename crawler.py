import requests
from bs4 import BeautifulSoup

def get_soup_obj_by_target_url(target_url):
    req = requests.get(target_url)
    req.encoding= None
    html = req.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

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
        except Exception as e:
            print(e)
            print("테크니들 오류발생")

    print(">>> TECHNIDDLE CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST

def crawl_ZDNet():
    target_url = 'https://zdnet.co.kr/news/?lstcode=0000&page=1'
    soup = get_soup_obj_by_target_url(target_url)

    # RESULT LIST INIT
    RESULT_LIST = []

    # GET POST SECTION
    post_section = soup.find('section',{'class','news_box'})

    # GET POST ITEMS 
    post_box_list = post_section.find_all('div',{'class':'newsPost'})

    # GET POST DATAS
    for post_box in post_box_list:
        try:
            post_data_dict = dict()
            post_data_dict['source'] = 'https://zdnet.co.kr'

            # GET POST THUMBNIAL
            img_tag = post_box.find('img')
            img_url = img_tag['src']
            print(img_url)
            post_data_dict['thumbnail_url'] = img_url

            # GET POST HEADLINE
            headline_tag = post_box.find('h3')
            headline_text = headline_tag.getText()
            print(headline_text)
            post_data_dict['headline'] = headline_text

            # GET POST LINK
            a_tag = post_box.find('a')
            news_link = a_tag['href']
            print(news_link)
            post_data_dict['url'] = news_link

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)
        except Exception as e:
            print(e)
            print("ZDNET 오류발생")

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
                post_data_dict['thumbnail_url'] = img_url
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
        except Exception as e:
            print(e)
            print("ITWORLD 오류발생")
    print(">>> ITWORLD CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST

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
        except Exception as e:
            print(e)
            print("KAKAO 오류발생")

    print(">>> KAKAO CRAWL DONE")
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
            headline_section = post_box.find('div',{'class','thumb'})
            headline_tag = headline_section.find('a')
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
            a_tag = headline_section.find('a')
            news_link = a_tag['href']
            post_data_dict['url'] = f"http://www.inews24.com{news_link}"

            # APPEND RESULT LIST
            RESULT_LIST.append(post_data_dict)
        except Exception as e:
            print(e)
            print("INEWS24 오류발생")

    print(">>> INEWS24 CRAWL DONE")
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
        except Exception as e:
            print(e)
            print("Velog 오류발생")

    print(">>> Velog CRAWL DONE")
    print(f">>> {len(RESULT_LIST)} HAS CRAWLED")
    print("#"*30)
    return RESULT_LIST


