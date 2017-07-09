import os
import subprocess

def takeScreenshot():
    directory = '/sdcard/Download/screenshot.png'
    subprocess.call(['adb', 'shell', 'screencap', '-p', directory])
    subprocess.call(['adb', 'pull', directory])

def takeVideo():
    directory = '/sdcard/Download/screenrecord.mp4'

    try:
        print('Starting screen record, press Ctrl+C to end screen record')
        adbProcess = subprocess.call(['adb', 'shell', 'screenrecord',  directory ])

    except KeyboardInterrupt: 
     adbProcess =  subprocess.call(['adb', 'pull', directory])

    

userInput = input('Welcome to scrrenGrabber.\n1. Take Screenshot of Device\n2. Take screen record of device')

if userInput == '1':
    takeScreenshot()

elif userInput == '2':
    takeVideo()

else:
    exit()        
