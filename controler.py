import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

# sets the GPIO pins
def pinOut(mode):
    if mode == 'BOARD':
        GPIO.setmode(GPIO.BOARD)


# function to create a new pwm
def newPWM(pin, frequency):
    GPIO.setup(pin, GPIO.OUT)
    pwm = GPIO.PWM(pin, frequency)
    return pwm

# close the connection
def closePWM(pwm):
    pwm.stop()
    GPIO.cleanup()

# reset the dc
def resetPWM(pwm):
    pwm.start(0)


# set frequency
def pwmFq(pwm, fq):
    pwm.ChangeFrequency(fq)

# function to reset the pwm
def motorStop(pwm, pin):
    pwm.ChangeDutyCycle(0)
    GPIO.output(pin, False)

# function to start motor
def motorStart(pwm, pin):
    GPIO.output(pin, True)

# function to set the motor speed
def motorSpeed(pwm, speed):
    # need to find the correct equation
    pwm.ChangeFrequency(speed * 5)
    pwm.ChangeDutyCycle(speed)


# function to move the servo to a certain position
def moveServo(pwm, pin, angle):
    duty = angle / 18 + 2
    GPIO.output(pin, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(pin, False)
    pwm.ChangeDutyCycle(0)
