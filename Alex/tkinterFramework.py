# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 00:33:52 2017

@author: alexp
"""

import tkinter as tk
import time

def labelmaker(_master, _text):
    return tk.Label(master=_master, text=_text)
    
def callback_adder(_element, _callback):
    _element["command"] = _callback
    return

    
class Screen(tk.Frame):
    """
    A screen is defined as a collection of displayable elements which
    together represent a single contiguous functional unit of display.
    Screens are constructed using the add elements method, which adds 
    elements to the internal representation of the screen. This screen
    is then added to the apps list of displayable screens
    """
    def __init__(self, master):
        self.master = master
        super(Screen, self).__init__(self.master)
        self.elements = []
        self.callbacks = []


    def get_elements(self):
        return self.elements
        
    def add_element(self, _element, _row, _column):
        element = (_element, _row, _column)
        self.elements.append(element)
        return
        
    def remove_element(self, _element):
        self.elements.remove(_element)
        return 
    
    def get_callbacks(self):
        return self.callbacks
        
    def add_callback(self, _element, _command):
        self.callbacks.append(_command)
        callback_adder(_element, _command)
        return
        
    def remove_callback(self, _element, _callback):
        self._element["command"] = None
        self.callbacks.remove(_callback)
        return
    def grid_elements(self):
        for x in self.elements:
            x[0].grid(row=x[1], column=x[2])
        return
        
       
    
class App(tk.Frame):
    """
    The App holds the list of screens and is responsible
    for any manipulation of those screens, primarily by
    adding or removing screens from the list of displayable screens
    (screens) or by invoking the set-active-screen method, which refreshes
    the elements buffer and populates it with the elements of the new screen
    """
    
    def __init__(self, master):
        self.master = master
        super(App, self).__init__(self.master)
        self.screens = []
        self.active_elements = []

    def add_screen(self, screen):
        self.screens.append(screen)
        return
        
    def remove_screen(self, screen):
        self.screens.remove(screen)
        return

    def set_active_screen(self, screen):
        #First dispose of any old elements
        for item in self.active_elements:
            item[0].grid_forget()
        #Empty the active elements list
        self.active_elements = []
        #Populate the active elements list with the elements listed
        #in the individual screens elements list
        for item in screen.elements:
            self.active_elements.append(item)
        #Activate each of the elements now in the active elements list
        for item in self.active_elements:
            item[0].grid(row=item[1], column=item[2])
        return
        
  

def ScreenFactory(master):
    screen = Screen(master)
    return screen
