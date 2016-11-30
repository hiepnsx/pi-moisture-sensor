#! /usr/bin/python
# python program to communicate with an MCP3008.
# Base Code written by seempie from instructables.com

# Import SpiDev wrapper and our sleep function
import spidev
import RPi.GPIO as GPIO
from time import sleep

RED=19
GREEN=13
BLUE=26
CURRENT=RED

# Establish SPI device on Bus 0,Device 0
spi = spidev.SpiDev()
spi.open(0,0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)
GPIO.output(BLUE, GPIO.LOW)

def toggleLED(CURRENT):
  GPIO.output(RED, GPIO.HIGH if CURRENT == RED else GPIO.LOW)
  GPIO.output(GREEN, GPIO.HIGH if CURRENT == GREEN else GPIO.LOW)
  GPIO.output(BLUE, GPIO.HIGH if CURRENT == BLUE else GPIO.LOW)

def getAdc(channel):
    #check valid channel
    if ((channel>7)or(channel<0)):
        return -1

    while True:
        # Perform SPI transaction and store returned bits in 'r'
        r = spi.xfer([1, (8+channel) << 4, 0])

        #Filter data bits from retruned bits
        adcOut = ((r[1]&3) << 8) + r[2]
        percent = 100 - int(round(adcOut/10.24))

        if(percent <= 20):
          CURRENT = RED
        elif(percent < 60):
          CURRENT = GREEN
        else:
          CURRENT = BLUE

        toggleLED(CURRENT)
        #print out 0-1023 value and percentage
        print "ADC Output: {0:4d} Percentage: {1:3}%".format (adcOut,percent)
        sleep(10)

if __name__ == '__main__':
    getAdc(0)
