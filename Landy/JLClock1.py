import tkinter
import time
import math


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
		self.start=0
		self.stop=0
		self.refresh=1
		self.stopped=0
		self.reset=1
		self.timer=self.timedif(self.start,self.stop)
		self.timebox=tkinter.Label(self.root,width=self.twidth,text=self.time)
		self.timebox.grid(row=0,columnspan=4,column=0)
		self.timerbox=tkinter.Label(self.root,width=self.twidth,text=self.timer)
		self.timerbox.grid(row=1,columnspan=4,column=0)
		
		
		self.config=[ #[type, grid row, grid column, text/label, command, (scale)[: from,to,increment,setvalue] ]
		['button',2,0,'Reset',self.resetb,0],#0
		['button',2,1,'Start',self.startb,1],#1
		['button',2,2,'Lap',self.lapb,2],#2
		['button',2,3,'Stop',self.stopb,3],#2
		]
		self.control=[]
		
		for j in self.config:
				self.control.append([tkinter.Button(self.root, text=j[3], command=j[4])])
				self.control[j[5]][0].grid(row=j[1],column=j[2])
		
		
		self.update()
				
	def	timedif(self,start,stop):
		difsec=stop-start
		print(difsec)
		
		if self.stopped>0:
			difsec-=self.stopped
		
		hour=math.floor(difsec/3600)
		hours=str(hour)
		if hour < 10:
			hours='0'+hours
		difsec=difsec%3600
		
		min=math.floor(difsec/60)
		mins=str(min)
		if min < 10:
			mins='0'+mins
		difsec=difsec%60
		
		secs=str(difsec)[:4]
		if difsec < 10:
			secs='0'+secs	
		
		difstring=hours+':'+mins+':'+secs
		
		return(difstring)
		
	def startb(self):
		if self.reset==1:
			self.start=time.time()
			self.reset=0
		
		if self.reset==0 and self.stop!=0:
			self.stopped+=time.time()-self.stop
			print(self.stopped)
			self.stop=0
		self.refresh=0
		
	
	def resetb(self):
		self.reset=1
		self.refresh=1
		self.stopped=0
		self.timerbox.config(text='00:00:00.00')
	
	def lapb(self):
		self.refresh=1
		
		
	def stopb(self):
		if self.stop==0:
			self.stop=time.time()
		self.refresh=2
		
	def update(self):
		self.time=time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
		self.timebox.config(text=self.time)
		if self.refresh==0:
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