import pandas as pd # 引用套件並縮寫為 pd

groups = ["Modern Web", "DevOps", "Cloud", "Big Data", "Security", "自我挑戰組"]
# 截至 2016-12-11 上午 11 時第 8 屆 iT 邦幫忙各組的鐵人分別是 54、8、18、14、6 與 65 人
ironmen = [54, 8, 18, 14, 6, 65]

ironmen_dict = {"groups": groups,
                "ironmen": ironmen
                }

ironmen_df = pd.DataFrame(ironmen_dict)
print(ironmen_df.dtypes)
ironmen_df.head(n=3)