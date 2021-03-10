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


# now = datetime.now()
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print(f'PROGRAM START\n>>> DATE : {NOW_KST_TIME}\n')	
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


CRWAL_DATA = dict()
CRWAL_DATA['date'] = str(NOW_KST_TIME)
CRWAL_DATA['data'] = []

CRWAL_DATA['data'].extend(crawl_TechNiddle())
CRWAL_DATA['data'].extend(crawl_ITWorld())
CRWAL_DATA['data'].extend(crawl_Woowabros())
CRWAL_DATA['data'].extend(crawl_Kakao())
CRWAL_DATA['data'].extend(crawl_INews24())
CRWAL_DATA['data'].extend(crawl_Velog())
random.shuffle(CRWAL_DATA['data'])
result_data_length = len(CRWAL_DATA['data'])

with open(os.path.join(BASE_DIR, 'news.json'), 'w+',encoding='utf-8') as json_file:
    json.dump(CRWAL_DATA, json_file, ensure_ascii = False, indent='\t')


print(f'\nPROGRAM DONE\n{result_data_length} DATA HAS STORED !\n')	
