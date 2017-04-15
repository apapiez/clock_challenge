# -*- coding: utf-8 -*-
"""
crudemodo
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
        print ("contents of active elements :")
        for item in self.active_elements:
            print(item[0], "row: ",item[1], "Column: ",item[2])
        return
        
  

def ScreenFactory(master):
    screen = Screen(master)
    return screen

root = tk.Tk()
app = App(root)

#main_screen = ScreenFactory(app)
#main_screen.add_element(tk.Label(text="Main menu"), 0, 0)
#main_screen.add_element(tk.Button(text="Test"), 1, 0)
#app.add_screen(main_screen)
#app.set_active_screen(app.screens[0])
#screen1 = ScreenFactory(app)
#screen1.add_element(tk.Label(text="hi there"),1, 1)
#app.add_screen(screen1)
#main_screen.add_callback(main_screen.elements[1][0], lambda: app.set_active_screen(app.screens[1]))
#import_sample_screen = ScreenFactory(app)
#import_sample_screen        
        
clock_screen = ScreenFactory(app)
year = str(time.gmtime()[0])
print(year)
my_clock = tk.Label(text=year)
clock_screen.add_element(my_clock, 0, 0)
app.add_screen(clock_screen)
print(app.screens[0])
app.set_active_screen(app.screens[0])

def update_time():
    my_clock["text"] = str(time.gmtime()[3])+":"+str(time.gmtime()[4])+":"+str(time.gmtime()[5])
    root.after(200, update_time)

if __name__ == "__main__":
    update_time()
    root.mainloop()
