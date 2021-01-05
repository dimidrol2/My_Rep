# This is a sample Python script.
import pyautogui
import time
import cv2
import numpy


from PIL import ImageGrab
import keyboard
# Press Shift+F10 to execute it or replace it with your code.ы
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

bool_repeat = False
size_screen = pyautogui.size()
pyautogui.FAILSAFE = True
dif_mean = 0
#x 700 , y 450 # 200x25
if size_screen == (1600, 900):
    x0, y0 = (700, 450), (785, 470)
    x1, y1 = (850, 450), (900, 470)
elif size_screen == (1920, 1080):
    x0, y0 = (840, 540), (920, 565)
    x1, y1 = (1015, 540), (1080, 565)
else:
    x0, y0 = (840, 540), (920, 565)
    x1, y1 = (1015, 540), (1080, 565)


def no_catch(x, y):
    if abs(x - y) > 20:
        return False
    else:
        return True


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp





def catch():
    clean_screen = ImageGrab.grab(bbox=(*x0, *y0))
    right_screen = ImageGrab.grab(bbox=(*x1, *y1))


    clean_screen.save("left_side.png")
    right_screen.save("right_side.png")

    array_right = [numpy.mean(right_screen)]
    if no_catch(dif_mean, array_right[-1]):
        return
    #array = [numpy.mean(clean_screen)]

    for i in range(1000):
        time.sleep(0.05)
        #l_screen = ImageGrab.grab(bbox=(*x0, *y0))
        r_screen = ImageGrab.grab(bbox=(*x1, *y1))
        #mean_l = numpy.mean(l_screen)
        mean_r = numpy.mean(r_screen)
        #diff_l = abs(array[0] - mean_l)
        diff_r = abs(array_right[0] - mean_r)

        if diff_r <= 1:
            pyautogui.mouseDown(button='left')

        elif diff_r >= 20:
            pyautogui.mouseUp(button='left')
            break
        else:
            pyautogui.mouseUp(button='left')

        '''if diff_l >= 2:
            pyautogui.mouseDown(button= 'left')
        else:
            pyautogui.mouseUp(button= 'left')

        if diff_l >= 20:
            pyautogui.mouseUp(button='left')
            #print('закончил играть diff=', diff)
            break'''


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

        if diff >= 10:
            #print('нажал на крючок', diff)
            dif_mean = numpy.mean(ImageGrab.grab(bbox=(*x1, *y1)))
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
        time.sleep(0.1)
        catch()
        time.sleep(2)
        count+=1
