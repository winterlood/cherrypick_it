import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import datetime
import random
import multiprocessing as mp
from pytz import timezone, utc

from crawler import *

def main():
    KST = timezone('Asia/Seoul')
    now = datetime.datetime.utcnow()
    # UTC 기준 naive datetime : datetime.datetime(2019, 2, 15, 4, 18, 28, 805879)

    utc.localize(now)
    # UTC 기준 aware datetime : datetime.datetime(2019, 2, 15, 4, 18, 28, 805879, tzinfo=<UTC>)

    KST.localize(now)
    # UTC 시각, 시간대만 KST : datetime.datetime(2019, 2, 15, 4, 18, 28, 805879, tzinfo=<DstTzInfo 'Asia/Seoul' KST+9:00:00 STD>)

    NOW_KST_TIME = utc.localize(now).astimezone(KST)
    # KST 기준 aware datetime : datetime.datetime(2019, 2, 15, 13, 18, 28, 805879, tzinfo=<DstTzInfo 'Asia/Seoul' KST+9:00:00 STD>)

    print(f'PROGRAM START\n>>> DATE : {NOW_KST_TIME}\n')	
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    proc = mp.current_process()
    print(proc.name)
    print(proc.pid)

    # NEWS 
    manager = mp.Manager()
    NEWS_DATA = manager.list()

    p1_news = mp.Process(name="techniddle", target=crawl_TechNiddle,args=[NEWS_DATA])
    p1_news.start()

    p2_news = mp.Process(name="itnews", target=crawl_itnews,args=[NEWS_DATA])
    p2_news.start()
    
    # p3_news = mp.Process(name="inews24", target=crawl_INews24,args=[NEWS_DATA])
    # p3_news.start()
    
    p4_news = mp.Process(name="itdonga", target=crawl_Itdonga,args=[NEWS_DATA])
    p4_news.start()


    # COLUMNS
    manager = mp.Manager()
    COLUMN_DATA = manager.list()

    p1_column = mp.Process(name="woowabros", target=crawl_Woowabros,args=[COLUMN_DATA])
    p1_column.start()

    p2_column = mp.Process(name="kakao", target=crawl_Kakao,args=[COLUMN_DATA])
    p2_column.start()
    
    p3_column = mp.Process(name="velog", target=crawl_Velog,args=[COLUMN_DATA])
    p3_column.start()


    p1_column.join() # woowa bros
    p2_column.join() # kakao
    p3_column.join() # velog
    random.shuffle(COLUMN_DATA)

    p1_news.join() # 테크니들
    p2_news.join() # it news
    # p3_news.join() # inews24
    p4_news.join() # it 동아
    random.shuffle(NEWS_DATA)

    print(len(COLUMN_DATA),' 개의 칼럼 추출완료')
    print(len(NEWS_DATA),' 개의 뉴스 추출완료')


  
    
    # TOTAL
    NEWS_DATA = list(NEWS_DATA)
    COLUMN_DATA = list(COLUMN_DATA)
    CRWAL_DATA = dict()
    CRWAL_DATA['date'] = str(NOW_KST_TIME)
    CRWAL_DATA['count_total'] = len(COLUMN_DATA) + len(NEWS_DATA)
    CRWAL_DATA['count_news'] = len(NEWS_DATA)
    CRWAL_DATA['count_column'] = len(COLUMN_DATA)
    CRWAL_DATA['data_news'] = NEWS_DATA
    CRWAL_DATA['data_column'] = COLUMN_DATA


    with open(os.path.join(BASE_DIR, 'output.json'), 'w+',encoding='utf-8') as json_file:
        json.dump(CRWAL_DATA, json_file, ensure_ascii = False, indent='\t')


    print(f'\nPROGRAM DONE\n{len(COLUMN_DATA) + len(NEWS_DATA)} DATA HAS STORED !\n')	


if __name__ == "__main__":
    main()