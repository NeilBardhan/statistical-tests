import os
import pandas as pd
from scipy import stats
from statistics import mean

os.chdir('..')
path = os.getcwd()

def load_data(data_file):
    return pd.read_csv(data_file, header = 'infer')

def anova(data, alpha):
    report = {}
    ss_list = []
    square_list = []
    N = 0
    k = 0
    total_sum = 0
    for col in data:
        k += 1
        col_mean = mean(data[col].dropna().values)
        N += len(data[col].dropna().values)
        total_sum += sum(data[col].dropna().values)
        square_list.append(sum([i ** 2 for i in data[col].dropna().values]))
        ss_list.append(sum([(i - col_mean) ** 2 for i in data[col].dropna().values]))
    ssw = sum(ss_list)
    sst = sum(square_list) - ((total_sum ** 2)/N)
    ssb = sst - ssw
    dfb = k - 1
    dfw = N - k
    msb = ssb/dfb
    msw = ssw/dfw
    F = round(msb/msw, 4)
    pvalue = round(stats.f.sf(F, dfb, dfw), 4)
    report["F_statistic"] = F
    report["p_value"] = pvalue
    if report["p_value"] <= alpha:
        report["significance"] = 1
        report["reject_H0"] = 1
    else:
        report["significance"] = 0
        report["reject_H0"] = 0
    return report

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

def print_report(report):
    print("F Stat :  ", report["F_statistic"])
    print("P Value:  ", report["p_value"])
    print("Significant Difference :  ", report["significance"])
    print("Reject the null hypothesis:  ", report["reject_H0"])

def main():
    data_file = path + '\\data\\NMttest.csv'
    df = load_data(data_file)
    alpha = 0.05
    print("\nscipy\n")
    print_report(anova_scipy(df, alpha))
    print("\nmanual\n")
    print_report(anova(df, alpha))

if __name__ == '__main__':
    main()