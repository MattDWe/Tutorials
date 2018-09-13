"""
Project From Automate The Boring Stuff Chapter 15
Project: Countdown Program
Github: MattDWe

Program is to countdown from 60 seconds while playing a sound at the end of the countdown.
"""

import time, subprocess

timeLeft = 60
while timeLeft > 58:
    print(timeLeft, end="")
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(["start", "alarm.wav"], shell=True)
