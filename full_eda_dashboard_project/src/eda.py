
import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path, parse_dates=['date'])
    return df

def quality_report(df):
    report = {}
    report['missing'] = df.isnull().sum()
    report['dtypes'] = df.dtypes
    report['describe'] = df.describe()
    return report

def add_time_features(df):
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['weekday'] = df['date'].dt.weekday
    return df

def missing_percentage(df):
    return (df.isnull().sum() / len(df)) * 100

def data_quality_report(df):
    report = {
        "missing": df.isnull().sum(),
        "missing_percent": (df.isnull().sum()/len(df))*100,
        "dtypes": df.dtypes,
        "describe": df.describe()
    }
    return report
