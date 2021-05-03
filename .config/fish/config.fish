fish_vi_key_bindings
set -gx EDITOR nvim
set dangerous_colors 000000 333333 666666 ffffff ffff00 ff6600 ff0000 ff0033 3300ff 0000ff 00ffff 00ff00

# Pacman
  function spi
    sudo pacman -S $argv;
  end

  function spr
    sudo pacman -Rs $argv;
  end

  function spu
    sudo pacman -Syu;
  end

# System 
  function cl
    clear;
  end

# Dwm
  function dc
    $EDITOR ~/.config/arco-dwm/config.def.h;
  end

  function smci
    cd ~/.config/arco-dwm; sudo rm config.h; sudo make clean install;
  end

# Fish
  function sc
    $EDITOR ~/.config/fish/config.fish;
  end

# Task Warrior
  function ta
    task add $argv;
  end

  function td
    task done $argv;
  end

  function tdel
    task delete $argv;
  end

  function tn
    task next;
  end

# Qtile
  function qc
    $EDITOR ~/.config/qtile/config.py;
  end

