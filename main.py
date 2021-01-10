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


size_screen = pyautogui.size()


Form, _ = uic.loadUiType('interface.ui')
# x 700 , y 450 # 200x25
if size_screen == (1600, 900):
    x0, y0 = (700, 450), (900, 470)

elif size_screen == (1920, 1080):
    x0, y0 = (840, 539), (1080, 569)

else:
    x0, y0 = (840, 539), (1080, 569)


class Game(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.stop = False
        self.hook_rad = 13
        self.time_eat = 30
        self.time_bait = 10
        self.eat, self.bait = False, False
        self.wait_eat, self.wait_bait = 0, 0
        self.key_eating, self.key_bait = 'f2', 'f1'
        self.i_click = 5


    def catch(self):
        time.sleep(0.1)
        hook = cv2.imread('hook.png', 0)
        hook_g = cv2.cvtColor(hook, cv2.COLOR_BAYER_BG2GRAY)
        count_fail = 0

        for i in range(1000):
            if self.stop:
                break

            #
            hook_screen = ImageGrab.grab(bbox=(*x0, *y0))
            hook_screen.save('hook_screen.png')
            hook_sc = cv2.imread('hook_screen.png', 0)

            hook_sg = cv2.cvtColor(hook_sc, cv2.COLOR_BAYER_BG2GRAY)

            res = cv2.matchTemplate(hook_sg, hook_g, cv2.TM_CCOEFF_NORMED)
            loc = numpy.where(res >= 0.75)


            try:
                a = loc[-1][-1]
                a -= 1
                if a < 170:
                    print(a)
                    pyautogui.mouseDown(button='left')
                else:
                    pyautogui.mouseUp(button='left')
                count_fail = 0
            except:
                pyautogui.mouseUp(button='left')
                count_fail += 1
                if count_fail >= 5:

                    return

            #

    def eating(self, time_e,  first_time):
        if self.eat and (time_e - first_time) > 30:
            pyautogui.press(self.key_eating)
            time.sleep(2)
            return True
        else:
            return False

    def baiting(self, time_b,  first_time):
        if self.bait and (time_b - first_time) > 30:
            pyautogui.press(self.key_eating)
            time.sleep(2)
            return True
        else:
            return False


    def throw_a_hook(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown(button='left')
        time.sleep(1)
        pyautogui.mouseUp(button='left')

    def wait(self):
        keyboard.wait('l')
        # print('нажал на л')
        return pyautogui.position()

    def cur_min(self):
        x = datetime.datetime.now()

        return x.hour * 60 + x.minute + x.year * 365 * 24 + x.day * 24 * 60

    def click_on_hook(self, x, y):
        zero_count = 0
        i_click = 5

        array = [numpy.mean(ImageGrab.grab(bbox=(x - self.hook_rad, y - self.hook_rad, x + self.hook_rad, y + self.hook_rad)))]

        for i in range(1000):
            if self.stop:
                print('Вышел')
                break

            time.sleep(0.05)
            clean_screen = ImageGrab.grab(bbox=(x - self.hook_rad, y - self.hook_rad, x + self.hook_rad, y + self.hook_rad))

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



    def run(self):
        #print('Плей пошел')
        bool_repeat = False
        eat_time = self.cur_min() - self.wait_eat
        bait_time = self.cur_min() - self.wait_bait
        coord0 = self.wait()
        coord1 = self.wait()
        self.wait()
        #print('Прожал L')
        time.sleep(0.1)
        if bool_repeat:
            bool_repeat = False

        while True:
            if self.stop:
                break
            current_time = self.cur_min()

            bool_repeat = False
            #print('Закидывает крючок')
            self.throw_a_hook(*coord0)
            if self.stop:
                break
            time.sleep(1.5)
            #print('Ждет поклева')
            self.click_on_hook(*coord1)
            if self.stop:
                break
            if bool_repeat:
                continue

            time.sleep(0.1)

            self.catch()
            if self.stop:
                break

            time.sleep(3)


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time() - t))
        return res

    return tmp



#######################################################################################################################



class Ui(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)

        self.thread = QtCore.QThread()
        self.game = Game()
        self.game.moveToThread(self.thread)
        self.thread.started.connect(self.game.run)

        self.start.clicked.connect(self.StartPressed)
        self.stop.clicked.connect(self.StopPressed)
        self.settings.clicked.connect(self.ConfirmSettings)


    def StartPressed(self):
        try:
            self.stop.setEnabled(True)
            self.start.setEnabled(False)
            self.game.moveToThread(self.thread)
            self.thread.started.connect(self.game.run)

            self.thread.start()
        except:
            print('ошибка старта')


    def StopPressed(self):
        try:
            self.start.setEnabled(True)
            self.stop.setEnabled(False)
            self.game.stop = True
            time.sleep(0.5)

        except:
            print('error stop')


    def ConfirmSettings(self):
        self.game.hook_rad = self.spinBox.value()
        self.game.eat = self.eat.isChecked()
        self.game.bait = self.bait.isChecked()
        self.game.wait_eat = self.wait_eat.value()
        self.game.wait_bait = self.wait_bait.value()
        self.lineEdit.setText('')
        if self.key_bait.toPlainText().lower() in key_array:
            self.game.key_bait = self.key_bait.toPlainText().lower()
        else:
            self.lineEdit.setText(f'{self.key_bait.toPlainText()} не может быть клавишей; {self.lineEdit.text()}')

        if self.key_eat.toPlainText().lower() in key_array:
            self.game.key_eating = self.key_eat.toPlainText().lower()
        else:
            self.lineEdit.setText(f'{self.key_eat.toPlainText()} не может быть клавишей; {self.lineEdit.text()}')

        if self.tophint.isChecked():
            self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        else:
            self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)


        self.show()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    w = Ui()
    w.show()



    sys.exit(app.exec_())
