from my_package import fib
import my_package.greet
import my_package.say #引用時要用全名


#for what ? 可以讓不同模組中有相同函式的名字，在引用時可以了解招喚的函式從何而來

print('------------' * 10)

print('不用帶前綴')
print(fib.fib2(3))
fib.ifmain()

print('------------' * 10)


print('不同模組中函式名稱相同')
my_package.greet.greet()
my_package.say.greet()

print('------------' * 10)
