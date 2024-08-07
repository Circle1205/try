print('------------' * 10)
# 位置或關鍵字引數 (Positional-or-Keyword Arguments)
print("Positional Arguments(*args)")

#在使用上更有發展性，不限於只輸入幾個參數
def plus(*nums):
    res = 0
    for i in nums:
        res += i
    print(f'相加 = {res}')
    print(type(nums))


plus(1, 2, 3)
plus(1, 2, 3, 4, 5, 6, 7)

print('------------' * 10)

print("Keyword Arguments(**kwargs)")


# *args **kwargs

def person(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}:{value}")


person(name='A')
print()
person(name='b', age='10', gender='F')

print('------------' * 10)
print('同時使用時，位置函數(*args)要在前面')


def num(*args01, **args02):
    print(args01)
    print(args02)


num(1, 2, 3, name='A', Age='10')
