import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import datetime
import random
from pytz import timezone, utc

from crawler import *

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


# NEWS
NEWS_DATA = []
NEWS_DATA.extend(crawl_TechNiddle())
NEWS_DATA.extend(crawl_ITWorld())
NEWS_DATA.extend(crawl_INews24())
random.shuffle(NEWS_DATA)

# COLUMNS
COLUMN_DATA = []
COLUMN_DATA.extend(crawl_Woowabros())
COLUMN_DATA.extend(crawl_Kakao())
COLUMN_DATA.extend(crawl_Velog())
random.shuffle(COLUMN_DATA)

# TOTAL
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
