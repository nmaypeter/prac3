import numpy as np
import pandas as pd

groups = ["Modern Web", "DevOps", np.nan, "Big Data", "Security", "自我挑戰組"]
ironmen = [59, 9, 19, 14, 6, np.nan]

ironmen_dict = {
                "groups": groups,
                "ironmen": ironmen
}

# 建立 data frame
ironmen_df = pd.DataFrame(ironmen_dict)

ironmen_df_na_drop = ironmen_df.dropna() # 有遺失值的觀測值都刪除
print(ironmen_df_na_drop)
print("---") # 分隔線
ironmen_df_na_fill = ironmen_df.fillna(0) # 有遺失值的觀測值填補 0
print(ironmen_df_na_fill)
print("---") # 分隔線
ironmen_df_na_f = ironmen_df.fillna({"groups": "Cloud", "ironmen": 73})
print(ironmen_df_na_f)
print("---") # 分隔線