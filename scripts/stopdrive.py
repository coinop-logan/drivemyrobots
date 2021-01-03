from driver import *

def main():
  pwm = makePwm()

  pwm.setServoPulse(0,1465)
  pwm.setServoPulse(1,1455)

main()
