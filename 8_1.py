# -*- coding: UTF-8 -*-
import math
import matplotlib.pyplot as plt



y=[]#输出序列
x=[]#时间序列
q=80#模拟采样周期数
for i in range(0,q):
    x.append(i+1)#x的序列
T=[1,2,4,6,1.5,5]#采样周期
for i in range(0,len(T)):
    y.append([])#y定义为多个采样周期的集合
    
def shengchengY(t,h):#计算y
    a=100/t/t
    b=20/t+200/t/t
    c=1+20/t+100/t/t
    y[h].append(1/c)
    y[h].append(1/c+b/c/c)
    for i in range(2,q):
        y[h].append(1/c+b/c*y[h][i-1]-a/c*y[h][i-2])


def plotData(x,y,t):  #生成曲线，标题为采样周期T的大小
    a='T='
    a+=str(t)
    a+='s Step response curve'
    plt.title(a) 
    plt.ylabel('y')
    plt.plot(x,y)

    
def shuchuquxian(x,y):#将多个曲线显示在一个窗口，并布置
    fig=plt.figure(figsize=(12.0,8.0))
    fig.subplots_adjust(left=0.05,right=0.95,bottom=0.05,top=0.95)
    figcount=len(T)
    figcol=2
    figrow=math.ceil(figcount/figcol)
    for i in range(figcount):
        fig.add_subplot(figrow, figcol,i+1)
        plotData(x,y[i],T[i])
    plt.show()

  

for i in range(0,len(T)):#生成y
    shengchengY(T[i],i)
shuchuquxian(x, y)