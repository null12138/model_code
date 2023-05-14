import numpy as np
import streamlit.pyplot as plt
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

def fitter(file,title):
    highs = data_reader(file)
    y = np.array(highs)
    x = list_creator(len(y)-1)
    x = np.array(x)

    f_fitted_factor = np.polyfit(x,y,3)
    p_fitted = np.poly1d(f_fitted_factor)

    plt.rcParams['font.sans-serif']=['SimHei']
    plt.suptitle(title)
    plt.xlabel('日期')
    plt.ylabel('搜索热度')

    plt.plot(x,y,c='blue',label='原图像')
    plt.plot(x, p_fitted(x),c='red',label='拟合后的图像')

    factors = f_fitted_factor

    h_max_t = max_finder(factors[0],factors[1],factors[2])
    plt.scatter(h_max_t,p_fitted(h_max_t),c='red')
    plt.axvline(x=h_max_t,ls="--",c="black")
    plt.text(h_max_t+5,p_fitted(h_max_t)+5,h_max_t)

    plt.legend()
    plt.show()
    #print the number of x
    print("x的个数为：",len(x))
    #print the number of y
    print("y的个数为：",len(y))
    return f_fitted_factor

print(fitter("KS.csv","关键词：咳嗽"))
print(fitter("FS.csv","关键词：发烧"))
print(fitter("SZT.csv","关键词：嗓子疼"))
print(fitter("GM.csv","关键词：感冒"))
print(fitter("BS.csv","关键词：鼻塞"))
