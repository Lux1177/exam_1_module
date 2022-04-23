
def bin_to_num(list):
    a = ''
    for i in list:
        a += str(i)
    return int(a, 2)

print(bin_to_num([1, 1, 1, 1, 1, 1, 1, 1]))
