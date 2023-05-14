import numpy as np
def Ex_translator(ip,n):
    ip = (np.array(ip)+n).tolist()
    return ip
x = [0,1,2,3]
print(Ex_translator(x,2))