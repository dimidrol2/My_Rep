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


def ret_side(x, y):

    x1 = 1920 / 2
    x2 = 1080 / 2

    side = 'template_lefthg.png'
    if x1 > x:
        side = 'template_lefthg.png'
    elif x1 < x:
        side = 'template_righthg.png'
    return side






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


def find_hook(tmp):
    #print('Ищу крючок!')
    array = [0]

    image = cv2.imread('screen.png')
    template = cv2.imread(tmp)
    w, h, z = template.shape[::1]
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rgb_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    res = cv2.matchTemplate(rgb_image, rgb_template, cv2.TM_CCOEFF_NORMED)

    loc = numpy.where(res >= 0.7)
    x = y = 1
    for pt in zip(*loc[::-1]):
        x = int(pt[0])
        y = int(pt[1])
        #print('Нашел')
        break

    if x == y == 1:
        bool_repeat = True
        #print('Не нашел')
        return


    for i in range(1000):
        clean_screen = ImageGrab.grab(bbox=(x, y, x + h, y + w))
        clean_screen.save('clean_screen.png')

        mean = numpy.mean(clean_screen)
        diff = array[-1] - mean



        array.append(mean)
        time.sleep(0.1)
        if diff >= 4:
            pyautogui.click()


            break


def catch():
    #print('начинаю ловить')
    x, y = (840,540) , (940,565)
    clean_screen = ImageGrab.grab(bbox = (*x, *y))
    clean_screen.save("Catch.png")

    array = [numpy.mean(clean_screen)]
    pyautogui.moveTo(1000, 555)
    for i in range(100):
        time.sleep(0.05)
        dif_screen = ImageGrab.grab(bbox=(*x, *y))
        mean = numpy.mean(dif_screen)
        diff = abs(array[0] - mean)



        if diff >=3:
            pyautogui.mouseDown(button= 'left')
        else:
            pyautogui.mouseUp(button= 'left')
            #print('отпускаю леску')
        if diff >= 20:
            pyautogui.mouseUp(button='left')
            break

def throw_a_hook():

    pyautogui.mouseDown(button='left')
    time.sleep(0.25)
    pyautogui.mouseUp(button='left')


def move_to_begin(x, y):
    pyautogui.moveTo(x, y)


def wait():
    while True:
        if keyboard.is_pressed('Enter'):
            break


if __name__ == '__main__':

    wait()
    x, y = pyautogui.position()
    tmp = ret_side(x, y)



    while True:
        bool_repeat = False

        throw_a_hook()

        time.sleep(1)
        make_screen()

        find_hook(tmp)
        if bool_repeat:
            continue

        time.sleep(0.2)
        catch()

        time.sleep(2)
        move_to_begin(x, y)
        if keyboard.is_pressed(Hotkey):
            break

        time.sleep(0.2)






