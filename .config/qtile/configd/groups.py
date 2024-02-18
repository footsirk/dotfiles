from libqtile.config import Group, Key
from libqtile.command import lazy
from .keys import mod, keys

groups = [Group(str(i)) for i in "1234uiop"]

for group in groups:
    keys.extend([
        Key(
            [mod],
            group.name,
            lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name),
        ),

        Key(
            [mod, "shift"],
            group.name,
            lazy.window.togroup(group.name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(group.name),
        ),
    ])

