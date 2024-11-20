from time import sleep

import setraw

botID = "bankbot"

SERVO_LOW_VAL = 10
SERVO_HIGH_VAL = 4095

def wheelValIsValid(wheelVal):
    try:
        return wheelVal >= 0 and wheelVal <= 1
    except:
        return False

def translateVal(inputVal):
    translated = inputVal * (SERVO_HIGH_VAL - SERVO_LOW_VAL) + SERVO_LOW_VAL
    # print(translated)
    return translated

def setup():
    pass

def close():
    pass

def enactInput(inputState):
    if not (wheelValIsValid(inputState['left_wheel']) and wheelValIsValid(inputState['right_wheel'])):
        raise ValueError("wheel vals out of acceptable range ({SERVO_LOW_VAL} - {SERVO_HIGH_VAL})")
    
    setraw.setRaw([translateVal(inputState['left_wheel']), translateVal(inputState['right_wheel'])])
