# Update 2024.11

Okay, digging into this project now in late 2024, at Lift, after 3 years (!!) of hibernation. Gonna try to get an overview of the project and make notes here.

## syncfromm, syncto

Shell scripts to aid in sending files back and forth between the pc and the Pi. Will need to adjust the hardcoded ip address.

## d and stopdrive

shell scripts to make calling underlying `stopdrive.py` and `setdrive.py` easier and faster to type.

`./d L R` where L and R are floats betweee -1 and 1, or just `./stopdrive`

## Python Script Structure

`drive_from_remote_input` sits at the top of the import hierarchy, but is not actually meant to be modified per bot. This file (iirc!) should be kept the same across bots - only changed if the control system thinking itself changes.

It imports `bot_driver`, and expects to find the functions `setup()`, `close()`, and `enactInput(inputState)`. The last of these is expected to know how to turn the *generic* inputState (generic in the sense that it is "some json structure with info on how to control this specific bot, which came from an interface program specific to it") into *specific* commands for the robot.

In the case of the bankbot, that is done by calling `setDrive` from th emodule `setdrive`, which (at the time of writing, but probably will change asap) uses some hardcoded values to turn (I think?) a float (-1 to 1) into an integer value meant to be sent directly to the motors.

`setRaw` from `setraw` does this by using `driver`, which looks like something copy-pasted from somewhere, and knows how to use the underlying library to operate servo motors via the Pi Servo Shield.