from libqtile import layout
from libqtile.config import Match, Click, Drag
from libqtile.lazy import lazy

from . import colors

layout_theme = {
    "border_width": 4,
    "margin": 4,
    "border_focus": colors.focus,
    "border_normal": colors.bg2
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

