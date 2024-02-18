from typing import Any
from libqtile import widget
from datetime import datetime, time, timedelta
from libqtile.utils import send_notification
from os import path
import subprocess
from myext.session import Session

class Clock(widget.Clock):
    defaults: [
        ("sessions", [], "Allowed sessions"),
        ("unallowed_colors", ["#ff0000", "#ffffff"], "Colors to choose from when not in any allowed session"),
        ("warn_interval", timedelta(minutes=1), "How often should it warn the user that he/she isn't in an allowed session"),
        ("shutdown_in", 3),
    ]

    def __init__(self, **config):
        super().__init__(**config)
        self.add_defaults(MyClock.defaults)
        # self.last_notified = None
        self.warn_cooldown = 0
        self.tick_count = 0
        self.current_session = None
        self.now = None

    def _get_session(self) -> int | None:
        for i, session in enumerate(self.sessions):
            if session.is_active(self.now.time()):
                self.current_session = i
                if i != self.current_session:
                    self.just_entered = True
                return i

            # idx = self.tick_count % len(session.colors)
            # self.foreground = session.colors[idx]

        # idx = self.tick_count % len(self.unallowed_colors)
        # self.foreground = self.unallowed_colors[idx]
        return None

    def _set_color(self):
        if self.current_session != None:
            colors = self.sessions[self.current_session].colors
            idx = self.tick_count % len(colors)
            self.foreground = colors[idx]

        else:
            idx = self.tick_count % len(self.unallowed_colors)
            self.foreground = self.unallowed_colors[idx]


    def _should_warn(self) -> bool:
        return self.warn_cooldown <= 0
        # if self.last_notified == None:
        #     return True
        
        # time_elapsed = now - self.last_notified
        # return time_elapsed >= self.warn_interval

    def mytick(self):
        self.tick_count += 1
        self.warn_cooldown -= 1
        self.now = datetime.now()
        self._get_session(now)
        self._set_color(now)

        if self.current_session == None and self._should_warn(now):
            # send_notification("HÉ!", "HA NEM KAPCSOLOD KI AKKOR ÉN FOGOM!")
            send_notification(
                "HÉ!",
                "KAPCSOLD MÁR KI!",
                urgent=True,
                timeout=2000
            )
            self.warn_cooldown = self.warn_ticks
            # self.last_notified = now

    def tick(self):
        try:
            self.mytick()
            self.draw()
        except Exception as e:
            send_notification("MyClock error", f"{e}")

        return super().tick()


