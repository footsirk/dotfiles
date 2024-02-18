from datetime import time, datetime, timedelta

def timedelta_to_str(td: timedelta):
    tot_secs = td.total_seconds()
    tot_mins = int(tot_secs // 60)
    hours = tot_mins // 60
    mins = tot_mins % 60
    return f"{hours}:{mins:02d}"

def time_to_datetime(t: time, now: datetime):
    return datetime.combine(now.date(), t)

def next_time(t: time, now: datetime):
    dt = datetime.combine(now.date(), t)
    if dt < now:
        dt += timedelta(days=1)

    return dt

def prev_time(t: time, now: datetime):
    dt = datetime.combine(now.date(), t)
    if dt > now:
        dt = dt.replace()

    return dt

