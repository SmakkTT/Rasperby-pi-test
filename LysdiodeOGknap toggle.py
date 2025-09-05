import RPi.GPIO as GPIO
import time

ledPin = 17  # define ledPin
buttonPin = 27  # define buttonPin

def setup():
    GPIO.setmode(GPIO.BCM)  # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)  # set ledPin to OUTPUT mode
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # set buttonPin to PULL UP INPUT mode
    GPIO.output(ledPin, GPIO.HIGH)  # Start with LED on

def loop():
    led_state = True  # Track LED state (True = on, False = off)
    prev_button_state = GPIO.HIGH  # Track previous button state (HIGH = released due to pull-up)
    
    while True:
        current_button_state = GPIO.input(buttonPin)  # Read current button state
        if prev_button_state == GPIO.HIGH and current_button_state == GPIO.LOW:  # Detect button press (HIGH to LOW transition)
            led_state = not led_state  # Toggle LED state
            GPIO.output(ledPin, GPIO.HIGH if led_state else GPIO.LOW)  # Update LED
            print('led turned ' + ('on >>>' if led_state else 'off <<<'))
            time.sleep(0.2)  # Debounce delay to avoid multiple toggles
        prev_button_state = current_button_state  # Update previous button state
        time.sleep(0.01)  # Small delay to reduce CPU usage

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