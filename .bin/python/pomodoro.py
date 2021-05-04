#!/usr/bin/env python
#-*- coding: utf-8 -*-

from importlib import reload
from datetime import datetime
from subprocess import call
import time, pomoCancel, subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send.sh', message])
    return

def play_sound(path, time):
    call(['aplay', '-d', str(time), path])
    return

def get_hour(*newMinute):
    hour = datetime.now().hour
    minute = datetime.now().minute
    second = datetime.now().second
    if len(str(hour)) == 1:
     hour = isMissingZero(hour)
    elif len(str(minute)) == 1:
     minute = isMissingZero(minute)
    elif len(str(second)) == 1:
     second = isMissingZero(second)
    if newMinute:
        toFormat = add_time(hour, minute, newMinute, second)
        return format_time(toFormat[0], toFormat[1], toFormat[2])
        
    if not newMinute:
     return format_time(hour, minute, second)

def isMissingZero(time):
    newTime = '0' + str(time)
    return newTime

def format_time(hour, minute, second):
    formated_time = str(hour) + ':' + str(minute) + ':' + str(second)
    return formated_time

def add_time(hour, minute, newMinute, second):
    bothMinutes = minute + newMinute[0]
    if bothMinutes >= 60:
        newHour = hour + 1
        alteratedMinute = bothMinutes - 60
        if len(str(newHour)) == 1:
            newHour = isMissingZero(newHour)
        elif len(str(alteratedMinute)) == 1:
            alteratedMinute = isMissingZero(alteratedMinute)
        return [newHour, alteratedMinute, second]
    return [hour, bothMinutes, second]
    

def notUnder60(newMinute):
    if minute >= 60:
        alteratedMinute = newMinute - 60
        return alteratedMinute
    

hour = datetime.now().hour
minute = datetime.now().minute + 25
alternativeMinute = datetime.now().minute + 15
newPlayingHour = None
newPlayingSecond = None
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

if alternativeMinute >= 60:
    alternativeMinute = alternativeMinute - 60
    newPlayingHour = hour + 1
    newPlayingSecond = second
    if len(str(alternativeMinute)) == 1:
       alternativeMinute = '0' + str(alternativeMinute)
    elif len(str(newPlayingSecond)) == 1:
        newPlayingSecond = '0' + str(second)
else:
    newPlayingHour = hour
    newPlayingSecond = second

sendmessage('Pomodoro')
play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-start.wav', 1)
playingAround = get_hour(5)
while current_time != pomodoro and not pomoCancel.cancel():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    #playingAround = str(newPlayingHour) + ':' + str(alternativeMinute) + ':' + str(newPlayingSecond)

    if playingAround == current_time:
        sendmessage('JUST DO IT!!!')
        play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-running.wav', 1)

    print(playingAround, current_time)
    time.sleep(1)
    reload(pomoCancel)
else:
    sendmessage('Done! Good Work!')
    play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-end.wav', 3)

