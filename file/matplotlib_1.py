import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import matplotlib
#print(dir(matplotlib))

#print(dir(plt))
##############################################
"""a =[10,20,30,35,4]
plt.plot(range(len(a)),a)#Line Plot
#plt.show()
x1 = range(10)
y1 = pd.Series(x1) **2
y2 = pd.Series(x1) **3
plt.plot(x1,y1,x1,y2)
plt.show()"""
##############################################
"""a =[10,20,30,35,4]
plt.figure(figsize =(16,5))
plt.subplot(1,2,1)

plt.plot(range(len(a)),a,'ro')#Marker = '^' line lopting
#plt.show()
x1 =range(10)
y1 = pd.Series(x1) **2
y2 = pd.Series(x1) **3
plt.subplot(1,2,2)
plt.plot(x1,y1,x1,y2)
plt.show()"""
##############################################
df= pd.read_csv('titanic_result.csv')
"""#print(df.head())
plt.plot(range(len(df.age)), df.age.sort_values())
plt.show()
r = df.gender.value_counts()
plt.figure(figsize =(16,5))
plt.subplot(1,2,1)
print(r)
print(r.plot(kind ='bar'))
plt.subplot(1,2,2)
plt.bar(r.index,r.values)
for idx in r.index:
    plt.text(idx,r[idx],str((r[idx],idx)))"
plt.show()"""
##############################################
"""r = df.gender.value_counts()
plt.figure(figsize=(16,5))
#pandas ploting
plt.subplot(1,2,1)
print(r)
print(r.plot(kind='barh'))
#usning matplotlib
plt.subplot(1,2,2)
plt.barh(r.index,r.values)
plt.show()"""
##############################################
"""r =df.gender.value_counts()
plt.figure(figsize=(16,5))
plt.subplot(1,2,1)
print(r)
print(r.plot(kind='pie'))
plt.subplot(1,2,2)
plt.pie(r.values,labels=r.index)
plt.legend()
plt.show()"""
##############################################
"""x = pd.Series(range(10))
y1 =x *2
y2 =x *4
plt.plot(x,y1, label ='s1')
plt.plot(x,y2, label = 's2')
plt.legend()
#plt.yticks(range(0,100,10))
plt.title('Title')
plt.xlabel('X-axis')
plt.ylabel('age')
plt.text(6,20,'Graph')
plt.show()"""
#############################################
"""x =pd.Series(range(10))
y =(x)**2
plt.plot(x,y)
plt.stem(x,y)
plt.axvline(1.5, ymin=0.2,  linewidth=5,  c='g')
plt.savefig('graph.png')
plt.show()"""
#############################################
"""plt.figure(figsize=(16,6))
_,bins,_=plt.hist(df.age,bins=20)
print(bins)
plt.xticks(bins)
plt.show()"""
#############################################
"""a = [10,20,15,5]
plt.pie(a,explode = [0,0,1,0.1],labels=list('abcd'))
plt.show()"""
#############################################
#Plot graph above graph
"""dff = pd.DataFrame({2001:[10,20,30,23,40],2009:[40,20,34,15,39],2019:[40,20,10,5,10]})
print(dff)

plt.bar(dff[2001].index,dff[2001].values,label ='2001')
plt.bar(dff[2009].index,dff[2009].values,bottom = dff[2001].values,label ='2009')
plt.bar(dff[2009].index,dff[2009].values,bottom = dff[2001].values+dff[2009].values,label ='2019')
plt.legend()
plt.show()"""
############################################
#use python way to print graph above graph
"""dff =pd.DataFrame({2001:[10,20,30,40,50],2009:[10,20,30,50,60],2019:[40,30,20,10,70]})
print(dff)
dff.plot(kind ='bar', stacked = True)
plt.show()"""
############################################
"""dff =pd.DataFrame({2001:[10,20,30,40,50],2009:[10,20,30,50,60],2019:[40,30,20,10,70]})
print(dff.plot())
plt.show()"""
############################################
"""dff =pd.DataFrame({2001:[10,20,30,40,50],2009:[10,20,30,50,60],2019:[40,30,20,10,70]})
plt.fill_between(dff[2001].index,dff[2001].values)
plt.show()"""
############################################
"""dff = pd.DataFrame({2001:[10,20,30,40,50],2009:[10,20,30,50,60],2019:[40,30,20,10,70]})
plt.fill_between(dff[2001].index,dff[2001].values)
plt.fill_between(dff[2001].index,dff[2001].values,dff[2001].values + dff[2009].values + dff[2019].values)
plt.show()"""
############################################
#python way
"""dff = pd.DataFrame({2001:[10,20,30,40,50],2009:[10,20,30,50,60],2019:[40,30,20,10,70]})
dff.plot(kind ='area')
plt.show()"""
###########################################
"""dff = pd.DataFrame({2001:[10,20,30,40,50],2009:[10,20,30,50,60],2019:[40,30,20,10,70]})
plt.boxplot(dff[2001])
plt.show()
plt.boxplot(dff[2009])
plt.show()"""
##########################################
"""dff = pd.DataFrame({2001:[10,20,30,23,40],2009:[40,20,10,5,5],2019:[4,25,30,31,40]})
dff.loc[:,(2001,2019)].plot(kind = 'bar')
plt.title('ABCD')
plt.show()"""
##########################################
"""plt.figure(figsize = (15,5))
data = df[df.gender =='male']
plt.scatter(range(len(data.age))  ,data.age,alpha=0.4, c ='r')
data = df[df.gender =='female']
plt.scatter(range(len(data.age))  ,data.age,alpha=0.4, c ='b')
plt.show()"""
#########################################
x = pd.Series(range(10))
y1 = x *2
y2 = x **3
print(y1,y2)
plt.plot(x,y1)
plt.twinx()
plt.plot(x,y2,c ='g')
plt.show()




