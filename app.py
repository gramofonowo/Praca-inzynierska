import sys
sys.path.append('/home/pi/inz/Praca inzynierska Oskar Staniszewski/')
import ds18b20 as ds
import dht11
import hcsr501 as mov
import RPi.GPIO as GPIO
import time
import lirc
import AppInterface


GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.output(16, 0)
GPIO.output(20, 0)
lista=[]
motion=[]
name3=ds.TempSensorDS18B20(sensid=2, path='/sys/bus/w1/devices/28-0000062c3765/w1_slave')
name4=ds.TempSensorDS18B20(sensid=1, path='/sys/bus/w1/devices/28-0315724e7dff/w1_slave')
name1=dht11.TempHumSensorDHT11(pin=22)
name2=mov.MotionSensorHCSR501(pin=21)
motion.append(name2)
lista.append(name2)
lista.append(name1)
lista.append(name3)
lista.append(name4)
sockid=lirc.init("ircontrol", blocking=False)
i=0
t=0
v=False
time.sleep(5)
#AppInterface.menu()
while True:
    
    codeIR=lirc.nextcode()
    lista[t].getStatus()
    time.sleep(1)

    if codeIR==['KEY_CHANNELUP']:
        GPIO.output(20, 0)
        GPIO.output(16, 0)
        if t>=len(lista)-1:
            t=0
        else:
            t+=1
    elif codeIR==['KEY_CHANNELDOWN']:
        GPIO.output(20, 0)
        GPIO.output(16, 0)
        t-=1
        if t<0:
            t=len(lista)-1

    elif codeIR==['KEY_CHANNEL']:
        GPIO.output(20, 0)
        GPIO.output(16, 0)
        v=not v
        if v==True:
            motion[0].setON()
        else:
            motion[0].setOFF()
    elif codeIR==['KEY_NUMERIC_0']:
        ds.lcdModule.lcdDisplay.setData("Koniec. . .", ds.lcdModule.lcdDisplay.LINE1)
        ds.lcdModule.lcdDisplay.setData("", ds.lcdModule.lcdDisplay.LINE2)
        GPIO.output(16, 0)
        GPIO.output(20, 0)
        break      
