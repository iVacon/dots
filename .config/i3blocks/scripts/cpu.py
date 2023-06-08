#! /usr/bin/env python

import psutil


cpu = psutil.cpu_percent(interval=1)
print("CPU: " + str(cpu))
