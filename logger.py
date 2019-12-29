import datetime
import os

os.system('')
RED = '\033[91m'   # mode 31 = red forground
GREEN = '\033[92m' 
YELLOW = '\033[93m' 
RESET = '\033[0m'  # mode 0  = reset

def log(category, message):
    now = datetime.datetime.now()
    print("[" + GREEN + now.strftime('%Y-%m-%dT%H:%M:%S.%f') + RESET + "]\t[" + category + "]" + "\t" + message)
    