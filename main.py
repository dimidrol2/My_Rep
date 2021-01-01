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


def make_screen():

    x, y = pyautogui.position()
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
    #print(*loc)
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

    right_zone = cv2.imread('right_zone.png')
    left_zone = cv2.imread('left_zone.png')
    gray_right_zone = cv2.cvtColor(right_zone, cv2.COLOR_BGR2GRAY)
    gray_left_zone = cv2.cvtColor(left_zone, cv2.COLOR_BGR2GRAY)
    image = cv2.imread('screen.png')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    res_r = cv2.matchTemplate(gray_image, gray_right_zone, cv2.TM_CCOEFF_NORMED)
    res_l = cv2.matchTemplate(gray_image, gray_left_zone, cv2.TM_CCOEFF_NORMED)
    loc_r = numpy.where(res_r >= 0.8)
    loc_l = numpy.where(res_l >= 0.8)
    y1, x1, z1 = right_zone.shape
    left_point, right_point = 0, 0
    for pt in zip(*loc_r[::-1]):
        x = int(pt[0])
        y = int(pt[1])

        right_point = (x - 20,y + y1//2)
        cv2.rectangle(image, right_point, right_point, (0, 255, 0), 1)

    for pt in zip(*loc_l[::-1]):
        x = int(pt[0])
        y = int(pt[1])

        left_point = (x + x1 + 10,y + y1 // 2)
        cv2.rectangle(image, left_point, left_point, (0, 255, 255), 1)

    cv2.imwrite("C:/Users/Dmitri/PycharmProjects/Test2/test.png",image)
    return left_point, right_point


def catch(x,y):
    x1, y1 = x
    x2, y2 = y
    f = True

    for i in range(100):
        time.sleep(0.1)
        pyautogui.moveTo(x2, y2)
        pyautogui.mouseDown(button='left')
        cs_left = ImageGrab.grab(bbox = (x1,y1,x1+1,y1+1))
        cs_right = ImageGrab.grab(bbox=(x2,y2,x2+1,y2+1))
        mean = numpy.mean(cs_left)
        if f:
            array=[mean]
            f = False

        diff = array[0] - mean
        print(mean)







        #print(numpy.mean(cs_left))





if __name__ == '__main__':

    time.sleep(6)


    make_screen()
    find_hook(tmp)
    time.sleep(0.2)
    x, y = play_with_fish()
    #print(x,y)
    time.sleep(0.2)
    catch(x, y)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
