import RPi.GPIO as GPIO
from time import sleep
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("moveDur", help="Duration of halfcycle in seconds",type=int)
args = parser.parse_args()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(27,GPIO.OUT,initial=GPIO.HIGH)
print('move {0:d}s'.format(args.moveDur))
GPIO.output(17,GPIO.LOW)
sleep(args.moveDur)
GPIO.output(17,GPIO.HIGH)
print('done')
GPIO.cleanup()
