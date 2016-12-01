import os
import time
import glob
import hd47780 as lcdModule
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

class TempSensorDS18B20():
    __sensorPath={}
    __sensorID=0
    __sensorList=[]
    __sensorName=""

    def __init__(self, sensid=None, path=None):        
        
        self.__sensorID=sensid or self.__setID()
        self.__sensorPath[self.__sensorID]=path or self.__setPath()        
        self.__setName()
        
    def __readPath(self):
        
        self.__sensorList=glob.glob('/sys/bus/w1/devices/28-*')
        
        
    def __checkPath(self):
   
        if os.path.exists(self.__sensorPath[self.__sensorID])==True:            
            print('path ok')
            self.__checkData()            
        else:
            print("Brak dostepu do sciezki %s"%self.__sensorPath[self.__sensorID]+' - usuwam niesprawny czujnik')
            lcdModule.lcdDisplay.setData('DS18B20 ID: %d'%self.__sensorID, lcdModule.lcdDisplay.LINE1)
            lcdModule.lcdDisplay.setData('Uszkodzony!', lcdModule.lcdDisplay.LINE2)
            GPIO.output(20, 1)
            self.__del__()
    def __checkData(self):        
       
        f=open(self.__sensorPath[self.__sensorID], 'r')        
        dataRead=f.readlines()
        f.close()
        endOfLine=dataRead[0].find('\n')        
        dataReadErr=dataRead[0].strip()[endOfLine-2:]      
        if dataReadErr=='NO':                
            print('Problem z odczytem na czujniku %s' %self.__sensorPath[self.__sensorID])
            lcdModule.lcdDisplay.setData('DS18B20 ID: %d'%self.__sensorID, lcdModule.lcdDisplay.LINE1)
            lcdModule.lcdDisplay.setData('Error', lcdModule.lcdDisplay.LINE2)
            GPIO.output(16, 0)
            GPIO.output(20, 1)
            time.sleep(0.3)
            GPIO.output(20, 0)
        else:                
            print('Odczyt danych na czujniku %s poprawny'%self.__sensorName)            
            self.__getData()
            
    def __getData(self):
        
        f=open(self.__sensorPath[self.__sensorID], 'r')
        dataRead=f.readlines()  
        f.close()            
        endOfLine=dataRead[1].find('t=')        
        temperature=dataRead[1].strip()[endOfLine+2:]
        temp_c=float(temperature)/1000.0
        print('temperatura na czujniku: %.1f C'%temp_c)        
        GPIO.output(16, 1)
        lcdModule.lcdDisplay.setData('DS18B20 ID: %d'%self.__sensorID, lcdModule.lcdDisplay.LINE1)
        lcdModule.lcdDisplay.setData('%.1f C'%temp_c, lcdModule.lcdDisplay.LINE2)    

    def getStatus(self):                   
            self.__checkPath()
       
        
    def getName(self):
        return self.__sensorName
    
    def __del__(self):
        print("USUNIETO CZUJNIK %s"%self.__sensorName)   
    
    def __setID(self):
        self.__sensorList=glob.glob('/sys/bus/w1/devices/28-*')
        print("Dodawanie czujnika temperatury, wykryto czujniki: ")
        for i in range(len(self.__sensorList)):
            print(i+1, self.__sensorList[i])
        sensid=int(input("wybierz z listy powyzej czujnik, ktory chcesz zainstalowac: "))
        return sensid
    
    def __setPath(self):
        path=self.__sensorList[self.__sensorID-1]+'/w1_slave'
        return path
    
    def __setName(self):
        self.__sensorName='DS18B20 ID: '+str(self.__sensorID)    



