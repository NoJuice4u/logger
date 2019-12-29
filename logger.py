import datetime
import os

os.system('')
RED = '\033[91m'   # mode 31 = red forground
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'  # mode 0  = reset

def log(category, message):
    now = datetime.datetime.now()
    print("[" + YELLOW + now.strftime('%Y-%m-%dT%H:%M:%S.%f') + RESET + "]\t[" + category + "]" + "\t" + message)
    