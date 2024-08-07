# Set
set1 = {5, 4, 3, 2, 1, 5, 6}
set2 = {6, 7, 8, 9, 1, 10}

print(f'集合一:{set1}')
print(f'集合一:{set2}')
print(f"交集:{set1 & set2}")
print(f"差集:{set1 - set2}")
print(f"聯集:{set1 | set2}")
set1.add(9)
set1.remove(1)
print(f'修改後的集合一:{set1}')

print('------------' * 10)
# list

list1 = [1, 2, 3]
print(list1)
print("新增")
list1.append(4)
print(list1)

print("修改")
list1[0] = 6
print(list1)

print("插入")
list1.insert(4, 10)
print(list1)

print('------------' * 10)

# Comprehension 列表推導式
# [expression for item in iterable]
print("0~9 數列")
numbers = [x for x in range(10)]
print(numbers)

print("加入條件: x % 3 ==0")
print([x for x in range(10) if x % 3 == 0])


# 只顯示大於15
print("只顯示大於5:")
print([x for x in numbers if x > 5])

# 滿足條件的數對
print('找出0~19中相加為30的數對')
print([(x, y) for x in range(20) for y in range(20) if x + y == 30])

print('------------' * 10)

# tuple
T1 = ('apple', 'banana', 'lemon')
T2 = ('kiwi',)

print("分配變量")
fruit1, fruit2, fruit3 = T1
print(fruit2)

print("合併")
print(T1 + T2)

print('------------' * 10)

# dictionary
dict1 = {"name": "Ishikawa", "age": 28, "Height": "191", "position": 'OH'}
print(dict1['name'])

print("修改資料")
dict1['age'] = '30'
print(f'年記: {dict1["age"]}')

# comprehensive
print("0~4的平方值")
dict2 = {x: x ** 2 for x in range(5)}
print(dict2)

