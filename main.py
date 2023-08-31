from os import system, environ
from userClass import User
from time import sleep
from monetaryMenu import Menu

menu = Menu()

while True:
    try:
        system("cls")
    except Exception:
        print(e)
    print("Welcome! For login, please insert your data!")
    sleep(2.5)
    username = str(input("User:\n=> "))
    age = int(input("Age:\n=> "))
    password = str(input("Insert your password:\n=> "))
    break

user = User(name=username, age=age, password=password)

system("cls")

user.hello_world()

menu.run_menu()