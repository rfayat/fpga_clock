"""Tools for handling a fpga clock

Author: Romain Fayat, May 2021
"""
import RPi.GPIO as GPIO
import time
from functools import wraps

# Default pins for the raspberry (BCM numbering)
ENABLE_PIN = 23
RESET_PIN = 24


class Clock_Handler():
    "Object handling the communication with the FPGA"

    def add_verbose_message(message=""):
        "Method decorator for adding a message if self.verbose is True"
        def decorator(f):
            @wraps(f)
            def decorated(self, *args, **kwargs):
                if self.verbose:
                    print(message)
                return f(self, *args, **kwargs)
            return decorated
        return decorator

    def __init__(self, enable_pin=ENABLE_PIN, reset_pin=RESET_PIN,
                 verbose=False):
        "Instantiate the object and take care of GPIO setup"
        self.verbose = verbose
        self.enable_pin = enable_pin
        self.reset_pin = reset_pin
        self.setup_gpio()

    @add_verbose_message("Setting up pins")
    def setup_gpio(self):
        "Setup of the gpio pins"
        GPIO.setwarnings(False)
        # Use BCM pin numbering
        GPIO.setmode(GPIO.BCM)
        # Set the enable pin as an output on low
        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.output(self.enable_pin, GPIO.LOW)
        # Set the reset pin as an output on low after a brief pulse
        GPIO.setup(self.reset_pin, GPIO.OUT)
        self.reset()

    @add_verbose_message("Resetting pins")
    def reset(self, reset_pulse_duration=.1):
        "Send a pulse of reset_pulse_duration seconds of on the reset pin"
        GPIO.output(self.reset_pin, GPIO.HIGH)
        time.sleep(reset_pulse_duration)
        GPIO.output(self.reset_pin, GPIO.LOW)

    @property
    def enable_state(self):
        "Return the state of the enable pin (False for low, True for high)"
        return GPIO.input(self.enable_pin)

    @add_verbose_message("Resetting and setting enable pin to high")
    def enable(self):
        "Change the state of the enable pin to high"
        GPIO.output(self.reset_pin, GPIO.HIGH)
        GPIO.output(self.enable_pin, GPIO.HIGH)
        time.sleep(1e-6)
        GPIO.output(self.reset_pin, GPIO.LOW)


    @add_verbose_message("Setting enable pin to low")
    def disable(self):
        "Change the state of the enable pin to low"
        GPIO.output(self.enable_pin, GPIO.LOW)

    @add_verbose_message("Cleaning up")
    def cleanup(self):
        "Clean up the GPIOs"
        self.disable()
        self.reset()
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        handler = Clock_Handler(verbose=True)
        time.sleep(1.)

        for _ in range(4):
            handler.enable()
            time.sleep(3.)
            handler.disable()
            time.sleep(1.)
        time.sleep(2.)
    finally:
        handler.cleanup()
