from time import sleep

import setdrive

botID = "bankbot"

def setup():
    pass

def close():
    pass

def enactInput(inputState):
    setdrive.setDrive(inputState['left_wheel'], inputState['right_wheel'])
