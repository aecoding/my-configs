#!/bin/bash

killall tomato

nh() {
  nohup $1 >/dev/null 2>&1& 
}

nh tomato -t
notify-send 'Started'

