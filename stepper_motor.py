import RPi.GPIO as GPIO
import time  
GPIO.setmode(GPIO.BCM) 

controlPin=[26,19,13,6]

for pin in controlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

#do tylu        
seq2=[ [1,0,1,0],
       [0,1,1,0],
       [0,1,0,1],
       [1,0,0,1] ]
#do przodu
seq3=[ [1,0,0,1],
       [0,1,0,1],
       [0,1,1,0],
       [1,0,1,0] ] 

def funkcja():
    for i in range(100):
        for halfstep in range(4):
            for pin in range(4):
                GPIO.output(controlPin[pin],seq2[halfstep][pin])
                time.sleep(0.002)
                
    for i in range(50):
        for halfstep in range(4):
            for pin in range(4):
                GPIO.output(controlPin[pin],seq3[halfstep][pin])
                time.sleep(0.002)       
     


