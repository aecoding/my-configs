#!/usr/bin/env python
#-*- coding: utf-8 -*-
from subprocess import call
import time, subprocess, sys, os, json 

homedir = os.environ['HOME']
configPath = homedir + '/.config/pomopy.json'

def play_sound(path, time):
    call(['aplay', '-d', str(time), path])
    return

def sendmessage(message):
    subprocess.Popen(['notify-send.py', '--replaces-id', '1', '--replaces-process', '1', '-u', 'critical', message])
    return

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
    config['revision'] = False
    config['revision_time'] = 10
    config['melody_folder'] = ''
    config['start_melody'] = ''
    config['end_melody'] = ''
    config['focus_time_melody'] = ''
    config['revision_melody'] = ''
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
        print('Config file created at: ~/.config/pomopy.json')
        exit()


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

