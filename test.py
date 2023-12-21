from time import sleep
import controler as py

# Set the board mode
py.pinOut('BOARD')


# Create and reset a new servo
#   servoPin = 11
#   servo = py.newPWM(servoPin, 50)
#   py.resetPWM(servo)

# Move the servo to 90 degrees
#   py.moveServo(servo, servoPin, 90)

# Create and reset a new motor
motorPin = 12
motor = py.newPWM(motorPin, 10)

py.resetPWM(motor)

py.motorStart(motor, motorPin)

py.motorSpeed(motor, 10)
sleep(10)

py.motorStop(motor, motorPin)


# Cleanup
#   py.closePWM(servo)
py.closePWM(motor)
