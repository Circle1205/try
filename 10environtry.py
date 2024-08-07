import os
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv("testENV.env")  # 如無指定檔名則讀取.env檔 程式碼要與.env檔在相同目錄
print("讀取testENV.env:")

User = os.environ.get('USER')
print(User)

DB = os.environ.get('DB')
print(DB)

port = os.environ.get('PORT')
print(port)

print("--" * 10)
print("讀取TestENV.env跟.env:")
# 讀取多檔 用dotenv_values
# dotenv_values ->只是用將,env檔的資料存成dict後回傳
configs = {
    **dotenv_values(".env"),
    **dotenv_values("testENV.env"),
    **os.environ,
}

print(configs.get("USER"))
print(configs.get("PORT"))
print(configs.get("DB"))
print(configs.get("ENV_NAME"))
print(configs.get("ENV_DB"))

# TODO:.env:環境變數可以用來區別測試或正式環境
