from datetime import datetime
from pynput.mouse import Listener
import logging

import time
import os
import getpass

username=getpass.getuser()
print(username)
#username=input("Enter Username:")



now=datetime.now()
date_time_s=now.strftime("%d_%m_%Y_%H_%M_%S")

Current_Date_Formatted = datetime.today().strftime('%d%m%Y')

log_dir = "mouse-logger"

try:
    os.mkdir(os.path.join(log_dir,username))
except Exception as e:
    print(e)
    
logging.basicConfig(filename=(os.path.join(log_dir,username,"mouselog_"+date_time_s)),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')


tmm = time.time()


def on_move(x, y):
    timestamp = time.time()-tmm
    logging.info('timestampp:{},NoButton,Move,x:{},y:{}'.format(timestamp,x, y))

def on_click(x, y, button, pressed):
    timestamp = time.time()-tmm
    if pressed:
        logging.info('timestampp:{},Button:{},Pressed,x:{},y:{}'.format(timestamp,button,x,y))
        
    else:
        logging.info('timestampp:{},Button:{},Released,x:{},y:{}'.format(timestamp,button,x,y)) 

def on_scroll(x, y,dx,dy):
    timestamp = time.time()-tmm
    if dy<0:
        logging.info('timestampp:{},scroll,down,x:{},y:{}'.format(timestamp,x,y))
    else:
        logging.info('timestampp:{},scroll,up,x:{},y:{}'.format(timestamp,x,y))

with Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
    listener.join()

