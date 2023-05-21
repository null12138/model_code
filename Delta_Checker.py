import numpy as np
import matplotlib.pyplot as plt
import csv
import math

title = ""
file = ''
f_fitted_factor = []
def list_creator(i):
    lst = []
    for j in range(i+1):
        lst.append(j)
    return(lst)

def data_reader(filename):
    with open(filename,encoding='UTF-8') as f:

        reader = csv.reader(f)
        header_row = next(reader)  
        highs = []
        for row in reader:
            high = int(row[5])
            highs.append(high)
    return(highs)

def max_finder(a,b,c):
    delta_1 = 4*b*b-12*a*c
    delta = math.sqrt(delta_1)
    t = -2*b-delta
    t_2 = t/(6*a)
    return t_2

def fitter(file):
    highs = data_reader(file)
    y = np.array(highs)
    x = list_creator(len(y)-1)
    x = np.array(x)

    f_fitted_factor = np.polyfit(x,y,3)
    
    return f_fitted_factor

def fitter_list(file):
    highs = data_reader(file)
    y = np.array(highs)
    x = list_creator(len(y)-1)
    x = np.array(x)

    f_fitted_factor = np.polyfit(x,y,3)
    
    return x

plt.rcParams['font.sans-serif']=['SimHei']
plt.suptitle(title)
plt.xlabel('日期')
plt.ylabel('搜索热度')

x1 = fitter('BS.csv')
x2 = fitter('FS.csv')
x3 = fitter('GM.csv')
x4 = fitter('KS.csv')
x5 = fitter('SZT.csv')

f1_fitted = np.poly1d(x1)
f2_fitted = np.poly1d(x2)
f3_fitted = np.poly1d(x3)
f4_fitted = np.poly1d(x4)
f5_fitted = np.poly1d(x5)

def checker(xx):
    a = 4 * xx[1] * xx[1]
    b = 12 * xx[0] * xx[2]
    if(a - b > 0 ):
        return "True"
    else:
        return "False"

print("x1: %s "%(checker(x1)))
print("x2: %s "%(checker(x2)))
print("x3: %s "%(checker(x3)))
print("x4: %s "%(checker(x4)))
print("x5: %s "%(checker(x5)))
