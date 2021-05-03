#!/bin/bash
service="sleep"

function playSound() {
  if [[ $2 = "time" ]] 
  then
    aplay ~/Documents/Musics/Pomodoro/$1.wav -d $3 &
  fi
  aplay ~/Documents/Musics/Pomodoro/$1.wav -d 1 &
}

function notification() {
  playSound $1
  if [[ $1 = "end" ]]
  then
    playSound pomo-end "time" 3
    zenity --warning --text="Good job! Now take some rest." &
    sleep 8 && bash ~/.bin/lock.sh 
  fi
}

function notify() {
  if [[ !$2 ]]
  then
    notify-send.sh --replace-file=/tmp/pomo $1 --expire-time=800
  fi
  notify-send.sh --replace-file=/tmp/pomo $1 --expire-time=$2
}

if [[ $1 = 'cancel' ]] 
then 
  var=$(pidof $service)
  notify 'Pomodoro canceled'
  notification pomo-cancel
  kill $var
  exit 1
fi

if pgrep -x "$service" 
then 
  notify 'Is already running!'
  notification pomo-running
else 
  notification pomo-start
  notify 'Started!'
  sleep 1200 && notification "end" 
fi


