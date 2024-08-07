
# 新人教育訓練


##  1.使用Pycharm

>    - 執行程式的方法
>    - 1.一般執行
>         - 右上角的三角形圖案
>         - 在project清單上想執行的檔案點擊右鍵，點選Run<filename>，程式即按照順序執行程式碼直到完成
>         - 在Pycharm右上角(Rum Widget)下拉選單選擇想執行的檔案
        
>    - 2.偵錯模式(debug)
>         - 右上角run旁邊的bug圖案
>         - 與一般模式一鍵跑到底不同，偵錯模式執行至(斷點)breakpoint即暫停運作，可以用來檢測程式到breakpoint當下的執行狀況， 
>           逐步確認中途的變數或輸出來找出出錯的地方，以確保最後輸出結果符合要求 
>         - breakpoint分為指定行數與例外(exception)
>         - 想在指定行數放置斷點只要在pycharm程式碼左邊行數點擊左鍵，或者在程式碼中輸入 breakpoint() 即可製造斷點
>         - 斷點行變藍即代表準備執行(尚未執行)
>         - 功能
>             - Rerun:Ctrl+F5，debug模式重新跑     
>             - resume :F9，跑到下一斷點 
>             - stop:ctrl+F2，停止，用來退出debug返回code編輯模式 
>             - view breakpoints:ctrl+shift+F8，查看所有的斷點 
>             
>             - step over:F8，單步執行，如果是函式則回傳函式結果
>             - step into:進入函式，如果是函式則開始函式逐行執行
>             - step into my code:只進入自定義的函式
>             - step out:函式執行到一半覺得沒問題，可以直接執行函式完畢並跳出函式


  > - 3.設定執行參數(parameters)
 >   - 當直譯器收到腳本名稱和額外引數後，會轉換成由字串組成的list並指派給sys模組的argv變數


  >   - 4.設定執行環境變數 (Environment variables)
  >     - pycharm可以透過右上角的edit configigurations功能，設定程式碼需要的環境變數，可以透過讀取.env檔或手動輸入
  >     - 使用.env檔儲存較機密資料(ex.資料庫帳密)，透過dotenv套件讀取.env檔以設定環境變數


  >  - 5.快速尋找方法或參數的「源頭」或是「有哪些方法在使用」

 >     - 1.找源頭
 >       - ctrl+B
 >       - 確認引用參數或方法的資料來源與內容
>     - 2.有哪些方法在使用
>       - ctrl+Alt+F7
>       - 更動前先確認引用的地方，如果有需要更動可以事先註解，以免出現錯誤
>       - 若要一次修改引用中的方法或參數名稱->右鍵->refactor->rename (shift+F6)
    
    
>    - 6.快速reformat程式碼
>        - 格式化，幫忙整理code空格、換行等，讓code看起來整齊乾淨，更好了解它的結構
>        - ctrl+Alt+L(單一檔案)
>        - ctrl+Alt+shift+L(整個project)

##   2.Python程式開發
>    - 1.如何執行一隻python程式
 >      -  在命令行或終端執行 
>       -  在Python編輯器或IDE中執行
>      - python直譯器(interpreter)將我們的程式碼翻譯成machine language ，讓電腦執行程式碼的要求
    
>    - 2.虛擬環境的操作
>       - 1. 進入專案目錄 C:\Users\irisyu\myenv>
>       - 2. 創建虛擬環境 C:\Users\irisyu\myenv>python -m venv myenv
>       - 3. 啟動 C:\Users\irisyu\myenv>myenv\Scripts\activate
>       - 4. 安裝套件 (myenv) C:\Users\irisyu\myenv>pip install 套件名
>       - 5. 離開 (myenv) C:\Users\irisyu\myenv>deactivate
>       -  虛擬環境提供我們獨立的環境去執行專案，以防止各專案間執行時套件與版本的衝突
>    - A.如何確認當前所在虛擬環境
>     - 確認有進入虛擬環境後，路徑前的小括號代表當下虛擬環境的名稱
>     
>    - B.requirements.txt的意義為何，如何建立與使用
>      - 是一份文本資料，紀錄python專案所需要使用的相依套件。每個套件以一行列出，須包含套件名稱與版本。
>      - 使用目的是大家建立專案後，方便共享與部署，並確保在不同環境下要重現專案時，透過文本的版本及套件資料來確保專案的環境與功能。
>      - pip freeze>requirements.txt
>    - 3.資料結構
>       - 1. Set { } 
>          - 無序、可變，集合中的多個元素不重複，使用逗號進行分隔
>          - 不需要考慮元素的順序與重複問題或需要進行集合運算時可以使用

>       - 2. List (*Comprehension)
>         - 存取多個元素，並需依索引值訪問元素時可使用，方便調整大小與修改內容
>         - [ expression for item in iterable ] 
>         -  可以完成有條件的序列
>       - 3. Tuple()
>         - 建立後不可修改，有序，可重複元素
>         - 若只有一個元素，後面需加上逗號
>             - 使用變數:可以一次賦予多個變數內容，變數數量要等於tuple的內容數量
>             - 索引值: 每個項目皆有所索引值offset，指定即可讀取該資料內容
        
>       - 4. Dictionary(*Comprehension)
>         - {key:value,key:value}，無序，可變
>         - 鍵與值唯一相對時，可以快速查找
    
> - 4.function
>   - 位置或關鍵字引數 (Positional-or-Keyword Arguments)
>     - 1. Positional Arguments(*args)
>       - 參數長度可變，會將位置參數收集到一個元組內
>       - 如果同時使用位置參數跟關鍵字參數，*args必須在所有參數後
>   
>     - 2. Keyword Arguments(**kwargs)
>       - 函式呼叫時，事先定義好參數並賦值，資料會存成一個dictionary
>       - 用來處理不定數量的關鍵字參數
>       
         

 >  - 5.return 與yield
>    - return會直到執行完結果再一次回傳，而yield可以做到將一長串運算分區進行，並單次輸出內容，避免記憶體一次使用過大問題 
   

  >  - 6.Type Hint
  >      - 事先註釋參數的型別(Type)，可以在後續閱讀程式碼更好理解與維護
  >      - 加上TypeHint可以讓IDE更好給函式提示
  


> - 7.Package(套件)及Module(模組)
>   - 1. Module(模組):為了重複使用function或class，將定義與函式放入檔案(.py)中，下次要使用時import檔案即可使用其中函式
>   - 2. Package是多個相關模組的目錄，必須包含一個名為"__init__.py"的檔案
  > -  如何引用與使用套件 
  >   - from [package] import[module] 
> 

> -8. if __name__ == '__main__'的意義
  >   - python執行時，檔案有個__name__隱藏變數，其意義是"模組名稱"，若該檔案為被引用，值為模組名稱 。
        若是透過命令列直接執行，值為__main__
  >   - if __name__ == '__main__'成立時，代表程式被當作主程式執行，而不是被當作模組引用
  >   - 有些指令在被引用時不需要執行，則使用此判斷式跳過不需要的指令
    
> - 9.環境變數如何設定與讀取(從IDE、python-dotenv設定)


> python延伸練習
> - 10.logging 
  >  - 層級與意義 
  >  - 分層的目的:可以指出日誌消息的重要性與嚴重性，讓使用者更好整理紀錄跟過濾log資訊
  >    - DEBUG:開發時使用
  >    - INFO:用來確認程式執行進度
  >    - WARNING:顯示警告EX.收到異常資料，不影響程式執行
  >    - ERROR:顯示某些功能因錯誤無法執行
  >    - CRITICAL:顯示程式已無法執行的訊息
    
   

> - 11.命名規則  (internal 是指class或module中private或protected變數)
  
  >  - 不使用"l"、"O"、"I"做單一字名稱
  >  - 開頭盡量不為"_"，不能以數字開頭
  >  - Package : 簡短、全小寫，lower_with_under 
  >  - Module  : 全小寫 lower_with_under
  >  - class   : 駝峰式 CapWords 
  >  - Function:全部小寫 lower_with_under()
  >  - Variable:小寫並用底線分字、好理解  lower_with_under
  >  - Global Constant:CAPS_WITH_UNDER (public), _CAPS_WITH_UNDER (private)

## 3.git
> - 1.什麼是git
>  - git是版本控制系統，主要功能的是追蹤文件的變更歷史，並支持恢復以前的版本，協助多人協作   
>  - 如何建立git repository
>    - 1. 全新的專案
>       - 1.建立目錄:C:\Users\irisyu\Desktop>mkdir try_git 
>       - 2.執行 C:\Users\irisyu\Desktop\try_git>git init
>    - 2. 已經有用git的專案 
>       - 1.C:\Users\irisyu\Desktop\try_git>git clone <網址or 檔名> <命名>
>    - 3. gitignore的意義
>       - 將不需要上傳的檔案寫在這，可以避免上傳到git，以免確認git status的時候過於繁雜
>   - 分支(branch)
>       - 允許在同個專案同時進行多個工作，不影響其他branch或主線(master)的程式碼
>
> - 何為衝突(conflict)  
>  -  當今天專案同時有超過一人以上修改同一行程式碼或檔案，造成合併(merge)分支時產生錯誤，即為衝突