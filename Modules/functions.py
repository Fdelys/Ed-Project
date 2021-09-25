# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 08:43:53 2021

@author: frand
"""

import os
import requests
import json


def factions(parent_dir,systems):
    directory = "factions"
    factions_path = os.path.join(parent_dir, directory)
    os.mkdir(factions_path)
    print("Directory '% s' created" % directory)
    
    for syst in systems:
        # RECUP INFOS FACTIONS SYSTEME + SAVE FILE
        URL = "https://www.edsm.net/api-system-v1/factions"
        params = {"systemName": syst, "showHistory" : 1}
        response = requests.get(URL, params)
        factions = response.json()
        # pprint.pprint(factions)
        
        with open(os.path.join(factions_path, syst+'.json'), 'w') as f:
            json.dump(factions, f)
            print(syst+"_factions")
            
def stations(parent_dir,systems):
    directory = "stations"
    stations_path = os.path.join(parent_dir, directory)
    os.mkdir(stations_path)
    print("Directory '% s' created" % directory)
    
    for syst in systems:
        
        # RECUP INFOS STATIONS SYSTEME + SAVE FILE
        URL = "https://www.edsm.net/api-system-v1/stations"
        params = {"systemName": syst}
        response = requests.get(URL, params)
        stations = response.json()
        # pprint.pprint(factions)
        
        with open(os.path.join(stations_path, syst+'.json'), 'w') as f:
            json.dump(stations, f)
            print(syst+"_stations")