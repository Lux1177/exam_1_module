 
def count(list):
    positives = 0
    negatives = 0
    for i in list:
        if i > 0:
             positives += 1
        elif i < 0:
            negatives += 1
    return (f'{positives}, {negatives}')

print(count([1, 0, -1]))