# This is a sample Python script.
import pyautogui
import time
import cv2
import numpy
import keyboard

from PIL import ImageGrab
import keyboard
# Press Shift+F10 to execute it or replace it with your code.ы
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

tmp = "template.png"
Hotkey = 'enter'
bool_repeat = False
size_screen = pyautogui.size()
pyautogui.FAILSAFE = True
#x 700 , y 450 # 200x25


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp


def make_screen():
    base_screen = ImageGrab.grab()
    base_screen.save("screen.png")


def catch():
    #print('начал играть')
    if size_screen==(1600,900):
        x0, y0 = (700, 450), (785, 470)
    elif size_screen == (1920,1080):
        x0, y0 = (840, 540), (940, 565)

    clean_screen = ImageGrab.grab(bbox = (*x0, *y0))
    clean_screen.save("Catch.png")

    array = [numpy.mean(clean_screen)]

    for i in range(1000):
        time.sleep(0.05)
        dif_screen = ImageGrab.grab(bbox=(*x0, *y0))
        mean = numpy.mean(dif_screen)
        diff = abs(array[0] - mean)

        if diff >= 2:
            pyautogui.mouseDown(button= 'left')
        else:
            pyautogui.mouseUp(button= 'left')

        if diff >= 20:
            pyautogui.mouseUp(button='left')
            #print('закончил играть diff=', diff)
            break


def throw_a_hook(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.mouseUp(button='left')
    #print('закинул удочку на ', x, y)


def wait():
    keyboard.wait('l')
    return pyautogui.position()


def click_on_hook(x, y):
    r = 15
    array = [0]
    for i in range(1000):

        clean_screen = ImageGrab.grab(bbox=(x-r, y - r, x + r, y + r))
        #clean_screen.save('clean_screen.png')

        mean = numpy.mean(clean_screen)
        diff = array[-1] - mean
        array.append(mean)
        time.sleep(0.1)

        if diff >= 4:
            #print('нажал на крючок', diff)
            pyautogui.click()
            break


if __name__ == '__main__':
    count = 1

    coord0 = wait()
    coord1 = wait()
    wait()
    time.sleep(0.1)

    while True:
        
        print(count)
        bool_repeat = False
        throw_a_hook(*coord0)
        time.sleep(1.5)
        click_on_hook(*coord1)
        time.sleep(0.2)
        catch()
        time.sleep(2)
        count+=1
