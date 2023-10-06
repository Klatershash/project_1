"""import random
a = []
for i in range(1001):
    a.append(random.randint(10,40))
for j in a:
    if j%2==0:
        print(f' {j} четный элемент')
    else:
        print(f' {j} не четный элемент')

b = (1, 2, 3)
c = {'login': 'user1', 'password': 'pasword'}"""
import time
s = 10000
file = open('users.txt', 'r')
d = file.read()
users = d.split(';')
users_new = []
for i in users:
    b = i.split(',')
    f = {}
    for j in b:
        c = j.split(':')
        if c[0] == 'pin' or c[0] == 'summa':
            f[c[0]] = int(c[1])
        else:
            f[c[0]] = c[1]
    users_new.append(f)
file.close()
print(users_new)
while True:
    print('You are Welcome')
    time.sleep(1)
    login = input('логин пользователя')
    time.sleep(1)
    for i in users_new:
        if login == i['login']:
            pin = int(input('пароль'))
            if pin == i['pin']:
                print(f'{i["summa"]} текущая сумма')
                summa = int(input('введите сумму'))
                if summa<=i['summa'] and i['summa']<=10000:
                    print('возьмите деньги')
                    time.sleep(2)
                    i['summa'] -= summa
                    print(i['summa'])
                else:
                    print('Error summa')
            else:
                print('Error pin')
        else:
            print('Error login')



