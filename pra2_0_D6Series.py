import pandas as pd

groups = ['AAA', 'BBB', 'CCC', 'DDD']
ironman = [11, 22, 33, 44]

iron_dict = {
    "groups": groups,
    "ironman": ironman
}
'''
print(iron_dict)
print(type(iron_dict))
'''
iron_df = pd.DataFrame(iron_dict)

print(iron_df)
'''
print(type(iron_df))
'''
print("---")
'''
# 資料描述查看 
print(iron_df.shape) # 回傳列數與欄數
print("---")
print(iron_df.describe()) # 回傳描述性統計
print("---")
print(iron_df.head(3)) # 回傳前三筆觀測值
print("---")
print(iron_df.tail(3)) # 回傳後三筆觀測值
print("---")
print(iron_df.columns) # 回傳欄位名稱
print("---")
print(iron_df.index) # 回傳 index
print("---")
print(iron_df.info) # 回傳資料內容
'''
'''
# 資料選擇與篩選
print(iron_df.iloc[0, 1]) # 第一列第二欄：組的人數
print("---")
print(iron_df.iloc[0:1, :]) # 第一列：組的組名與人數
print("---")
print(iron_df.iloc[:, 1]) # 第二欄：各組的人數
print("---")
print(iron_df["ironman"]) # 各組的人數
print("---")
print(iron_df.ironman) # 各組的人數
'''

# 可以使用布林值篩選
print(iron_df[iron_df.loc[:, 'ironman'] > 30])