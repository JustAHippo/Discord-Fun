import keyboard
import os
import time
selected = 1
def show_menu():
    global selected
    print("\n" * 30)
    print(f"""
██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ███████╗██╗░░░██╗███╗░░██╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝██║░░░██║████╗░██║
██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  █████╗░░██║░░░██║██╔██╗██║
██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ██╔══╝░░██║░░░██║██║╚████║
██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ██║░░░░░╚██████╔╝██║░╚███║
╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝""")
    print("I, hippo, am not responsible for getting yo ass banned from Discord. This is a selfbotting tool. Use responsibly")
    print("Choose an option:")
    for i in range(1, 3):
        print("{1} {0} {0} {2}".format('', ">" if selected == i else " ", "Spam Bot" if i == 1 else "Typing Bot", "<" if selected == i else " "))

def up():
    global selected
    if selected == 1:
        return
    selected -= 1
    os.system('cls')
    show_menu()

def down():
    global selected
    if selected == 4:
        return
    selected += 1
    os.system('cls')
    show_menu()
def select():
    if selected == 1:
        print('Loading script...')
        time.sleep(1)
        os.system('python scripts/spambot.py')
        exit()
    if selected == 2:
        print('Loading script...')
        time.sleep(1)
        os.system('python scripts/typing.py')
        exit()
show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('enter', select)
keyboard.wait()
