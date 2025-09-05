import RPi.GPIO as GPIO

ledPin = 17  # define ledPin
buttonPin = 27  # define buttonPin

def setup():
    GPIO.setmode(GPIO.BCM)  # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)  # set ledPin to OUTPUT mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set buttonPin to PULL UP INPUT mode

def loop():
    prev_state = None  # Track previous LED state
    while True:
        current_state = GPIO.input(buttonPin) == GPIO.LOW  # True if button pressed, False otherwise
        if current_state != prev_state:  # Only act on state change
            if current_state:  # Button is pressed
                GPIO.output(ledPin, GPIO.HIGH)  # turn on led
                print('led turned on >>>')
            else:  # Button is released
                GPIO.output(ledPin, GPIO.LOW)  # turn off led
                print('led turned off <<<')
            prev_state = current_state  # Update previous state

def destroy():
    GPIO.output(ledPin, GPIO.LOW)  # turn off led
    GPIO.cleanup()  # Release GPIO resource

if __name__ == '__main__':  # Program entrance
    print('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program
        destroy()