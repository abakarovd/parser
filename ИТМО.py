from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

nums = [str(i) for i in range(0, 10)]
def num(x):
    srt_x, new_x = str(x), ''
    for i in srt_x:
        if i in nums:
            new_x += i
    if len(new_x) > 0: return int(new_x)
    return 0


urls = [
    # 01.03.02 Прикладная математика и информатика
    'https://abit.itmo.ru/ranking/bachelor/budget/1801',
    # 09.03.01 Информатика и вычислительная техника
    'https://abit.itmo.ru/ranking/bachelor/budget/1803',
    # 09.03.03 Прикладная информатика
    'https://abit.itmo.ru/ranking/bachelor/budget/1805',
    # 09.03.04 Программная инженерия
    'https://abit.itmo.ru/ranking/bachelor/budget/1806',
    # 10.03.01 Информационная безопасность
    'https://abit.itmo.ru/ranking/bachelor/budget/1807',
    # 38.03.05 Бизнес-информатика
    'https://abit.itmo.ru/ranking/bachelor/budget/1823'
]

def get_data(url):
    service = Service(
        executable_path="/Users/maybeabakarov/Desktop/поступление /chromedriver_mac_arm64/chromedriver"
    )
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(url=url)
        time.sleep(4)
        src = driver.page_source
    except Exception as ex:
        ...
        #print(ex)
    finally:
        driver.close()
        driver.quit()
    table_1 = BS(src, 'html.parser').find_all('div', class_='RatingPage_table__FbzTn')[-1].find_all('div')
    for i in range(0, len(table_1), 11):
        info = table_1[i].text.split()
        if num(info[11]) >= 201:
            number = num(info[0])
            snils = num(info[1])
            orig = info[-1]
            all_info = str(number) + ' ' + str(snils) + ' ' + str(orig) + ' ' + url + '\n'
            with open('/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсыИТМО.txt', 'a') as pr:
                pr.write(all_info)
            #print(number, snils, orig)

with open('/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсыИТМО.txt', 'w') as pr:
    pr.close()

for url in urls:
    get_data(url)