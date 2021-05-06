from libqtile import widget
from colors import colors

colors = colors()

widget_defaults = dict(
  font='FantasqueSansMono Nerd Font',
)

extension_defaults = widget_defaults.copy()

def widgets():
  widgetLists = [
    widget.GroupBox(
        active=colors[1],
        background=colors[0],
        disable_drag=True,
        highlight_color=colors[1],
        highlight_method='line',
        inactive=colors[0],
        block_highlight_text_color=colors[0],
        margin_y=4,
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
      linewidth=0,
    ),
    widget.Systray(
      background=colors[0],
      padding=6
    ),
    widget.Sep(
      background=colors[0],
      foreground=colors[0],
      linewidth=6,
    ),
    widget.Clock(
      background=colors[0],
      format='%d/%m %a %H:%M'
    ),
  ]
  return widgetLists;
