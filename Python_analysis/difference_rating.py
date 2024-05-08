"""
We will analyse if there a significative difference between the cities in the ratings
"""

# IMPORT
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

# EXTRACT
df_CHA=pd.read_csv('generated_data/daily_CHA.csv', header=0)
df_CLE=pd.read_csv('generated_data/daily_CLE.csv', header=0)
df_LV=pd.read_csv('generated_data/daily_LV.csv', header=0)
df_PHO=pd.read_csv('generated_data/daily_PHO.csv', header=0)
df_PIT=pd.read_csv('generated_data/daily_PIT.csv', header=0)

# DATA MANIPULATION
frames=[df_CHA,df_CLE,df_LV,df_LV,df_PHO,df_PIT]
df_full=pd.concat(frames)
df_full.drop_duplicates(inplace=True)

# take the index out as a column, maybe useful for later
df_full_index=df_full.reset_index()

# date
df_full_date=df_full
df_full_date['date']=pd.to_datetime(df_full_date['date'])
df_full_date=df_full_date.sort_values('date')

# BOX PLOT
# all years (10y)
df_full_boxplot=df_full[['city','avg_stars']]
df_full_boxplot.boxplot(by='city', fontsize=14)
plt.title('all years (2008 to 2017)', fontsize=12)
plt.show()

# three last years (3y)
df_3y=df_full_date[df_full_date.date.between('2015-01-01','2017-12-31')]
df_3y_boxplot=df_3y[['city','avg_stars']]

df_3y_boxplot.boxplot(by='city')
plt.title('3 years (2015 - 2016 - 2017)', fontsize=12)
plt.show()

# one year (2017)
df_1y=df_full_date[df_full_date.date.between('2017-01-01','2017-12-31')]
df_1y_boxplot=df_1y[['city','avg_stars']]

df_1y_boxplot.boxplot(by='city')
plt.title('2017', fontsize=12)
plt.show()

# Seaborn
var = \
    ("""sns.catplot(
    data=iris, x='target', y='value',
    col='variable', kind='box', col_wrap=2)
    """)


# ANOVA-TEST
# all years
# sample size
df_full_boxplot['city'].value_counts()

stats.probplot(df_full_boxplot[df_full_boxplot['city']=='Charlotte']['avg_stars'], dist="norm", plot=plt)
plt.title('Probability Plot - Charlotte')
plt.show()
stats.probplot(df_full_boxplot[df_full_boxplot['city']=='Cleveland']['avg_stars'], dist="norm", plot=plt)
plt.title('Probability Plot - Cleveland')
plt.show()
stats.probplot(df_full_boxplot[df_full_boxplot['city']=='Las Vegas']['avg_stars'], dist="norm", plot=plt)
plt.title('Probability Plot - Las Vegas')
plt.show()
stats.probplot(df_full_boxplot[df_full_boxplot['city']=='Phoenix']['avg_stars'], dist="norm", plot=plt)
plt.title('Probability Plot - Phoenix')
plt.show()
stats.probplot(df_full_boxplot[df_full_boxplot['city']=='Pittsburgh']['avg_stars'], dist="norm", plot=plt)
plt.title('Probability Plot - Pittsburgh')
plt.show()

model=ols('avg_stars~C(city)', data=df_full_boxplot).fit()
anova_table_full=sm.stats.anova_lm(model, typ=2)
print(anova_table_full)

# three last years (3y)
df_3y_boxplot['city'].value_counts()

model=ols('avg_stars~C(city)', data=df_3y_boxplot).fit()
anova_table_3y=sm.stats.anova_lm(model, typ=2)
print(anova_table_3y)

# one year (2017)
df_1y_boxplot['city'].value_counts()

model=ols('avg_stars~C(city)', data=df_1y_boxplot).fit()
anova_table_1y=sm.stats.anova_lm(model, typ=2)
print(anova_table_1y)

# !!! uneven sample size -> not true because it's a daily basis so there is one average star per day
# but if we consider the number of review, then there is an unequal sample size

# 1. seems like no difference for 10 years -> ANOVA

# 2. seems like no difference for 3 years -> ANOVA

# 3. seems like a small difference for 1 year (2017) -> ANOVA -> plot rain and temperature (as assumption)

# 4. analysis for Charlotte and Las Vegas -> no clear evidence

# 5.

# ANOVA structure ()
data = [['Between Groups', '', '', '', '', '', ''], ['Within Groups', '', '', '', '', '', ''], ['Total', '', '', '', '', '', '']]
anova_table = pd.DataFrame(data, columns = ['Source of Variation', 'SS', 'df', 'MS', 'F', 'P-value', 'F crit'])
anova_table.set_index('Source of Variation', inplace = True)

# calculate SSTR and update anova table
x_bar = df_full_boxplot['avg_stars'].mean()
SSTR = df_full_boxplot.groupby('city').count() * (df_full_boxplot.groupby('city').mean() - x_bar)**2
anova_table['SS']['Between Groups'] = SSTR['avg_stars'].sum()

# calculate SSE and update anova table
SSE = (df_full_boxplot.groupby('city').count() - 1) * df_full_boxplot.groupby('city').std()**2
anova_table['SS']['Within Groups'] = SSE['avg_stars'].sum()

# calculate SSTR and update anova table
SSTR = SSTR['avg_stars'].sum() + SSE['avg_stars'].sum()
anova_table['SS']['Total'] = SSTR

# update degree of freedom
anova_table['df']['Between Groups'] = df_full_boxplot['city'].nunique() - 1
anova_table['df']['Within Groups'] = df_full_boxplot.shape[0] - df_full_boxplot['city'].nunique()
anova_table['df']['Total'] = df_full_boxplot.shape[0] - 1

# calculate MS
anova_table['MS'] = anova_table['SS'] / anova_table['df']

# calculate F
F = anova_table['MS']['Between Groups'] / anova_table['MS']['Within Groups']
anova_table['F']['Between Groups'] = F

# p-value
anova_table['P-value']['Between Groups'] = 1 - stats.f.cdf(F, anova_table['df']['Between Groups'], anova_table['df']['Within Groups'])

# F critical
alpha = 0.05
# possible types "right-tailed, left-tailed, two-tailed"
tail_hypothesis_type = "two-tailed"
if tail_hypothesis_type == "two-tailed":
    alpha /= 2
anova_table['F crit']['Between Groups'] = stats.f.ppf(1-alpha, anova_table['df']['Between Groups'], anova_table['df']['Within Groups'])

# Final ANOVA Table
print(anova_table)

