from libqtile.lazy import lazy
from libqtile.config import Group, EzKey
from keys import keys

groups = [Group(i) for i in "asdfhjkl"]

for i in groups:
  keys.extend([
    EzKey('M-%s' % i.name, lazy.group[i.name].toscreen(),
      desc="Switch to group {}".format(i.name)),
    EzKey('A-%s' % i.name, lazy.window.togroup(i.name),
      desc="move focused window to group {}".format(i.name)),
  ])
