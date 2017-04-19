from tkinterFramework import *
import tkinter.ttk as ttk
from timedict import *

root = tk.Tk()
app = App(root)
note = ttk.Notebook(root)
     
        
clock_screen = ScreenFactory(note)
my_clock = tk.Label(clock_screen, text="")
clock_screen.add_element(my_clock, 0, 0)
clock_screen.grid_elements()

wordclock_screen = ScreenFactory(note)
my_wordclock = tk.Label(wordclock_screen, text="")
wordclock_screen.add_element(my_wordclock, 0, 0)
wordclock_screen.grid_elements()



note.add(clock_screen, text="clock screen")
note.add(wordclock_screen, text="wordclock screen")
note.grid(row=0, column=0)

def update_time():
    my_clock["text"] = str(time.localtime()[3])+":"+str(time.localtime()[4])+":"+str(time.localtime()[5])
    hours, minutes, seconds = time.localtime()[3:6]
    my_wordclock["text"] = make_time_string(hours, minutes, seconds)
    root.after(200, update_time)
    
def make_time_string(hours, minutes, seconds):
    hourstring = hourdict[hours]
    to_hourstring = hourdict[hours+1]
    minstring = w_dict[minutes]
    secstring = w_dict[seconds]
   # print(hourstring, to_hourstring, minstring, secstring)
    if minutes and seconds == 0:
        timestring = "It is "+hourstring+" O' clock"
        return timestring
    if minutes == 30 and seconds == 0:
        timestring = "It is half past "+hourstring
        return timestring
    if minutes == 0 and seconds != 0:
        timestring = "It is "+hourstring+" O' clock and "+secstring+" seconds."
        return timestring
    if minutes < 30 and seconds == 0:
        timestring = "It is "+minstring+" past "+hourstring
        return timestring
    if minutes < 30 and seconds != 0:
        timestring = "It is "+minstring+" past "+hourstring+" and "+secstring+" seconds."
        return timestring
    if minutes > 30 and seconds == 0:
        timestring = "It is "+minstring+" to "+to_hourstring
        return timestring
    if minutes > 30 and seconds != 0:
        timestring = "It is "+minstring+" to "+to_hourstring+" and "+secstring+" seconds."
        return timestring

if __name__ == "__main__":
    update_time()
    root.mainloop()
