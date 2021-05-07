from libqtile import widget
from colors import colors

colors = colors()

widget_defaults = dict(
  font='FantasqueSansMono Nerd Font',
)

extension_defaults = widget_defaults.copy()

def open_calendar(qtile):  # spawn calendar widget
    qtile.cmd_spawn('gsimplecal next_month')

def close_calendar(qtile):  # kill calendar widget
    qtile.cmd_spawn('killall -q gsimplecal')

# add widget with callbacks somewhere

# widget.Clock(format='%Y-%m-%d %a %H:%M', mouse_callbacks={'Button1': open_calendar, 'Button2': close_calendar})

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
    widget.Notify(
      background=colors[0],
      default_timeout=5,
      foreground=colors[1]
    ),
    widget.Sep(
      background=colors[0],
      foreground=colors[0],
      linewidth=0,
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
      format='%d/%m %a %H:%M',
      mouse_callbacks={'Button1': open_calendar, 'Button2': close_calendar}
    ),
  ]
  return widgetLists;
