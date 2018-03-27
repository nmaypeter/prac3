import numpy as np

ironmen = [56, 8, 19, 14, 6, 71]
groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
ironmen_array = np.array(ironmen)
groups_array = np.array(groups)

# 用人數去篩選組別
print(ironmen_array >= 10) # 布林值陣列
print(groups_array[ironmen_array >= 10]) # 鐵人數大於 10 的組別
print(ironmen_array[ironmen_array >= 10]) # 鐵人數大於 10 的組別

# 用組別去篩選人數
print(groups_array != "自我挑戰組") # 布林值陣列
print(ironmen_array[groups_array != "自我挑戰組"]) # 除了自我挑戰組以外的鐵人數

# 建立一個 2d array
my_1d_array = np.arange(10)
my_2d_array = my_1d_array.reshape((2, 5))
print("---") # 分隔線
print(my_2d_array)
print("---") # 分隔線
print(my_2d_array.T)
print("---") # 分隔線
