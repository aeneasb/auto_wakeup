import RPi.GPIO as GPIO
import time
from time import sleep
class Move():
    '''
    Move-class with multiple move methods 
    Args:
        configFile: .json file with hardware parameters
	mode: chill, normal, rush
    Returns:
        Move object
    '''
    def __init__ (self,configFile,mode):
        # Hardware settings
        self.moveUpPin = int(configFile.get('moveUpPin',0))
        self.moveDownPin = int(configFile.get('moveDownPin',0))
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.moveUpPin,GPIO.OUT,initial=GPIO.HIGH)
        GPIO.setup(self.moveDownPin,GPIO.OUT,initial=GPIO.HIGH)
        # mode settings
        self.mode = mode
        self.moveDur = int(configFile.get('moveDur',0))
        self.snoozeDur = int(configFile.get('snoozeDur',0))
        self.shakeDur = int(configFile.get('shakeDur',0))
    def trigger(self):
        if self.mode == "chill":
            self.chill()
        elif self.mode == "normal":
            self.normal()
        elif self.mode == "rush":
            self.rush()
    def normal(self):
        self.moveUp(self.moveDur)
    def chill(self):
        intervals = self.snoozeDur//60
        intervalDur = 6/intervals
        for i in range(intervals):
            self.moveUp(intervalDur)
            sleep(60)
        self.moveDown(5)
    def rush(self):
        timeout = time.time() + self.shakeDur
        while time.time() < timeout:
            self.moveUp(1)
            sleep(1)
            self.moveDown(1)
            sleep(1)
    def moveUp(self, dur):
        print("Move up!")
        GPIO.output(self.moveUpPin,GPIO.LOW)
        sleep(dur)
        GPIO.output(self.moveUpPin,GPIO.HIGH)
    def moveDown(self, dur):
        print("Move down!")
        GPIO.output(self.moveDownPin,GPIO.LOW)
        sleep(dur)
        GPIO.output(self.moveDownPin,GPIO.HIGH)
    def cleanup(self):
        GPIO.cleanup()
