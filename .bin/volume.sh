#! /bin/bash

# Deal with notification
function notifaction() {
# This will give me the status of alsa volume
  volumePercentage=$(amixer sget Master | grep 'Right:' | awk -F'[][]' '{ print $2 }')
  notify-send.sh --replace-file=/tmp/volumenotification "$volumePercentage" --expire-time=800
}

# Deal with the volume
function volume() {
  if [[ "$1" = "down" ]]
  then
    sh -c "pactl set-sink-mute @DEFAULT_SINK@ false ; pactl set-sink-volume @DEFAULT_SINK@ -2%"
    notifaction
  fi

  if [[ "$1" = "up" ]]
  then
    sh -c "pactl set-sink-mute @DEFAULT_SINK@ false ; pactl set-sink-volume @DEFAULT_SINK@ +2%"
    notifaction
  fi
}

volume "$1"
