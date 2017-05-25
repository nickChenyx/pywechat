# -*- encoding=utf-8 -*-
"""
This script uses to test module>datetime usage.
"""

from datetime import datetime

LAST = datetime.now()
print LAST
for x in range(1, 1000):
    x = x+1
NOW = datetime.now()
print (NOW - LASTT).total_seconds()
