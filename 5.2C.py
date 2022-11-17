from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##HARDWARE
red = LED(23)
green = LED(24)
blue = LED(25)

##GUI Defintions
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = "Helvetica", size = 24 , weight = "bold")

def redToggle():
    if red.is_lit:
        red.off()
        redButton["text"] = "Turn RED on"
    else:
        red.on()
        redButton["text"] = "Turn RED off"
        green.off()
        greenButton["text"] = "Turn GREEN on"
        blue.off()
        blueButton["text"] = "Turn BLUE on"

def greenToggle():
    if green.is_lit:
        green.off()
        greenButton["text"] = "Turn GREEN on"
    else:
        green.on()
        greenButton["text"] = "Turn GREEN off"
        blue.off()
        blueButton["text"] = "Turn BLUE on"
        red.off()
        redButton["text"] = "Turn RED on"
        
        
def blueToggle():
    if blue.is_lit:
        blue.off()
        blueButton["text"] = "Turn GREEN on"
    else:
        blue.on()
        blueButton["text"] = "Turn BLUE off"
        green.off()
        greenButton["text"] = "Turn GREEN on"
        red.off()
        redButton["text"] = "Turn RED on"
        
def close():
    RPi.GPIO.cleanup
    win.destroy()
    
##WIDGETS

redButton = Button(win, text = 'Turn RED on', font = myFont, command = redToggle, bg = 'bisque2', height = 1, width = 24)
redButton.grid(row=0, column = 1)

greenButton = Button(win, text = 'Turn GREEN on', font = myFont, command = greenToggle, bg = 'bisque2', height = 1, width = 24)
greenButton.grid(row=1, column = 1)

blueButton = Button(win, text = 'Turn BLUE on', font = myFont, command = blueToggle, bg = 'bisque2', height = 1, width = 24)
blueButton.grid(row=2, column = 1)

exitButton = Button(win, text = 'EXIT', font = myFont, command = close, bg = 'red', height = 2, width = 24)
exitButton.grid(row=3, column = 1)

win.mainloop()


            
        
        
                           
