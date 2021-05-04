#!/usr/bin/env python
#-*- coding: utf-8 -*-

from importlib import reload
from datetime import datetime
from subprocess import call
import time, pomoCancel, subprocess, simpleaudio as sa

def sendmessage(message):
    subprocess.Popen(['notify-send.sh', message])
    return

def play_sound(path, time):
    call(['aplay', '-d', str(time), path])
    return

hour = datetime.now().hour
minute = datetime.now().minute + 25
alternativeMinute = datetime.now().minute + 5
second = datetime.now().second
current_time = None

pomodoro = None

if minute >= 60:
    alter = minute - 60
    newMinute = alter
    newSecond = second
    if len(str(newMinute)) == 1:
       newMinute = '0' + str(alter)
    elif len(str(newSecond)) == 1:
       newSecond = '0' + str(newSecond)
    newHour = hour + 1
    pomodoro = str(newHour) + ':' + str(newMinute) + ':' + str(newSecond)
else:
    pomodoro = str(hour) + ':' + str(minute) + ':' + str(second)

sendmessage('Pomodoro')
play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-start.wav', 1)
while current_time != pomodoro and not pomoCancel.cancel():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    playingAround = str(hour) + ':' + str(alternativeMinute) + ':' + str(second)

    if playingAround == current_time:
        sendmessage('JUST DO IT!!!')
        play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-running.wav', 1)

    print(current_time, pomodoro)
    time.sleep(1)
    reload(pomoCancel)
else:
    sendmessage('Done! Good Work!')
    play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-end.wav', 3)

