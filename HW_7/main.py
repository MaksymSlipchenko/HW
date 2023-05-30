#1
def fibonachi(n):
    if n in [1, 2]:
        return 1
    return (fibonachi(n - 1) + fibonachi(n - 2))
print(fibonachi(5))
print('='*30)
#2
def sum_range(start, end):
    sum = 0
    if start > end:
        start, end = end, start
    for i in range(start, end + 1):
        sum += i
    return sum
print(sum_range(3, 2))
print('='*30)
#3
def season(n):
    if n in [1, 2, 12]:
        return 'Зима'
    elif n in [3, 4, 5]:
        return 'Весна'
    elif n in [6, 7, 8]:
        return 'Літо'
    elif n in [9, 10, 11]:
        return 'Осінь'
    else:
        return 'такого місяця не існує'
print(season(11))
print('='*30)
#4
def get_filtered(a):
    for i in a:
        if i < 5:
            print(i)
get_filtered([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
