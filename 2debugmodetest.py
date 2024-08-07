numbers = [5, 4, 9, 3]
Ans = []
result = int(input())
for i in range(len(numbers)):
    frontnumber = numbers[i]

    for j in range(i + 1, len(numbers)):
        backnumber = numbers[j]
        if (frontnumber + backnumber == result):
            Ans.append(frontnumber)
            Ans.append(backnumber)

Ans = sorted(Ans)
print(Ans)
