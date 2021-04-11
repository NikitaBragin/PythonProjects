import keyboard
import time
import subprocess
import pandas as pd
import pyautogui
import psutil
from datetime import date, datetime
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from googleapiclient.discovery import build
import io
import os

def KClick(command):  # keyboard event
    keyboard.press_and_release(command)
    time.sleep(1)

path = 'F:\\FORIDLE\\'
recordings_path = str(path) + 'Recordings'
buttons_path = str(path) + 'buttons'
path_zoom = 'F:\\Zoom\\bin\\Zoom.exe'
path_ocam = 'F:\\oCam\\oCam.exe'
# gift = subprocess.Popen(str(path_zoom))
time.sleep(2)
KClick('Alt+h')  # turn on the chat
pyautogui.moveTo(pyautogui.size()[0]/2.59, pyautogui.size()[1] / 3.8)
time.sleep(1)
pyautogui.dragTo(pyautogui.size()[0]/1.01, pyautogui.size()[1] / 3.8, 0.5, button='left')



