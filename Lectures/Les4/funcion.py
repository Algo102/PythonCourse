def umn(x):
    return x*x


print(umn(5))  # 25

a = umn  # переменная а, хранит в себе функцию на функцию umn
print(type(umn))  # <class 'function'>
print(type(a))  # <class 'function'>
print(a(5))  # 25


# КАЛЬКУЛЯТОР
def calkSum(a):
    return a+a


def calkUmn(a):
    return a*a


def calkMath(op, x):
    print(op(x))


calkMath(calkUmn, 10)


# КАЛЬКУЛЯТОР
def calkSum2(a, b):
    return a+b


def calkUmn2(a, b):
    return a*b


def calkMath2(op, x, b):
    print(op(x, b))


calkMath2(calkSum2, 5, 45)


# КАЛЬКУЛЯТОР с labda функцией
def calkMath3(op, x, b):
    print(op(x, b))


# calc3 = lambda a, b: a+b
# def calc3(a, b): return a+b


# calkMath3(calc3, 5, 50)
calkMath3(lambda a, b: a+b, 5, 50)
