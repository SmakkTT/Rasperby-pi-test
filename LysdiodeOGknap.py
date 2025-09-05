import RPi.GPIO as GPIO


ledPin = 24 # define ledPin

buttonPin = 23 # define buttonPin


def setup():

    GPIO.setmode(GPIO.BCM) # use PHYSICAL GPIO Numbering

    GPIO.setup(ledPin, GPIO.OUT) # set ledPin to OUTPUT mode

    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set buttonPin to PULL UP INPUT mode


def loop():

    while True:

        if GPIO.input(buttonPin)==GPIO.LOW: # if button is pressed

            GPIO.output(ledPin,GPIO.HIGH) # turn on led

            print ('led turned on >>>') # print information on terminal

        else : # if button is relessed

            GPIO.output(ledPin,GPIO.LOW) # turn off led

            print ('led turned off <<<')


def destroy():

    GPIO.output(ledPin, GPIO.LOW) # turn off led

    GPIO.cleanup() # Release GPIO resource


if __name__ == '__main__': # Program entrance

    print ('Program is starting...')

    setup()

try:
    loop()
except KeyboardInterrupt: # Press ctrl-c to end the program.

    destroy()