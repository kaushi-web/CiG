# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:28:34 2021

@author: Kaushi
"""

from win32gui import GetWindowText, GetForegroundWindow
from datetime import datetime
import csv
import psutil, win32process, win32gui, time
import os
import pandas as pd

category_path=os.getcwd()+'/App Type'
app_filenames=os.listdir(category_path)

app_types=[app_filename[:-4] for app_filename in app_filenames]
print(app_types)

apps_all=[]

for app_filename in app_filenames:
    
    app_path=os.path.join(category_path,app_filename)
    app_file=pd.read_csv(app_path,encoding="ISO-8859-1",engine='python').values
    apps_all.append(app_file[:,0])
    #print(apps_all)

def active_window_process_name():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow()) #This produces a list of PIDs active window relates to
    app=psutil.Process(pid[-1]).name()

    return app #pid[-1] is the most likely to survive last longer

current_window=""
previous_time=datetime.now()
duration=0
log_file_path='app_log.csv'
import re

while(True):
    
    window=GetWindowText(GetForegroundWindow())
    
    if(window!=current_window):

        now=datetime.now()
        date_time_s=now.strftime("%d/%m/%Y,%H:%M:%S") 
        file_name=now.strftime("%d_%m_%Y")+'.csv'
        
        with open(file_name,'a',newline='') as file:
            
            if(window!=''):
                writer=csv.writer(file)
                application=active_window_process_name()[:-4]
                #print(application)
                app_type='Unkown'
                for i,apps in enumerate(apps_all):
                    #for app in apps:
                        #print(app)
                        #if re.search(application,app,re.IGNORECASE):
                   if application.lower() in (app.lower() for app in apps):
                        app_type=app_types[i]
                        print(app_type,application,app_types[i])
                        break
    
                print([date_time_s,window,app_type,str(duration)])
                writer.writerow([date_time_s,application,app_type,str(duration)])
                
                previous_time=now
            else:
                try:
                    duration=now-previous_time
                    duration=duration.total_seconds()
                except:
                    pass
        current_window=window
