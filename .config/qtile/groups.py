from libqtile.lazy import lazy
from libqtile.config import Group, Key
from keys import keys
from modkey import mod, alt 

groups = [Group(i) for i in "asdfhjkl"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
          desc="Switch to group {}".format(i.name)),
        Key([alt], i.name, lazy.window.togroup(i.name),
          desc="move focused window to group {}".format(i.name)),
    ])
