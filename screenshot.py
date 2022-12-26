# import speech_recognition as s_r

import pyautogui
import time


def screenshot():
    print("screenshot worked")
    while True:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'images\ss.png')
        time.sleep(10)