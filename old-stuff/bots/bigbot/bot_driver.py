# 0 - 0xff (header)
# 1 - 0xfe (header)
# 2 - leftVal
# 3 - leftVal
# 4 - rightVal
# 5 - rightVal
# 6 - sum of bytes 0-5
# 7 - sum of bytes 0-5

import serial
import RPi.GPIO as GPIO
from time import sleep
import struct

ser = None
pwmServo = None

camServoPin = 5
servoDutyCycleRange = (3.0,9.0)

botID = "bigbot"

def setup():
    print("setting up")
    global ser
    global pwmServo
    ser = serial.Serial ("/dev/ttyS0", 19200)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(camServoPin, GPIO.OUT)
    
    pwmServo = GPIO.PWM(camServoPin, 50)
    pwmServo.start(camInputToDutyCycle(0.0))

def close():
    GPIO.cleanup()

def camInputToDutyCycle(x):
    sanitized = clamp(x)
    unitized = (sanitized+1)/2.0
    return (servoDutyCycleRange[1] - servoDutyCycleRange[0])*unitized + servoDutyCycleRange[0]

def enactCamInput(x):
    pwmServo.ChangeDutyCycle(camInputToDutyCycle(x))

def makeDriveCmd(leftVal, rightVal):
    headers = bytearray.fromhex("fffe")

    packedVals = struct.pack("<hh",leftVal,rightVal)

    hackedVals = bytearray([packedVals[1],packedVals[0],packedVals[3],packedVals[2]])

    packedCmd = headers + hackedVals

    toSum = struct.unpack("<BBBBBB",packedCmd)
    total = 0
    for val in toSum:
        total += val
    
    packedChecksum = struct.pack("<H", total)

    hackedChecksum = bytearray([packedChecksum[1],packedChecksum[0]])

    packedCmdWithChecksum = packedCmd + hackedChecksum

    return packedCmdWithChecksum

def clamp(x):
    return max(min(x,1.0),-1.0)

def enactInput(inputState):
    leftDrive = int(clamp(inputState['left_wheel']) * 200.0)
    rightDrive = int(clamp(inputState['right_wheel']) * 200.0)
    driveCmd = makeDriveCmd(leftDrive, rightDrive)

    ser.write(driveCmd)

    enactCamInput(inputState['cam_pos'])