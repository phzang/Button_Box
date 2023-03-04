# Flight Simulator Control Box
Python and Arduino code to make my Microsoft Flight Simulator (MSFS) and X-Plane 11 flight simulator control box work.  

Box is comprised of a Mega 2560 R3 (for dials and buttons) and Zero Delay USB Encoder (for switches).
Ardino sends a single byte representing the state of the rotary encoders (left, right, push, release) and buttons (push, release).
Python converts byte to Simconnect command to MSFS.
