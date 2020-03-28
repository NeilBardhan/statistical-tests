import os
import pandas as pd
from scipy import stats

os.chdir('..')
path = os.getcwd()

data_file = path + '\\data\\NMttest.csv'
data = pd.read_csv(data_file, header = 'infer')

anova = stats.f_oneway(data['shiftClass21'].dropna().values, data['shiftClass22'].dropna().values,
               data['shiftClass23'].dropna().values, data['shiftClass31'].dropna().values,
               data['shiftClass32'].dropna().values)
print(anova)