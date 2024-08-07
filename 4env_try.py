import os

#環境變數的使用情境:可以用來判斷該環境下需不需要執行某些程式碼
print("環境變數:")
print(os.getenv("TRY"))
print(os.getenv("VAR1"))
print(os.getenv("VAR2"))
print(os.getenv("DB"))
