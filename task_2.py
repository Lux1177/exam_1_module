import math

def get_century(year):
    if year % 100 == 0:
        return int(year / 100)
    else: 
        return int(year / 100 + 1)

print(get_century(2022))


