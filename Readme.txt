Very simple script to set the color of a Dell G5 5000 front stripe LED

python3 led.py red
python3 led.py off

requires pyusb - pip install pyusb

I use it from systemd to turn it off at startup.
A useful source of learning about the mysterious controller - it's not
like other AlienWare LED controllers as seen by OpenRGB.

For OpenRgb, the platform_id is 0x0901 - one zone. Uncomment the 'print'
in elc_ng.py to see what is sent to the controller. 

I mentioned this in this thread
https://gitlab.com/CalcProgrammer1/OpenRGB/-/issues/2507

-Cecil Coupe, Feb 15, 2023

From:
https://gist.github.com/Cheaterman/2d166b510adc5eb9d582eaa83282c410
and
https://gist.github.com/Cheaterman/accd912c6886f4055f45d0594b88553c

Found in this discussion
https://github.com/rsm-gh/akbl/issues/74
