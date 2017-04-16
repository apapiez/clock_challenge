from tkinterFramework import *
from timedict import *

root = tk.Tk()
app = App(root)

     
        
clock_screen = ScreenFactory(app)
my_clock = tk.Label(text="")
clock_screen.add_element(my_clock, 0, 0)
app.add_screen(clock_screen)

app.set_active_screen(app.screens[0])

def update_time():
    hours, minutes, seconds = time.localtime()[3:6]
    my_clock["text"] = make_time_string(hours, minutes, seconds)
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
