from playsound import playsound
import time
import os
script_dir = os.path.dirname(__file__)
file_name = "Alarm-ringtone.mp3"
abs_sound_file_path = os.path.join(script_dir, file_name)
timeUnit = input(
    "Which Unit of time do you want to use? [0]Hours [1]Minutes [2]Seconds ")
timeIntervall = int(input("How long do you want to wait? (In whole numbers.)"))


def hoursInMinutes(hours):
    return hours * 60


def minutesInSeconds(minutes):
    return minutes * 60


if timeUnit == "0":
    timeIntervall = hoursInMinutes(minutesInSeconds(timeIntervall))
elif timeUnit == "1":
    timeIntervall = minutesInSeconds(timeIntervall)
time.sleep(timeIntervall)
playsound(abs_sound_file_path)
