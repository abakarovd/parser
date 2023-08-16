import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os


def save_pdf(pdf_url):
    pdf_document = requests.get(pdf_url)  # скачиваем файл
    name = pdf_url.split('/')[-1]
    with open(f'/Users/maybeabakarov/Desktop/{name}', 'wb') as f:  # сохраняем пдф
        f.write(pdf_document.content)


def convert(url):  # конвертируем в xlsx
    service = Service(
        executable_path='/Users/maybeabakarov/Desktop/поступление /chromedriver_mac_arm64/chromedriver'
    )
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(url=url)
        time.sleep(25)
    except Exception as ex:
        print(ex)


pdf_document_url_1 = 'https://priem.bmstu.ru/lists/upload/enrollees/first/MGTU-1/01.03.02.pdf'
pdf_document_url_2 = 'https://priem.bmstu.ru/lists/upload/enrollees/first/MGTU-1/09.03.04.pdf'
pdf_document_url_3 = 'https://priem.bmstu.ru/lists/upload/enrollees/first/MGTU-1/09.03.03.pdf'
url_convert = 'https://www.ilovepdf.com/ru/pdf_to_excel'

# save_pdf(pdf_document_url_1)
save_pdf(pdf_document_url_2)
convert(url_convert)

try:
    os.remove(f'/Users/maybeabakarov/Desktop/поступление /итс эксель /Программная инженерия МГТУ.xlsx')
except:
    ...
os.renames(f'/Users/maybeabakarov/Downloads/09.03.04.xlsx',
           f'/Users/maybeabakarov/Desktop/поступление /итс эксель /Программная инженерия МГТУ.xlsx')
