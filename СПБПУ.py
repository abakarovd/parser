import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

faculties = [
    'Прикладная математика и информатика',
    'Информатика и вычислительная техника',
    'Прикладная информатика',
    'Программная инженерия',
    'Информационная безопасность',
    'Бизнес-информатика'
]
url = 'https://enroll.spbstu.ru/applicants/bachelor-specialist/rating'
nums = [str(i) for i in range(0, 10)]


def num(x):
    str_x, new_x = str(x), ''
    for i in str_x:
        if i in nums:
            new_x += i
    if len(new_x) > 0: return int(new_x)
    return 0


def get_data(url, faculty_name):
    service = Service(executable_path="/Users/maybeabakarov/Desktop/поступление /chromedriver_mac_arm64/chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(url=url)
        time.sleep(3)

        form_select = driver.find_element(By.ID, 'react-select-2-input')
        form_select.send_keys('Очная')
        form_select.send_keys(Keys.DOWN)
        form_select.send_keys(Keys.ENTER)

        pay_select = driver.find_element(By.ID, 'react-select-3-input')
        pay_select.send_keys('Бюджет')
        pay_select.send_keys(Keys.ENTER)

        time.sleep(1)
        spec_select = driver.find_element(By.ID, 'react-select-4-input')
        spec_select.send_keys(faculty_name)
        time.sleep(1)
        spec_select.send_keys(Keys.ENTER)

        time.sleep(3)
        src = driver.page_source
    except Exception as ex:
        ...
        # print(ex)
    finally:
        driver.close()
        driver.quit()
    table_1 = BS(src, 'html.parser').find_all('tr')

    for i in range(len(table_1)):
        info = table_1[i].find_all('td')
        try:
            if len(info) > 5 and num(info[3].text) >= 201:
                number = info[0].text
                snils = num(info[1].text.split('/')[0])
                orig = info[-2].text
                all_info = str(number) + ' ' + str(snils) + ' ' + str(orig) + ' ' + faculty_name.replace(' ', '') + '\n'
                with open('/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсыСПБПУ.txt', 'a') as pr:
                    pr.write(all_info)
                # print(number, snils,orig)
        except:
            print('error')


with open('/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсыСПБПУ.txt', 'w') as pr:
    pr.close()

for faculty_name in faculties:
    get_data(url, faculty_name)
