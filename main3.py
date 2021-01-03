# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2,numpy
from PIL import ImageGrab
import pyautogui
import keyboard
import msvcrt
from PIL import ImageGrab
import time

def wait():
    while True:
        if keyboard.is_pressed('enter'):
            return pyautogui.position()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [0]
    x0,y0 = wait()
    time.sleep(0.1)
    #print(x0,y0)
    x1, y1 = wait()
    #print(x1,y1)
    screen = ImageGrab.grab()
    for i in range(3000):
        tmp = ImageGrab.grab(bbox=(x1 - 15,y1 - 15,x1 + 15, y1 + 15))
        mean = numpy.mean(tmp)
        diff = array[-1] - mean
        array.append(mean)
        print(diff)
        if diff >=2:
            pyautogui.click()
            pyautogui.mouseDown()
            time.sleep(2)
            break

    screen.save('screen.png')
    tmp.save('template.png')





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
