import serial
from sympy import *
from math import exp,sqrt
import RPi.GPIO as GPIO
import time

f = open("rssi1_dttm","a")
LED = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.LOW)
ser = serial.Serial ("/dev/ttyAMA0")
serial.baudrate = 9600
time.sleep(5)
GPIO.output(LED,GPIO.HIGH)

data=""
inputname = ""
inputrssi = 0

nobr=0
username=[]
ble1rssi=[]
ble2rssi=[]
ble3rssi=[]
divide1=[]
divide2=[]
divide3=[]
d1=0
d2=0
d3=0
s=1.1
x=[]
y=[]



def checknamerssi():

	global inputname
	global username
	global nobr
	#print "checknamerssi"
	#print inputname
	thesame=0
	for i in range(0,len(username)):
		if username[i] == inputname:
			thesame=1
			nobr=i
			i=len(username)
	if thesame == 0:
		username.append(inputname)
		nobr = len(username)-1
		divide1.append(1)
		ble1rssi.append(0.0)
		divide2.append(1)
		ble2rssi.append(0.0)
		divide3.append(1)
		ble3rssi.append(0.0)
		x.append(0.0)
		y.append(0.0)


	thesame = 0
	#print "user",len(username)
	#print	username
	#print "nobr",nobr
	

def carsystem():


	global inputname
	global username
	global nobr

	
	while True:

		data =	ser.readline()
		print data
		if data == "BLE1\0\n":
			print "ok1"
			inputname = ser.readline()
			print inputname
			inputrssi = ser.readline(4)		
			print inputrssi
			checknamerssi()
			print "nobr",nobr
			if divide1[nobr] != 3:
				ble1rssi[nobr] = float(inputrssi)
				
			elif divide1[nobr] == 3:
				ble1rssi[nobr] -= ble1rssi[nobr] / divide1[nobr]
				ble1rssi[nobr] += float(inputrssi)
		elif data == "BLE3\0\n":
			print "ok2"
			inputname = ser.readline()
			print inputname
			inputrssi = ser.readline(4)
			print inputrssi
			checknamerssi()
			if divide2[nobr] != 3:
				ble2rssi[nobr] = float(inputrssi)
				
			elif divide1[nobr] == 3:
				ble2rssi[nobr] -= ble2rssi[nobr] / divide2[nobr]
				ble2rssi[nobr] += float(inputrssi)
		elif data == "BLE2\0\n":
			print "ok3"
			inputname = ser.readline()
			print inputname
			inputrssi = ser.readline(4)
			print inputrssi
			checknamerssi()
			if divide3[nobr] != 3:
				ble3rssi[nobr] = float(inputrssi)
				
			elif divide3[nobr] == 3:
				ble3rssi[nobr] -= ble3rssi[nobr] / divide3[nobr]
				ble3rssi[nobr] += float(inputrssi)
		elif data == "#\n":
			for i in range(0,len(username)):
				print "rssi:",ble1rssi[i],ble2rssi[i],ble3rssi[i]
				print "div:",divide1[i],divide2[i],divide3[i]
				if divide1[i] * divide2[i] * divide3[i] != 0:
					d1 = 10**((-62-(ble1rssi[i]/divide1[i]))/32.5)
					print "d1:",d1
					if username[i] == "B4994C64C9F6\x00\n":
						f.write(str(ble1rssi[i])+"\n")
					d2 = 10**((-62-(ble2rssi[i]/divide2[i]))/32.5)
					print "d2:",d2
					d3 = 10**((-62-(ble3rssi[i]/divide3[i]))/32.5)
					print "d3:",d3
					s = (d1+d2+2)/2
					y[i] =sqrt(abs(s * (s-d1) * (s-d2) * (s-2)))/2
					x[i] =sqrt(abs(d2**2 - y[i]**2))-sqrt(abs(d1**2 - y[i]**2))
					if sqrt(abs(d2**2 - y[i]**2))>2 :
						if x[i]>0:
							x[i] += 1
						elif x[i]<0:
							x[i] -= 1
					if sqrt(abs(d1**2 - y[i]**2))>2 :
						if x[i]>0:
							x[i] += 1
						elif x[i]<0:
							x[i] -= 1					
					
					if (sqrt(abs(d3**2-x[i]**2)) - y[i]) < 2:
						y[i] *= (-1)
					print x[i]
					print y[i]

		
			i =	len(username)-1

			#GPIO.output(LED,GPIO.LOW)
			ser.close()
			
			return i,username,x,y
			break

		#else:
			#GPIO.output(LED,GPIO.LOW)
			#GPIO.output(LED,GPIO.HIGH)