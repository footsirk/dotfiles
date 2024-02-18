from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import send_notification

mod = "mod4"

myTerm = "alacritty"
myBrowser = "floorp"
myExplorer = myTerm + " -e ranger"

myTeams = "chromium" + " --profile-directory=Default --app-id=cifhbcnohmdccbgoicgdjpfamggdegmo"
myClock = "gnome-clocks"
myElement = "flatpak run im.riot.Riot"
myVolCtl = "mate-volume-control"
myCalendar = myTerm + " -e khal interactive"

myTLauncher = "java -jar /home/gyk/minecraft/TLauncher-2.885.jar "

winc = {
    "w": myBrowser,
    "e": myExplorer,
    "g": "gimp",
    "m": myTLauncher,
    "k": myBrowser + " https://klik035310001.e-kreta.hu/",
    "t": myTeams,
    "a": myVolCtl,
    "p": myElement,
    "s": myClock,
    "c": myCalendar,
}

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "space", lazy.group.next_window(), desc="Move window focus to other window"),
    Key([mod, "shift"], "space", lazy.group.prev_window(), desc="Move window focus to other window"),

    # Move windows
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "Left",  lazy.screen.prev_group()),
    Key([mod, "control"], "Right", lazy.screen.next_group()),
    

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
        [mod], "a",
        [
            Key([], k, lazy.spawn(c))
            for k, c in winc.items()
        ],
        name="spawn",
    ),
    Key([mod], "Return", lazy.spawn(myTerm)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),

    Key([mod], "b", lazy.hide_show_bar("top")),

    # Change volume
    # Key([], "XF86AudioMute", lazy.widget["volume"].mute()),
    # Key([], "XF86AudioLowerVolume", lazy.widget["volume"].decrease_vol()),
    # Key([], "XF86AudioRaiseVolume", lazy.widget["volume"].increase_vol()),

    # Other
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "p", lazy.restart()),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show run")),
]

