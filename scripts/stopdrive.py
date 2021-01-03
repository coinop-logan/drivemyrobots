from driver import *

def main():
  pwm = makePwm()

  pwm.setServoPulse(0,1470)
  pwm.setServoPulse(1,1455)

main()
