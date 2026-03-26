
import scipy.stats as stats
import pandas as pd

def shapiro_test(series):
    return stats.shapiro(series)

def normality_test(data):
    return stats.shapiro(data)

def t_test(a, b):
    return stats.ttest_ind(a, b)

def chi_square_test(df, col1, col2):
    table = pd.crosstab(df[col1], df[col2])
    return stats.chi2_contingency(table)