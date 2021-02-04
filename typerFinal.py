from pynput.keyboard import Key, Controller
import time
import datetime

#keyboard added as an input function
keyboard = Controller()

#time
now = datetime.datetime.now()
timeitisnow = now.strftime('%I:%M %p')

#message that will be spammed
text = 'guys guess what time it is! it\'s'

#time until typer starts (in seconds) 
time.sleep(3)

#time between messages
timeBetweenMessages = 3


while True:
    #writing the text
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(.02)

    keyboard.press(Key.space)
    keyboard.release(Key.space)

    #writing the time
    for char in timeitisnow:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(.02)

    keyboard.press('!')
    keyboard.release('!')

    keyboard.press(Key.enter)
    
    time.sleep(timeBetweenMessages)
    
    #guys guess what time it is! it's 07:28:PM!
