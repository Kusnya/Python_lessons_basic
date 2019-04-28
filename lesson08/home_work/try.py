import re
city_name = []
moscow = "Moscow asdasd"

sup_name = "Mos"

def city_name_found():
    m = re.search(sup_name + '.*', moscow)
    k = str(m.group(0))
    return k

print(city_name_found())