"""
Analysis: Charlotte
"""

# IMPORT
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.linear_model import LinearRegression
import sklearn.metrics as metrics

# EXTRACT
df_CHA=pd.read_csv('generated_data/daily_CHA.csv', header=0)
df_CHA['date']=pd.to_datetime(df_CHA['date'], format='%Y-%m-%d')

# One year
data_1y=df_CHA[df_CHA.date.between('2017-01-01','2017-12-31')]
x=data_1y['date']
avg_star=data_1y['avg_stars']
moving_avg_star=avg_star.rolling(window=15).mean()
avg_precip=data_1y['avg_temp']
moving_avg_precip=avg_precip.rolling(window=15).mean()

fig, ax1=plt.subplots()

color= 'tab:red'
ax1.set_xlabel('date')
ax1.set_ylabel('avg_stars', color=color)
ax1.plot(x, avg_star, color=color, label='avg_stars', alpha=0.5)
ax1.plot(x, moving_avg_star, color=color, label='moving_avg_stars (15 days)')
ax1.tick_params(axis='y', labelcolor=color)

ax2=ax1.twinx()

color='tab:blue'
ax2.set_ylabel('precipitation', color=color)
ax2.plot(x, avg_precip, color=color, label='average temperature', alpha=0.5)
ax2.plot(x, moving_avg_precip, color=color, label='moving_avg_temperature (15 days)')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Average Stars, Temperature in Charlotte (2017)', fontsize=16)
fig.legend()

plt.show()

# correlation matrix
matrix_corr_CHA=df_CHA.corr()
matrix_corr_CHA_1y=data_1y.corr()
print('3 year matrix correlation')
print(matrix_corr_CHA)
print('1 year matrix correlation')
print(matrix_corr_CHA_1y)
# Regression
CHA=df_CHA

y=CHA['avg_stars']
x=CHA[['count_review','diff_precip','avg_temp']]
reg=LinearRegression()
reg.fit(x,y)
y_pred=reg.predict(x)


def regression_results(y_true, y_pred):

    # Regression metrics
    explained_variance=metrics.explained_variance_score(y_true, y_pred)
    mean_absolute_error=metrics.mean_absolute_error(y_true, y_pred)
    mse=metrics.mean_squared_error(y_true, y_pred)
    mean_squared_log_error=metrics.mean_squared_log_error(y_true, y_pred)
    median_absolute_error=metrics.median_absolute_error(y_true, y_pred)
    r2=metrics.r2_score(y_true, y_pred)
    print("Intercept: ", reg.intercept_)
    print("Coefficients:")
    lst_coef = list(zip(x, reg.coef_))
    for i in lst_coef:
        print(i[0], ' : ', i[1])
    print('\nexplained_variance: ', round(explained_variance,4))
    print('mean_squared_log_error: ', round(mean_squared_log_error,4))
    print('r2: ', round(r2,4))
    print('MAE: ', round(mean_absolute_error,4))
    print('MSE: ', round(mse,4))
    print('RMSE: ', round(np.sqrt(mse),4))
print('3 year linear regression\n')
regression_results(y,y_pred)
# Regression 1y

CHA=data_1y

y=CHA['avg_stars']
x=CHA[['count_review','diff_precip','avg_temp']]
reg=LinearRegression()
reg.fit(x,y)
y_pred=reg.predict(x)

print('1 year linear regression\n')
regression_results(y,y_pred)


