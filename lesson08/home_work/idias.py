import json
import re

file = open("list.txt", encoding='utf-8')
my_file = json.load(file)

#for i in my_file:
#    if str(i["country"]) == "RU":
#        print(str(i["id"]))
#        print(str(i["name"]))
    #print(str(i["country"]))
    #print(str(i["coord"]))

all_country = []

for j in my_file:
    if str(j['country']) not in all_country:
        all_country.append(str(j['country']))
        #print(str(j['country']))

print(all_country)


selected_country = str(input("Введите страну для получения списка городов: "))

all_selected_country_city = []

for i in my_file:
    if str(i["country"]) == selected_country:
        print('{}: {}'.format(str(i["name"]), str(i["id"])))
        all_selected_country_city.append(str(i["name"]))
        #print(str(i["name"]), str(i["id"]))
        #print(str(i["id"]))

city_name = []
moscow = "Moscow"
sup_name = "Mos"

def city_name_found():
    m = re.search(sup_name + '.*', all_selected_country_city)
    k = str(m.group(0))
    return k

for m in my_file:
    if (str(i["name"]) not in

    #print(str(i["country"]))
    #print(str(i["coord"]))