import csv
import re

lst = list()

with open("Crimes.csv", "r") as f:
    reader = csv.reader(f)

    for line in reader:
        reg = r"\d\d/\d\d/2015"
        if re.search(reg, line[2]):
            if line[5] not in lst:
                lst.append(line[5])             # лист в котором список типов преступлений
f.close()

count_list = [0 for i in range(25)]

with open("Crimes.csv", "r") as f:
    reader = csv.reader(f)

    for line in reader:
        reg = r"\d\d/\d\d/2015"
        if re.search(reg, line[2]):
            for i in range(len(lst)):
                if lst[i] == line[5]:
                    count_list[i] += 1

for i in range(len(count_list)):
    if count_list[i] == max(count_list):
        print("Самое распространенное преступление:", lst[i])
        print("Количество раз:", count_list[i])
