#!/bin/bash
redshift &
safeeyes &
# I don't need to change or deal with the internet, so there's no need to have the applet
# nm-applet &
xmodmap ~/.Xmodmap &
# nitrogen --restore &
hsetroot -solid "#282828" &
xcape -e "Control_L=Escape" &
flashfocus &
picom --experimental-backend &
pacmd set-card-profile 0 output:analog-stereo+input:analog-stereo &
startServer &
pcmanfm -d &
# xfce4-power-manager &
guake &
searxStart &
