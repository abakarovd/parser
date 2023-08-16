import pandas
from dataВышка import names

nums = [str(i) for i in range(0, 10)]


def num(x):
    str_x, new_x = str(x), ''
    for i in str_x:
        if i in nums: new_x += i
    if len(new_x) > 0: return int(new_x)
    return 0


with open('/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсыВЫШКА.txt', 'w') as pr:
    pr.close()

for name in names:
    name = name[1]
    ex = pandas.read_excel(f'/Users/maybeabakarov/Desktop/поступление /итс эксель /{name}', sheet_name='TDSheet')
    k = ex.shape[0]
    for i in range(k):
        # get(j) 4,6,8,10 проверка на общий конкурс, 26 проверка баллов
        if all(ex.loc[i].get(j) == 'Нет' for j in [4, 6, 8, 10]) and num(ex.loc[i].get(26)) >= 201:
            number = ex.loc[i].get(0)
            snils = num(ex.loc[i].get(2))
            orig = ex.loc[i].get(30)
            all_info = str(number) + ' ' + str(snils) + ' ' + str(orig) + ' ' + name[:-5].replace(' ', '') + '\n'
            with open('/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсыВЫШКА.txt', 'a') as pr:
                pr.write(all_info)
            # print(number, snils, orig,name)
