import RPi.GPIO as GPIO 
import time
 
ledPin = 22    
 
def setup():
        GPIO.setmode(GPIO.BOARD)       
        GPIO.setup(ledPin, GPIO.OUT)   
        GPIO.output(ledPin, GPIO.LOW)  
 
def loop():
        while True:
                print 'LED on'
                GPIO.output(ledPin, GPIO.HIGH)   
                time.sleep(1.0)                  
                print 'LED off'
                GPIO.output(ledPin, GPIO.LOW)   
                time.sleep(1.0)                 
def endprogram():
 
        GPIO.output(ledPin, GPIO.LOW)     
        GPIO.cleanup()                    
 
if __name__ == '__main__':         
        setup()
        try:
                loop()
        except KeyboardInterrupt:  
                endprogram()