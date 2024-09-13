import pyautogui as botMouse
import webbrowser
import random
import time
import keyboard

webbrowser.open('https://www.datachar.com')
while True:
    
    print(botMouse.position())
    x = random.randint(400,900)
    y = random.randint(100,700)

    #botMouse.moveTo(x, y,0.5)
    time.sleep(2)