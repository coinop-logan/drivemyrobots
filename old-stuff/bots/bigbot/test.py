# 0 - 0xff (header)
# 1 - 0xfe (header)
# 2 - leftVal
# 3 - leftVal
# 4 - rightVal
# 5 - rightVal
# 6 - sum of bytes 0-5
# 7 - sum of bytes 0-5

import serial
from time import sleep
import struct

ser = serial.Serial ("/dev/ttyS0", 19200)

def makeCmd(leftVal, rightVal):
    headers = bytearray.fromhex("fffe")

    packedVals = struct.pack("<hh",leftVal,rightVal)

    hackedVals = b''+packedVals[1]+packedVals[0]+packedVals[3]+packedVals[2]

    packedCmd = headers + hackedVals

    toSum = struct.unpack("<BBBBBB",packedCmd)
    total = 0
    for val in toSum:
        total += val
    
    packedChecksum = struct.pack("<H", total)

    hackedChecksum = b''+packedChecksum[1]+packedChecksum[0]

    packedCmdWithChecksum = packedCmd + hackedChecksum

    print(packedCmdWithChecksum)
    return packedCmdWithChecksum

def clamp(x):
    return max(min(x,1.0),-1.0)

def enactInput(inputState):
    left = int(clamp(inputState['left_wheel']) * 100.0)
    right = int(clamp(inputState['right_wheel']) * 100.0)
    print(left,right)
    cmd = makeCmd(left,right)
    ser.write(cmd)