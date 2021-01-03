import sys
import driver

def main():
    if len(sys.argv) == 1:
        print("need more args")
        return
    
    for i in range(len(sys.argv)):
        int(i) # crash here if we can't convert all values
    
    pwm = driver.makePwm()
    
    for i in range(len(sys.argv) - 1):
        val = int(sys.argv[i + 1])
        pwm.setServoPulse(i, val)

main()