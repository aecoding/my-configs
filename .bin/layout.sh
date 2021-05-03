#!/bin/bash
usbkdb=`xkb-switch`

function setLayout() {
  setxkbmap "$@"
  xmodmap ~/.Xmodmap
}

if [[ $usbkdb = 'br' ]]
then 
  setLayout br nodeadkeys &
  notify-send.sh "nodeadkeys" --expire-time=800 &
else
  setLayout br &
  notify-send.sh "br" --expire-time=800 &
fi


