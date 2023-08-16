import csv
university_names = [
    'снилсыВЫШКА.txt', 'снилсыМФТИ.txt', 'снилсыИТМО.txt', 'снилсыМИРЭА.txt',
    'снилсыМИСИС.txt', 'снилсыМИФИ.txt', 'снилсыСПБГУ.txt', 'снилсыМАИ.txt',
    'снилсыСПБПУ.txt', 'снилсыМЭИ.txt', 'снилсыЛЭТИ.txt', 'снилсыНГТУ.txt'
]

all_info = []
def to_collect_all_snils(university_name, k):
    d = dict()
    a = [x for x in open(f'/Users/maybeabakarov/Desktop/поступление /ол снилс/{university_name}')]
    for info in a:
        snils = int(info.split()[1])
        number = info.split()[0]
        orig = info.split()[2]
        if k ==1:
            url = info.split()[3]
            d[snils] = number + ' ' + orig + ' ' + url
        else:
            prioritet = info.split()[3]
            d[snils] = number + ' ' + orig + ' ' + prioritet
    return  d


## Указываем отдельно направление
baum = to_collect_all_snils('снилсы09.03.04.txt',0)
for snils in baum:
    number = str(baum[snils].split()[0])
    orig = str(baum[snils].split()[1])
    prioritet = str(baum[snils].split()[2])
    all_info += [[number,str(snils),orig,prioritet]]

name_1 = [x[6:][:-4] for x in university_names]
name_2 = ['БАУМАНКА', ' ', ' ', ' ']
for i in name_1:
    name_2 += [i] + [' '] + [' ']
print(name_2)

for university_name in university_names:
    a = to_collect_all_snils(university_name,1)

    for i in range(len(all_info)):
        try:
            c = a[int(all_info[i][1])]
            all_info[i] += c.split()
        except:
            all_info[i] += ' ' + ' ' + ' '


with open('/Users/maybeabakarov/Desktop/09.03.04.csv', 'w', encoding='cp1251') as pr:
    writer = csv.writer(pr)
    writer.writerow(name_2)
for snils in all_info:
    with open('/Users/maybeabakarov/Desktop/09.03.04.csv','a', encoding='cp1251') as pr:
        writer = csv.writer(pr)
        writer.writerow(snils)




