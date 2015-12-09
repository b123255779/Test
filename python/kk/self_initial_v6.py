#-*- coding: utf-8 -*-　　 
#-*- coding: cp950 -*-
#!/usr/bin/python

import sys
import input_test
import time
from PyQt4.QtGui import *
from PyQt4.QtCore import *

i = -1	#預設值
userID = []
x = []
y = []

class Project(QWidget):
		
	def __init__(self):
		super(Project,self).__init__()
		
		self.initUI()	#基本的介面設定
		pix,car_re,person_icon_re,car_icon_re,pix_site = self.layout()	#畫面初始化
		
		self.thread = WorkerThread(pix,car_re,person_icon_re,car_icon_re,pix_site)
		self.connect(self.thread,SIGNAL("refresh(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"),self.refresh)
		self.thread.start()
		# inputUI(1,["car","person"],[50,100],[80,160])
		
		# self.timer = QTimer(self)
		# self.connect(self.timer,SIGNAL("timeout()"),lambda:self.refresh(pix,car_re,pix_site))
		# self.timer.start(2000)
		
	def initUI(self):
		self.setWindowTitle("Project")
		self.setGeometry(0,0,600,600)
		self.setWindowIcon(QIcon("icon_pin.png"))
		self.center()
		
	def center(self):	#將視窗放在螢幕中央
		screen = QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width() - size.width()) / 2,(screen.height() - size.height()) / 2)
		
	def layout(self):
		title = QLabel("<font color=red size=20><b>Micro-location<b></font>",self)
		
		#-------------------畫圖--------------------
		# pix = QPixmap(500,500)
		# pix.fill(Qt.black)
		pix = QPixmap("road.png")	#載入道路圖片
		pix_re = pix.scaled(500,500,Qt.IgnoreAspectRatio)
		
		car = QPixmap("car2.png")	#載入車子圖片
		car_re = car.scaled(80,160,Qt.IgnoreAspectRatio)	#改變車子大小
		
		person_icon = QPixmap("person_icon2.png")	#載入車的icon
		person_icon_re = person_icon.scaled(25,25,Qt.IgnoreAspectRatio)
		
		car_icon = QPixmap("car_icon.png")		#載入人的icon
		car_icon_re = car_icon.scaled(25,25,Qt.IgnoreAspectRatio)
		
		draw = QPainter()
		draw.begin(pix)
		draw.drawPixmap(210,170,car_re)	#畫車子 #(210,170)為圖片左上角的位子
		
		draw.end()
		
		#-------------------------------------------

		pix_site = QLabel(self)	#pix以Label方式顯示
		pix_site.setPixmap(pix)
		
		title.move(205,20)
		pix_site.move(50,70)
		
		return pix,car_re,person_icon_re,car_icon_re,pix_site
		
	def refresh(self,pix,car_re,person_icon_re,car_icon_re,pix_site):
		pix = QPixmap("road.png")
		
		draw = QPainter()
		draw.begin(pix)
		draw.drawPixmap(210,170,car_re)	#畫車子 #(210,170)為圖片左上角的位子
		
		j = i	#區域接全域
		while j >= 0:
			# print "userID[%d] ="%j,userID[j]
			if userID[j] == "car":
				
				draw.drawPixmap(int(x[j]),int(y[j]),car_icon_re)
		
				# draw.setPen(Qt.cyan)	#筆畫框
				# draw.setBrush(Qt.cyan)	#刷子填滿
				# draw.drawRect(int(x[j]),int(y[j]),15,15)
				# print "this is car_determine\n","j =",j
			elif userID[j] == "person":
				
				draw.drawPixmap(int(x[j]),int(y[j]),person_icon_re)
				
				# draw.setPen(Qt.yellow)	#筆畫框
				# draw.setBrush(Qt.yellow)	#刷子填滿
				# draw.drawEllipse(int(x[j]),int(y[j]),10,10)
				# print "this is person_determine\n","j =",j
			else:
				# print "The userID are neither car nor person"
				pass
			j = j - 1
		# print "endj =",j
		
		draw.end()
		
		pix_site.setPixmap(pix)
		pix_site.move(50,70)
		
		# self.update() #更新畫面
		# print "--------------------demarcation--------------------"
		
class WorkerThread(QThread):
	def __init__(self,pix,car_re,person_icon_re,car_icon_re,pix_site):
		super(WorkerThread,self).__init__()
		self.pix = pix
		self.car_re = car_re
		self.person_icon_re = person_icon_re
		self.car_icon_re = car_icon_re
		self.pix_site = pix_site
		
	def __del__(self):
		self.wait()
	
	def run(self):
		while True:
			
			# 放小屁孩的function
			global i,userID,x,y
			i,userID,x,y = input_test.calculate()
			# print i
			# print userID
			# print x
			# print y
			
			time.sleep(0.01)
			self.emit(SIGNAL("refresh(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"),self.pix,self.car_re,self.person_icon_re,self.car_icon_re,self.pix_site)
			
			# print "Done with the thread"
			
# def inputUI(i_in,userID_in,x_in,y_in):
	
	# global i,userID,x,y
	
	# i = i_in
	# userID = userID_in
	# x = x_in
	# y = y_in
	
	# print i
	# print userID
	# print x
	# print y

if __name__ == "__main__":
	
	app = QApplication(sys.argv)
	pj = Project()
	pj.show()
	app.exec_()
	
	
	


