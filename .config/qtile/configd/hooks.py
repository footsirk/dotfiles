from os import path
import subprocess
from libqtile import hook
from libqtile.utils import send_notification

home_path = path.expanduser("~")
qtile_path = path.join(home_path, ".config", "qtile")

@hook.subscribe.startup_once
def start_once():
    subprocess.call([
        path.join(qtile_path, "autostart.sh")
    ])
