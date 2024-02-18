from libqtile.widget import base
import sys
import time
from datetime import datetime, timedelta
from libqtile.utils import send_notification
from myext.session import Session
from myext import util
import traceback

class SessionWidget(base.InLoopPollText):
    defaults = [
        ("update_interval", 10),
        ("sessions", []),
        ("inactive_color", "#ff0000", "when no sessions are active"),
        ("active_format",   "{name} {left}"),
        ("inactive_format", "since {since}"),
        ("warn_ticks", 1)
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(SessionWidget.defaults)
        self.current_session = None
        self.tick_count = 0
        self.inactive_start = None
        self.last_warned = None

    def _get_current_session(self):
        for session in self.sessions:
            if session.is_active(self.now):
                self.current_session = session
                # self.inactive_start = None
                return

        self.current_session = None

        # if self.inactive_start == None:
        #     self.inactive_start = self.now

    def _get_inactive_since(self):
        last = None
        for session in sessions:
            if last == None:
                last = session
                continue

    def _set_color(self):
        if isinstance(self.current_session, Session):
            self.foreground = self.current_session.color

        else:
            self.foreground = self.inactive_color

    def _should_warn(self) -> bool:
        if self.current_session == None:
            if self.last_warned == None:
                return True

            if self.tick_count - self.last_warned <= self.warn_ticks:
                return True

        return False

    def _warn(self):
        self.last_warned = self.tick_count
        send_notification(
            "HÉ!",
            "KAPCSOLD MÁR KI!",
            urgent=True,
            timeout=2000
        )

    def tick(self):
        try:
            self.tick_count += 1
            self.now = datetime.now()
            self._get_current_session()

            if self._should_warn():
                self._warn()

            self._set_color()
            text = self.poll()
            # send_notification("session_widget", text)
            self.update(text)
            return self.update_interval - time.time() % self.update_interval
        except Exception as e:
            txt = traceback.format_exc()
            txt = str(e) + '\n' + txt
            send_notification("session_widget error", txt)

    def poll(self):
        if isinstance(self.current_session, Session):
            name = self.current_session.get_name()
            left = self.current_session.time_left(self.now)
            left = util.timedelta_to_str(left)
        
            return self.active_format.format(
                name=name,
                left=left
                # left=self.current_session.time_left()
            )

        else:
            send_notification("e", self.current_session)
            # since = self.now - self.inactive_start
            # since = util.timedelta_to_str(since)
            # return self.inactive_format.format(
            #     since=since
            # )
            return "inactive"

