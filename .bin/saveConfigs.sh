#!/bin/bash

dir=$(pwd)

function copy() {
  cp $1 $2 -a
}

function save() {
  cd ~/.my-configs;
  git add .;
  git commit -m 'New Changes!';
  git push -u origin main;
  cd $dir;
}

case $1 in
  qtile)
    copy ~/.config/qtile ~/.my-configs/.config
    save
    ;;
  nvim)
    copy ~/.config/nvim ~/.my-configs/.config
    save
    ;;
  picom)
    copy ~/.config/nvim ~/.my-configs/.config
    save
    ;;
  st)
    copy ~/.config/st ~/.my-configs/.config
    save
    ;;
  mpv)
    copy ~/.config/mpv ~/.my-configs/.config
    save
    ;;
  qutebrowser)
    copy ~/.config/qutebrowser ~/.my-configs/.config
    save
    ;;
  dunst)
    copy ~/.config/dunst ~/.my-configs/.config
    save
    ;;
  rofi)
    copy ~/.config/rofi ~/.my-configs/.config
    save
    ;;
  bin)
    copy ~/.bin ~/.my-configs/
    save
    ;;
  zsh)
    copy ~/.zshrc ~/.my-configs/
    save
    ;;
  *)
    notify-send 'Not found!'
  ;;
esac



