import requests
from bs4 import BeautifulSoup as BS

nums = [str(i) for i in range(0, 10)]


def num(x):
    str_x, new_x = str(x), ''
    for i in str_x:
        if i in nums:
            new_x += i
    if len(new_x) > 0: return int(new_x)
    return 0


# 01.03.02 Прикладная математика и информатика
pmu_url = 'https://priem.mipt.ru/applications/bachelor_range/%D0%9A%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D1%81%D0%BD%D1%8B%D0%B5%20%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20%D0%9E%D0%B1%D1%89%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%81%D1%82%D0%B0%20(%D0%9F%D1%80%D0%B8%D0%BA%D0%BB%D0%B0%D0%B4%D0%BD%D0%B0%D1%8F%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0%20%D0%B8%20%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0_%D0%91%D1%8E%D0%B4%D0%B6%D0%B5%D1%82)%20(HTML).html'
pmu = requests.get(pmu_url)
# 09.03.01 Информатика и вычислительная техника
inf_url = 'https://priem.mipt.ru/applications/bachelor_range/%D0%9A%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D1%81%D0%BD%D1%8B%D0%B5%20%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20%D0%9E%D0%B1%D1%89%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%81%D1%82%D0%B0%20(%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D1%8B%D0%B5%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8%20(%D0%98%D0%92%D0%A2)_%D0%91%D1%8E%D0%B4%D0%B6%D0%B5%D1%82)%20(HTML).html'
inf = requests.get(inf_url)
# 09.03.04 ВШПИ Программная инженерия
progB_url = 'https://priem.mipt.ru/applications/bachelor_range/%D0%9A%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D1%81%D0%BD%D1%8B%D0%B5%20%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20%D0%9E%D0%B1%D1%89%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%81%D1%82%D0%B0%20(%D0%92%D0%A8%D0%9F%D0%98%20%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F_%D0%91%D1%8E%D0%B4%D0%B6%D0%B5%D1%82)%20(HTML).html'
progB = requests.get(progB_url)
# 09.03.04 ПИШ РПИ Программная инженерия
progP_url = 'https://priem.mipt.ru/applications/bachelor_range/%D0%9A%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D1%81%D0%BD%D1%8B%D0%B5%20%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20%D0%9E%D0%B1%D1%89%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%81%D1%82%D0%B0%20(%D0%9F%D0%98%D0%A8%20%D0%A0%D0%9F%D0%98%20%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%B0%D1%8F%20%D0%B8%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%8F_%D0%91%D1%8E%D0%B4%D0%B6%D0%B5%D1%82)%20(HTML).html'
progP = requests.get(progP_url)
# 10.05.01 Компьютерная безопасность
kompB_url = 'https://priem.mipt.ru/applications/bachelor_range/%D0%9A%D0%BE%D0%BD%D0%BA%D1%83%D1%80%D1%81%D0%BD%D1%8B%D0%B5%20%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B8%20%D0%9E%D0%B1%D1%89%D0%B8%D0%B5%20%D0%BC%D0%B5%D1%81%D1%82%D0%B0%20(%D0%9A%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%BD%D0%B0%D1%8F%20%D0%B1%D0%B5%D0%B7%D0%BE%D0%BF%D0%B0%D1%81%D0%BD%D0%BE%D1%81%D1%82%D1%8C_%D0%91%D1%8E%D0%B4%D0%B6%D0%B5%D1%82)%20(HTML).html'
kompB = requests.get(kompB_url)

faculties = [[pmu_url, pmu], [inf_url, inf], [progB_url, progB], [progP_url, progP], [kompB_url, kompB]]

with open('/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсыМФТИ.txt', 'w') as pr:
    pr.close()


def get_snils(faculty_html, faculty_url):
    table_1 = BS(faculty_html.content, 'html.parser').find_all('tr')
    for i in range(len(table_1)):
        info = table_1[i].find_all('td')
        if len(info) > 7 and num(info[3].text) >= 201:
            number = num(info[0].text)
            snils = num(info[1].text)
            orig = info[-4].text
            if orig == 'Копия':
                orig = 'нет'
            elif orig == 'Оригинал':
                orig = 'да'
            else:
                orig = 'неизвество'
            all_info = str(number) + ' ' + str(snils) + ' ' + str(orig) + ' ' + faculty_url + '\n'
            with open('/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсыМФТИ.txt', 'a') as pr:
                pr.write(all_info)
            # print(number,snils,orig)


for faculty_html_url in faculties:
    faculty_url, faculty_html = faculty_html_url[0], faculty_html_url[1]
    get_snils(faculty_html, faculty_url)
