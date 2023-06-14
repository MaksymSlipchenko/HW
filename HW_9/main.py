# Lambda
a = lambda x, y = 100: print(str(x) * y)
a(10)

b = lambda x, y: x if x > y else y
print(b(3, 4))

c = lambda: print(10)
c()

# Decorators
def make_bold(fn):
    def wrapper():
        print("<b>", end="")
        fn()
        print("</b>", end="")
    return wrapper

def make_italic(fn):
    def wrapper():
        print("<i>", end="")
        fn()
        print("</i>", end="")
    return wrapper

def make_underline(fn):
    def wrapper():
        print("<u>", end="")
        fn()
        print("</u>", end="")
    return wrapper

@make_bold
@make_italic
@make_underline
def say_hi():
     print('hi', end="")

say_hi()


# List comprehension
print(end='\n')
lst1 = [44, 54, 64, 74, 104]
lst2 = [i + 6 for i in lst1]
print(lst2)

lst3 = [2, 4, 6, 8, 10, 12, 14]
lst4 = [i*i for i in lst3]
print(lst4)

car_dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
list5 = [i.upper() for i in car_dict if car_dict[i] < 5000]
print(list5)