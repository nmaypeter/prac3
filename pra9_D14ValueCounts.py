import pandas as pd

gender = ["Male", "Male", "Female", "Male", "Male", "Pet", "Female", "Male", "Skeleton"]
name = ["蒙其·D·魯夫", "羅羅亞·索隆", "娜美", "騙人布", "文斯莫克·香吉士", "多尼多尼·喬巴", "妮可·羅賓", "佛朗基", "布魯克"]

# 建立 data frame
sex = pd.DataFrame(gender, columns=["gender"], index=name)
'''print(sex)'''

# 計算男女各有幾個觀測值
print(pd.value_counts(sex.gender))