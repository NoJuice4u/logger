import datetime

def log(category, message):
    now = datetime.datetime.now()
    print("[" + now.strftime('%Y-%m-%dT%H:%M:%S.%f') + "]\t[" + category + "]" + "\t" + message)