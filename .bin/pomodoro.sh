#!/bin/bash

if [[ $1 = 'start' ]]
then
  cp -f ~/.bin/python/start.py ~/.bin/python/pomoCancel.py 
  python ~/.bin/python/pomodoro.py &
elif [[ $1 = 'cancel' ]]
then
  cp -f ~/.bin/python/cancel.py ~/.bin/python/pomoCancel.py
fi
