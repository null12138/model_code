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

def fitter(file,m):
    highs = data_reader(file)
    y = np.array(highs)
    x = list_creator(len(y)-1)
    x = np.array(x)
    x = Ex_translator(x,m)
    f_fitted_factor = np.polyfit(x,y,3)
    
    return f_fitted_factor

def fitter_list(file):
    highs = data_reader(file)
    y = np.array(highs)
    x = list_creator(len(y)-1)
    x = np.array(x)

    f_fitted_factor = np.polyfit(x,y,3)
    
    return x

def Ex_translator(ip,n):
    ip = (np.array(ip)+n).tolist()
    return ip

plt.rcParams['font.sans-serif']=['SimHei']
plt.suptitle(title)
plt.xlabel('日期')
plt.ylabel('搜索热度')

x1 = fitter('BS.csv',-5)
x2 = fitter('FS.csv',-1)
x3 = fitter('GM.csv',-0)
x4 = fitter('KS.csv',-7)
x5 = fitter('SZT.csv',-1)



f1_fitted = np.poly1d(x1)
f2_fitted = np.poly1d(x2)
f3_fitted = np.poly1d(x3)
f4_fitted = np.poly1d(x4)
f5_fitted = np.poly1d(x5)


plt.plot(fitter_list('BS.csv'),f1_fitted(fitter_list('BS.csv')),c='blue',label='鼻  塞,ΔT=5')
factors1 = x1
h_max_t_1 = max_finder(factors1[0],factors1[1],factors1[2])
plt.scatter(h_max_t_1,f1_fitted(h_max_t_1),c='blue')

plt.plot(fitter_list('FS.csv'),f2_fitted(fitter_list('FS.csv')),c='gold',label='发  烧,ΔT=1')
factors2 = x2
h_max_t_2 = max_finder(factors2[0],factors2[1],factors2[2])
plt.scatter(h_max_t_2,f2_fitted(h_max_t_2),c='gold')

plt.plot(fitter_list('GM.csv'),f3_fitted(fitter_list('GM.csv')),c='green',label='感  冒,ΔT=0')
factors3 = x3
h_max_t_3 = max_finder(factors3[0],factors3[1],factors3[2])
plt.scatter(h_max_t_3,f1_fitted(h_max_t_3),c='green')

plt.plot(fitter_list('KS.csv'),f4_fitted(fitter_list('KS.csv')),c='red',label='咳  嗽,ΔT=7')
factors4 = x4
h_max_t_4 = max_finder(factors1[0],factors1[1],factors1[2])
plt.scatter(h_max_t_4,f4_fitted(h_max_t_4),c='red')

plt.plot(fitter_list('SZT.csv'),f5_fitted(fitter_list('SZT.csv')),c='pink',label='嗓子疼,ΔT=1')
factors5 = x5
h_max_t_5 = max_finder(factors5[0],factors5[1],factors5[2])
plt.scatter(h_max_t_5,f5_fitted(h_max_t_5),c='pink')

plt.legend()
plt.show()