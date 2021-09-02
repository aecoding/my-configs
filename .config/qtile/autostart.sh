#!/bin/bash
redshift &
safeeyes &
# I don't need to change or deal with the internet, so there's no need to have the applet
# nm-applet &
xmodmap ~/.Xmodmap &
# nitrogen --restore &
hsetroot -solid "#282828" &
xcape -e "Control_L=Escape;Alt_L=Return" &
picom --experimental-backend &
startServer &
xfce4-power-manager &
guake &
searxStart &
