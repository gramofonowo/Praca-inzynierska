import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import hd47780 as lcdModule
       
seq_backwards=[ [1,0,1,0],
       [0,1,1,0],
       [0,1,0,1],
       [1,0,0,1] ]

seq_forward=[ [1,0,0,1],
       [0,1,0,1],
       [0,1,1,0],
       [1,0,1,0] ] 

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
class MotionSensorHCSR501():
    __pin=0    
    __sensorName=""
    __controlPin=[26,19,13,6]
    __status=0
    
    def __init__(self,pin):
        self.__pin=pin        
        self.__setName()
        
    def getStatus(self):        
        if self.__status==0:
            lcdModule.lcdDisplay.setData('HCSR501 PIN: %d'%self.__pin, lcdModule.lcdDisplay.LINE1)
            lcdModule.lcdDisplay.setData('stan: OFF', lcdModule.lcdDisplay.LINE2)
            GPIO.output(16, 0)
            GPIO.output(20, 1)
        else:
            lcdModule.lcdDisplay.setData('HCSR501 PIN: %d'%self.__pin, lcdModule.lcdDisplay.LINE1)
            lcdModule.lcdDisplay.setData('stan: AKTYWNY', lcdModule.lcdDisplay.LINE2)
            GPIO.output(20,0)
            GPIO.output(16, 1)
            if GPIO.input(self.__pin):
                time.sleep(3)
                            
                for pin in self.__controlPin:
                    GPIO.setup(pin, GPIO.OUT)
                    GPIO.output(pin, 0)
                    
                for i in range(50):
                    for fullstep in range(4):
                        for pin in range(4):
                            GPIO.output(self.__controlPin[pin],seq_backwards[fullstep][pin])
                            time.sleep(0.002)
                time.sleep(1)            
                for i in range(50):
                    for fullstep in range(4):
                        for pin in range(4):
                            GPIO.output(self.__controlPin[pin],seq_forward[fullstep][pin])
                            time.sleep(0.002) 
    def setOFF(self):
        GPIO.setup(self.__pin, GPIO.OUT)
        GPIO.output(self.__pin, 0)
        self.__status=0
        
    def setON(self):
        GPIO.setup(self.__pin, GPIO.IN)
        self.__status=1        
       
    def __setName(self):
        name='HCSR501 PIN: '+str(self.__pin)
        self.__sensorName=name
        
    def getName(self):
        return self.__sensorName
    
    def __del__(self):
        print("USUNIETO CZUJNIK %s"%self.__sensorName)


