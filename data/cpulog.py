#!/usr/bin/python3

import sys
import time
import datetime
import psutil

TEMPFILE = '/sys/class/thermal/thermal_zone0/temp' # CPU temperature file
label = 'cpulog' # Default label if not overriden

def collect(label):
    ts = datetime.datetime.utcnow()
    cpu = psutil.cpu_percent()
    with open(TEMPFILE, 'r') as tempfile_handle:
        temp = float(tempfile_handle.read())/1000
    print(label + ';' + str(ts) + ';' + str(cpu) + ';' + str(temp))

def help():
    print('cpulog.py: print cpu usage in % and cpu temp in C to stdout.\n' +
          '  Usage: python3 cpulog.py seconds [label]\n')
    sys.exit()
    
if __name__ == '__main__':
    # Not enough parameters
    if (len(sys.argv) < 2):
        help()

    # Read parameters and run main loop
    if (len(sys.argv) >= 2):

        # Read in # of seconds and label, if provided
        try:
            seconds = int(sys.argv[1])
            if (len(sys.argv) > 2):
                label = sys.argv[2]
        except Exception:
            help()
            
        # Loop and collect cpu/temp stats
        try:
            print('label;ts;cpu;temp')
            while seconds > 0:
                time.sleep(1)
                collect(label)
                seconds = seconds - 1
        except Exception:
            print('Something went wrong.')
        sys.exit()
