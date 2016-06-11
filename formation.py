import sqlite3

con = sqlite3.connect("MaimBD.db")
cur = con.cursor()

data = []   #дата
numb = []   #кол-во людей в соответствии с датой
mxn = [0]   #косяк косяков!!!!(максимум онлайн)


all_name = []         #список всех имен
stat_name = [[], []]  #статистика по именам [i][0] - дата [i][1..n] - время

def new_update():
    name = []
    cur.execute("select name, data from glassary ORDER BY data DESC")
    #data.append(0)

    for n, d in cur.fetchmany(1):
        data.append(d[5:10])
        name.append(n)
        # print(d[0:10])
        numb.append(1)
    '''
    for n, d in cur.fetchmany(1):
        if d[0:10] == data[i]:  # если дата все еще та же
            if name.count(n) == 0:
                name.append(n)
                numb[i] += 1
        else:  # а если дата другая
            data.append(d[0:10])
            name.clear()
            name.append(n)
            numb.append(1)
            ex = 1
'''

    for i in range(5):
        ex = 0
        while ex == 0:
            for n, d in cur.fetchmany(1):
                if d[5:10] == data[i]:  # если дата все еще та же
                    if name.count(n) == 0:
                        name.append(n)
                        numb[i] += 1
                else:  # а если дата другая
                    data.append(d[5:10])
                    name.clear()
                    name.append(n)
                    numb.append(1)
                    ex = 1
    mx = 0

    for n in numb:
        if n > mx:
            mx = n
    mxn[0] = mx   #косяк косяков!!!!


def count_mane():
    cur.execute("select name from glassary ORDER BY name")
    all_name.append(cur.fetchmany(1))
    for n in cur.fetchall():
        ex = True
        for al in all_name:
            if n == al:
                ex = False
        if ex:
            all_name.append(n)



#def name_new_update(user):




def prin():
    cur.execute("select name, data from glassary ORDER BY data DESC")
    for n, d in cur.fetchall():
        print(n, d)

count_mane()
print(all_name)
#new_update()
prin()
print(data)


# print(cur.fetchmany(1))
'''


    for n, d in cur.fetchall():
        print(d)
        '''
