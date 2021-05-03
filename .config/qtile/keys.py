from libqtile.config import EzClick, EzDrag, EzKey
from libqtile.lazy import lazy

EzKey.modifier_keys = {
   'M': 'mod3',
   'A': 'mod4',
   'S': 'shift',
   'C': 'control',
}

terminal = "st"
secondaryTerminal = "st"

def latest_group(qtile):
  qtile.current_screen.set_group(qtile.current_screen.previous_group)

keys = [
    # Windows
    EzKey(
      'M-n',
      lazy.layout.next()
    ),

    EzKey(
      'M-<space>',
      lazy.next_layout()
    ),

    EzKey(
      'M-p',
      lazy.layout.previous()
    ),

    EzKey(
      'M-S-h',
      lazy.layout.swap_left()
    ),

    EzKey(
      'M-S-l',
      lazy.layout.swap_right()
    ),

    EzKey(
      'M-S-j',
      lazy.layout.shuffle_down()
    ),

    EzKey(
      'M-S-k',
       lazy.layout.shuffle_up()
    ),

    EzKey(
      'M-i',
      lazy.layout.grow()
    ),

    EzKey(
      'M-o',
      lazy.layout.shrink()
    ),

    EzKey(
      'M-c',
      lazy.window.kill()
    ),

    # System
    EzKey(
      'M-C-r',
      lazy.restart()
    ),

    EzKey(
      'M-C-q',
      lazy.shutdown()
    ),

    EzKey(
      'M-S-p',
      lazy.spawn('reboot')
    ),

    # Custom functionalities
    EzKey(
      'M-b',
      lazy.function(latest_group)
    ),

    # Terminal
    EzKey(
      'M-t',
      lazy.spawn(terminal)
    ),

    EzKey(
      'A-t',
      lazy.spawn(secondaryTerminal)
    ),

    # Browsers
    EzKey(
      'M-w',
      lazy.spawn('qutebrowser')
    ),

    # Dmenu/Rofi
    EzKey(
      'M-r',
      lazy.spawn('rofi -show')
    ),

    # Scripts
    EzKey(
      'M-S-e',
      lazy.spawn('layout')
    ),

    EzKey(
      'M-S-u',
      lazy.spawn('volume up')
    ),

    EzKey(
      'M-S-d',
      lazy.spawn('volume down')
    ),

    EzKey(
      'M-C-t',
      lazy.spawn('getHours')
    ),

    EzKey(
      'M-C-l',
      lazy.spawn('lockIt')
    ),

    # Terminal Based Apps
    EzKey(
      'M-S-r',
      lazy.spawn(terminal + " -e ttrv")
    ),

    EzKey(
      'A-n',
      lazy.spawn(terminal + " -e nnn")
    ),

    EzKey(
      'M-v',
      lazy.spawn(terminal + ' -e nvim /home/aedigo/.vimwiki/index.md')
    ),
]

mouse = [
    EzDrag('M-1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    EzDrag('M-3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    EzClick('M-2', lazy.window.bring_to_front())
]

