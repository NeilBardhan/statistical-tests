import os
import pandas as pd
from scipy import stats

os.chdir('..')
path = os.getcwd()

def load_data(data_file):
    return pd.read_csv(data_file, header = 'infer')

def anova_scipy(data):
    xlist = []
    for col in data:
        xlist.append(data[col].dropna().values)
    anova = stats.f_oneway(*xlist)
    return anova

def main():
    data_file = path + '\\data\\NMttest.csv'
    df = load_data(data_file)
    alpha = 0.05
    sig_flag = 0
    anova0 = anova_scipy(df)
    anova0_F = round(anova0[0], 4)
    anova0_pval = round(anova0[1], 4)
    if anova0_pval <= alpha:
        sig_flag = 1
    print("F Stat :  ", anova0_F)
    print("P Value:  ", anova0_pval)
    print("Significant Difference :  ", sig_flag)

if __name__ == '__main__':
    main()