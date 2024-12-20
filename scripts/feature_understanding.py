import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

#plotes a bar plot for a specific column with specified number of returns
def plot_bar(data, column, top):
    ax = column.value_counts()\
                        .head(top)\
                        .plot(kind='bar')
    return ax

def plot_kde(data, column):
    ax = column.value_counts().plot(kind='kde')
    return ax

def top_10_handset(data):
    return data['Handset Type'].value_counts().head(10)
    
def top_manufacturer(data):
    return data['Handset Manufacturer'].value_counts().head(3)