import sys
from setraw import setRaw

def convertValue(isLeftMotor, vecValOrNone):
    if vecValOrNone is None:
        return None
    else:
        vecVal = vecValOrNone
    
    neutralVal = 1465 if isLeftMotor else 1455
    maxForwardAdd = 250 if isLeftMotor else -250
    maxBackwardAdd = -250 if isLeftMotor else 250

    valIsForward = (vecVal > 0)
    if valIsForward:
        multiplier = vecVal
        toAdd = maxForwardAdd * multiplier
    else:
        multiplier = -vecVal
        toAdd = maxBackwardAdd * multiplier
    
    finalVal = neutralVal + toAdd
    return finalVal

def main():
    if len(sys.argv) != 3:
        print("needs 2 args")
        return
    
    vals = [
        convertValue(True, float(sys.argv[1])),
        convertValue(False, float(sys.argv[2]))
    ]
    
    setRaw(vals)

if __name__ == '__main__':
    main()