
# coding: utf-8

# In[17]:


from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.cross_validation import train_test_split

# 讀入鳶尾花資料
iris = load_iris()
iris_X = iris.data
iris_y = iris.target

# 切分訓練與測試資料
train_X, test_X, train_y, test_y = train_test_split(iris_X, iris_y, test_size = 0.3)

# 建立分類器
clf = tree.DecisionTreeClassifier()
iris_clf = clf.fit(train_X, train_y)

# 預測
test_y_predicted = iris_clf.predict(test_X)
print(test_y_predicted)

# 標準答案
print(test_y)


# In[26]:


count = 0
for i in range(0, len(test_y_predicted)):
    if test_y_predicted[i] != test_y[i]:
        count += 1
        print(i, end=" ")

print("\n", count)


# In[25]:


from sklearn import metrics
accuracy = metrics.accuracy_score(test_y, test_y_predicted)
print(accuracy)


# In[70]:


from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn import metrics


# 讀入鳶尾花資料
iris = load_iris()
iris_X = iris.data
iris_y = iris.target

def SplitIris(times):
    maxi = 0
    for j in range(times):
        # 切分訓練與測試資料
        train_X, test_X, train_y, test_y = train_test_split(iris_X, iris_y, test_size = 0.3)
        
        # 建立分類器
        clf = tree.DecisionTreeClassifier()
        iris_clf = clf.fit(train_X, train_y)
        
        # 預測
        test_y_predicted = iris_clf.predict(test_X)
        
        count = 0
        for i in range(0, len(test_y_predicted)):
            if test_y_predicted[i] != test_y[i]:
                count += 1
                print(count, end=" ")
            
            if count > maxi:
                maxi = count
                
        print("")
    
    return maxi   


SplitIris(3)

