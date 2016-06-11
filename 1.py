import matplotlib

import matplotlib.pyplot as plt

#%matplotlib inline

import os
import matplotlib.pyplot as plt

def save(name, fmt):
    pwd = os.getcwd()
    #os.chdir('./pictures/%s' % fmt)
    plt.savefig('%s.%s' % (name, fmt), fmt)
    os.chdir(pwd)
    #plt.close()

print("+")
fig = plt.figure()   # Создание объекта Figure
#print(fig.axes)   # Список текущих областей рисования пуст
#print(type(fig))   # тип объекта Figure
plt.scatter(1.0, 1.0)
plt.scatter(1.0, 2.0)# scatter - метод для нанесения маркера в точке (1.0, 1.0)
print(fig.lines)
# После нанесения графического элемента в виде маркера
# список текущих областей состоит из одной области
#print(fig.axes)

# смотри преамбулу
plt.savefig('example 142a.png', fmt='png')
#save('pic_1_4_1', 'png')
#save(name='pic_1_4_1', fmt='png')

plt.show()


