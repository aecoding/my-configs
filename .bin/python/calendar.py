#!/usr/bin/env python 
from datetime import date
import subprocess

def notify(message):
    subprocess.Popen(['notify-send.sh', message])
    return

today = date.today()

calendar = today.strftime("%b-%d %a")
notify(calendar)


