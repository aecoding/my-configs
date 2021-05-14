from libqtile.config import Click, Drag, Key, KeyChord
from libqtile.lazy import lazy

mod = 'mod3'
alt = 'mod4'

terminal = "st"
secondaryTerminal = "st"

def latest_group(qtile):
  qtile.current_screen.set_group(qtile.current_screen.previous_group)

keys = [
    # Window Management
    Key([mod], 'n', lazy.layout.next()),
    Key([mod], 'space', lazy.next_layout()),
    Key([mod], 'p', lazy.layout.previous()),
    Key([mod, 'Shift'], 'h', lazy.layout.swap_left()),
    Key([mod, 'Shift'], 'l', lazy.layout.swap_right()),
    Key([mod, 'Shift'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'Shift'], 'k', lazy.layout.shuffle_up()),
    Key([mod], 'i', lazy.layout.grow()),
    Key([mod], 'o', lazy.layout.shrink()),
    Key([mod], 'c', lazy.window.kill()),

    # System
    Key([mod, 'Control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.shutdown()),
    Key([alt, 'Shift'], 'p', lazy.spawn('reboot')),

    # Custom functionalities
    Key([mod], 'b', lazy.function(latest_group)),

    # Terminal
    Key([mod], 't', lazy.spawn(terminal)),
    Key([alt], 't', lazy.spawn(secondaryTerminal)),

    # Applications
    Key([mod], 'w', lazy.spawn('qutebrowser')),
    Key([mod], 'r', lazy.spawn('dmenu_history -h 20 -s')),

    # Scripts
    Key([mod, 'Shift'], 'e', lazy.spawn('layout')),
    Key([alt, 'Shift'], 's', lazy.spawn('scrot -p -q 100 /home/aedigo/Documents/Pictures/%Y-%m-%d-%T-screenshot.png')),
    Key([mod, 'Shift'], 'u', lazy.spawn('volume inc')),
    Key([mod, 'Shift'], 'd', lazy.spawn('volume dec')),
    Key([mod, 'Shift'], 'm', lazy.spawn('volume mute')),
    Key([mod, 'Control'], 't', lazy.spawn('getHours')),
    Key([mod, 'Control'], 'l', lazy.spawn('lockIt')),
    KeyChord([mod, 'Shift'], 'p', [
            Key([], 's', lazy.spawn('pomodoro ""')),
            Key([], 'c', lazy.spawn('pomodoro cancel')),
            Key([], 'r', lazy.spawn('pomodoro revision')),
        ]),

    # Terminal Based Apps
    Key([mod, 'Shift'], 'r', lazy.spawn(terminal + " -e ttrv")),
    Key([alt], 'n', lazy.spawn(terminal + " -e nnn")),
    Key([mod], 'v', lazy.spawn(terminal + ' -e nvim /home/aedigo/.vimwiki/index.md')),
    Key([mod, 'Shift'], 't', lazy.spawn(terminal + ' -e gotop')),
]

mouse = [
    Drag([alt], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([alt], 'Button3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([alt], 'Button2', lazy.window.bring_to_front())
]

