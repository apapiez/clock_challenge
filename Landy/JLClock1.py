import tkinter
import time



def runconfig():
	width=40
	depth=200
	tick=50
	return([width,depth,tick])

class Window:

	def __init__(self,root,width,height,tick):
		self.tick=tick
		self.root=root
		self.twidth=width
		self.cheight=height
		self.time=time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
		self.start=time.time()
		self.stop=time.time()
		self.timer=self.timedif(self.start,self.stop)
		self.timebox=tkinter.Label(self.root,width=self.twidth,text=self.time)
		self.timebox.grid(row=0,columnspan=4,column=0)
		self.timerbox=tkinter.Label(self.root,width=self.twidth,text=self.timer)
		self.timerbox.grid(row=1,columnspan=4,column=0)
		
		
		self.config=[ #[type, grid row, grid column, text/label, command, (scale)[: from,to,increment,setvalue] ]
		#['button',2,0,'Mode',self.mode,0],#0
		['button',2,1,'Start',self.startb,0],#1
		['button',2,2,'Stop',self.stopb,1],#2
		]
		self.control=[]
		
		for j in self.config:
				self.control.append([tkinter.Button(self.root, text=j[3], command=j[4])])
				self.control[j[5]][0].grid(row=j[1],column=j[2])
		
		
		self.update()
				
	def	timedif(self,start,stop):
		difsec=stop-start
			
		
		return(difsec)
		
	def startb(self):
		print("go")
		self.start=time.time()
		self.stop=0
		print("go")
		
	def stopb(self):
		print("go")
		self.stop=1
		
	def update(self):
		self.time=time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
		self.timebox.config(text=self.time)
		if self.stop==0:
			self.timerbox.config(text=self.timedif(self.start,time.time()))
		root.after(self.tick, lambda: self.update())


config=runconfig()

width=config[0]
height=config[1]
tick=config[2]


root = tkinter.Tk()
root.resizable(0,0)
window = Window(root,width,height,tick)
root.mainloop()