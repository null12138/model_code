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


plt.plot(fitter_list('BS.csv'),f1_fitted(fitter_list('BS.csv')),c='blue',label='鼻塞')
factors1 = fitter('BS.csv')
h_max_t_1 = max_finder(factors1[0],factors1[1],factors1[2])
plt.scatter(h_max_t_1,f1_fitted(h_max_t_1),c='red')

plt.plot(fitter_list('FS.csv'),f2_fitted(fitter_list('FS.csv')),c='gold',label='发烧')
factors2 = fitter('FS.csv')
h_max_t_2 = max_finder(factors2[0],factors2[1],factors2[2])
plt.scatter(h_max_t_2,f2_fitted(h_max_t_2),c='red')

plt.plot(fitter_list('GM.csv'),f3_fitted(fitter_list('GM.csv')),c='green',label='感冒')
factors3 = fitter('GM.csv')
h_max_t_3 = max_finder(factors3[0],factors3[1],factors3[2])
plt.scatter(h_max_t_3,f1_fitted(h_max_t_3),c='red')

plt.plot(fitter_list('KS.csv'),f4_fitted(fitter_list('KS.csv')),c='red',label='咳嗽')
factors4 = fitter('KS.csv')
h_max_t_4 = max_finder(factors1[0],factors1[1],factors1[2])
plt.scatter(h_max_t_4,f4_fitted(h_max_t_4),c='red')

plt.plot(fitter_list('SZT.csv'),f5_fitted(fitter_list('SZT.csv')),c='pink',label='嗓子疼')
factors5 = fitter('SZT.csv')
h_max_t_5 = max_finder(factors5[0],factors5[1],factors5[2])
plt.scatter(h_max_t_5,f5_fitted(h_max_t_5),c='red')

plt.legend()
plt.show()