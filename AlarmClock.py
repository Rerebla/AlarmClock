import time
from playsound import playsound
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
playsound('C:\\PythonProject\\MegaProjectList\\Numbers\\Alarm-ringtone.mp3')
