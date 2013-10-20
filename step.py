import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
#enable_pin = 4
coil_A_1_pin = 17
coil_A_2_pin = 18
coil_B_1_pin = 27
coil_B_2_pin = 22
 
#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

step_order = [
    (1, 0, 0, 1),
    (1, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 1, 1),
]
 
#GPIO.output(enable_pin, 1)
 
def rotate(delay, steps):  
    if steps < 0:
        dir = -1
        steps = -steps
    else:
        dir = 1

    for ix in range(steps):
        for args in step_order[::dir]:
            setStep(*args)
            time.sleep(delay)
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

def off():
    setStep(0,0,0,0)
 
if __name__=='__main__':
    import sys
    delay = 2
    if len(sys.argv) == 2:
        rotate(float(delay) / 1000.0, int(sys.argv[1]))
        off()
    else:
        try:
            while True:
                #delay = raw_input("Delay between steps (milliseconds)?")
                steps = raw_input("How many steps? ")
                rotate(float(delay) / 1000.0, int(steps))
        except KeyboardInterrupt:
            off()

