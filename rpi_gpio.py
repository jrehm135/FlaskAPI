import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# GPIO selectors
channel_list = [1 , 7 , 8 , 25]
GPIO.setup(channel_list, GPIO.OUT)

# PWM Setup
GPIO.setup(12, GPIO.OUT)

#For use referencing which channel goes where
dirDict = {
    0: 1,  #OPEN/CLOSE
    1: 7,  #UP/DOWN
    2: 8,  #FORWARD/BACK
    3: 25, #LEFT/RIGHT
}

# Takes in a number, converts to binary, and powers all ones,
#   as well as shutting off all zeros
def select_servos(direction):
    servoNum = 0
    for num in range(0, 3):
        #Grab value stored in byte
        setVal = (direction >> num) & 1
        #Grab appropriate value from dict and output to it
        # GPIO.output(dirDict.get(num), setVal)
        if setVal == 1:
            servoNum = dirDict.get(num)
            print(dirDict.get(num), num, setVal)
        #GPIO.cleanup()
    return servoNum


def pwm_move(servo):
    p = GPIO.PWM(servo.servoNum, 50)  # channel=12 frequency=50Hz
    p.start(servo.dutyCycle)
    time.sleep(.5)
    p.stop()
    GPIO.cleanup()