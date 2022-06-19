from gmssl import sm3,func
import time,os,math
import numpy as np
round=0
flag=0
bit_num=32                                           #碰撞位数
count=2<<(int(bit_num/2)-1)                          #生日攻击，选取消息的数目
print(int(bit_num/2))
print(count)
while(1):
    y={}
    s={}
    x=[]
    round=round+1
    data_1=[os.urandom(64) for i in range (count)]   #随机生成64byte的数据，作为Hash函数的输入
    for i in range (count):
        y[i] = sm3.sm3_hash(func.bytes_to_list(data_1[i]))  #SM3
        #print(y[i])
        x.append(int(y[i][0:int(bit_num/4)],16))     #截取Hash结果的前bit_num/4位并转化成int型
    #z=[0]*(2<<bit_num-1)
    z=np.zeros(2<<bit_num-1,int)
    print(x)
    r={}
    for i,j in enumerate(x):                         #查找Hash结果中是否存在碰撞
        z[j]=z[j]+1
        if z[j]>=2:
            flag=1
            r[j]=(r[j],y[i])
            print("第%d轮，发现碰撞"%(round))
            print("碰撞比特：",x[i],hex(x[i]))
            print(r[j])
            break
        r[j]=y[i]
    if flag==1:
        break
    #if round==1:
        #print(111)
    #if round==2:
        #print(222)

