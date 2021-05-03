#!/bin/bash
redshift &
nm-applet &
xmodmap ~/.Xmodmap &
dunst &
nitrogen --restore &
picom --experimental-backend &
conky &
betterlockscreen -u ~/Documents/Wallpapers/Forest_fog_deer.jpg &
xidlehook --not-when-fullscreen --not-when-audio --timer 300 'betterlockscreen -l' '' &
searxStart &

