import random
import User

"""a = []
for i in range(1001):
    a.append(random.randint(10,40))
for j in a:
    if j%2==0:
        print(f' {j} четный элемент')
    else:
        print(f' {j} не четный элемент')"""

b = (1, 2, 3)
c = {'login': 'user1', 'password': 'pasword'}
import time
s = 10000
u = User.User()
users_new = u.parsefile('users.txt')
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
    print(users_new)
    print(users_new)


"""
class User:
    def __init__(self, name, age, password):
       self.name = name
       self.age = age
       self.__password = password
    def say(self, message):
        print(message)
    def display_info(self):
        return (f'Name: {self.name} Age: {self.age}')

    @property
    def password(self):
        return self.__password

class Employee(User):
    def work(self):
        print(f'{self.name} works')


user1 = Employee('User 1', 22, 'asfasfqr')
print(user1.display_info())
print(user1.password)"""