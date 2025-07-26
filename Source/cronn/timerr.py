from datetime import datetime
from platform import system

with open("/Users/vicky/V/Technical/python_workspace/python25/Source/cronn/log.txt","a") as file:
    file.write(f'Time is {datetime.now()}\n')