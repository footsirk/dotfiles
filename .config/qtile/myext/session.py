from datetime import datetime, time, timedelta
from myext import util

class Session:
    def __init__(self, name: str, color: str, start: time, end: time):
        self.start = start
        self.end = end
        self.color = color
        self.name = name

    def get_name(self) -> str:
        if isinstance(self.name, str):
            return self.name
        return "-"

    def is_active(self, now: datetime) -> bool:
        start_dt = util.time_to_datetime(self.start, now)
        end_dt   = util.time_to_datetime(self.end,   now)
        return start_dt < now < end_dt

    def time_left(self, now: datetime) -> timedelta:
        end_dt   = util.time_to_datetime(self.end,   now)
        return end_dt - now

    def inactive_since(self, now: datetime) -> timedelta:
        pass
        

