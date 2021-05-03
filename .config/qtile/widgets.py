from libqtile import widget
from libqtile.log_utils import logger
from colors import colors

colors = colors()

widget_defaults = dict(
    font='FantasqueSansMono Nerd Font',
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()

def widgets():
  widgetLists = [
      widget.GroupBox(
        active=colors[2],
        background=colors[0],
        disable_drag=True,
        highlight_color=colors[1],
        highlight_method='line',
        inactive=colors[0],
        ),
      widget.Spacer(
        background=colors[0],
        ),
      widget.Memory(
        background=colors[0],
        format='{MemUsed}M',
        ),
      widget.Sep(
        background=colors[0],
        foreground=colors[0],
        linewidth=8,
        ),
      widget.Systray(
        background=colors[0],
        ),
      widget.Sep(
        background=colors[0],
        foreground=colors[0],
        linewidth=8,
        ),
      widget.Clock(
        background=colors[0],
        format='%m/%d %a %H:%M'
        ),
      widget.Sep(
        background=colors[0],
        foreground=colors[0],
        linewidth=8,
        ),
      widget.QuickExit(
        background=colors[0],
        default_text='Off',
        countdown_format='{}',
        ),
      ]
  return widgetLists;

