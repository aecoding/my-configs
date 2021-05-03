from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from keys import keys, mouse
from groups import groups
from widgets import widgets
import os, subprocess, numpy
from colors import colors

@hook.subscribe.startup_once
def autostart():
  home = os.path.expanduser('~')
  subprocess.Popen([home + '/.config/qtile/autostart.sh'])

colors = colors()

layouts = [
  layout.MonadTall(
    border_width=1,
    border_focus=colors[1],
    border_normal=colors[0],
    margin=2,
    single_border_width=0,
    single_margin=0,
  ),
  layout.Max(),
]

screens = [
  Screen(
    top=bar.Bar(
      widgets(),
      20
    ),
  ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_width=0,
    max_border_width=0,
    fullscreen_border_width=0,
    float_rules=[
      *layout.Floating.default_float_rules,
      Match(wm_class='confirmreset'),
      Match(wm_class='makebranch'),
      Match(wm_class='maketag'),
      Match(wm_class='ssh-askpass'),
      Match(wm_class='steam'),
      Match(wm_class='guake'),
      Match(wm_class='feh'),
      Match(title='branchdialog'),
      Match(title='pinentry'),
      ])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
