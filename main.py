# This is a sample Python script.
import pyautogui
import time
import cv2
import numpy

from PIL import ImageGrab
import keyboard
# Press Shift+F10 to execute it or replace it with your code.ы
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

tmp = "C:/Users/Dmitri/PycharmProjects/Test2/template.png"
Hotkey = 'enter'


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp


def make_screen(x, y):

    base_screen = ImageGrab.grab(bbox = (0, 0, x + 200, y + 200))
    base_screen.save("C:/Users/Dmitri/PycharmProjects/Test2/screen.png")




def find_hook(tmp):
    array = [0]

    # Use a breakpoint in the code line below to debug your script.
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

    for i in range(1000):
        clean_screen = ImageGrab.grab(bbox=(x, y, x + h, y + w))
        mean = numpy.mean(clean_screen)
        diff = array[-1] - mean

        array.append(mean)
        time.sleep(0.1)
        if diff >= 4:
            pyautogui.click()
            print('click')

            break


def play_with_fish():
    make_screen()
    array = [0]
    #x = 840,+240,840
    #y = 540,+30,510

    left_point, right_point = 0, 0

    #right_zone = cv2.imread('right_zone.png')
    left_zone = cv2.imread('left_zone.png')
   # gray_right_zone = cv2.cvtColor(right_zone, cv2.COLOR_BGR2GRAY)
    gray_left_zone = cv2.cvtColor(left_zone, cv2.COLOR_BGR2GRAY)
    image = cv2.imread('screen.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #res_r = cv2.matchTemplate(gray_image, gray_right_zone, cv2.TM_CCOEFF_NORMED)
    res_l = cv2.matchTemplate(gray_image, gray_left_zone, cv2.TM_CCOEFF_NORMED)
    y1, x1, z1 = left_zone.shape

   # loc_r = numpy.where(res_r >= 0.8)
    loc_l = numpy.where(res_l >= 0.8)

    '''for pt in zip(*loc_r[::-1]):
        x = int(pt[0])
        y = int(pt[1])

        right_point = (x - 20,y + y1//2)
        cv2.rectangle(image, right_point, right_point, (0, 255, 0), 10)
'''

    for pt in zip(*loc_l[::-1]):
        x = int(pt[0])
        y = int(pt[1])

        left_point = (x + x1 + 10,y + y1 // 2)
        cv2.rectangle(image, left_point, left_point, (0, 255, 255), 1)


    cv2.imwrite("C:/Users/Dmitri/PycharmProjects/Test2/test.png",image)
    return left_point


def catch():
    x, y = (840,540) , (940,565)
    clean_screen = ImageGrab.grab(bbox = (*x, *y))
    clean_screen.save("C:/Users/Dmitri/PycharmProjects/Test2/Catch.png")
    array = [numpy.mean(clean_screen)]
    pyautogui.moveTo(1000, 555)
    for i in range(100):
        time.sleep(0.1)
        dif_screen = ImageGrab.grab(bbox=(*x, *y))
        mean = numpy.mean(dif_screen)
        diff = abs(array[0] - mean)

        if diff >=3:
            pyautogui.mouseDown(button= 'left')
        else:
            pyautogui.mouseUp(button= 'left')
        if diff >= 10:
            pyautogui.mouseUp(button='left')
            break


def throw_a_hook():
    x, y = pyautogui.position()
    pyautogui.mouseDown(button='left')
    time.sleep(0.05)
    pyautogui.mouseUp(button='left')
    return x, y


def move_to_begin( x, y):
    pyautogui.moveTo(x, y)


if __name__ == '__main__':
    time.sleep(6)
    while True:
        x, y = throw_a_hook()
        time.sleep(1)
        make_screen(x, y)
        find_hook(tmp)
        time.sleep(0.2)
        catch()
        time.sleep(2)
        move_to_begin(x,y)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
