# list
# tuple
# dictionary

# 當直譯器收到腳本名稱和額外引數後，會轉換成由字串組成的list並指派給sys模組的argv變數
import sys


print("用list儲存變數" , sys.argv)

print(f"腳本名: {sys.argv[0]}")  # 腳本名

print(f'list長度: {len(sys.argv)}')

if len(sys.argv) > 2:
    a = eval(sys.argv[1])
    b = eval(sys.argv[2])
    print(f"a+b= {a + b}")

else:
    print("沒有參數")
# python


