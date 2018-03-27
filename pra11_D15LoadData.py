import pandas as pd

url = "https://storage.googleapis.com/2017_ithome_ironman/data/iris.csv" # 在雲端上儲存了一份 csv 檔案
iris_df = pd.read_csv(url)
iris_df.head()