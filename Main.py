import pyautogui, time, keyboard, os
print  ("""
            O O
           dO Ob
          dOO OOO
         dOOO OOOb
        dOOOO OOOOb
        OOOOO OOOOO
        OOOOO OOOOO
        OOOOO OOOOO
        YOOOO OOOOO
         YOOO OOOP
    oOOOOOOOOOOOOb
  oOOOOOOOOOOOOOOOb
 oOOOb dOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOO
OOOOOOOOOOOOOOOOOOP
OOOOOOOOOOOOOOOOOP
 YOOOOOOOOOOOOOOP
   YOOOOOOOOOOOP
  %%%%%%%%%%%%%%
 %%%%%%OOOjgsOOO

Created by VMaz
inst: vmaz_original
""")
run = True
#Остановка спама
def stop():
    global run
    run = False
# Начало спама
def spam(text):
    global run
    while run == True:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        keyboard.add_hotkey("Ctrl + 9", stop)
    main()

# Запуск кода
def main():
    global run
    run = True
    txt = input('Input msg: ')
    print(txt)
    print("To start press 'Ctrl + 0'\nTo stop press 'Ctrl + 9'")
    keyboard.wait("Ctrl + 0")
    spam(txt)

main()
