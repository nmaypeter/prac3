
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import preprocessing, linear_model

url = "https://storage.googleapis.com/2017_ithome_ironman/data/kaggle_titanic_train.csv"
titanic_train = pd.read_csv(url)

# 將 Age 遺漏值以 median 填補
age_median = np.nanmedian(titanic_train["Age"])
new_Age = np.where(titanic_train["Age"].isnull(), age_median, titanic_train["Age"])
titanic_train["Age"] = new_Age
titanic_train

# 創造 dummy variables
label_encoder = preprocessing.LabelEncoder()
encoded_Sex = label_encoder.fit_transform(titanic_train["Sex"])

# 建立 train_X
train_X = pd.DataFrame([titanic_train["Pclass"],
                        encoded_Sex,
                        titanic_train["Age"]
]).T

# 建立模型
logistic_regr = linear_model.LogisticRegression()
logistic_regr.fit(train_X, titanic_train["Survived"])

# 印出係數
print(logistic_regr.coef_)

# 印出截距
print(logistic_regr.intercept_ )


# In[21]:


print("titanic_train[\"Survived\"] ="
      , logistic_regr.intercept_[0]
      , logistic_regr.coef_[0][0], " * titanic_train[\"Pclass\"]"
      , logistic_regr.coef_[0][1], " * encoded_Sex"
      , logistic_regr.coef_[0][2], " * titanic_train[\"Age\"]")


# In[22]:


from sklearn.feature_selection import f_regression
# 印出 p-value
print(f_regression(train_X, titanic_train["Survived"])[1])


# In[23]:


# 計算準確率
survived_predictions = logistic_regr.predict(train_X)
accuracy = logistic_regr.score(train_X, titanic_train["Survived"])
print(accuracy)

