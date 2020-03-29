import os
import pandas as pd
from scipy import stats

os.chdir('..')
path = os.getcwd()

def load_data(data_file):
    return pd.read_csv(data_file, header = 'infer')

def anova_scipy(data, alpha):    
    report = {}
    xlist = []
    for col in data:
        xlist.append(data[col].dropna().values)
    
    anova = stats.f_oneway(*xlist)
    report["F_statistic"] = round(anova[0], 4)
    report["p_value"] = round(anova[1], 4)
    if report["p_value"] <= alpha:
        report["significance"] = 1
        report["reject_H0"] = 1
    else:
        report["significance"] = 0
        report["reject_H0"] = 0
    return report

def main():
    data_file = path + '\\data\\NMttest.csv'
    df = load_data(data_file)
    alpha = 0.05
    anova_report = anova_scipy(df, alpha)
    print("F Stat :  ", anova_report["F_statistic"])
    print("P Value:  ", anova_report["p_value"])
    print("Significant Difference :  ", anova_report["significance"])
    print("Reject the null hypothesis:  ", anova_report["reject_H0"])

if __name__ == '__main__':
    main()