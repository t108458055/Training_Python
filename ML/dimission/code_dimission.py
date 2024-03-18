#1. 提出問題  目的 那些因素更容易影響員工的離職
# 引入library
import numpy as np #引入　numpy
import pandas as pd #引入Pandas
import warnings  # 引入warnings module 用於管理警告
warnings.filterwarnings('ignore') #忽略警告訊息
#導入數據
#訓練數據導入
trains =  pd.read_csv('./data/pfm_train.csv') #導入數據
#測試數據導入
test =  pd.read_csv('./data/pfm_test.csv')
# print(f'訓練數據:\n', trains)
# print(f'測試數據:\n', test)
print(f'訓練數據:', trains.shape) # .shape 第一元素是行數colume 第二元素是列數 rows
print(f'訓練數據: 行數colume = {trains.shape[0]}, 列數reows = {trains.shape[1]}') 
print(f'測試數據:', test.shape)
#合併數據 ,以利於兩個數據集進行清洗
full = pd.concat([trains, test], ignore_index = True) #合併兩個數據 並忽略原始索引 ,產生新的數據集索引
print(f'合併後數據集:',full.shape)
# 使用 pandas describe 進行描述性統計 包括 計數、均值、標準差、最小值、25%分位數、50%中位數、75%分位數，最大值
full.describe()
# 查看數據字段資訊
full.info()
# 3數據清洗
# * 特徵值提取
# 分類數據 用數值代替類別one hot 編碼
#性別 公 1 母 0
full['Gender'] = full.Gender.map({'Male':1, 'Female': 0}) # 使用map函數將性別轉換
full.Gender.head()
# 是否加班 1 加班 0 不加班
full['OverTime'] = full.OverTime.map({'Yes':1, 'No': 0}) # 使用map函數
full.OverTime.head()
# 年齡是否超過18
full['Over18'] = full.Over18.map({'Y':1}) # 使用map函數
full.Over18.head()
# 出差頻率: 用get_dummies進行 one hot編碼 產生虛擬變量 One Hot Encoding(獨熱)
BusinessTravel_Df = pd.get_dummies(full.BusinessTravel, prefix='BT')
BusinessTravel_Df.head()
# 員工所在部門: 用get_dummies進行 one hot編碼 產生虛擬變量 One Hot Encoding(獨熱)
Department_Df = pd.get_dummies(full.Department, prefix='Depart')
Department_Df.head()
#專業領域
EducationField_Df=pd.get_dummies(full.EducationField,prefix='Edu')
EducationField_Df.head()
#工作角色
JobRole_Df = pd.get_dummies(full.JobRole,prefix='JR')
JobRole_Df.head()
# 婚姻狀況
MaritalStatus_Df = pd.get_dummies(full.MaritalStatus,prefix='MS')
MaritalStatus_Df.head()
# 將數據集和產生的虛擬變量合併
fullDf = pd.concat([full,BusinessTravel_Df,Department_Df,EducationField_Df,JobRole_Df,MaritalStatus_Df],axis=1)
print(fullDf)
#刪除原來的分辨量
fullDf.drop(['BusinessTravel','Department','EducationField','JobRole','MaritalStatus'],axis=1,inplace=True)
print(fullDf)
print('新的數據集Size：',fullDf.shape)
print('*'*50)
fullDf.info()
# 特徵選擇
# 相關係數 計算各個特徵與標籤的相關係數
fullDf.corr().Attrition.sort_values(ascending = False)
# 可以看到加班（overtime）和離職（attrition）有較高的正相關性，而總工齡（TotalWorkingYears）與attrition有較高的負相關性。
#刪除不相關的數據
fullDf.drop(['Over18','StandardHours','EmployeeNumber'],axis=1, inplace=True)
#原始數據集特徵
source_X=fullDf[:1100]
source_X.drop('Attrition',axis=1,inplace=True)
source_X.head()
#原始數據集標籤 
source_y=fullDf.loc[:1099,'Attrition']
source_y.head()
# 預測數據集特徵
pred_X=fullDf[1100:]
pred_X.drop('Attrition',axis=1,inplace=True)
pred_X.head()
print('原始集特徵：',source_X.shape)
print('原始集標籤：',source_y.shape)
print('預測集特徵：',pred_X.shape)
# 4.建構模型
# 4.1 建立數據集和測試數據集
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

#特徵縮放
scaler = StandardScaler()
source_X_scaler = scaler.fit_transform(source_X)
pred_X_scaler = scaler.transform(pred_X)
# 將原始集按照4:1分割成訓練集和測試集
train_X,test_X,train_y,test_y=train_test_split(source_X_scaler,source_y,test_size=0.2,random_state=123)
print('訓練數據集特徵：',train_X.shape)
print('測試數據集特徵：',test_X.shape)
print('訓練數據標籤：',train_y.shape)
print('測試練數據標籤：',test_y.shape)
# 4.2 選擇機器學習算法
# 選項選擇邏輯回歸算法
#邏輯回歸模型
from sklearn.linear_model import LogisticRegression
# 網格搜索
from sklearn.model_selection import GridSearchCV

#利用GSV 網格搜索最優參數值
lg = LogisticRegression()
clf = GridSearchCV(lg, param_grid=[{'C':np.arange(0.001,0.005,0.001)}],cv=5)
#4.3 訓練模型 並得到最好參數
clf.fit(train_X,train_y)
best_model = clf.best_estimator_
clf.best_params_
# 5.評估模型
#  分類問題 score 得到的是模型準確率
best_model.score(test_X, test_y)
# 6 方案實施
# predict 預測
result = best_model.predict(pred_X_scaler)
result

result=result.astype(int)
result_Df=pd.DataFrame({'result':result})
print(result_Df)
# result_Df.to_csv('result.csv',index=False)

"""ref:
jaygege/dimission: 员工离职预测训练赛：利用pandas和sklearn包，分析哪些因素会影响员工的离职情况，并对测试集进行相关预测。
https://github.com/jaygege/dimission/tree/master
    
"""