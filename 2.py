
import formation

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker
import pylab

formation.new_update()
s = formation.data
x = [1, 2, 3, 4, 5,6]
z = np.random.random(5)
z1 = formation.numb
print(z1)
z2 = [12, 14, 21, 13, 17]






#pylab.rc('font',**{'family':'verdana'})
figure = pylab.figure()
axes = figure.add_subplot (1, 1, 1)
formatter = matplotlib.ticker.FixedFormatter(s)
axes.xaxis.set_major_formatter(formatter)
#pylab.bar(x, z1, align='center', width=1)
#pylab.frange(10, 10)
pylab.errorbar(x, z1, xerr=0, yerr=0)
pylab.ylim(0, formation.mxn[0]+2)   #косяк косяков!!!!
pylab.title("9giap")
plt.xlabel("dжа")
plt.ylabel("number of persons")
pylab.grid(True)
#pylab.plot(2, 2, 'bs')

'''
# bar()
fig = plt.figure()
plt.bar(x, z1)
plt.title('Simple bar chart')
plt.grid(True)   # линии вспомогательной сетки



# pie()
fig = plt.figure()
plt.pie(z1, labels=s)
plt.title('Simple pie chart')



# hist()
fig = plt.figure()
print(z)
plt.hist(0.48396569)
plt.title('Simple histogramm')
plt.grid(True)
print(fig.texts)
'''

# смотри преамбулу
plt.savefig('example 142a.png', fmt='png')
#save(name='pic_2_2', fmt='pdf')
#save(name='pic_2_2', fmt='png')

plt.show()