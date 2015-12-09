import serial
import RPi.GPIO as GPIO
import time

	
	
data=""

ser = serial.Serial ("/dev/ttyAMA0")

serial.baudrate = 9600
LED = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,GPIO.LOW)
time.sleep(5)
GPIO.output(LED,GPIO.HIGH)

while True:
	
	data = ser.readline()
	
	
	print data
	



