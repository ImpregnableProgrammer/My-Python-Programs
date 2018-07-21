""" A simple typing program

Press "H" to draw an H
Press "E" to draw an E
Press "L" to draw a L
Press "O" to draw an O
Press "W" to draw a W
Press "R" to draw a R
Press "D" to draw a D
Press "ENTER" to go to the next line
Press "SPACE" to make a space
Press "BACKSPACE" to go backwards an indent
Press the "Up" or "Down" arrow keys to move the turtle up or down the canvas
Press "TAB" to clear the canvas of your drawings
Press "ESC" to exit the program
Press any number from 1-0 on the key board (1 = 1, 0 = 10) to set the letter thickness
Press any key from F1-F10 to set a random color of the letter
(F1-F8 = colors, F9 = Custom Color, F10 = Original color)
Finally, press "k" to enter different letter dimensions (If you press cancel, previous values returned)

That is all you need to know! Enjoy! """


import os,shutil,subprocess, sys

##try:
##   print(os.environ["PATH"] )
##   her = sys.platform
##   if her == 'darwin':
##      os.environ["PATH"] += ":/usr/local/bin"
##   elif her == 'win32':
##      try:
##         os.environ["PATH"] += ";C:\\Program Files\\gs\\gs9.18\\bin"
##      except:
##         os.environ["PATH"] += ";C:\\Program Files (x86)\\gs\\gs9.18\\bin"
##   print(os.environ["PATH"] )
##   print("Ghostscript found and utilized")
##except:
##   print("You do not have GhostScript installed. Please install it for your platform to run this program.")
##   sys.exit(0)

#see if gs is avaible
her = sys.platform
if her == "win32":
    print("Windows is your Operating System")
    win_gs = ["gs","gswin32c","gswin64c"]
    if all( shutil.which(gs_version) is None for gs_version in win_gs ):
        paths = ["C:\\Program Files\\gs\\gs9.18\\bin","C:\\Program Files (x86)\\gs\\gs9.18\\bin"]
        for path in (x for x in paths if os.path.exists(x)) :
            os.environ["PATH"] += ";" + path
            break
        if any( shutil.which(gs_version) for gs_version in win_gs ):
            print("GhostScript 9.18 for Windows found and utilized")
        else:
            print("You do not have GhostScript 9.18 installed for Windows. Please install it.")
            sys.exit(0)
    else:
        print("GhostScript 9.18 for Windows found and utilized")
elif her == 'darwin':
    print("Macintosh is your Operating System")
    if shutil.which("gs") is None:
        os.environ["PATH"] += ":/usr/local/bin"
        if shutil.which("gs") is None:
            print("You do not have GhostScript installed for Macintosh. Please install it.")
            sys.exit(0)
        else:
            print("GhostScript for Macintosh found and utilized")

##if shutil.which("gs") is None:
##   print("GhostScript not avaible...Searching")
##   try:
##      gs = subprocess.Popen("which gs",stdout=subprocess.PIPE,shell=True)
##      gs_path = gs.stdout.read()
##      print(gs_path)
##      gs_path = gs_path.decode() if isinstance(gs_path,bytes) else gs_path
##      print("GhostScript found in",gs_path)
##      os.environ["PATH"] += ":"+ os.path.dirname(gs_path)
##   except Exception as e:
##      raise Warning("GhostScript not found. This program will not be able to save your work. If you want to save your work, please install GhostScript.")
##
##del subprocess
##del shutil
from turtle import *
from tkinter import *
import time
import queue
import threading
import math
from tkinter.colorchooser import *
import copy
from functools import wraps
import collections
import multiprocessing
import json
import pickle
import io
from PIL import Image, ImageEnhance, ImageOps

data = {}
data["penup"] = False

class Point:
   def __init__(self,x,y,color,width,penup,function,letterheight,letterwidth,spacewidth,turtleshape,turheading):
      self.x = x
      self.y = y
      self.color = color
      self.width = width
      self.penup = penup
      self.function = function
      self.letterheight = letterheight
      self.letterwidth = letterwidth
      self.spacewidth = spacewidth
      self.turtleshape = turtleshape
      self.turheading = turheading
 
   def draw2(self):
      if self.penup:
         penup()
      else:
         pendown()
         color(self.color)
         width(self.width)
      goto(self.x,self.y)
 
   def getXY(self):
      return (self.x, self.y)

   def getX(self):
      return (self.x)

   def getY(self):
      return (self.y)

   def getfunction(self):
      return (self.function)

   def getletterheight(self):
      return (self.letterheight)

   def getletterwidth(self):
      return (self.letterwidth)

   def getspacewidth(self):
       return (self.spacewidth)

   def getwidth(self):
      return (self.width)

   def getcolor(self):
      return (self.color)

   def __str__(self):
      return "({})".format(self.function)

   def recieveshape(self):
       return (self.turtleshape)

   def recieveheading(self):
       return (self.turheading)

class Color:
   def __init__(self, color):
      self.color = color

   def getcolor2():
      return (self.color)

t0 = time.clock()

# Function variables

space_width = 30 # Default value: 30
letter_height = 100 # Default value: 100
letter_width = 50 # Default value: 50

while True:
    a = input("Would you like to change the size of the letters from the default value? y/n?: ")
    if a == "y" or a == "Y":
        while True:
            try:
                letter_height = int(input("Enter a value from 10-170 to set the height of each letter in pixels: "))
                break
            except ValueError:
                print("That is not an integer! Please enter an integer from 10-170!")
        while letter_height > 170:
            try:
                letter_height = int(input("That value is too much. Please reenter a value from 10-170: "))
                while letter_height < 10:
                    letter_height = int(input("That value is too little. Please reenter a value from 10-170: "))
            except ValueError:
                print("That is not an integer! Please enter an integer from 10-170!")
        while letter_height < 10:
            try:
                letter_height = int(input("That value is too little. Please reenter a value from 10-170: "))
                while letter_height > 170:
                    letter_height = int(input("That value is too much. Please reenter a value from 10-170: "))
            except ValueError:
                print("That is not an integer! Please enter an integer from 10-170!")
        while True:
            try:
                letter_width = int(input("Enter a value from 10-170 to set the width of each letter in pixels: "))
                break
            except ValueError:
                print("That is not an integer! Please enter an integer from 10-170!")
        while letter_width > 170:
            try:
                letter_width = int(input("That value is too much. Please reenter a value from 10-170: "))
                while letter_width < 10:
                    letter_width = int(input("That value is too little. Please reenter a value from 10-170: "))
            except ValueError:
                print("That is not an integer! Please enter an integer from 10-170!")
        while letter_width < 10:
            try:
                letter_width = int(input("That value is too little. Please reenter a value from 10-170: "))
                while letter_width > 170:
                    letter_width = int(input("That value is too much. Please reenter a value from 10-170: "))
            except ValueError:
                print("That is not an integer! Please enter an integer from 10-170!")
            break
        break
    elif a == "n" or a == "N":
        letter_height = 100 # Default value: 100
        letter_width = 50 # Default value: 50
        break
    elif a != "y" or a != "Y" or a != "n" or a != "N":
        print("That is not an answer! Please enter either y or n!")

#The 'while' loop below will tell the user to choose a color name, but if the color is invalid, an exception is thrown, and the user must reenter a color name until a valid color name is entered. 

while True:
    try:
        pen_color=input("Enter a color name to set the pen color: ")
        pencolor(pen_color)
        break
    except:
        print("That is either not an available color or not a valid color name. Please reenter the name of another color or a valid one.")


newlist = list()

def changeletterwidth(width):
   global letter_width
   letter_width = (width)
   update()
   listen()

def changeletterheight(height):
   global letter_height
   letter_height = (height)
   update()
   listen()

def NewLetterDimensions():
    tracer(1, 0)
    NewLetterDimensions.done = True
    if not hasattr(NewLetterDimensions, "counter"):
       NewLetterDimensions.counter = 0
    NewLetterDimensions.counter += 1
    global letter_height
    user_height_input = (numinput("New Letter Height", "Please set the new letter height (Number between 10-170): ", minval = 10, maxval = 170))
    letter_height = letter_height if user_height_input is None else user_height_input
    if letter_height == user_height_input:
       mno.config(state = NORMAL)
    global vfo
    vfo = list()
    vfo.append(letter_height)
    re.add_command(label = "{}".format(letter_height), command = lambda letter_height = letter_height:changeletterheight(letter_height))

    global letter_width
    user_width_input = (numinput("New Letter Width", "Please set the new letter width (Number between 10-170): ", minval = 10, maxval = 170))
    letter_width = letter_width if user_width_input is None else user_width_input
    if letter_width == user_width_input:
       hjk.config(state = NORMAL)
    global hlf
    hlf = list()
    hlf.append(letter_width)
    do.add_command(label = "{}".format(letter_width), command = lambda letter_width = letter_width:changeletterwidth(letter_width))

    if letter_height == user_height_input or letter_width == user_width_input:
       original.config(state = NORMAL)
    if letter_height == letter_height and letter_width == letter_width:
        penup()
        goto(xcor(), ycor() -letter_height)
        pendown()

    penup()
    goto(xcor(), ycor() +letter_height)
    pendown()
    listen()
    tracer(0, 0)
    
    
def draw_space():
    # Add a space 30 pixels wide.
    penup()
    forward(space_width)
    pendown()
    
    
def move_turtle():
    # Pick up the turtle and move it to its starting location.
    penup()
    goto(-200, 100)
    pendown()
    

def draw_A():

    if letter_width/2 > letter_height:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))
    if letter_height/2 > letter_width:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))
    else:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))

    if letter_width/2 > letter_height:
        starting_angle = (math.degrees(math.acos((letter_height/2)/leg)))
    if letter_height/2 > letter_width:
        starting_angle = (math.degrees(math.acos((letter_width/2)/leg)))
    else:
        starting_angle = (math.degrees(math.acos((letter_width/2)/leg)))

    if letter_width/2 > letter_height:
        A_angle = ((math.degrees(math.asin((letter_height/2)/leg)))*2)
    if letter_height/2 > letter_width:
        A_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)
    else:
        A_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)
        
    end_angle = (180 - starting_angle)


    if letter_height/2 > letter_width:
        left(starting_angle)
        forward(leg/2)
        right(starting_angle)
        forward(letter_width/2)
        forward(-(letter_width/2))
        left(starting_angle)
        forward(leg/2)
        left(180)
        left(A_angle)
        forward(leg)
        left(starting_angle)
        draw_space()
        update()

    else:
        left(starting_angle)
        forward(leg/2)
        right(starting_angle)
        forward(letter_width/2)
        forward(-(letter_width/2))
        left(starting_angle)
        forward(leg/2)
        left(180)
        left(A_angle)
        forward(leg)
        left(starting_angle)
        draw_space()
        update()

def draw_B():

    if letter_width > letter_height:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - (letter_height/2))
        circle(-letter_height/4, 180)
        forward(letter_width - (letter_height/2))
        right(180)
        forward(letter_width - (letter_height/2))
        circle(-letter_height/4, 180)
        forward(letter_width - (letter_height/2))
        right(180)
        penup()
        forward((letter_width - letter_height/2) + letter_height/2 + space_width)
        pendown()
        update()

    elif letter_height/2 > letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - letter_width/2)
        circle(-letter_width/2, 90)
        forward((letter_height/2) - letter_width)
        circle(-letter_width/2, 90)
        forward(letter_width - letter_width/2)
        right(180)
        forward(letter_width - letter_width/2)
        circle(-letter_width/2, 90)
        forward((letter_height/2) - letter_width)
        circle(-letter_width/2, 90)
        forward(letter_width - letter_width/2)
        right(180)
        penup()
        forward((letter_width - letter_width/2) + (letter_width/2) + space_width)
        pendown()
        update()

    elif letter_height > letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - letter_width/2)
        circle(-letter_width/4, 90)
        forward(((letter_height/2) - (letter_width/2)))
        circle(-letter_width/4, 90)
        forward(letter_width - letter_width/2) 
        right(180)
        forward(letter_width - letter_width/2) 
        circle(-letter_width/4, 90)
        forward(((letter_height/2) - (letter_width/2)))
        circle(-letter_width/4, 90)
        forward(letter_width - letter_width/2)
        right(180)
        penup()
        forward((letter_width - letter_width/2) + (letter_width/2) + space_width)
        pendown()
        update()

    elif letter_height == letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_height*0.75)
        circle(-letter_height/4, 180)
        forward(letter_height*0.75)
        right(180)
        forward(letter_height*0.75)
        circle(-letter_height/4, 180)
        forward(letter_height*0.75)
        right(180)
        penup()
        forward(letter_height + space_width)
        pendown()
        update()
        

def draw_G():

    if letter_width > letter_height:
        penup()
        forward(letter_height/2)
        right(180)
        circle(-letter_height/2, 180)
        forward(letter_width - letter_height)
        circle(-letter_height/2, 45)
        right(180)
        pendown()
        circle(letter_height/2, 45)
        forward(letter_width - letter_height)
        circle(letter_height/2, 180)
        forward(letter_width - letter_height)
        circle(letter_height/2, 90)
        left(90)
        forward(letter_height/2)
        backward(letter_height/2)
        left(90)
        circle(-letter_height/2, 90)
        right(180)
        penup()
        forward(letter_height/2 + space_width)
        pendown()
        update()
        

    elif letter_height > letter_width:
        penup()
        forward(letter_width/2)
        right(180)
        circle(-letter_width/2, 90)
        forward(letter_height - letter_width)
        circle(-letter_width/2, 135)
        pendown()
        right(180)
        circle(letter_width/2, 135)
        forward(letter_height - letter_width)
        circle(letter_width/2, 180)
        forward((letter_height - letter_width)/2)
        left(90)
        forward(letter_width/2)
        backward(letter_width/2)
        left(90)
        penup()
        forward((letter_height - letter_width)/2)
        circle(-letter_width/2, 90)
        right(180)
        penup()
        forward(letter_width/2 + space_width)
        pendown()
        update()

    elif letter_height == letter_width:
        penup()
        forward(letter_height/2)
        right(180)
        circle(-letter_height/2, 225)
        pendown()
        right(180)
        circle(letter_height/2, 315)
        left(90)
        forward(letter_height/2)
        backward(letter_height/2)
        left(90)
        penup()
        circle(-letter_height/2, 90)
        right(180)
        forward(letter_height/2 + space_width)
        pendown()
        update()

        
def draw_V():
    if letter_width/2 > letter_height:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))
    if letter_height/2 > letter_width:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))
    else:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))

    if letter_width/2 > letter_height:
        starting_angle = (180 - (math.degrees(math.acos((letter_height/2)/leg))))
    if letter_height/2 > letter_width:
        starting_angle = (180 - (math.degrees(math.acos((letter_width/2)/leg))))
    else:
        starting_angle = (180 - (math.degrees(math.acos((letter_width/2)/leg))))

    if letter_width/2 > letter_height:
        Vertex_angle = ((math.degrees(math.asin((letter_height/2)/leg)))*2)
    if letter_height/2 > letter_width:
        Vertex_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)
    else:
        Vertex_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)

    if letter_width/2 > letter_height:
        end_angle = (math.degrees(math.acos((letter_height/2)/leg)))
    if letter_height/2 > letter_width:
        end_angle = (math.degrees(math.acos((letter_width/2)/leg)))
    else:
        end_angle = (math.degrees(math.acos((letter_width/2)/leg)))

    end_space_length = (math.sqrt((leg**2) - (letter_height**2)))
    
    penup()
    left(90)
    forward(letter_height)
    pendown()
    left(180)
    left(Vertex_angle/2)
    forward(leg)
    left(180)
    right(Vertex_angle)
    forward(leg)
    left(180)
    left(Vertex_angle/2)
    penup()
    forward(letter_height)
    left(90)
    pendown()
    draw_space()
    update()

def draw_X():
    if letter_width/2 > letter_height:
        leg = math.sqrt(((letter_width/2)**2) + ((letter_height/2)**2))
    if letter_height/2 > letter_width:
        leg = math.sqrt(((letter_width/2)**2) + ((letter_height/2)**2))
    else:
        leg = math.sqrt(((letter_width/2)**2) + ((letter_height/2)**2))

    if letter_width/2 > letter_height:
        starting_angle = (180 - (math.degrees(math.acos((letter_height/2)/leg))))
    if letter_height/2 > letter_width:
        starting_angle = (180 - (math.degrees(math.acos((letter_width/2)/leg))))
    else:
        starting_angle = (180 - (math.degrees(math.acos((letter_width/2)/leg))))

    if letter_width/2 > letter_height:
        Vertex_angle = ((math.degrees(math.asin((letter_height/2)/leg)))*2)
    if letter_height/2 > letter_width:
        Vertex_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)
    else:
        Vertex_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)

    penup()
    left(90)
    forward(letter_height)
    pendown()
    left(180)
    left(Vertex_angle/2)
    forward(leg)
    left(180)
    right(Vertex_angle)
    forward(leg)
    left(180)
    left(Vertex_angle/2)
    penup()
    forward(letter_height)
    pendown()
    left(180)
    left(Vertex_angle/2)
    forward(leg)
    left(180)
    right(Vertex_angle)
    forward(leg)
    right(180)
    right(90-(Vertex_angle/2))
    penup()
    forward(letter_width)
    pendown()
    draw_space()
    update()

    
   

def draw_K():
    if letter_width > letter_height:
        slant_height = (math.sqrt((letter_width**2) + ((letter_height/2)**2)))
    elif letter_height/2 > letter_width:
        slant_height = (math.sqrt((letter_width**2) + ((letter_height/2)**2)))
    elif letter_height > letter_width:
        slant_height = (math.sqrt((letter_width**2) + ((letter_height/2)**2)))
    elif letter_height == letter_width:
        slant_height = (math.sqrt((letter_height**2) + ((letter_height/2)**2)))

    if letter_width > letter_height:
        slant_angle = (90-(math.degrees(math.acos((letter_width/slant_height)))))
    elif letter_height/2 > letter_width:
        slant_angle = (90-(math.degrees(math.acos((letter_width/slant_height)))))
    elif letter_height > letter_width:
        slant_angle = (90-(math.degrees(math.acos((letter_width/slant_height)))))
    elif letter_height == letter_width:
        slant_angle = (90-(math.degrees(math.acos(letter_height/slant_height))))

    space_angle = (90 - slant_angle)

    left(90)
    forward(letter_height)
    penup()
    backward(letter_height/2)
    pendown()
    right(slant_angle)
    forward(slant_height)
    penup()
    backward(slant_height)
    left(slant_angle)
    pendown()
    left(180)
    left(slant_angle)
    forward(slant_height)
    left(space_angle)
    draw_space()
    update()    

        
    

def draw_I():
    forward(letter_width)
    backward(letter_width/2)
    left(90)
    forward(letter_height)
    left(90)
    forward(letter_width/2)
    forward(-letter_width)
    forward(letter_width/2)
    left(90)
    forward(letter_height)
    left(90)
    penup()
    forward((letter_width/2) + space_width)
    pendown()
    update()

def draw_T():
    penup()
    forward(letter_width)
    backward(letter_width/2)
    pendown()
    left(90)
    forward(letter_height)
    left(90)
    forward(letter_width/2)
    forward(-letter_width)
    forward(letter_width/2)
    left(90)
    forward(letter_height)
    left(90)
    penup()
    forward((letter_width/2)+space_width)
    pendown()
    update()

def draw_S():

    if letter_width > letter_height:
        penup()
        forward(letter_height/4)
        right(180)
        circle(-letter_height/4, 45)
        right(180)
        pendown()
        circle(letter_height/4, 45)
        forward(((letter_width) - (letter_height/2)))
        circle(letter_height/4, 180)
        forward(((letter_width) - (letter_height/2)))
        circle(-letter_height/4, 180)
        forward(((letter_width) - (letter_height/2)))
        circle(-letter_height/4, 45)
        penup()
        right(180)
        circle(letter_height/4, 45)
        forward(((letter_width) - (letter_height/2)))
        circle(letter_height/4, 180)
        forward(((letter_width) - (letter_height/2)))
        circle(-letter_height/4, 180)
        right(180)
        penup()
        forward(letter_height/4 + space_width)
        pendown()
        update()

    elif letter_height/2 > letter_width:
        penup()
        forward(letter_width/2)
        right(180)
        circle(-letter_width/2, 45)
        right(180)
        pendown()
        circle(letter_width/2, 135)
        forward(((letter_height/2) - (letter_width)))
        circle(letter_width/2, 90)
        circle(-letter_width/2, 90)
        forward(((letter_height/2) - (letter_width)))
        circle(-letter_width/2, 135)
        right(180)
        penup()
        circle(letter_width/2, 135)
        forward(((letter_height/2) - (letter_width)))
        circle(letter_width/2, 90)
        circle(-letter_width/2, 90)
        forward(((letter_height/2) - (letter_width)))
        circle(-letter_width/2, 90)
        penup()
        right(180)
        penup()
        forward(letter_width/2 + space_width)
        pendown()
        update()
        

    elif letter_height > letter_width:
        penup()
        forward(letter_width/4)
        right(180)
        circle(-letter_width/4, 45)
        right(180)
        pendown()
        circle(letter_width/4, 45)
        forward(letter_width - letter_width/2)
        circle(letter_width/4, 90)
        forward(((letter_height/2) - (letter_width/2)))
        circle(letter_width/4, 90)
        forward(letter_width - letter_width/2)
        circle(-letter_width/4, 90)
        forward(((letter_height/2) - (letter_width/2)))
        circle(-letter_width/4, 90)
        forward(letter_width - letter_width/2)
        circle(-letter_width/4, 45)
        right(180)
        penup()
        circle(letter_width/4, 45)
        forward(letter_width - letter_width/2)
        circle(letter_width/4, 90)
        forward(((letter_height/2) - (letter_width/2)))
        circle(letter_width/4, 90)
        forward(letter_width - letter_width/2)
        circle(-letter_width/4, 90)
        forward(((letter_height/2) - (letter_width/2)))
        circle(-letter_width/4, 90)
        penup()
        right(180)
        penup()
        forward(letter_width/4 + space_width)
        pendown()
        update()
        

    elif letter_height == letter_width:
        penup()
        right(180)
        circle(-letter_height/4, 45)
        right(180)
        pendown()
        circle(letter_height/4, 45)
        forward(letter_height*0.5)
        circle(letter_height/4, 180)
        forward(letter_height*0.5)
        circle(-letter_height/4, 180)
        forward(letter_height*0.5)
        circle(-letter_height/4, 45)
        penup()
        right(180)
        circle(letter_height/4, 45)
        forward(letter_height*0.5)
        circle(letter_height/4, 180)
        forward(letter_height*0.5)
        circle(-letter_height/4, 180)
        right(180)
        forward(letter_height/4 + space_width)
        pendown()
        update()

def draw_Y():
    if not hasattr(draw_Y, "counter"):
        draw_Y.counter = 0

    if letter_width/2 > letter_height:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))
    if letter_height/2 > letter_width:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))
    else:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))

    if letter_width/2 > letter_height:
        vertex_angle = ((math.degrees(math.asin((letter_height/2)/leg)))*2)
    if letter_height/2 > letter_width:
        vertex_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)
    else:
        vertex_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)

    end_space_length = (math.sqrt(((leg/2)**2) - ((letter_height/2)**2)))    

    penup()
    forward(end_space_length)
    pendown()
    left(90)
    forward(letter_height/2)
    left(vertex_angle/2)
    forward(leg/2)
    forward(-leg/2)
    right(vertex_angle)
    forward(leg/2)
    forward(-leg/2)
    left(vertex_angle/2)
    forward(-letter_height/2)
    right(90)
    penup()
    forward(end_space_length + space_width)
    pendown()
    update()

def draw_H():
    # Draws an H
    left(90)
    forward(letter_height)
    forward(-letter_height/2)
    right(90)
    forward(letter_width)
    left(90)
    forward(letter_height/2)
    forward(-letter_height)
    right(90)
    draw_space()
    update()
    

def draw_E():
    # Draw an E.
    left(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    forward(-letter_width)
    right(90)
    forward(letter_height/2)
    left(90)
    forward(letter_width)
    forward(-letter_width)
    right(90)
    forward(letter_height/2)
    left(90)
    forward(letter_width)
    draw_space()
    update()

def draw_F():
    left(90)
    forward(letter_height)
    right(90)
    forward(letter_width)
    backward(letter_width)
    right(90)
    forward(letter_height/2)
    left(90)
    forward(letter_width)
    backward(letter_width)
    right(90)
    forward(letter_height/2)
    left(90)
    penup()
    forward(letter_width + space_width)
    pendown()
    update()

def draw_L():
    # Draw an L
    left(90)
    forward(letter_height)
    forward(-letter_height)
    right(90)
    forward(letter_width)
    draw_space()
    update()

def draw_J():

    if letter_width > letter_height:
        penup()
        forward(letter_width - letter_height)
        pendown()
        circle(letter_height/2, 90)
        forward(letter_height - letter_height/2)
        left(90)
        forward(letter_width/4)
        backward(letter_width/2)
        forward(letter_width/4)
        right(90)
        right(180)
        forward(letter_height - letter_height/2)
        circle(-letter_height/2, 90)
        forward(letter_width - letter_height)
        circle(-letter_height/2, 45)
        right(180)
        penup()
        circle(letter_height/2, 45)
        forward((letter_width - letter_height/2) + letter_height/2 + space_width)
        pendown()
        update()

    elif letter_height > letter_width:
        penup()
        forward(letter_width/2)
        pendown()
        circle(letter_width/2, 90)
        forward(letter_height - (letter_width/2))
        left(90)
        forward(letter_width/2)
        backward(letter_width)
        forward(letter_width/2)
        left(90)
        forward(letter_height - (letter_width/2))
        penup()
        circle(-letter_width/2, 90)
        pendown()
        circle(-letter_width/2, 90)
        right(180)
        penup()
        circle(letter_width/2, 90)
        forward(letter_width/2 + space_width)
        pendown()
        update()

    elif letter_height == letter_width:
        penup()
        forward(letter_height/2)
        pendown()
        circle(letter_height/2, 90)
        forward(letter_height - (letter_height/2))
        left(90)
        forward(letter_width/2)
        backward(letter_width)
        forward(letter_width/2)
        left(90)
        forward(letter_height - (letter_height/2))
        penup()
        circle(-letter_height/2, 90)
        pendown()
        circle(-letter_height/2, 45)
        right(180)
        penup()
        circle(letter_height/2, 45)
        forward(letter_height/2 + space_width)
        pendown()
        update()

def draw_U():
    if letter_width > letter_height:
        penup()
        forward(letter_width - letter_height)
        pendown()
        circle(letter_height/2, 90)
        forward(letter_height - letter_height/2)
        right(180)
        forward(letter_height - letter_height/2)
        circle(-letter_height/2, 90)
        forward(letter_width - letter_height)
        circle(-letter_height/2, 90)
        forward(letter_height - letter_height/2)
        right(180)
        penup()
        forward(letter_height - letter_height/2)
        circle(letter_height/2, 90)
        forward((letter_width - letter_height) + letter_height + space_width)
        pendown()
        update()

    elif letter_height > letter_width:
        penup()
        forward(letter_width/2)
        pendown()
        circle(letter_width/2, 90)
        forward(letter_height - (letter_width/2))
        left(180)
        forward(letter_height - (letter_width/2))
        penup()
        circle(-letter_width/2, 90)
        pendown()
        circle(-letter_width/2, 90)
        forward(letter_height - (letter_width/2))
        right(180)
        penup()
        forward(letter_height - (letter_width/2))
        circle(letter_width/2, 90)
        forward(letter_width/2 + space_width)
        pendown()
        update()

    elif letter_height == letter_width:
        penup()
        forward(letter_height/2)
        pendown()
        circle(letter_height/2, 90)
        forward(letter_height - (letter_height/2))
        left(180)
        forward(letter_height - (letter_height/2))
        penup()
        circle(-letter_height/2, 90)
        pendown()
        circle(-letter_height/2, 90)
        forward(letter_height - (letter_height/2))
        right(180)
        penup()
        forward(letter_height - (letter_height/2))
        circle(letter_height/2, 90)
        forward(letter_height/2 + space_width)
        pendown()
        update()

def draw_O():
    # Draw an O

    if letter_width > letter_height:
        penup()
        forward(letter_height/2)
        pendown()
        right(180)
        circle(-letter_height/2, 180)
        forward(letter_width - letter_height)
        circle(-letter_height/2, 180)
        forward(letter_width - letter_height)
        right(180)
        penup()
        forward((letter_width - letter_height) + letter_height/2 + space_width)
        pendown()
        update()

    elif letter_height > letter_width:
        penup()
        forward(letter_width/2)
        pendown()
        circle(letter_width/2, 90)
        forward(letter_height - letter_width)
        circle(letter_width/2, 180)
        forward(letter_height - letter_width)
        circle(letter_width/2, 90)
        penup()
        forward(letter_width/2 + space_width)
        pendown()
        update()

    elif letter_height == letter_width:
        penup()
        forward(letter_height/2)
        pendown()
        circle(letter_height/2)
        penup()
        forward(letter_height/2 + space_width)
        pendown()
        update()

def draw_Q():
    if letter_width > letter_height:
        penup()
        forward(letter_height/2)
        pendown()
        right(180)
        circle(-letter_height/2, 180)
        forward(letter_width - letter_height)
        circle(-letter_height/2, 180)
        forward(letter_width - letter_height)
        right(180)
        penup()
        forward(letter_width - letter_height)
        pendown()
        left(135)
        forward(letter_height/4)
        backward(letter_height/2)
        forward(letter_height/4)
        right(135)
        penup()
        forward(letter_height/2 + space_width)
        pendown()
        update()
        

    elif letter_height > letter_width:
        penup()
        forward(letter_width/2)
        pendown()
        circle(letter_width/2, 90)
        forward(letter_height - letter_width)
        circle(letter_width/2, 180)
        forward(letter_height - letter_width)
        circle(letter_width/2, 90)
        penup()
        forward(letter_width/4)
        pendown()
        left(135)
        forward(letter_width/4)
        backward(letter_width/2)
        forward(letter_width/4)
        right(135)
        penup()
        forward(letter_width/4 + space_width)
        pendown()
        update()

    elif letter_height == letter_width:
        penup()
        forward(letter_height/2)
        pendown()
        circle(letter_height/2)
        penup()
        forward(letter_height/4)
        pendown()
        left(135)
        forward(letter_height/4)
        backward(letter_height/2)
        forward(letter_height/4)
        right(135)
        penup()
        forward(letter_height/4 + space_width)
        pendown()
        update()

def draw_C():
    if letter_width > letter_height:
        penup()
        forward(letter_height/2)
        pendown()
        forward(letter_width - letter_height)
        circle(letter_height/2, 45)
        right(180)
        circle(-letter_height/2, 45)
        penup()
        forward(letter_width - letter_height)
        pendown()
        circle(-letter_height/2, 180)
        forward(letter_width - letter_height)
        circle(-letter_height/2, 45)
        right(180)
        penup()
        circle(letter_height/2, 225)
        forward(letter_height/2 + space_width)
        pendown()
        update()

    elif letter_height > letter_width:
        penup()
        forward(letter_width/2)
        pendown()
        circle(letter_width/2, 45)
        right(180)
        penup()
        circle(-letter_width/2, 45)
        pendown()
        circle(-letter_width/2, 90)
        forward(letter_height - letter_width)
        circle(-letter_width/2, 135)
        right(180)
        penup()
        circle(letter_width/2, 135)
        forward(letter_height - letter_width)
        circle(letter_width/2, 90)
        forward(letter_width/2 + space_width)
        pendown()
        update()

    elif letter_height == letter_width:
        penup()
        forward(letter_height/2)
        circle(letter_height/2, 45)
        pendown()
        right(180)
        circle(-letter_height/2, 270)
        right(180)
        penup()
        circle(letter_height/2, 225)
        forward(letter_height/2 + space_width)
        pendown()
        update()
    

def draw_W():
    if not hasattr(draw_W, "counter"):
        draw_W.counter = 0

    if letter_width/2 > letter_height:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))
    if letter_height/2 > letter_width:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))
    else:
        leg = math.sqrt(((letter_width/2)**2) + (letter_height**2))

    if letter_width/2 > letter_height:
        starting_angle = (180 - (math.degrees(math.acos((letter_height/2)/leg))))
    if letter_height/2 > letter_width:
        starting_angle = (180 - (math.degrees(math.acos((letter_width/2)/leg))))
    else:
        starting_angle = (180 - (math.degrees(math.acos((letter_width/2)/leg))))

    if letter_width/2 > letter_height:
        Vertex_angle = ((math.degrees(math.asin((letter_height/2)/leg)))*2)
    if letter_height/2 > letter_width:
        Vertex_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)
    else:
        Vertex_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)

    if letter_width/2 > letter_height:
        end_angle = (math.degrees(math.acos((letter_height/2)/leg)))
    if letter_height/2 > letter_width:
        end_angle = (math.degrees(math.acos((letter_width/2)/leg)))
    else:
        end_angle = (math.degrees(math.acos((letter_width/2)/leg)))

    end_space_length = (math.sqrt((leg**2) - (letter_height**2)))
        
    
    # This function will draw a W
    left(90)
    penup()
    forward(letter_height)
    pendown()
    left(180)
    left(Vertex_angle/2)
    forward(leg)
    right(180)
    right(Vertex_angle)
    forward(leg/2)
    right(180)
    left(Vertex_angle)
    forward(leg/2)
    right(180)
    right(Vertex_angle)
    forward(leg)
    left(180)
    left(Vertex_angle/2)
    penup()
    forward(letter_height)
    left(90)
    pendown()
    draw_space()
    update()

def draw_M():
    if letter_width/2 > letter_height:
        leg = math.sqrt((letter_width**2) + (letter_height**2))
    elif letter_height/2 > letter_width:
        leg = math.sqrt((letter_width**2) + (letter_height**2))
    else:
        leg = math.sqrt((letter_width**2) + (letter_height**2))

    if letter_width/2 > letter_height:
        starting_angle = (math.degrees(math.acos((letter_height/2)/leg)))
    elif letter_height/2 > letter_width:
        starting_angle = (math.degrees(math.acos((letter_width/2)/leg)))
    else:
        starting_angle = (math.degrees(math.acos((letter_width/2)/leg)))

    if letter_width/2 > letter_height:
        M_angle = (math.degrees(math.asin(letter_width/leg)))
    elif letter_height/2 > letter_width:
        M_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)
    else:
        M_angle = (math.degrees(math.asin(letter_width/leg)))

    left(90)
    forward(letter_height)
    left(180)
    left(M_angle)
    forward(leg/2)
    left(180)
    right(M_angle*2)
    forward(leg/2)
    right(180)
    left(M_angle)
    forward(letter_height)
    left(90)
    draw_space()
    update()

def draw_N():

    if letter_width/2 > letter_height:
        leg = math.sqrt((letter_width**2) + (letter_height**2))
    elif letter_height/2 > letter_width:
        leg = math.sqrt((letter_width**2) + (letter_height**2))
    else:
        leg = math.sqrt((letter_width**2) + (letter_height**2))
    
    if letter_width/2 > letter_height:
        N_angle = (math.degrees(math.asin(letter_width/leg)))
    elif letter_height/2 > letter_width:
        N_angle = ((math.degrees(math.asin((letter_width/2)/leg)))*2)
    else:
        N_angle = (math.degrees(math.asin(letter_width/leg)))

    left(90)
    forward(letter_height)
    right(180)
    left(N_angle)
    forward(leg)
    right(180)
    right(N_angle)
    forward(letter_height)
    backward(letter_height)
    right(90)
    draw_space()
    update()

def draw_Z():
    if letter_width/2 > letter_height:
        leg = math.sqrt((letter_width**2) + (letter_height**2))
    elif letter_height/2 > letter_width:
        leg = math.sqrt((letter_width**2) + (letter_height**2))
    else:
        leg = math.sqrt((letter_width**2) + (letter_height**2))
    
    if letter_width/2 > letter_height:
        Z_angle = ((math.degrees(math.asin((letter_height/2)/leg)))*2)
    elif letter_height/2 > letter_width:
        Z_angle = (math.degrees(math.asin(letter_height/leg)))
    else:
        Z_angle = ((math.degrees(math.asin((letter_height/2)/leg)))*2.34)

    penup()
    left(90)
    forward(letter_height)
    right(90)
    pendown()
    forward(letter_width)
    left(180)
    left(Z_angle)
    forward(leg)
    right(180)
    right(Z_angle)
    forward(letter_width)
    draw_space()
    update()

def draw_R():
    # This function will draw an R

    if letter_width > letter_height:
        slant_height = (math.sqrt((((letter_width - letter_height/4) + letter_height/4)**2) + ((letter_height/2)**2)))
    elif letter_height/2 > letter_width:
        slant_height = (math.sqrt((letter_width**2) + ((letter_height/2)**2)))
    elif letter_height > letter_width:
        slant_height = (math.sqrt((letter_width**2) + ((letter_height/2)**2)))
    elif letter_height == letter_width:
        slant_height = (math.sqrt((letter_height**2) + ((letter_height/2)**2)))

    if letter_width > letter_height:
        slant_angle = (90+(90-(math.degrees(math.acos((((letter_width - letter_height/4) + letter_height/4)/slant_height))))))
    elif letter_height/2 > letter_width:
        slant_angle = (90+(90-(math.degrees(math.acos((letter_width/slant_height))))))
    elif letter_height > letter_width:
        slant_angle = (90+(90-(math.degrees(math.acos((letter_width/slant_height))))))
    elif letter_height == letter_width:
        slant_angle = (90+(90-(math.degrees(math.acos(letter_height/slant_height)))))
        


        
    space_angle = (180 - slant_angle)

    if letter_width > letter_height:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - (letter_height/4))
        circle(-letter_height/4, 180)
        forward(letter_width - (letter_height/4))
        left(slant_angle)
        forward(slant_height)
        left(space_angle)
        draw_space()
        update()

    elif letter_height/2 > letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - letter_width/2)
        circle(-letter_width/2, 90)
        forward((letter_height/2) - letter_width)
        circle(-letter_width/2, 90)
        forward(letter_width - letter_width/2)
        left(slant_angle)
        forward(slant_height)
        left(space_angle)
        penup()
        forward(space_width)
        pendown()
        update()

    elif letter_height > letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - letter_width/4)
        circle(-letter_width/4, 90)
        forward(((letter_height/2) - (letter_width/2)))
        circle(-letter_width/4, 90)
        forward(letter_width - letter_width/4)
        left(slant_angle)
        forward(slant_height)
        left(space_angle)
        penup()
        forward(space_width)
        pendown()
        update()
        

    elif letter_height == letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_height*0.75)
        circle(-letter_height/4, 180)
        forward(letter_height*0.75)
        left(slant_angle)
        forward(slant_height)
        left(space_angle)
        draw_space()
        update()
        

def draw_P():
    if letter_width > letter_height:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - (letter_height/4))
        circle(-letter_height/4, 180)
        forward(letter_width - (letter_height/4))
        left(90)
        forward(letter_height/2)
        left(90)
        penup()
        forward((letter_width - (letter_height/4)) + letter_height/4 + space_width)
        pendown()
        update()

    elif letter_height/2 > letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - letter_width/2)
        circle(-letter_width/2, 90)
        forward((letter_height/2) - letter_width)
        circle(-letter_width/2, 90)
        forward(letter_width - letter_width/2)
        left(90)
        forward(letter_height/2)
        left(90)
        penup()
        forward((letter_width - letter_width/2) + letter_width/2 + space_width)
        pendown()
        update()

    elif letter_height > letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - letter_width/4)
        circle(-letter_width/4, 90)
        forward(((letter_height/2) - (letter_width/2)))
        circle(-letter_width/4, 90)
        forward(letter_width - letter_width/4)
        left(90)
        forward(letter_height/2)
        left(90)
        penup()
        forward((letter_width - letter_width/4) + letter_width/4 + space_width)
        pendown()
        update()
        

    elif letter_height == letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_height*0.75)
        circle(-letter_height/4, 180)
        forward(letter_height*0.75)
        left(90)
        forward(letter_height/2)
        left(90)
        penup()
        forward((letter_height*0.75) + (letter_height/4) + space_width)
        pendown()
        update()
    
def draw_D():
    # This function will draw a REAL D


    if letter_width > letter_height:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - (letter_height/2))
        circle(-letter_height/2, 180)
        forward(letter_width - (letter_height/2))
        right(180)
        penup()
        forward((letter_width - (letter_height/2)) + letter_height/2 + space_width)
        pendown()
        update()
        

    elif letter_height/2 > letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - letter_width/2)
        circle(-letter_width/2, 90)
        forward(letter_height - letter_width)
        circle(-letter_width/2, 90)
        forward(letter_width - letter_width/2)
        right(180)
        penup()
        forward((letter_width - letter_width/2) + letter_width/2 + space_width)
        pendown()
        update()

    elif letter_height > letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_width - letter_width/4)
        circle(-letter_width/4, 90)
        forward((letter_height - (letter_width/2)))
        circle(-letter_width/4, 90)
        forward(letter_width - letter_width/4)
        right(180)
        penup()
        forward((letter_width - letter_width/4) + letter_width/4 + space_width)
        pendown()
        update()

    elif letter_height == letter_width:
        left(90)
        forward(letter_height)
        right(90)
        forward(letter_height/2)
        circle(-letter_height/2, 180)
        forward(letter_height/2)
        right(180)
        penup()
        forward(letter_height + space_width)
        pendown()
        update()

def period():
   dot()
   penup()
   draw_space()
   pendown()
   update()

def question():
   if letter_width > letter_height:
      dot()
      left(90)
      penup()
      forward(letter_height*0.25)
      pendown()
      forward(letter_height*0.25)
      right(90)
      forward(letter_width - (letter_height/2))
      circle(letter_height/4, 180)
      forward(letter_width - (letter_height/2))
      right(180)
      penup()
      forward(letter_width - (letter_height/2))
      circle(-letter_height/4, 180)
      forward(letter_width - (letter_height/2))
      left(90)
      forward(letter_height*0.5)
      left(90)
      forward((letter_width - letter_height/2) + letter_height/2 + space_width)
      pendown()
      update()

   elif letter_height/2 > letter_width:
      dot()
      left(90)
      penup()
      forward(letter_height*0.25)
      pendown()
      forward(letter_height*0.25)
      right(90)
      forward(letter_width - letter_width/2)
      circle(letter_width/2, 90)
      forward((letter_height/2) - letter_width)
      circle(letter_width/2, 90)
      forward(letter_width - letter_width/2)
      right(180)
      penup()
      forward(letter_width - letter_width/2)
      circle(-letter_width/2, 90)
      forward((letter_height/2) - letter_width)
      circle(-letter_width/2, 90)
      forward(letter_width - letter_width/2)
      left(90)
      forward(letter_height*0.5)
      left(90)
      forward((letter_width - letter_width/2) + (letter_width/2) + space_width)
      pendown()
      update()

   elif letter_height > letter_width:
      dot()
      left(90)
      penup()
      forward(letter_height*0.25)
      pendown()
      forward(letter_height*0.25)
      right(90)
      forward(letter_width - letter_width/2)
      circle(letter_width/4, 90)
      forward(((letter_height/2) - (letter_width/2)))
      circle(letter_width/4, 90)
      forward(letter_width - letter_width/2) 
      right(180)
      penup()
      forward(letter_width - letter_width/2)
      circle(-letter_width/4, 90)
      forward(((letter_height/2) - (letter_width/2)))
      circle(-letter_width/4, 90)
      forward(letter_width - letter_width/2) 
      left(90)
      forward(letter_height*0.5)
      left(90)
      forward((letter_width - letter_width/2) + (letter_width/2) + space_width)
      pendown()
      update()

   elif letter_height == letter_width:
      dot()
      left(90)
      penup()
      forward(letter_height*0.25)
      pendown()
      forward(letter_height*0.25)
      right(90)
      forward(letter_height*0.75)
      circle(letter_height/4, 180)
      forward(letter_height*0.75)
      right(180)
      penup()
      forward(letter_height*0.75)
      circle(-letter_height/4, 180)
      forward(letter_height*0.75)
      left(90)
      forward(letter_height*0.5)
      left(90)
      forward(letter_height + space_width)
      pendown()
      update()

def exclamation():
   dot()
   left(90)
   penup()
   forward(letter_height*0.25)
   pendown()
   forward(letter_height*0.75)
   right(180)
   penup()
   forward(letter_height)
   left(90)
   draw_space()
   pendown()
   update()

def comma():
   right(135)
   forward(letter_height*0.25)
   backward(letter_height*0.25)
   left(135)
   draw_space()
   update()
   
   

setup(1.0, 1.0)

def soar():
    penup()
    left(90)
    forward(letter_height + 5)
    right(90)
    pendown()

def fall():
    penup()
    right(90)
    forward(letter_height + 5)
    left(90)
    pendown()

def RotateRight():
    right(90)
    
def RotateLeft():
    left(90)

def width1():
    width(1)

def width2():
    width(2)

def width3():
    width(3)

def width4():
    width(4)

def width5():
    width(5)

def width6():
    width(6)

def width7():
    width(7)

def width8():
    width(8)

def width9():
    width(9)

def width10():
    width(10)

def Blue():
    color("blue")
    update()

def Red():
    color("red")
    update()

def DarkGreen():
    color("dark green")
    update()

def Purple():
    color("purple")
    update()

def Pink():
    color("pink")
    update()

def Brown():
    color("brown")
    update()

def Orange():
    color("orange")
    update()

def Black():
    color("Black")
    update()

def White():
   color("white")
   update()

def OriginalColor():
    color(pen_color)
    update()

colors = collections.deque()

def getColor():
    tracer(1, 0)
    try:
        Color = askcolor()
        color_name = Color[1]
        colormode(255)
        color(color_name)
        lp = Color(color_name)
        colors.append(lp)
    except TypeError:
        colormode(1)
        current_color = pencolor()
        color(current_color)
    tracer(0, 0)

def OriginalLetters():
    global letter_height
    letter_height = 100
    global letter_width
    letter_width = 50

##def function2_deque(function2 = collections.deque()):
##   global newerdeq
##   newerdeq = function2
##   try:
##      for i in function2:
##            k = i.getXY()
##            penup()
##            goto(k)
##            pendown()
##            hk = i.getletterheight()
##            global letter_height
##            letter_height = hk
##            rk = i.getletterwidth()
##            global letter_width
##            letter_width = rk
##            hw = i.getwidth()
##            width(hw)
##            op = i.getcolor()
##            try:
##               color(op)
##            except:
##               for g in colors:
##                  cp = g.getcolor2()
##                  colormode(255)
##                  color(cp)
##            j = i.getfunction()
##            j()
##            print("Yesh")
##   except:
##         pass


##function2_deque()
newerdeq = collections.deque()
mynewdeq = collections.deque()
memory = collections.deque()   
coordinatex = collections.deque()
coordinatey = collections.deque()
function = collections.deque()
##coordinate = collections.deque()
q = queue.Queue()
drawing = False
drawingLock = threading.Lock()

def increase():
   if not hasattr(increase, "counter"):
      increase.counter = 0
   increase.counter += 1


def letter():
   letter.work = True
   if not hasattr(letter, "counter"):
      letter.counter = 0
   letter.counter += 1

a_lock = threading.Lock()

def selectundo(x):
   with a_lock:
      for ty in range(x, len(function)):
         undoHandler()
         update()

dc = queue.Queue()

def doit(x):
    doit.drawing = True
    if not hasattr(doit, 'counter'):
         doit.counter = 0
    global drawing
    dc.put(x)
    process = False
    drawingLock.acquire()
    if not drawing:
        process = True
        drawing = True
    drawingLock.release()
    if process:
        if not dc.empty():
            x()
        drawingLock.acquire()
        drawing = False
        drawingLock.release()

def draw(x):
    draw.drawing = True
    if not hasattr(draw, 'counter'):
         draw.counter = 0
    global drawing
    q.put(x)
    process = False
    drawingLock.acquire()
    if not drawing:
        process = True
        drawing = True
    drawingLock.release()
    if process:
        if not q.empty():
            resetall.config(state = NORMAL)
            v = xcor()
            y = ycor()
            c = pencolor()
            w = width()
            ph = letter_height
            pw = letter_width
            iwe = space_width
            tf = shape()
            hde = heading()
            x()
            po = Point(v,y,c,w,isdown(),x,ph,pw,iwe,tf,hde)
            function.append(po)
            global loki
            kli.config(state = NORMAL)
            loki = ("{}".format(po.getfunction()))
            increase()
            he = str(increase.counter) + str(po)
            undo1.add_command(label = he, command = lambda: doit(lambda: selectundo(undo1.index(he))))
            if len(newerdeq) > 0:
               newerdeq.pop()
               redo1.delete(len(newerdeq))
            letter()
            draw.counter += 1
##            print("`draw` has been called {} times.".format(draw.counter))
            if x == draw_W:
                draw_W.drawing = True
                draw_W.counter += 1
                draw.counter -= 1
            elif x == draw_Y:
                draw_Y.drawing = True
                draw_Y.counter += 1
                draw.counter -= 1
            global h
            h = (x) 
        drawingLock.acquire()
        drawing = False
        drawingLock.release()

jmb = queue.Queue()

def doit1(x):
    doit1.doit = True
    if not hasattr(doit1, 'counter'):
         doit1.counter = 0
    global drawing
    jmb.put(x)
    process = False
    drawingLock.acquire()
    if not drawing:
        process = True
        drawing = True
    drawingLock.release()
    if process:
        if not jmb.empty():
            x()
            jth = xcor()
            jft = ycor()
            global coordinate
            coordinate = (jth, jft)
##            coordinate.append(tree)
##            if len(coordinate) >= 2:
##               coordinate.popleft()
            print(coordinate)
        drawingLock.acquire()
        drawing = False
        drawingLock.release()

increase.increasing = False
letter.work = False

def skip(x, y):
    skip.skipping = True
    if not hasattr(skip, "counter"):
       skip.counter = 0
    skip.counter += 1
    penup()
    goto(x, y)
    global o
    o = xcor()
    global p
    p = ycor()
    j = (o,p)
    draw.counter = 0
    walk.counter = 0
    back.counter = 0
    draw_W.counter = 0
    draw_Y.counter = 0
##    if increase.increasing == True:
##       newerdeq.clear()
##       function.clear()
    pendown()
    update()

def Clear():
   clear()
   speed(0)
   tracer(0,0)

def walk():
    walk.walking = True
    if not hasattr(walk, "counter"):
        walk.counter = 0
    walk.counter += 1
    penup()
    forward(space_width + letter_width)
    global fg
    fg = xcor()
    global yg
    yg = ycor()
    malk = (fg,yg)
    pendown()
    draw.counter = 0
    update()

walk.walking = False
draw.drawing = False
draw_W.drawing = False
draw_Y.drawing = False
skip.skipping = False

def back():
    back.backing = True
    if not hasattr(back, "counter"):
        back.counter = 0
    back.counter += 1
    penup()
    bk(space_width + letter_width)
    global l
    l = xcor()
    global u
    u = ycor()
    io = (l,u)
    pendown()
    draw.counter = 0
    update()

back.backing = False

def Up():
    Up.upping = True
    penup()
    goto(xcor(),ycor()+(letter_height+letter_height/2))
    global jrt
    jrt = xcor()
    global yup
    yup = ycor()
    sammy = (jrt,yup)
    pendown()
    draw.counter = 0
    walk.counter = 0
    back.counter = 0
    draw_W.counter = 0
    draw_Y.counter = 0
    update()

def Down():
    Down.downing = True
    penup()
    goto(xcor(),ycor()-(letter_height+letter_height/2))
    pendown()
    draw.counter = 0
    walk.counter = 0
    back.counter = 0
    draw_W.counter = 0
    draw_Y.counter = 0
    update()

Up.upping = False
doit1.doit = False
Down.downing = False

def gohere():
   if len(function) == 0:
      penup()
      skip(xcor(), ycor())
      pendown()

def selectredo(y):
   for fh in range(y, len(newerdeq)):
      redoHandler()
      update()

def increase3():
   if not hasattr(increase3, "counter"):
      increase3.counter = 0
   increase3.counter += 1

newcoordinates = []

stampcoors = collections.deque()
   
def undoHandler():
   if len(function) > 0 and draw.drawing == True:
      undoHandler.handling = True
      if not hasattr(undoHandler, "counter"):
         undoHandler.counter = 0
      undoHandler.counter += 1
      draw.counter -= 1
##      print("`draw` has been called {} times.".format(draw.counter))
      Clear()
      h = function.pop()
      undo1.delete(len(function))
      global kol
      fav.config(state = NORMAL)
      kol = ("{}".format(h.getfunction()))
      newerdeq.append(h)
      increase3()
      fi = str(increase3.counter) + str(h)
      redo1.add_command(label = fi, command = lambda: doit(lambda: selectredo(redo1.index(fi))))
##      print("From undo {}".format(newerdeq))
      penup()
      goto(-200, 100)
      pendown()
##      elif back.backing == True and letter.work == True and letter.counter == (letter.counter + 1):
##         july = coordinate2.pop()
##         goto(july)
##      elif draw.counter == 0 and walk.walking == True:
##         goto(fg,yg)
##      elif draw.counter == 0 and Up.upping == True:
##         goto(jrt,yup)
##      else:
##         goto(-200, 100)
      if len(mynewdeq) > 0:
         mynewdeq.pop()
         

      try:
         for i in function:
##            if i == StampPic:
##                penup()
##                goto(hg, fg)
####                k = i.getXY
####                goto(k)
##    ##            if doit1.doit == True:
##    ##               penup()
##    ##               goto(coordinate)
##    ##               pendown()
##    ##            else:
##    ##               pass
##    ##            if increase.increasing == False:
##    ##               goto(k)
##    ##            elif increase.increasing == True and skip.skipping == False:
##    ##               pass
##    ##            else:
##    ##               skip(xcor(), ycor())
##                pendown()
##            else:
##                pass
            tsd = i.recieveshape()
            shape(tsd)
            mndf = i.recieveheading()
            setheading(mndf)
            hk = i.getletterheight()
            global letter_height 
            letter_height = hk
            rk = i.getletterwidth()
            global letter_width
            letter_width = rk
            milk = i.getspacewidth()
            global space_width
            space_width = milk
            hw = i.getwidth()
            width(hw)
            op = i.getcolor()
            try:
               color(op)
            except:
               for g in colors:
                  cp = g.getcolor2()
                  colormode(255)
                  color(cp)
            j = i.getfunction()
            j()
      except:
         pass

      newx = xcor()
      newy = ycor()

      try:
         if newx == o and newy == p:
            undoHandler.counter = 0
##            print("`undo` has been called {} times.".format(undoHandler.counter))
      except:
         if newx == -200 and newy == 100 and skip.skipping == False:
            undoHandler.counter = 0
##            print("`undo` has been called {} times.".format(undoHandler.counter))
          
             

   update()

undoHandler.handling = False

def increase2():
   if not hasattr(increase2, "counter"):
      increase2.counter = 0
   increase2.counter += 1

def redoHandler():
   if undoHandler.handling == True and draw.drawing == True and len(newerdeq) > 0:
      redoHandler.handling = True
      if not hasattr(redoHandler, "counter"):
         redoHandler.counter = 0
      redoHandler.counter += 1
      draw.counter += 1
##      print("`draw` has been called {} times.".format(draw.counter))
      ui = newerdeq.pop()
      redo1.delete(len(newerdeq))
      global kid
      kli.config(state = NORMAL)
      kid = ("{}".format(ui.getfunction()))
      increase2()
      fe = str(increase2.counter) + str(ui)
      undo1.add_command(label = fe, command = lambda: selectundo(undo1.index(fe)))
##      print("Before from redo {}".format(newerdeq))
      function.append(ui)
      mynewdeq.append(ui)
##      print(mynewdeq)
      penup()
      pendown()

##      print("After from redo {}:".format(mynewdeq))
      i = mynewdeq.pop()
      k = i.getXY()
      penup()
##         if increase.increasing == False:
##            goto(k)
##         elif increase.increasing == True and skip.skipping == False:
##            pass
      pendown()
      kild = i.recieveshape()
      shape(kild)
      mndf = i.recieveheading()
      setheading(mndf)
      hk = i.getletterheight()
      global letter_height
      letter_height = hk
      rk = i.getletterwidth()
      global letter_width
      letter_width = rk
      malk = i.getspacewidth()
      global space_width
      space_width = malk
      hw = i.getwidth()
      width(hw)
      op = i.getcolor()
      try:
         color(op)
      except:
         for g in colors:
            cp = g.getcolor2()
            colormode(255)
            color(cp)
      j = i.getfunction()
      j()

          
             

   update()

def draw_newline():
    draw_newline.lining = True
    if not hasattr(draw_newline, "counter"):
       draw_newline.counter = 0
    draw_newline.counter += 1

    if walk.walking == False:
        h = 0
    elif walk.walking == True:
        h = walk.counter

    if draw.drawing == False:
        j = 0
    elif draw.drawing == True:
        j = draw.counter

    if back.backing == False:
        k = 0
    elif back.backing == True:
        k = back.counter

    if draw_W.drawing == False:
        f = 0
    elif draw_W.drawing == True:
        f = draw_W.counter

    if draw_Y.drawing == False:
        g = 0
    elif draw_Y.drawing == True:
        g = draw_Y.counter

##    if undoHandler.handling == False:
##        a = 0
##    elif undoHandler.handling == True:
##        a = undoHandler.counter

    penup()
    goto(xcor() -((((letter_width + space_width)*j) + (((letter_width + letter_width/2) + space_width)*f) + (((letter_width/2) + space_width)*g) + ((space_width*h) - (space_width*k)))), ycor() -(letter_height + letter_height/2))
    pendown()
    update()

draw_newline.lining = False

def clearer(x, y):
   draw(lambda: skip(x, y))
   memory.append(skip)
   global h
   h = (x)
   global a
   a = (y)
   coordinatex.append(h)
   coordinatey.append(a)
   listen()

def gotohere(x, y):
    penup()
    goto(x, y)
    pendown()

def dragHandler(x, y):
    doit(lambda: gotohere(x, y))
    update()

def CleaR():
    tracer(1, 0)
    clear()
    draw.counter = 0
    walk.counter = 0
    back.counter = 0
    draw_W.counter = 0
    draw_Y.counter = 0
    undoHandler.counter = 0
    move_turtle()
    tracer(0, 0)

NewLetterDimensions.done = False

def setdefaultturtle():
   shape('classic')
   color(pen_color)
   ondrag(nothing)
   manipulateimage.config(state = DISABLED)
   flipButton.config(state = DISABLED)
   mirrorButton.config(state = DISABLED)
   originalButton.config(state = DISABLED)
   resetturtle.config(state = DISABLED)
   setheading(0)
   
   update()

def ClearALL():
    clear()
    resetall.config(state = DISABLED)
    draw.counter = 0
    walk.counter = 0
    back.counter = 0
    draw_W.counter = 0
    draw_Y.counter = 0
    undoHandler.counter = 0
    move_turtle()
    function.clear()
    newerdeq.clear()
    increase()
    undo1.delete(0, increase.counter)
    kli.config(state = DISABLED)
    redo1.delete(0, increase.counter)
    fav.config(state = DISABLED)
    color(pen_color)
    OriginalLetters()
    mno.config(state = DISABLED)
    hjk.config(state = DISABLED)
    width(1)
    penup()
    goto(-200, 100)
    pendown()
    if NewLetterDimensions.done == True:
        re.delete(0, len(hlf))
        do.delete(0, len(vfo))
    original.config(state = DISABLED)
    bgpic('nopic')
    setdefaultturtle()
    update()

def unmutate2():
   draw(CleaR)

def unmutate():
   doit(undoHandler)

def unmutate3():
   doit(redoHandler)

def Print():
   canv = getscreen().getcanvas()
   here = canv.postscript(file = "Saved.ps")
   lpr = subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
   lpr.write(here)

def confirmation():
   if messagebox.askyesno("Are you sure?", "You will lose EVERYTHING, so make sure you save your work before proceeding!"):
      ClearALL()
   else:
      pass

NewLetterDimensions.done = False

def BGblue():
    bgcolor("blue")
    bgpic('nopic')
    update()

def BGred():
    bgcolor("red")
    bgpic('nopic')
    update()

def BGdarkgreen():
    bgcolor("dark green")
    bgpic('nopic')
    update()

def BGpurple():
    bgcolor("purple")
    bgpic('nopic')
    update()

def BGpink():
    bgcolor("pink")
    bgpic('nopic')
    update()

def BGbrown():
    bgcolor("brown")
    bgpic('nopic')
    update()

def BGorange():
    bgcolor("orange")
    bgpic('nopic')
    update()

def BGblack():
    bgcolor("Black")
    bgpic('nopic')
    update()

def background():
   bgresizebutton.config(state = NORMAL)
   originalbgButton.config(state = NORMAL)
   global cng
   cng = filedialog.askopenfilename()
   global img
   img = Image.open(cng)
   print(img)
   img.save(cng + '.gif', 'GIF')
   bgpic(cng + '.gif')
   bgcolor('white')

def bgresize():
    if not hasattr(bgresize, "counter"):
        bgresize.counter = 0
    bgresize.counter += 1
    width = img.size[0]
    height = img.size[1]
    NewOne2 = numinput('Width of Image', 'Set the width of the image: ', minval = 1)
    NewOne = numinput('Height of Image', 'Set the height of your image: ', minval = 1)
    Picwidth = NewOne2 if NewOne2 != None else width
    Picheight = NewOne if NewOne != None else height
    editpic = img.resize((int(Picwidth), int(Picheight)), Image.ANTIALIAS)
    editpic.save(cng + str(bgresize.counter) + '.gif', 'GIF')
    bgpic(cng + str(bgresize.counter) + '.gif')
    update()

def originalBG():
    bgpic(cng + '.gif')
    update()

def BGgetColor():
    tracer(1, 0)
    Color = askcolor()
    color_name = Color[1]
    colormode(255)
    bgcolor(color_name)
    bgpic('nopic')
    tracer(0, 0)

def clearbg():
   bgresizebutton.config(state = DISABLED)
   originalbgButton.config(state = DISABLED)
   bgpic('nopic')
   bgcolor('white')

def savefirst():
   try:
      cnv = getscreen().getcanvas()
      ps = cnv.postscript(colormode = 'color')
      global hen
      hen = filedialog.asksaveasfilename()
      print(hen)
      im = Image.open(io.BytesIO(ps.encode('utf-8')))
      im = im.resize((2560, 1600), Image.ANTIALIAS)
      quality_val = 95
      sharp = ImageEnhance.Sharpness(im)
      sharp.enhance(2.0).save(hen + '.png', 'PNG')
      savefirst.save = True
   except:
      pass

def save():
   ghi = getscreen().getcanvas()
   try:
      ms = ghi.postscript(colormode = 'color')
      am = Image.open(io.BytesIO(ms.encode('utf-8')))
      am = am.resize((2560, 1600), Image.ANTIALIAS)
      quality_val = 95
      sharp = ImageEnhance.Sharpness(am)
      sharp.enhance(2.0).save(hen + '.png', 'PNG')
   except:
      pass

def defaultheight():
   global letter_height
   letter_height = 100

def defaultwidth():
   global letter_width
   letter_width = 50

def swidth30():
   global space_width
   space_width = 30

def swidth25():
   global space_width
   space_width = 25

def swidth20():
   global space_width
   space_width = 20

def swidth15():
   global space_width
   space_width = 15

def swidth10():
   global space_width
   space_width = 10

def swidth5():
   global space_width
   space_width = 5

def swidth0():
   global space_width
   space_width = 0

def DrawMode():
   tracer(1)
   turn_speed = 50
   move_speed = 50
   def goforward():
      forward(move_speed)
   def gobackward():
      backward(move_speed)
   def goleft():
      left(turn_speed)
   def goright():
      right(turn_speed)
   penup()
   onkey(goforward, "Up")
   onkey(gobackward, "Down")
   onkey(goleft, "Left")
   onkey(goright, "Right")
   listen()

def nothing():
    pass

def rotateright():
    right(15)
    update()

def rotateleft():
    left(15)
    update()

pictures = collections.deque()
originality = collections.deque()
edited = collections.deque()
    
def TurtleShape():
   try:
       manipulateimage.config(state = NORMAL)
       flipButton.config(state = NORMAL)
       mirrorButton.config(state = NORMAL)
       originalButton.config(state = NORMAL)
       resetturtle.config(state = NORMAL)
       global klob
       klob = filedialog.askopenfilename()
       global im
       im = Image.open(klob)
       pictures.append(im)
       edited.clear()
       print(im)
       im.save(klob + '.gif', 'GIF')
       register_shape(klob + '.gif')
       shape(klob + '.gif')
       update()
   except:
       pass  

def TurtleImageResize():
    if not hasattr(TurtleImageResize, "counter"):
        TurtleImageResize.counter = 0
    TurtleImageResize.counter += 1
    width = im.size[0]
    height = im.size[1]
    NewOne2 = numinput('Width of Image', 'Set the width of the image: ', minval = 1)
    NewOne = numinput('Height of Image', 'Set the height of your image: ', minval = 1)
    Picwidth = NewOne2 if NewOne2 != None else width
    Picheight = NewOne if NewOne != None else height
    try:
        gear = edited.pop()
        editpic = gear.resize((int(Picwidth), int(Picheight)), Image.ANTIALIAS)
        print("Hooplah!")
        edited.append(gear)
    except:
        editpic = im.resize((int(Picwidth), int(Picheight)), Image.ANTIALIAS)
        print("Normal!")
    pictures.append(editpic)
    editpic.save(klob + str(TurtleImageResize.counter) + '.gif', 'GIF')
    register_shape(klob + str(TurtleImageResize.counter) + '.gif')
    shape(klob + str(TurtleImageResize.counter) + '.gif')
    update()

def StampPic():
   stamp()
   draw_space()
   global hg
   hg = xcor()
   global fg
   fg = ycor()
   update()

def flippic():
    if not hasattr(flippic, "counter"):
        flippic.counter = 0
    flippic.counter += 1
    ghy = pictures.pop()
    kpl = ImageOps.flip(ghy)
    pictures.append(kpl)
    try:
        edited.pop()
    except:
        pass
    edited.append(kpl)
    kpl.save(klob + str(flippic.counter) + '.gif')
    register_shape(klob + str(flippic.counter) + '.gif')
    shape(klob + str(flippic.counter) + '.gif')
    update()

def mirror():
    if not hasattr(mirror, "counter"):
        mirror.counter = 0
    mirror.counter += 1
    bbc = pictures.pop()
    fgrt = ImageOps.mirror(bbc)
    pictures.append(fgrt)
    try:
        edited.pop()
    except:
        pass
    edited.append(fgrt)
    fgrt.save(klob + str(mirror.counter) + ".gif")
    register_shape(klob + str(mirror.counter) + ".gif")
    shape(klob + str(mirror.counter) + ".gif")
    update()

def original23():
    if not hasattr(original23, "counter"):
        original23.counter = 0
    original23.counter += 1
    shape(klob + ".gif")
    edited.clear()
    update()

def Options():
    master = Frame()
    master.pack(side = 'top')

    
    colorphoto = PhotoImage(file = 'Images/font_color_icon.gif')
    mb = Menubutton(image = colorphoto)
    mb.colorphoto = colorphoto
    mb.pack(side = 'left')
    mb.menu = Menu(mb, tearoff = 0)
    mb["menu"] = mb.menu
    color = mb.menu
    color.add_command(label = "Blue", command = Blue)
    color.add_command(label = "Red", command = Red)
    color.add_command(label = "Green", command = DarkGreen)
    color.add_command(label = "Purple", command = Purple)
    color.add_command(label = "Pink", command = Pink)
    color.add_command(label = "Brown", command = Brown)
    color.add_command(label = "Orange", command = Orange)
    color.add_command(label = "Black", command = Black)
    color.add_command(label = "White", command = White)
    color.add_command(label = "Custom...", command = getColor)
    color.add_command(label = "Original Color", command = OriginalColor)
    mb.pack()


    thickphoto = PhotoImage(file = 'Images/Line-thickness-icon.gif')
    tb = Menubutton(image = thickphoto)
    tb.thickphoto = thickphoto
    tb.pack(side = 'left')
    tb.menu = Menu(tb, tearoff = 0)
    tb["menu"] = tb.menu
    thick = tb.menu
    thick.add_command(label = "1", command = width1)
    thick.add_command(label = "2", command = width2)
    thick.add_command(label = "3", command = width3)
    thick.add_command(label = "4", command = width4)
    thick.add_command(label = "5", command = width5)
    thick.add_command(label = "6", command = width6)
    thick.add_command(label = "7", command = width7)
    thick.add_command(label = "8", command = width8)
    thick.add_command(label = "9", command = width9)
    thick.add_command(label = "10", command = width10)
    tb.pack()

    imagery = PhotoImage(file = 'Images/undo-icon.gif')
    undoButton = Button(image = imagery, command=unmutate)
    undoButton.imagery = imagery
    undoButton.pack(side = "left")


    global kli
    kli = Menubutton(text = "Selective undo", state = DISABLED)
    kli.pack(side = "left")
    kli.menu = Menu(kli, tearoff = 0)
    kli["menu"] = kli.menu
    global undo1
    undo1 = kli.menu
    kli.pack()

    imagery2 = PhotoImage(file = 'Images/Redo.gif')
    redoButton = Button(image = imagery2, command = unmutate3)
    redoButton.imagery2 = imagery2
    redoButton.pack(side = "left")

    global fav
    fav = Menubutton(text = "Selective redo", state = DISABLED)
    fav.pack(side = "left")
    fav.menu = Menu(fav, tearoff = 0)
    fav["menu"] = fav.menu
    global redo1
    redo1 = fav.menu
    fav.pack()

    fontimage = PhotoImage(file = 'Images/toption-2.gif')
    change = Button(image = fontimage, command = NewLetterDimensions)
    change.fontimage = fontimage
    change.pack(side = 'left')

    global mno
    mno = Menubutton(text = "Previous heights", state = DISABLED)
    mno.pack(side = "left")
    mno.menu = Menu(mno, tearoff = 0)
    mno["menu"] = mno.menu
    global re
    re = mno.menu
    mno.pack()

    global hjk
    hjk = Menubutton(text = "Previous widths", state = DISABLED)
    hjk.pack(side = "left")
    hjk.menu = Menu(hjk, tearoff = 0)
    hjk["menu"] = hjk.menu
    global do
    do = hjk.menu
    hjk.pack()
    
    global original
    original = Button(text = "Set to Default Dimensions", command = OriginalLetters, state = DISABLED)
    original.pack(side = 'left')

    broomphoto = PhotoImage(file = 'Images/Broom_icon.gif')
    resetButton = Button(image = broomphoto, command = lambda: draw(CleaR))
    resetButton.broomphoto = broomphoto
    resetButton.pack(side = 'left')

    trashphoto = PhotoImage(file = 'Images/trash.gif')
    global resetall
    resetall = Button(image = trashphoto, command = confirmation, state = DISABLED)
    resetall.trashphoto = trashphoto
    resetall.pack(side = 'left')

    listen()

def options2():
   Options()

   saveasphoto = PhotoImage(file = 'Images/add_file.gif')
   savasButton = Button(image = saveasphoto, command = savefirst)
   savasButton.saveasphoto = saveasphoto
   savasButton.pack(side = 'left')

   photo = PhotoImage(file = 'Images/save.gif')
   saveButton = Button(image = photo, command = save)
   saveButton.photo = photo
   saveButton.pack(side = 'left')

   bgpicphoto = PhotoImage(file = 'Images/image.gif')
   bgButton = Button(image = bgpicphoto, command = background)
   bgButton.bgpicphoto = bgpicphoto
   bgButton.pack(side = 'left')

   bgresizephoto = PhotoImage(file = 'Images/image-resize.gif')
   global bgresizebutton
   bgresizebutton = Button(image = bgresizephoto, command = bgresize, state = DISABLED)
   bgresizebutton.bgresizephoto = bgresizephoto
   bgresizebutton.pack(side = 'left')

   global originalbgButton
   resetBG = PhotoImage(file = "Images/Reset Image.gif")
   originalbgButton = Button(image = resetBG, command = originalBG, state = DISABLED)
   originalbgButton.resetBG = resetBG
   originalbgButton.pack(side = "left")

##   bgphoto = PhotoImage(file = '/Users/Rohan/Pictures/paintcan.gif')
##   tba = Menubutton(image = bgphoto)
##   tba.bgphoto = bgphoto
##   tba.pack(side = 'left')
##   tba.menu = Menu(tba, tearoff = 0)
##   tba["menu"] = tba.menu
##   bgcolor1 = tba.menu
##   bgcolor1.add_command(label = "Blue", command = BGblue)
##   bgcolor1.add_command(label = "Red", command = BGred)
##   bgcolor1.add_command(label = "Green", command = BGdarkgreen)
##   bgcolor1.add_command(label = "Purple", command = BGpurple)
##   bgcolor1.add_command(label = "Pink", command = BGpink)
##   bgcolor1.add_command(label = "Brown", command = BGbrown)
##   bgcolor1.add_command(label = "Orange", command = BGorange)
##   bgcolor1.add_command(label = "Black", command = BGblack)
##   bgcolor1.add_command(label = "Custom...", command = BGgetColor)
##   tba.pack()

   clearbg2 = PhotoImage(file = 'Images/ClearImage.gif')
   emptybg = Button(image = clearbg2, command = clearbg)
   emptybg.clearbg2 = clearbg2
   emptybg.pack(side = 'left')

   gho = Menubutton(text = 'Compactness')
   gho.pack(side = 'left')
   gho.menu = Menu(gho, tearoff = 0)
   gho["menu"] = gho.menu
   pol = gho.menu
   pol.add_command(label = "30", command = swidth30)
   pol.add_command(label = "25", command = swidth25)
   pol.add_command(label = "20", command = swidth20)
   pol.add_command(label = "15", command = swidth15)
   pol.add_command(label = "10", command = swidth10)
   pol.add_command(label = "5", command = swidth5)
   pol.add_command(label = "0", command = swidth0)
   gho.pack()
   
   picture = PhotoImage(file = "Images/TurtleImage.gif")
   turtlepic = Button(image = picture, command = TurtleShape)
   turtlepic.picture = picture
   turtlepic.pack(side = 'left')

   stampy = PhotoImage(file = "Images/stamp-medium-2.gif")
   stampimage = Button(image = stampy, command = lambda: draw(StampPic))
   stampimage.stampy = stampy
   stampimage.pack(side = 'left')

   global resetturtle
   turtly = PhotoImage(file = "Images/Turtle2.gif")
   resetturtle = Button(image = turtly, command = setdefaultturtle, state = DISABLED)
   resetturtle.turtly = turtly
   resetturtle.pack(side = 'left')

   global manipulateimage
   turtleone = PhotoImage(file = "Images/TurtleImageResize.gif")
   manipulateimage = Button(image = turtleone, command = TurtleImageResize, state = DISABLED)
   manipulateimage.turtleone = turtleone
   manipulateimage.pack(side = 'left')

   global flipButton
   flipImage = PhotoImage(file = "Images/Vertical Flip.gif")
   flipButton = Button(image = flipImage, command = flippic, state = DISABLED)
   flipButton.flipImage = flipImage
   flipButton.pack(side = 'left')

   global mirrorButton
   mirrorImage = PhotoImage(file = "Images/Horizontal Flip.gif")
   mirrorButton = Button(image = mirrorImage, command = mirror, state = DISABLED)
   mirrorButton.mirrorImage = mirrorImage
   mirrorButton.pack(side = 'left')

   global originalButton
   originalTimage = PhotoImage(file = "Images/ResetTurtleImage.gif")
   originalButton = Button(image = originalTimage, command = original23, state = DISABLED)
   originalButton.originalTimage = originalTimage
   originalButton.pack(side = "left")

##   var = IntVar()
##   opti = Checkbutton(text = "Draw Mode", variable = var, command = DrawMode)
##   opti.pack(side = 'left')

##   printButton = Button(text = "Print",command = Print)
##   printButton.pack(side = "left")


def handle_enter():
    draw.counter = 0
    walk.counter = 0
    back.counter = 0
    draw_W.counter = 0
    draw_Y.counter = 0
    undoHandler.counter = 0

def Carriage_functions():
    draw_newline()
    handle_enter()

savefirst.save = False

def savior():
   if messagebox.askyesno('Are you sure?', 'Are you sure you want to quit?'):
      if savefirst.save == False:
         if messagebox.askyesno('Save', 'You have not saved your work yet. Would you like to save?'):
            savefirst()
      save()
      bye()
   

title("QuikCreator")
move_turtle()
color(pen_color)
options2()
speed(0)
delay(0)
tracer(0)
listen()
onscreenclick(clearer)
onkey(width1, "1")
onkey(width2, "2")
onkey(width3, "3")
onkey(width4, "4")
onkey(width5, "5")
onkey(width6, "6")
onkey(width7, "7")
onkey(width8, "8")
onkey(width9, "9")
onkey(width10, "0")
onkey(Blue, "F1")
onkey(Red, "F2")
onkey(DarkGreen, "F3")
onkey(Purple, "F4")
onkey(Pink, "F5")
onkey(Brown, "F6")
onkey(Orange, "F7")
onkey(Black, "F8")
onkey(getColor, "F9")
onkey(OriginalColor, "F10")
onkey(lambda: draw(back), "Left")
onkey(lambda: draw(Up), "Up")
onkey(lambda: draw(draw_H), "h")
onkey(lambda: draw(draw_A), "a")
onkey(lambda: draw(draw_B), "b")
onkey(lambda: draw(draw_G), "g")
onkey(lambda: draw(draw_V), "v")
onkey(lambda: draw(draw_I), 'i')
onkey(lambda: draw(draw_T), "t")
onkey(lambda: draw(draw_S), "s")
onkey(lambda: draw(draw_Y), "y")
onkey(lambda: draw(draw_M), "m")
onkey(lambda: draw(draw_N), "n")
onkey(lambda: draw(draw_C), "c")
onkey(lambda: draw(draw_F), "f")
onkey(lambda: draw(draw_P), "p")
onkey(lambda: draw(draw_J), "j")
onkey(lambda: draw(draw_Q), "q")
onkey(lambda: draw(draw_U), "u")
onkey(lambda: draw(draw_Z), "z")
onkey(lambda: draw(draw_K), "k")
onkey(lambda: draw(draw_X), "x")
onkey(savior, "Escape")
onkey(lambda: draw(draw_E), "e")
onkey(lambda: draw(draw_L), "l")
onkey(lambda: draw(draw_O), "o")
onkey(lambda: draw(draw_W), "w")
onkey(lambda: draw(draw_R), "r")
onkey(lambda: draw(draw_D), "d")
onkey(lambda: draw(period), ".")
onkey(lambda: draw(question), "?")
onkey(lambda: draw(exclamation), "!")
onkey(lambda: draw(comma), ",")
onkey(lambda: draw(walk), "space")
onkey(lambda: draw(Down), "Down")
onkey(lambda: doit(redoHandler), "Right")
onkey(lambda: doit(undoHandler), "BackSpace")
onkey(rotateright, ">")
onkey(rotateleft, "<")

if __name__ == "__main__":
   redoHandler()
   undoHandler()

if sys.platform == 'win32':
   input()
else:
   pass
