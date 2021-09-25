# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 23:12:44 2021

@author: frand
"""
import os
import datetime
from datetime import date
# import requests
import pprint
# import json
import sys
sys.path.append ('D:\Code-ED-Project\Modules')
import functions
today = str(date.today())
# print(today)

# heure = str(datetime.datetime.now().time())
# # print(heure)

# ndossier = today+"_"+heure
# print(ndossier)

systems = ("Albisaki", "Apoyot", "Arawot", "Biamebitoto", "Bijedeta", "Gliese 2119", "Gliese 9547", "Helgarai",
           "HIP 76629", "HIP 77310", "HIP 79576", "HIP 79636", "HIP 80221", "HIP 80250", "HIP 80706", "HIP 84255",
           "Hou Yangk", "Iota-1 Normae", "Kitchang Mu", "Nganjang", "Ovimbaia", "Scorpii Sector EL-Y c29", "Scorpii Sector JW-W b1-3",
           "Shen Nung", "Shen Yi", "V841 Arae", "Wo 9512 B", "Yamandara")


#LISTE INUTILE DES STATIONS, Récupération dans le json du system. A METTRE EN PLACE
    # stations = ("Altieri Botanical Garden", "Aniefuna Extraction Enterprise", "Anosike Dredging Reserve", "Archambeau Mining Complex", "Arnold Refinery",
    #             "Avicenna Station", "Baek Nutrition Enterprise", "Bahuguna's Syntheticals", "Baldock Agricultural Holdings", "Balmer's Progress",
    #             "Banmeke Mineralogic Base", "Baudry Terminal", "Beauchene Manufacturing Base", "Bennett Synthetics Depot", "Bentham Horizons", "Bonetti's Territory",
    #             "Bunsen Port", "Caceres Military Complex", "Cardoso Mining Installation", "Carey Landing", "Carpenter Hub", "Cavalcante Metallurgic Exploration",
    #             "Chamitoff Installation", "	Chancellor Metallurgic Complex", "Chandola Agricultural Holdings", "Chang Synthetics Holdings", "Chovnyk Chemical",
    #             "Cixin Mines", "Cixin Mines", "Cleve Hub", "Coles Barracks", "Coulomb Relay", "Crowther Prospecting Exchange", "Curie Settlement", "Daramy Command Site",
    #             "Dawes Prospecting Installation", "Dewsnap Military Complex")

# directory = today
  
# Parent Directory path
parent_dir = os.path.join("D:\projet elite", today)
os.mkdir(parent_dir)
  
# Path
# print("Directory '% s' created" % directory)

# # NE PAS FAIRE RETOURNER CETTE BOUCLE A MOINS NECESSITE APRES AJOUT DEV
# for syst in systems:
#     # RECUP INFOS CORPS SYSTEME + SAVE JSON
#     URL = "https://www.edsm.net/api-system-v1/bodies"
#     params = {"systemName": syst}
#     response = requests.get(URL, params)
#     bodies = response.json()
#     # pprint.pprint(bodies)
   
#     with open('bodies_'+syst+'_'+today+'.json', 'w') as f:
#         json.dump(bodies, f)

functions.factions(parent_dir,systems)
    
functions.stations(parent_dir,systems)

# # RECUP INFOS MARCHES SYSTEME + SAVE FILE
# URL = "https://www.edsm.net/api-system-v1/stations/market"
# params = {"systemName": "HIP 79636","stationName": "Nakamura City"}
# response = requests.get(URL, params)
# markets = response.json()
# # pprint.pprint (markets)

# with open('Naka_'+today+'.json', 'w') as f:
#     json.dump(markets, f)