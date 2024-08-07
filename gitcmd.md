## 1. 創建目錄
C:\Users\irisyu\Desktop>mkdir trygit2

C:\Users\irisyu\Desktop\trygit2>git init

## 2. 複製已經有git的專案
C:\Users\irisyu\Desktop\try_git>git clone  <網址或檔名>  <目錄名稱>
# 試本地
## 3. 創建.gitignore檔
C:\Users\irisyu\Desktop\trygit2>echo.>.gitignore

C:\Users\irisyu\Desktop\trygit2>git status

## 4. 告知即將提交
C:\Users\irisyu\Desktop\trygit2>git add waittoc.txt

## 5. 提交commit
C:\Users\irisyu\Desktop\trygit2>git commit -m try1
(後面是commit massage)


## 6. 返回版本

## (操作不打hard)
C:\Users\irisyu\Desktop\trygit2>git reset --hard <版本號>

## 7. 還原檔案
##### 還原內容
C:\Users\irisyu\Desktop\trygit2>git checkout -- new1.txt  
(--是用來指出後面內容為文件名)
##### 還原狀態
(從準備提交變回unstage)
C:\Users\irisyu\Desktop\trygit2>git checkout -- new1.txt
##### 清空
C:\Users\irisyu\Desktop\trygit2>git reset --hard HEAD



## 8. 分支(branch)
C:\Users\irisyu\Desktop\trygit2>git branch (查看所有分支)
## 9. 建立分支
C:\Users\irisyu\Desktop\trygit2>git branch try
切換
C:\Users\irisyu\Desktop\trygit2>git checkout try


## 10.衝突 (在兩個Branch編輯同一檔案並交後合併)
C:\Users\irisyu\Desktop\trygit2>git branch <分支名>  # 創建分支
C:\Users\irisyu\Desktop\trygit2>git checkout <分支名> #切換分支
C:\Users\irisyu\Desktop\trygit2>git merge <別的分支名> #與現分支合併

合併後打開錯誤檔案
修改留下需要的內容 
重新commit



## 11.上傳github
cd C:\Users\yuhao\IdeaProjects\myproject    #要上傳的檔案位置

輸入git config --global user.name "pc端使用者名稱"
再輸入git config --global user.email example@email.com


git init
git add README.md (打git add .就好)
git commit -m "first commit" (""中為敘述，可任意更改)
git branch -M main
git remote add origin https://github.com/Circle1205/-name--basic-training.git 
(https後的那串每個人都不同，結構為https://github.com/使用者名稱/空間名.git)
git push -u origin main (意即push)
