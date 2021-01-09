# This is a sample Python script.
import pyautogui
import time
import numpy
from PIL import ImageGrab
import keyboard
import cv2
from PyQt5 import uic, QtWidgets
import sys
from PyQt5 import QtCore
import datetime

key_array = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
             ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
             '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
             'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
             'browserback', 'browserfavorites', 'browserforward', 'browserhome',
             'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
             'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
             'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
             'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
             'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
             'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
             'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
             'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
             'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
             'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
             'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
             'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
             'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
             'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
             'command', 'option', 'optionleft', 'optionright']
# Press Shift+F10 to execute it or replace it with your code.ы
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
hook_rad = 13
time_eat = 30
time_bait = 10
eat, bait = False, False
wait_eat , wait_bait = 0, 0
key_eating, key_bait = 'f2', 'f1'

size_screen = pyautogui.size()
count = 1
i_click = 5
#stop = False
Form, _ = uic.loadUiType('interface.ui')
# x 700 , y 450 # 200x25
if size_screen == (1600, 900):
    x0, y0 = (700, 450), (900, 470)

elif size_screen == (1920, 1080):
    x0, y0 = (840, 539), (1080, 569)

else:
    x0, y0 = (840, 539), (1080, 569)


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time() - t))
        return res

    return tmp


def eating(time_e ,eat,  first_time):
    if eat and (time_e - first_time)>30:
        pyautogui.press(key_eating)
        time.sleep(2)
        return True
    else:
        return False


def baiting(time_b, bait, first_time):
    if bait and (time_b - first_time) > 30:
        pyautogui.press(key_eating)
        time.sleep(2)
        return True
    else:
        return False


def cur_min():
    x = datetime.datetime.now()

    return x.hour * 60 + x.minute + x.year*365*24 + x.day * 24 * 60


def play():

    bool_repeat = False
    eat_time = cur_min() - wait_eat
    bait_time = cur_min() - wait_bait
    coord0 = wait()
    coord1 = wait()
    wait()

    time.sleep(0.1)
    if bool_repeat:
        bool_repeat = False

    while True:
        current_time = cur_min()


        bool_repeat = False
        print('Закидывает крючок')
        throw_a_hook(*coord0)
        time.sleep(1.5)
        print('Ждет поклева')
        click_on_hook(*coord1)
        if bool_repeat:
            continue

        time.sleep(0.1)

        catch()

        
        time.sleep(3)


def catch():
    time.sleep(0.1)
    hook = cv2.imread('hook.png', 0)
    hook_g = cv2.cvtColor(hook, cv2.COLOR_BAYER_BG2GRAY)
    count_fail = 0

    for i in range(1000):



        #
        hook_screen = ImageGrab.grab(bbox=(*x0, *y0))
        hook_screen.save('hook_screen.png')
        hook_sc = cv2.imread('hook_screen.png', 0)

        hook_sg = cv2.cvtColor(hook_sc, cv2.COLOR_BAYER_BG2GRAY)

        res = cv2.matchTemplate(hook_sg, hook_g, cv2.TM_CCOEFF_NORMED)
        loc = numpy.where(res >= 0.70)
        time.sleep(0.05)

        try:
            a = loc[-1][-1]
            a -= 1
            if a < 170:
                pyautogui.mouseDown(button='left')
            else:
                pyautogui.mouseUp(button='left')
            count_fail = 0
        except:
            pyautogui.mouseUp(button='left')
            count_fail += 1
            if count_fail >= 5:
                print('Не поймал')
                return

        #


def throw_a_hook(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown(button='left')
    time.sleep(1)
    pyautogui.mouseUp(button='left')


def wait():
    keyboard.wait('l')
    #print('нажал на л')
    return pyautogui.position()


def click_on_hook(x, y):
    zero_count = 0

    array = [numpy.mean(ImageGrab.grab(bbox=(x - hook_rad, y - hook_rad, x + hook_rad, y + hook_rad)))]

    for i in range(1000):

        time.sleep(0.05)
        clean_screen = ImageGrab.grab(bbox=(x - hook_rad, y - hook_rad, x + hook_rad, y + hook_rad))

        mean = numpy.mean(clean_screen)
        diff = abs(array[-1] - mean)
        # print(round(diff, 3))

        array.append(mean)

        if diff >= i_click:
            # print('нажал на крючок', diff)
            pyautogui.click()
            break

        if diff < 0.1:  # Проверка на наличие крючка в воде
            zero_count += 1
        else:
            zero_count = 0
        if zero_count >= 10:
            bool_repeat = True
            break

#######################################################################################################################


class Creator(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.isWork = False

    def run(self):
            while self.isWork:
                play()


class Ui(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)

        self.thread = QtCore.QThread()
        self.creator = Creator()


        self.thread.finished.connect(self.StopPressed)

        self.start.clicked.connect(self.StartPressed)

        self.stop.clicked.connect(self.StopPressed)

        self.settings.clicked.connect(self.ConfirmSettings)


    def StartPressed(self):
        try:

            self.stop.setEnabled(True)
            self.start.setEnabled(False)
            self.creator.moveToThread(self.thread)
            self.thread.started.connect(self.creator.run)
            self.creator.isWork = True
            self.thread.start()
            print(self.thread.isFinished())
        except:
            print('ошибка старта')


    def StopPressed(self):
        try:
            self.start.setEnabled(True)
            self.stop.setEnabled(False)
            self.creator.isWork = False
            self.thread.started.disconnect(self.creator.run)


            print(self.thread.isFinished())

        except:
            print('error stop')




    def ConfirmSettings(self):
        global hook_rad, eating, bait, key_bait, key_eating
        self.lineEdit.setText('')
        if self.key_bait.toPlainText().lower() in key_array:
            key_bait = self.key_bait.toPlainText().lower()
        else:
            self.lineEdit.setText(f'{self.key_bait.toPlainText()} не может быть клавишей; {self.lineEdit.text()}')

        if self.key_eat.toPlainText().lower() in key_array:
            key_eating = self.key_eat.toPlainText().lower()
        else:
            self.lineEdit.setText(f'{self.key_eat.toPlainText()} не может быть клавишей; {self.lineEdit.text()}')

        #print(key_bait, key_eating)

        hook_rad = self.spinBox.value()
        eating = self.eat.isChecked()
        bait = self.bait.isChecked()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = Ui()
    w.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    w.show()



    sys.exit(app.exec_())
