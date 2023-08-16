import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

names = [
    # old name, new name
    ['BD_BI.xlsx', 'Бизнес-информатика.xlsx'],
    ['BD_ITSS.xlsx', 'Инфокоммуникационные технологии и системы связи.xlsx'],
    ['BD_IVT.xlsx', 'Информатика и вычислительная техника.xlsx'],
    ['BD_IB.xlsx', 'Информационная безопасность.xlsx'],
    ['BD_KB.xlsx', 'Компьютерная безопасность.xlsx'],
    ['BD_Compds.xlsx', 'Компьютерные науки и анализ данных.xlsx'],
    ['BD_Math.xlsx', 'Математика.xlsx'],
    ['BD_AM.xlsx', 'Прикладная математика.xlsx'],
    ['BD_AMI.xlsx', 'Прикладная математика и информатика.xlsx'],
    ['BD_Data.xlsx', 'Прикладной анализ данных.xlsx'],
    ['BD_SE.xlsx', 'Программная инженерия.xlsx']
]

urls = [
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_BI.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_ITSS.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_IVT.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_IB.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_KB.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_Compds.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_Math.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_AM.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_AMI.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_Data.xlsx',
    'https://enrol.hse.ru/storage/public_report_2023/moscow/Bachelors/BD_SE.xlsx',
]

for name in names:
    old_name, new_name = name[0], name[1]
    try:
        os.remove(f'/Users/maybeabakarov/Desktop/поступление /итс эксель /{new_name}')
    except:
        ...


def get_data(url):
    service = Service(
        executable_path="/Users/maybeabakarov/Desktop/поступление /chromedriver_mac_arm64/chromedriver"
    )
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(url=url)
        time.sleep(2)
    except Exception as ex:
        print(ex)
    # finally:
    # driver.close()
    # driver.quit()


for url in urls:
    get_data(url)

for name in names:
    old_name, new_name = name[0], name[1]
    try:
        os.renames(f'/Users/maybeabakarov/Downloads/{old_name}',
                   f'/Users/maybeabakarov/Desktop/поступление /итс эксель /{new_name}')
        print(f'В {new_name} все хорошо')
    except:
        print(f'Ошибка в {new_name}')
