import pandas as pd

dict = {
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
    "k4": "v4",
    "k5": "v5",
}

select = pd.Series(dict, index=dict.keys()) # 排序與原 dict 相同

print(select[0])
print(select['k3'])
print(select[[0, 2, 4]])
print(select[[1]])
print(select[['k1', 'k2', 'k4']])

# Data Slice
print(select[2:])
print(select[:2])
print(select['k3':])