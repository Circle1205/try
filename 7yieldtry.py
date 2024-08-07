def fibreturn(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print(fibreturn(3))
print('-----------' * 10)


# return是一次性回傳所有答案


def fibyield():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  # a.b持續追蹤前兩個數字


g = fibyield()

for _ in range(4):
    print(next(g))
# yeild則是製造生成器，可以單次計算回傳，可以用next跟for控制計算
