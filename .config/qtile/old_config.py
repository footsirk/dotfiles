import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile, extension
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.command import lazy
from libqtile.utils import send_notification
from libqtile import extension
from configd.colorschemes import colors

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

mod = "mod4"

myTerm = "alacritty"
myBrowser = "chromium"
myExplorer = "thunar"

myTeams = myBrowser + " --profile-directory=Default --app-id=cifhbcnohmdccbgoicgdjpfamggdegmo"
myClock = "gnome-clocks"
myElement = "flatpak run im.riot.Riot"
myVolCtl = "mate-volume-control"

myTLauncher = "java -jar /home/gyk/minecraft/TLauncher-2.885.jar "

winc = {
    "c": myTerm,
    "w": myBrowser,
    "e": "thunar",
    "g": "gimp",
    "m": myTLauncher,
    "k": myBrowser + " https://klik035310001.e-kreta.hu/",
    "t": myTeams,
    "a": myVolCtl,
    "p": myElement,
    "s": myClock
}

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Switch betwen screens
    Key([mod], "q", lazy.prev_screen(), desc='Move focus to prev monitor'),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    # Spawn shortcuts
    KeyChord(
        [mod], "c",
        [
            Key([], k, lazy.spawn(c))
            for k, c in winc.items()
        ],
        name="spawn",
    ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),

    # Other
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "p", lazy.restart()),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show run"))
]

groups = [Group(str(i)) for i in "1234uiop"]

for group in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors[2],
    "border_normal": colors[0]
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(),
    # layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.MonadTall(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    # font="sans",
    # font="BigBlueTerm437 Nerd Font",
    font="0xProto Nerd Font",
    fontsize=16,
    padding=8,
    foreground=colors[1],
)
extension_defaults = widget_defaults.copy()
bar_height = 36

def init_primary_top_widgets():
    return [
        widget.WindowName(),
    ]
# end init_widgets_list

def init_primary_bottom_widgets():
    return [
        widget.GroupBox(
            # highlight_method="box",
            active=colors[2],
            inactive=colors[3],
            # this_current_screen_border=colors[2],
            # disable_drag=True,
            # foreground=colors[1],
        ),

        widget.Prompt(),

        widget.Chord(
            chords_colors={
                "spawn": ("", colors[2]),
            },
            name_transform=lambda name: name.upper()
        ),

        widget.Spacer(),

        widget.Clock(
            format="%b %d %a %H:%M:%S",
            update_interval=3,
            # format="%d %H:%M",
        ),
        
        widget.Spacer(),

        widget.Systray(),

        widget.Sep(),

        widget.Battery(
            format="{char}{percent:.1%}",
            notify_below=20,
            discharge_char="↓",
            charge_char="↑",
            update_interval=5
        ),

        widget.Sep(),

        widget.Volume(
            device="pulse",
            fmt=" {}",
            update_interval=0.1
        ),

        widget.Sep(),

        widget.KeyboardLayout(
                configured_keyboards=["hu", "us"]
        ),
    ]
# def init_bottom_bar_widgets

def init_secondary_widgets():
    return [
        widget.GroupBox(
            active = colors[2],
            inactive = colors[3],
        )
    ]

new_bar = lambda f: bar.Bar(
    f(), 
    bar_height, 
    margin = 10,
    background = colors[0]
)

screens = [
    Screen(
        # top    = new_bar(init_primary_top_widgets),
        bottom = new_bar(init_primary_bottom_widgets)
    ),
    Screen(
        bottom = new_bar(init_secondary_widgets),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True
cursor_warp = True
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "qtile"
