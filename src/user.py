from db.db import DB
import os

class User:
    def __listUser(self):
        no = 1
        for user in DB('users')._get():
            print(f'{user[0]}) {user[1]} - {user[2]}')
            no += 1

    def __insert(self):
        name = input('Name: ')
        phone = input('Phone: ')

        DB('users')._insert({'name': name, 'phone': phone})

    def __update(self):
        id = input('ID: ')
        name = input('Name: ')
        phone = input('Phone: ')
        data = {}

        if name: data['name'] = name
        if name: data['phone'] = phone

        if len(data) > 0: DB('users')._where('id', id)._update(data)

    def __delete(self):
        id = input('ID: ')

        DB('users')._where('id', id)._delete()

    def createNewUser(self):
        os.system('clear')
        self.__listUser()
        print('\nCreate New User\n')
        self.__insert()
        os.system('clear')
        self.__listUser()
        print()

    def editUser(self):
        os.system('clear')
        self.__listUser()
        print('\nEdit User\n')
        self.__update()
        os.system('clear')
        self.__listUser()
        print()

    def deleteUser(self):
        os.system('clear')
        self.__listUser()
        print('\nDelete User\n')
        self.__delete()
        os.system('clear')
        self.__listUser()
        print()

    def searchUser(self):
        os.system('clear')
        self.__listUser()
        print('\nSearch User\n')
        keyword = input('Search: ')
        users = DB('users')._where('name', 'like', keyword)._get()
        no = 1

        os.system('clear')
        for user in users:
            print(f'{user[0]}) {user[1]} - {user[2]}')
            no += 1

        print(f'\nFound {len(users)} user\n')


User().createNewUser()
User().editUser()
User().deleteUser()
User().searchUser()

# Examples:
# DB('users')._where('phone', '0811111')._get()
# DB('users')._where('name', 'like', 'jack')._get()
# DB('users')._where('id', 1)._delete()
# DB('users')._where('id', 1)._update({'name': 'jill'})
# DB('users')._insert({'name': 'billy', 'phone': 0855555})