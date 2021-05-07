#!/usr/bin/env python
#-*- coding: utf-8 -*-

from importlib import reload
from datetime import datetime
from subprocess import call
import time, cancelIt, subprocess, sys, os

wantToCancel = None
isRunningPath = '/home/aedigo/.local/share/pomodoro/isrunning'

if sys.argv[1] == 'cancel':
    wantToCancel = True
else:
    wantToCancel = False

def sendmessage(message):
    subprocess.Popen(['notify-send.sh', message])
    return

def play_sound(path, time):
    call(['aplay', '-d', str(time), path])
    return

def canceling(state):
    f = open('/home/aedigo/.bin/python/cancelIt.py', 'w')
    f.write('cancel=' + str(state))
    f.close()

if os.path.isfile(isRunningPath):
    if wantToCancel:
        os.remove('/home/aedigo/.local/share/pomodoro/isrunning')
        canceling(True)
        exit()
    else:
        sendmessage('Is running!')
        exit()

else:
    if wantToCancel:
        sendmessage('Not running!')
        canceling(False)
        exit()
    f = open(isRunningPath, 'w')
    f.close()
    sendmessage('Pomodoro started')
            
current_time = None

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
    newSecond = second
    bothMinutes = int(minute) + int(newMinute[0])
    newHour = hour
    if bothMinutes >= 60:
        newHour = int(newHour) + 1
        alteratedMinute = bothMinutes - 60
        if len(str(newHour)) == 1:
            newHour = isMissingZero(newHour)
        if len(str(alteratedMinute)) == 1:
            alteratedMinute = isMissingZero(alteratedMinute)
            print(alteratedMinute)
        if len(str(newSecond)) == 1:
            newSecond = isMissingZero(newSecond)
        return [newHour, alteratedMinute, newSecond]

    if len(str(newSecond)) == 1:
        newSecond = isMissingZero(newSecond)
        return [newHour, bothMinutes, newSecond]

    return [newHour, bothMinutes, newSecond]

def notUnder60(newMinute):
    if minute >= 60:
        alteratedMinute = newMinute - 60
        return alteratedMinute
    
pomodoro = get_hour(25)
playingAround = get_hour(5)

play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-start.wav', 1)

print(cancelIt.cancel, current_time != pomodoro)
while current_time != pomodoro and not cancelIt.cancel:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if playingAround == current_time:
        sendmessage('JUST DO IT!!!')
        play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-running.wav', 1)

    print(current_time, pomodoro, playingAround)
    time.sleep(1)
    reload(cancelIt)
else:
    if cancelIt.cancel:
        sendmessage('Pomodoro has been canceled!')
    else:
        sendmessage('Done! Good Work!')
    play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-end.wav', 3)
    os.remove('/home/aedigo/.local/share/pomodoro/isrunning')
    canceling(False)

