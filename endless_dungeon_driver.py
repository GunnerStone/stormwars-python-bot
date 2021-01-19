from stormAPI import *
import time
from threading import Thread
from prompt_toolkit import HTML, print_formatted_text
from prompt_toolkit.styles import Style
import sys
import os

try:
    driver = stormAPI().register_window()
    wx, wy = driver.get_window_rect()[:2]

    ROUND_COUNT = 0
    print = print_formatted_text
    style = Style.from_dict({
            'msg': '#71f076 bold',
            'sub-msg': '#616161 italic'
        })

    def display_metrics():
            while(True):
                global ROUND_COUNT
                driver.clear_console()
                #Current dungeon run number
                str_buffer = str(ROUND_COUNT)
                print(HTML(
                    u'<b>></b> <ansicyan><u>Current Dungeon Run</u></ansicyan>'+"<b> : </b>"+'<i><ansigrey>'+str_buffer+'</ansigrey></i>'
                ), style=style)

                time.sleep(1)

    metric_thread = Thread(target=display_metrics,args=())

    try:
        metric_thread.start()
        while True:
            driver.run_endless_dungeon()
            ROUND_COUNT += 1
    except KeyboardInterrupt:
            print ('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
except Exception as e:
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)