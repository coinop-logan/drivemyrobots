# Drive My Robots

Drive them. I'll help!

## State of the Project - 2024.11.25

Currently, a lot of this works in bits and pieces and with some caveats.

### For motor control from server:

#### Server:

1. Use the AWS security group for the bots project. Or just look through and open up the obvious ports in whatever cloud server solution.
2. Upload `web/backend/scripts/` and `web/backend/input_state.json` to the server
3. Run `python3 serve_input_requests.py 0.0.0.0 4546`

For camera control, see `bot/test_cam_servo.py`.

#### Setup the Pi

1. Ensure bot/bankbot/scripts/ is in the current Pi
2. Call `python3 drive_from_remote_input.py [SERVER IP] 4546`

Then just modify `input_state.json` in the server and watch the bot do its thang
I think the mid values are around 0.35 ... for one motor, higher vals means forward; the other motor is the opposite.

### Camera streaming:

I was able to get streaming from the pi to another pc on the local network working for some definition of the word.

This involved some command that I don't have access to now (the pi is at home), but should be in recent-ish command history;
and using VLC's "open remote stream" tool (or sth).

I didn't test sending it out of the local network, but that should work the same (albeit with a bit more lag probs) as long as ports are opened and forwarded correctly.

But! There was about 1.5 seconds of lag, which is pretty unacceptable.

# Next steps

## Reduce Camera Lag

This will probably involve intensive research into "ultra low latency" video streaming techniques. But who knows, maybe there is a low hanging fruit somewhere - in the form possibly of flags sent to the gstreamer (or whatever) command that the Pi uses.

Until camera lag is drastically reduced, nothing else really matters.

## Web Frontend

Now that the Pi can easily "listen to" the server's `input_state.json`, all we need to extend control to the frontend is just a webpage that calls (say) a PHP file (see `frontend/index.php`) that can edit this file on the server.

There is a sketch design of what this could look like, including camera controls, in your notecard organizer / mobile office thingy.