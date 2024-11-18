# Install/setup Janus

Go [here](https://groups.google.com/forum/#!topic/meetecho-janus/RYP4FBaeUi0), follow instructions.

Install libstpt  v1.2 or 1.5. Ctrl+f [here](https://github.com/meetecho/janus-gateway) for 'libsrtp' for more.

I needed to install extra dependencies, which I found relatively quickly by googling; they should still be in bookmarks under "dmr resources / install janus".

In the above instructions, some config files will be generated. Find this directory of config files (maybe `/opt/janus/etc/janus`), and overwrite the existing janus.pluging.streaming.jcfg with the one in this folder (this adds a stream ID which is compatible with the streaming cmd from the pi).

Copy the folder janus-dir/html to a location apache can serve from, and load the "streaming" demo.

Then run Janus with these configs via:

`./janus -F [/dir/to/janus/configs/]`

# Install gstreamer

Well...
This link is for gstreamer 1.18 which was not on my pi. But it did get me most of the way through the install/setup.
https://qengineering.eu/install-gstreamer-1.18-on-raspberry-pi-4.html
So maybe do this one first?

Then I found this, which seems to be aimed at the version I have on the pi (1.14), and focuses specifically on getting rpicamsrc working with gstreamer
https://hoani.net/posts/guides/2021-10-22-gstreamerRPiStreaming/

I also had to run quite a few other installs, by googling around reacting to missing packages. Some of these were:
`sudo apt-get install gstreamer1.0-plugins-bad gstreamer1.0-plugins-bad`

# Send the stream

Run this cmd on the Pi with the camera plugged in:

`gst-launch-1.0 rpicamsrc bitrate=1000000 ! 'video/x-h264,width=640,height=480' ! h264parse ! rtph264pay config-interval=1 pt=96 ! udpsink host=[janus host ip address] port=8088` (that port was set with the overwritten config file)

# Is it running?

That streaming command itself won't output much, but the terminal running the Janus server should mention a new "\[from-the-pi\]" vid stream.

In the streaming demo, the stream list should now show the pi's stream. Select and run it. You should see the stream from the camera!