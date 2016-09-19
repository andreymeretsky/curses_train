#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------
# Curses Programming Template
#-------------------------------
import curses
import apsw
import curses.textpad
import string
import webbrowser

from time import  sleep, time

class Display(object):

    screen = None

    def __init__(self):
        self.screen = curses.initscr()
        self.screen.nodelay(1)
        self.max_height,self.max_width = self.screen.getmaxyx()
        self.max_height-=1
        self.max_width-=1

        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        self.directions = {
            'UP': self.inc_y,
            'DOWN': self.dec_y,
            'LEFT': self.dec_x,
            'RIGHT': self.inc_x,
            }
        self.init_debug_area()

    def init_debug_area(self):
        self.screen_debug = curses.newwin(4, 4, 2, 0)
        self.screen_debug.border(0)
        # tb = curses.textpad.Textbox(self.screen_debug)
        # text = tb.edit()
        # curses.addstr(4,1,text.encode('utf_8'))

        # curses.addstr(0,0, 'oh')

    def inc_x(self):
        """docstring for inc_x"""
        self.x+=1

    def dec_x(self):
        """docstring for inc_x"""
        self.x-=1
        
    def inc_y(self):
        """docstring for inc_y"""
        self.y+=1

    def dec_y(self):
        """docstring for inc_y"""
        self.y-=1
        
    def InitScreen(self, Border):
        if Border == 1:
            self.screen.border(0)

    def addLine(self):
        self.screen.addstr(0,0, "Mouse hello!")
        self.screen.addstr(25,68, "Mouse hello second!")
        self.screen.addstr(1,1, "Press Any Key to Continue")

    def __del__(self):
        pass

    def bullet(self):
        for i in range(100):
            self.screen.addstr(0,0, str(i), curses.color_pair(1))
            self.screen.refresh()
            sleep(0.1)
            # for j in range(10):
                # self.screen.erase()
                # self.screen.erase()

        # curses.endwin()
    x = 0
    y = 0
    def draw(self):
        """docstring for draw"""
        try:
            self.screen.clear()
            self.screen.addch(self.y, self.x, '-')
            self.screen.refresh()
            sleep(0.1)
        except Exception as e:
            self.screen.addch(self.prev_y, self.prev_x, '-')
            self.screen.refresh()
            raise e

    def move(self, direction):
        """docstring for move"""
        self.prev_x = self.x
        self.prev_y = self.y
        self.directions(direction)()
        self.draw()

        
    def snake(self):
        key = 'X'

        while key != ord('0'):
            key = self.screen.getch(12, 22)
            self.screen.addstr(0, 0 , str ( key ))
            try:
                if key == 65: # UP
                    self.move('UP')
                elif key == 66: #DOWN
                    self.move('DOWN')
                elif key == 68: # LEFT 
                    self.move('LEFT')
                elif key == 67: # RIGHT
                    self.move('RIGHT') 
            except:
                self.screen.addstr(self.max_height/2, self.max_width/2, 'border detected')
                self.screen.refresh()
            finally:
                pass

            self.screen.addstr(self.max_height, 0, str(time()))
            # sleep(1)

    def get_params(self):
        """docstring for get_paramset"""
        height,width = self.screen.getmaxyx()
        num = min(height,width)
        for x in range(num):
            self.screen.addstr(x,x,str(num))
        self.screen.refresh()
        sleep(3)

    def put_area(self):
        
        """docstring for put"""
        height,width = self.screen.getmaxyx()
        
        key = 'X'

        while key != ord('0'):
            key = self.screen.getch(12, 22)
            

        
try:
    display = Display()
    display.InitScreen(1)
    display.snake()
    # display.get_params()
    # display.put_area()
    # display.bullet()
    # display.screen.getch()

except Exception as e:
    print e
    sleep(10)
    display.screen.getch()
finally:
    curses.endwin()
