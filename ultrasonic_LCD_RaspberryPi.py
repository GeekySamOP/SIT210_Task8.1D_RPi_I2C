#Libraries
import RPi.GPIO as GPIO
import time
from rpi_lcd import LCD

lcd = LCD()
#GPIO Mode which is set to board
GPIO.setmode(GPIO.BOARD)
 
#setting GPIO Pins
GPIO_TRIGGER = 8
GPIO_ECHO = 10




#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)



def distance():
    # set Trigger pin to HIGH when it will triggers a signal
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW that it will not trigger the signal again
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    #initialising two variables for time diffrence
    StartTime = time.time()
    StopTime = time.time()
 
    # store StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # store time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime

    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back

    distance = (TimeElapsed * 34300) / 2
    x= int(distance)
    return x

try:
	while True:
		dist = distance()
		msg = str(dist) +" cm"
		
		print("Measured Distance = %.1f cm" % dist)
		lcd.text("distance:",1)
		lcd.text(msg,2)
		time.sleep(0.01)
        
except KeyboardInterrupt:
    print("\nProgram is stopped")
    
GPIO.cleanup()
