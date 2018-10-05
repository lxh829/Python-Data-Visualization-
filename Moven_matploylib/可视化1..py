import matplotlib.pyplot as plt
import numpy as np
#这是所有有关的函数和数据，linespace命令是(以下面为例）从-3到10上等分取100个点
x = np.linspace(-3,10,100)
y1 = x**2 + 5
y2 = 2**x + 2
y3 = x**3 + 1
y4 = x**3 + x**2 + 2
y5 = 2*x + 2
#这是画出的第一个图，num=3是图的编号为3，figsize是图的大小，长，宽
plt.figure(num=3,figsize=(8,5))
plt.plot(x,y1)
#这是画出的第二个图，这个图中一共4条线，linewidth线的宽度，linestyle线的类型
plt.figure(num=6,figsize=(9,6))
plt.plot(x,y2,c='C5',linewidth=1.0,linestyle='--')
plt.plot(x,y3,c='C6',marker='D',linewidth=1.0,linestyle='--')
plt.plot(x,y4,c='C8',marker='*',linewidth=1.0,linestyle='-.')
plt.plot(x,y5,c='C9',marker='<',linewidth=1.0,linestyle=':')

plt.show()

