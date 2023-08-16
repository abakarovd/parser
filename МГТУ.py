import pandas
import openpyxl

nums = [str(x) for x in range(0, 10)]


def num(x):
    str_x, new_x = str(x), ''
    for i in str_x:
        if i in nums:
            new_x += i
    if len(new_x) > 0: return int(new_x)
    return 0


sheet_name = openpyxl.load_workbook('итс эксель /Программная инженерия МГТУ.xlsx').sheetnames[-1]
ex = pandas.read_excel('итс эксель /Программная инженерия МГТУ.xlsx', sheet_name=sheet_name)
k = ex.shape[0]

with open(f'/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсы09.03.04.txt', 'w') as pr:
    pr.close()

for i in range(k):
    if 201 <= num(ex.loc[i].get(3)) <= 500:
        number = str(ex.loc[i].get(0)).split()[0]
        snils = num(ex.loc[i].get(1))
        orig = ex.loc[i].get(10)
        if orig == 'Да':
            orig = 'yes'
        else:
            orig = 'no'
        priot = ex.loc[i].get(11)
        all_info = str(number) + ' ' + str(snils) + ' ' + str(orig) + ' ' + str(priot) + '\n'
        with open(f'/Users/maybeabakarov/Desktop/поступление /ол снилс/снилсы09.03.04.txt', 'a') as pr:
            pr.write(all_info)
            print(number, snils, orig, priot)
