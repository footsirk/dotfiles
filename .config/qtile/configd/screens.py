from libqtile import bar, widget
from libqtile.config import Screen
from datetime import time, timedelta

from . import colors
import myext

bar_scale_1 = 1.0
bar_scale_2 = 1.0

widget_defaults_unscaled = dict(
    # font="sans",
    # font="BigBlueTerm437 Nerd Font",
    font="0xProto Nerd Font",
    fontsize=16,
    padding=8,
    foreground=colors.fg,
)

# extension_defaults = widget_defaults.copy()
bar_height = 36

separator = lambda: widget.Sep(
    padding=int(10 * bar_scale_1),
    linewidth=int(2 * bar_scale_1),
    size_percent=80,
    foreground=colors.white
)

groupbox = lambda: widget.GroupBox(
    highlight_method="box",
    active=colors.active,
    inactive=colors.inactive,
    this_current_screen_border=colors.focus,
    this_screen_border=colors.focus,
    center_aligned=True
    # disable_drag=True,
    # foreground=colors[1],
),

systray = lambda: widget.Systray()

def widgets_both_left():
    return [
        widget.GroupBox(
            highlight_method="box",
            active=colors.active,
            inactive=colors.inactive,
            this_current_screen_border=colors.focus,
            this_screen_border=colors.focus,
            # center_aligned=True
            # disable_drag=True,
            # foreground=colors[1],
        ),

        widget.Chord(
            chords_colors={
                "spawn": ("", colors.active),
            },
            name_transform=lambda name: name.upper()
        ),

    ]

def widgets_both_center():
    return [

        widget.Clock(
            format="%b %d %a %H:%M:%S",
            # format="%d %H:%M",
            # format="%H:%M",
            update_interval=5,
        ),

    ]

def widgets_both_right():
    return [

        widget.Battery(
            format="{char} {percent:.0%} {hour:d}:{min:02d}",
            show_short_text=False,
            notify_below=20,
            low_percentage=0.2,
            discharge_char="↓",
            charge_char="↑",
            update_interval=1,
            low_foreground=colors.critical
        ),

        separator(),

        widget.Volume(
            device="pulse",
            fmt=" {}",
            update_interval=0.1
        ),

        separator(),

        widget.KeyboardLayout(
            configured_keyboards=["hu", "us"]
        ),

    ]


def widgets_screen_1():
    return [
        *widgets_both_left(),
        widget.Prompt(),

        widget.Spacer(),

        *widgets_both_center(),

        widget.Spacer(),

        systray(),
        separator(),

        myext.SessionWidget(
            sessions = [
                myext.Session(
                    "pistike",
                    colors.focus,
                    time(8, 00),
                    time(22, 00),
                ),
            ],
            inactive_color=colors.critical,
            update_interval=10,
        ),

        separator(),

        *widgets_both_right(),
    ]

def widgets_screen_2():
    return [
        *widgets_both_left(),
        widget.Spacer(),
        *widgets_both_center(),
        widget.Spacer(),
        *widgets_both_right(),
    ]

def new_bar(widgets, scale):
    global widget_defaults, extension_defaults

    widget_defaults = widget_defaults_unscaled.copy()

    widget_defaults.update(**dict(
        fontsize = int(widget_defaults["fontsize"] * scale),
        padding  = int(widget_defaults["padding"] * scale),
    ))

    extension_defaults = widget_defaults.copy()

    return bar.Bar(
        widgets, 
        int(bar_height * scale), 
        margin = 10,
        background = colors.bg
    ) 

# new_bar = lambda widgets, scale: bar.Bar(
#     widgets, 
#     int(bar_height * scale), 
#     # margin = 10,
#     background = colors.bg
# )

screens = [
    Screen(
        bottom = new_bar(widgets_screen_1(), bar_scale_1)
    ),

    Screen(
        bottom = new_bar(widgets_screen_2(), bar_scale_2)
    ),
]


# myext.Clock(
#     # format="%c",
#     format="%b %d. %a %H:%M:%S",
#     update_interval=1,
#     sessions=[
#         myclock.Session(
#             start=time(8, 00),
#             end  =time(20, 00),
#             color=colors.focus#"#48ff48"
#         ),
#     ],
#     unallowed_colors=[
#         colors.fg,
#         colors.critical,
#     ],
#     warn_ticks=4,
#     warn_interval=timedelta(seconds=3),
#     shutdown_in=3
# ),



# def init_primary_bottom_widgets():
#     return [
#         widget.GroupBox(
#             highlight_method="box",
#             active=colors.active,
#             inactive=colors.inactive,
#             this_current_screen_border=colors.focus,
#             this_screen_border=colors.focus,
#             center_aligned=True
#             # disable_drag=True,
#             # foreground=colors[1],
#         ),

#         widget.OpenWeather(
#             location="Budapest",
#             language="hu",
#             format="{temp}°{units_temperature}"
#         ),


#         widget.Spacer(),

#     ]
# # def init_bottom_bar_widgets


