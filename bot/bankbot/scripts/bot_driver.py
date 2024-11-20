from time import sleep

import setraw

botID = "bankbot"

def wheelValIsValid(wheelVal):
    try:
        return wheelVal >= 0 and wheelVal < 4096
    except:
        return False

def setup():
    pass

def close():
    pass

def enactInput(inputState):
    if not (wheelValIsValid(inputState['left_wheel']) and wheelValIsValid(inputState['right_wheel'])):
        raise ValueError("wheel vals out of acceptable range")
        
    setraw.setRaw([inputState['left_wheel'], inputState['right_wheel']])
