# Update 2024.11

Just looked around and found 3 different folders for this project. I guess I shouldn't be surprised for what must by now be a 10 year old project, touched perhaps 3 or 4 times!

Anyway, I've put them all in the same repo and (for now) into their own subfolders in old-stuff/. To roughly describe their contents:
* bankbot-driver: code related to the most recent version of the bot, the bankbot. Has tools for command line control and a (likely outdated and trashable) script related to web control.
* dmr-networking: stuff much more related to the website and server.
* old-stuff: who the fuck knows. Probably nothing relevant in here for going forward. But better to keep it just in case.

The first two on those list share some redundant files.

I suppose one of the things I'll be doing is merging these into a common/ folder... and probably then making some new folder(s) for my current stint of work on this project.

Anyway, here's some more commentary on the code I found.

## bankbot-driver/

Okay, digging into this project now in late 2024, at Lift, after 3 years (!!) of hibernation. Gonna try to get an overview of the project and make notes here.

(the following applies to the effectively-archived `old_scripts/`).

### syncfromm, syncto

Shell scripts to aid in sending files back and forth between the pc and the Pi. Will need to adjust the hardcoded ip address.

### d and stopdrive

shell scripts to make calling underlying `stopdrive.py` and `setdrive.py` easier and faster to type.

`./d L R` where L and R are floats betweee -1 and 1, or just `./stopdrive`

### Command-line Script Structure

`drive_from_remote_input` sits at the top of the import hierarchy, but is not actually meant to be modified per bot. This file (iirc!) should be kept the same across bots - only changed if the control system thinking itself changes.

It imports `bot_driver`, and expects to find the functions `setup()`, `close()`, and `enactInput(inputState)`. The last of these is expected to know how to turn the *generic* inputState (generic in the sense that it is "some json structure with info on how to control this specific bot, which came from an interface program specific to it") into *specific* commands for the robot.

In the case of the bankbot, that is done by calling `setDrive` from th emodule `setdrive`, which (at the time of writing, but probably will change asap) uses some hardcoded values to turn (I think?) a float (-1 to 1) into an integer value meant to be sent directly to the motors.

`setRaw` from `setraw` does this by using `driver`, which looks like something copy-pasted from somewhere, and knows how to use the underlying library to operate servo motors via the Pi Servo Shield.

### Web control

`serve_websocket.py` confuses me... It doesn't look like it's handling an `enactInput` json structure as described above...?

## dmr-networking/

server/ has a basic php webpage, which modifies a server_input.json, and a serve_input_requests.py, which looks for this and serves requests from named bots for input. Probably a decent seed for building the next version of the webserver.

client/ has what seems to be a template "starter project" for getting another bot onboarded with our control system here. This should be a good place to start but we should first compare the `drive_from_remote_input.py` files contents from here, from `/bankbot-driver/scripts/`, and from `old-stuff/botbrain/`. Hopefully they're identical; if not try to figure out which one is latest/best - and while you're at it you should probably delete duplicates.

# Next Steps?

As of right now, I have yet to merge the various org/ files of the repos. I'm going to start a next-steps.md and bs.md there now; meet me there!