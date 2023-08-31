from time import sleep

class Menu:
    def __init__(self):
        pass
    def run_menu(self):
        menu_text = """
        1 - Deposit
        2 - Payment
        0 - EXIT"""
        formatted_menu = menu_text.ljust(30, " ")
        print(formatted_menu)
        option = int(input("=> "))
        options = [0, 1, 2]

        while option not in options:
            print(formatted_menu)
            option = int(input("=> "))
        
        exit_resposts = ["y", "n"]

        match option:
            case 0:
                exit_option = str(input("You chose 'EXIT' option. Are you sure? y/n?\n=> "))

                while exit_option.lower() not in exit_resposts:
                    exit_option = str(input("You chose 'EXIT' option. Are you sure? y/n?\n=> "))
                if exit_option.lower() == "y":
                    print("You chose 'y'. Exiting..")
                    sleep(2.5)
                    exit()
                else:
                    pass
                
            case 1:
                print("You chose 'Deposit' option.")
            case 2:
                print("You chose 'Payment' option.")
            case _:
                pass