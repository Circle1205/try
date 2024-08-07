# Fibonacci numbers module

def fib(k):  # write Fibonacci series up to n

    a, b = 0, 1
    while a < k:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def ifmain():
    print(f'來自{__name__}的函式')
    if __name__ == '__main__':
        print('主程式')
    else:
        print('被引用')


if __name__ == '__main__':
    ifmain()

print("寫在外面的話，import時會先被執行")