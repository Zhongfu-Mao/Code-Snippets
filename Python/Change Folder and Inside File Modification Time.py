import datetime as dt
import os
import time
from pathlib import Path

if __name__ == '__main__':
    path = Path(r"<folder_path>")
    year = 2020
    month = 8
    day = 8
    hour = 18
    minute = 18
    date = dt.datetime(year, month, day, hour, minute)
    mod_time = time.mktime(date.timetuple())

    for p in path.rglob("**/**/*"):
        os.utime(p, (mod_time, mod_time))
