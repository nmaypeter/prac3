
# coding: utf-8

# In[1]:


import pandas as pd

name = ["蒙其·D·魯夫", "羅羅亞·索隆", "娜美", "騙人布", "賓什莫克·香吉士", "多尼多尼·喬巴", "妮可·羅賓", "佛朗基", "布魯克"]
occupation = ["船長", "劍士", "航海士", "狙擊手", "廚師", "醫生", "考古學家", "船匠", "音樂家"]

# 建立 dict
straw_hat_dict = {"name": name,
                  "occupation": occupation
}

# 建立第一個 data frame
straw_hat_df = pd.DataFrame(straw_hat_dict)

name = ["蒙其·D·魯夫", "多尼多尼·喬巴", "妮可·羅賓", "布魯克"]
devil_fruit = ["橡膠果實", "人人果實", "花花果實", "黃泉果實"]

# 建立 dict
devil_fruit_dict = {"name": name,
                    "devil_fruit": devil_fruit
}

# 建立第二個 data frame
devil_fruit_df = pd.DataFrame(devil_fruit_dict)

# 連接
straw_hat_merged = pd.merge(straw_hat_df, devil_fruit_df)
straw_hat_merged


# In[2]:


print(straw_hat_merged)


# In[3]:


pd.merge(straw_hat_df, devil_fruit_df, how = "left")


# In[4]:


pd.merge(straw_hat_df, devil_fruit_df, how = "right")


# In[5]:


pd.merge(straw_hat_df, devil_fruit_df, how = "outer")


# In[6]:


name = ["娜菲鲁塔利·薇薇"]
occupation = ["阿拉巴斯坦王國公主"]
princess_vivi_dict = {"name": name,
                      "occupation": occupation
}

# 建立第二個 data frame
princess_vivi_df = pd.DataFrame(princess_vivi_dict, index = [9])
princess_vivi_df


# In[7]:


# 新增一個觀測值
straw_hat_df_w_vivi = pd.concat([straw_hat_df, princess_vivi_df])
straw_hat_df_w_vivi

age = [19, 21, 20, 19, 21, 17, 30, 36, 90, 18]
age_dict = {"age": age
}

# 建立第三個 data frame
age_df = pd.DataFrame(age_dict)

# 新增一個變數欄位
straw_hat_df_w_vivi_age = pd.concat([straw_hat_df_w_vivi, age_df], axis = 1)
straw_hat_df_w_vivi_age


# In[8]:


straw_hat_df_w_vivi


# In[9]:


height = [174, 181, 170, 176, 180, 90, 188, 240, 277]

# 建立 dict
straw_hat_dict = {
    "name": name,
    "age": age,
    "height": height
}


# In[16]:


name = ["蒙其·D·魯夫", "羅羅亞·索隆", "娜美", "騙人布", "賓什莫克·香吉士", "多尼多尼·喬巴", "妮可·羅賓", "佛朗基", "布魯克"]
age = [19, 21, 20, 19, 21, 17, 30, 36, 90]
height = [174, 181, 170, 176, 180, 90, 188, 240, 277]

# 建立 dict
straw_hat_dict = {
    "name": name,
    "age": age,
    "height": height
}

# 建立一個長表格
straw_hat_df_long = pd.DataFrame(straw_hat_dict).stack().unstack()
straw_hat_df_long

