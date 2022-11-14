# SPDX-FileCopyrightText: Copyright (c) 2022 Cedar Grove Maker Studios
#
# SPDX-License-Identifier: MIT
"""
`pyportal_failover.py`
================================================================================

Used after a fatal error to dim the display to keep the board cooler. Flashes
L13 (red LED) during a pre-reset delay. Microcontroller is reset after the delay.

pyportal_failover.py  2022-10-25 1.0.1  Cedar Grove Studios

* Author(s): JG for Cedar Grove Maker Studios
"""

# imports__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/CedarGroveStudios/Failover"


import board
import time
import microcontroller
import digitalio

DELAY = 20  # seconds

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

board.DISPLAY.brightness = 0.2  # Dim the REPL display to keep things cool

print("pyportal_failover: begin reset delay")
end_delay = time.monotonic() + DELAY
while time.monotonic() < end_delay:
    """Flash red LED during delay period."""
    time.sleep(0.5)
    led.value = not led.value

print("pyportal_failover: resetting microcontroller")
microcontroller.reset()
