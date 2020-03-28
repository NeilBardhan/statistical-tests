import os
import math
import csv
from scipy import stats
from itertools import combinations
import time

def ttest(writer, combo, a, b):
    sigFlag = 0
#    print("Combo of", combo[0], "and", combo[1])
    sumA = float(sum(a))
    sumB = float(sum(b))

    sumAsq = sumA ** 2
    sumBsq = sumB ** 2

    avgA = sumA/len(a)
    avgB = sumB/len(b)

    ssqA = sum(map(lambda x: x ** 2, a))
    ssqB = sum(map(lambda x: x ** 2, b))
    df = len(a) + len(b) - 2

    t = (avgA - avgB)/math.sqrt((((ssqA - sumAsq/len(a))+(ssqB - sumBsq/len(b)))/df)*(1.0/len(a)+1.0/len(b)))
#    print("T value ->", t)

    pval = stats.t.sf(abs(t), df)*2
#    print("2 Tailed P value ->", pval)

    if(pval < 0.05):
        sigFlag = 1
    res = [combo[0], combo[1], round(t, 5), df, round(pval, 6), sigFlag]
    writer.writerow(res)
#    print(res)

def main():
    ctr = 0
    path = os.getcwd()
    start = time.time()
    results = open(path + '\\results.csv', 'wt', newline='')
    writer = csv.writer(results, delimiter = ',')
    head = ['var_1', 'var_2', 't_value', 'degrees_of_freedom', 'p_value', 'significant']
    writer.writerow(head)
    rstart = time.time()
    csvFile = path + "\\data\\NMttest.csv"
    with open(csvFile, newline='') as fp:
        reader = csv.DictReader(fp)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]
        for key, value in data.items():
            data[key] = list(filter(None, data[key]))
            data[key] = list(map(lambda x: float(x), data[key]))
        featureCombos = (list(combinations(data.keys(),2)))
        print("Time to read file ->", round(time.time() - rstart, 3), "seconds.", end = '\n')
        print("Total Combinations ->", len(featureCombos))
        for elem in featureCombos:
            ctr += 1
            sampleA = data[elem[0]]
            sampleB = data[elem[1]]
            ttest(writer, elem, sampleA, sampleB)
            print('Write success. Combination number ->', ctr, end = '\n')
#        print(data)
#    csvFile.close()
    results.close()
    fin = time.time() - start
    print("Total Time Elapsed ->", round(fin, 3), "seconds." ,end = '\n')
if __name__ == '__main__':
    main()
