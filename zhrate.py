#%%
import pandas as pd
import statsmodels.api as sm
import pmdarima as pm
from statsmodels.stats.diagnostic import acorr_ljungbox as lb_test

# 载入数据与初始化
df = pd.read_csv("D:/material/大学资料/毕业论文/实践/死亡率与预期寿命/kt.csv", encoding='gbk')
df = df.iloc[:, 1]
df.index = [str(i) for i in range(1959, 2021)]
# 给行命名
df.columns = "总和生育率"
# 给列命名
noise = []
model = []
future_value = []
# 对第i列数据进行时间序列预测，划分测试集和数据集
train = df.iloc[1:62]
res = sm.tsa.stattools.adfuller(train)
train1 = train - train.shift(1)
train1 = train1.iloc[1:]
res1 = sm.tsa.stattools.adfuller(train1)
train2 = train1 - train1.shift(1)
train2 = train2.iloc[1:]
res2 = sm.tsa.stattools.adfuller(train2)
#%%
re = lb_test(train2, lags=(len(train2)-1))
#%%
m = pm.auto_arima(train, d=2)
fit_data = m.fit(train)
fitted_values = m.predict_in_sample()
future_forecast = m.predict(n_periods=10)
future_forecast.index = [str(i) for i in range(2021, 2031)]
future_value.append(future_forecast)