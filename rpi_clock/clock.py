"""Tools for handling a fpga clock

Author: Romain Fayat, May 2021
"""
import RPi.GPIO as GPIO
import time

# Default output pin for the raspberry
OUTPUT_PIN = 21  # BCM numbering


class Clock_Handler():
    "Object handling the communication with the FPGA"

    def __init__(self, output_pin=OUTPUT_PIN):
        "Instantiate the object and take care of GPIO setup"
        self.output_pin = output_pin
        self.setup_gpio()

    def setup_gpio(self):
        "Setup of the gpio pins"
        GPIO.setwarnings(False)
        # Use BCM pin numbering
        GPIO.setmode(GPIO.BCM)
        # Set the output pin as an output on low
        GPIO.setup(self.output_pin, GPIO.OUT)
        GPIO.output(self.output_pin, GPIO.LOW)

    @property
    def output_state(self):
        "Return the state of the output (False for low, True for high)"
        return GPIO.input(self.output_pin)

    def toggle_output(self):
        "Change the state of the output pin (e.g. low if it was high)"
        GPIO.output(self.output_pin, not self.output_state)

    def cleanup(self):
        "Clean up the GPIOs"
        GPIO.output(self.output_pin, GPIO.HIGH)
        GPIO.cleanup()

if __name__ == "__main__":
    handler = Clock_Handler()
    try:
        while True:
            time.sleep(3.)
            status_str = "high" if handler.output_state else "low"
            status_str_new = "low" if handler.output_state else "high"
            print(f"Was {status_str}, setting to {status_str_new}")
            handler.toggle_output()
    finally:
        handler.cleanup()
