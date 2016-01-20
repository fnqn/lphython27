#!/usr/bin/env python
# -*- coding: utf-8 -*-
# alarm_clock.py

# Description: A simple Python program to make the computer act
# like an alarm clock. Start it running from the command line
# with a command line argument specifying the duration in seconds
# after which to sound the alarm. It will sleep for that long,
# and then beep a few times. Use a duration of 0 to test the
# alarm immediiately, e.g. for checking that the volume is okay.

# Author: Vasudev Ram - http://www.dancingbison.com

import sys
import string
from time import sleep

sa = sys.argv
lsa = len(sys.argv)
if lsa != 2:
    print "Usage: [ python ] alarm_clock.py duration_in_seconds"
    print "Example: [ python ] alarm_clock.py 10"
    print "Use a value of 0 seconds for testing the alarm immediately."
    print "Beeps a few times after the duration is over."
    print "Press Ctrl-C to terminate the alarm clock early."
    sys.exit(1)

try:
    seconds = int(sa[1])
except ValueError:
    print "Invalid numeric value (%s) for seconds" % sa[1]
    print "Should be an integer >= 0"
    sys.exit(1)

if seconds < 0:
    print "Invalid value for seconds, should be >= 0"
    sys.exit(1)

seconds = seconds * 60

if seconds == 1:
    unit_word = " minute"
else:
    unit_word = " seconds"

try:
    if seconds > 0:
        print "Sleeping for " + str(seconds) + unit_word
        sleep(seconds)
    print "Wake up"
    for i in range(5):
        print chr(7),
        sleep(1)
except KeyboardInterrupt:
    print "Interrupted by user"
    sys.exit(1)

# EOF