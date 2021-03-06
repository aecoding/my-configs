#!/bin/bash

dir=$(pwd)

function copy() {
  cp $1 $2 -a
}

function save() {
  cd ~/.my-configs;
  git add .;
  git commit -m 'New Changes!';
  git push -u origin master;
  cd $dir;
}

case $1 in
  qtile)
    copy ~/.config/qtile ~/.my-configs/.config
    save
    ;;
  nvim)
    copy ~/.config/nvim/configs ~/.my-configs/.config/nvim/configs
    copy ~/.config/nvim/init.vim ~/.my-configs/.config/nvim/
    save
    ;;
  picom)
    copy ~/.config/picom ~/.my-configs/.config
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
    copy ~/.oh-my-zsh/aliases.zsh ~/.my-configs/.oh-my-zsh/
    save
    ;;
  *)
    notify-send 'Not found!'
  ;;
esac



