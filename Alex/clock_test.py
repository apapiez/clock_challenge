from tkinterFramework import *

root = tk.Tk()
app = App(root)

     
        
clock_screen = ScreenFactory(app)
my_clock = tk.Label(text="")
clock_screen.add_element(my_clock, 0, 0)
app.add_screen(clock_screen)

app.set_active_screen(app.screens[0])

def update_time():
    my_clock["text"] = str(time.localtime()[3])+":"+str(time.localtime()[4])+":"+str(time.localtime()[5])
    root.after(200, update_time)

if __name__ == "__main__":
    update_time()
    root.mainloop()
