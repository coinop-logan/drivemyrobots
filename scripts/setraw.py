import sys
import driver

def main():
    if len(sys.argv) == 1:
        print("need more args")
        return
    
    valsOrNone = []
    for i in range(len(sys.argv) - 1):
        arg = sys.argv[i + 1]
        if arg.lower() == 'n':
            valsOrNone.append(None)
        else:
            valsOrNone.append(int(arg))
    
    pwm = driver.makePwm()
    
    for i in range(len(valsOrNone)):
        val = valsOrNone[i]
        
        if val is None:
            continue

        pwm.setServoPulse(i, val)

main()