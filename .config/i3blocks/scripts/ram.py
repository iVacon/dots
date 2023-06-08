#! /usr/bin/env python
import psutil


ramused = round(psutil.virtual_memory().used / 1048576)
total = round(psutil.virtual_memory().total / 1048576)
print("RAM: " + str(ramused) + "MB / " + str(total) + "MΒ χρησιμοποιούνται")

