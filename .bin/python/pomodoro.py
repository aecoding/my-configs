#!/usr/bin/env python
#-*- coding: utf-8 -*-
from subprocess import call
import time, subprocess, sys, os, json 

import socket



homedir = os.environ['HOME']
configPath = homedir + '/.config/pomopy.json'

def play_sound(path, time):
    call(['aplay', '-d', str(time), path])
    return

def sendmessage(message):
    subprocess.Popen(['notify-send.py', '--replaces-id', '1', '--replaces-process', '1', '-u', 'critical', message])
    return

class AppMutex:
    """
    Class serves as single instance mutex handler (My application can be run only once).
    It use OS default property where single UDP port can be bind only once at time.
    """

    @staticmethod
    def enable():
        """
        By calling this you bind UDP connection on specified port.
        If binding fails then port is already opened from somewhere else.
        """
        
        try:
            AppMutex.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
            AppMutex.sock.bind(("127.0.0.1", 40000))
        except OSError:
            raise Exception("Application can be run only once.") and sendmessage('Running!!')

AppMutex.enable()

def user_config():
    with open(configPath) as json_data_file:
        data = json.load(json_data_file)
        return data

def save_user_settings(*args):
    with open(configPath, 'w') as tosave:
        json.dump(args[0], tosave, indent=4)

def default_user_config():
    config = {}
    config['active'] = False
    config['canceling'] = False
    config['pomodoro'] = 25
    config['leisure'] = True
    config['leisure_time'] = 5
    config['revision_time'] = 10
    return config

def create_user_config(*args):
    config = {}
    for x, y in user_config().items():
        config[x] = y

    if len(args):
        for x in args:
            config[x[0]] = x[1]
    else:
        print('Need two arguments.')
        exit()
    os.remove(configPath)
    save_user_settings(config)
    return config

try:
    with open(configPath) as f:
        data = user_config()
        if sys.argv[1] != 'cancel':
            if data['active']:
                sendmessage('Is running!')
                exit()
except FileNotFoundError:
    with open(configPath, 'w') as outfile:
        json.dump(default_user_config(), outfile, indent=4)

if sys.argv[1] == 'cancel':
    if user_config()['active']:
        create_user_config(['canceling', True])
        exit()
    else:
        sendmessage('Not active!')
        play_sound('/home/aedigo/Documents/Musics/Pomodoro/cancel-while-inactive.wav', 1)
        exit()
else:
    create_user_config(['active', True])
    sendmessage('Pomodoro Started!')
    play_sound('/home/aedigo/Documents/Musics/Pomodoro/start.wav', 1)

pomodoro_counter = None
free_time = None
content_revision = None

with open(configPath) as json_data_file:
    data = json.load(json_data_file)
    pomodoro_counter=data['pomodoro'] * 60
    free_time=pomodoro_counter - (data['leisure_time'] * 60)
    if sys.argv[1] == 'revision':
        content_revision= pomodoro_counter - (data['revision_time'] * 60)

while pomodoro_counter != 0:
    if user_config()['canceling']:
        sendmessage('Pomodoro has been canceled!')
        play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-running.wav', 1)
        create_user_config(['canceling', False], ['active', False])
        break;

    pomodoro_counter = pomodoro_counter -1
    if pomodoro_counter == free_time:
        sendmessage('Focus Time!')
        play_sound('/home/aedigo/Documents/Musics/Pomodoro/pomo-start.wav', 1)

    if content_revision:
        if content_revision == pomodoro_counter:
            sendmessage('Revision Time!')
    time.sleep(1)
else:
    sendmessage('Done! Good Work!')
    play_sound('/home/aedigo/Documents/Musics/Pomodoro/end.wav', 3)
    create_user_config(['active', False])
    subprocess.Popen(['lockIt'])

