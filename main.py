import datetime
import numpy as np
idate=datetime.datetime.now()
print(f"datetime now: {idate}")
idate=idate.replace(year=2012, month=7, day=21)
date2000=idate.replace(year=2000, month=1, day=1,hour=0,minute=0,second=0,microsecond=0)
print(f"datetime before: {idate}")
print(f"datetime 2000: {date2000}")
hp2000=idate-date2000
print(f"diff: {hp2000}")
print(f"days*24: {hp2000.days*24}")
hours_raw=hp2000.days*24+hp2000.seconds/3600
hours=int(np.round(hours_raw))
print(f"diff: {hours} hours")
