import csv
with open('SampleCSVFile_11kb.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(' '.join(row))
print('*'*40)

import json
with open('sample2.json', 'r') as jsonfile:
    reader = json.load(jsonfile)
    print(reader)
print('*'*40)

try:
    print(10000 ** 10000)
except ZeroDivisionError as z:
    print(f'Zero Division Error: {z}')
except Exception as e:
    print(f'Error: {e}')
finally:
    print('end of the block')
    print('*' * 40)

list = [1, 2, 3]
list1 = []
try:
    list1.append(list[3])
    list1.append(list[2])
except IndexError as i:
    print(f'IndexError: {i}')
except Exception as e:
    print(f'Error: {e}')
finally:
    print(list1)
    print('*'*40)




