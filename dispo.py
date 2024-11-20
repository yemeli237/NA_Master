import tkinter
from typing import *
import customtkinter
from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import filtre
import os
import json
from tkinter import filedialog
import time
import webbrowser
import asyncio

def hf(self,):
    new = customtkinter.CTkToplevel(self)
    new.title("Disponibilite des sites du hor Mfoundi")
    new.geometry(f"{640}x{320}")
    new.minsize(width=640, height=320)
    new.attributes('-topmost', True)
    new.resizable(FALSE, FALSE)
    new.focus_force()
    # new.iconbitmap("icon.ico")
    disponible = pd.read_excel("disponible.xlsx")
    hf = pd.DataFrame()
    code =  []
    codes = [
        "BMY201","MKN138","YDE198","NEB142","NTU141","BZG210","AYS144",
        "ESK258",'MTE206',"MNB213","NGM199","BJK254","YDE200","MBY252","BFA137",
        ]
    for i in range(disponible.index.stop):
        code.append(disponible.loc[i, "MO Name"][:6])
    # print(code)

    disponible["dispo"] = code

    #YDE043 = alarm[alarm["Sites"] == "YDE043"]
    for i in range(len(codes)):
        hf = pd.concat([hf, disponible[disponible["dispo"] == codes[i]]], ignore_index=True)
        
    global file1    
    file1 =  pd.DataFrame()    
    if os.path.exists("hf.xlsx"):
        try:
            file1 = pd.read_excel("hf.xlsx")
        
        except:
            pass
    
    new.grid_columnconfigure(1, weight=1)
    new.grid_columnconfigure((2, 3), weight=0)
    new.grid_rowconfigure((0, 1, 2), weight=1)
        
    textbox = customtkinter.CTkFrame(new, width=640)
    textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
    textbox.grid_columnconfigure(1, weight=1)
    textbox.grid_columnconfigure((1, 2), weight=0)
    textbox.grid_rowconfigure((0, 0, 0), weight=1)
    
    total = hf.index.stop
    indis =  file1.index.stop
    rapport = hf.index.stop - file1.index.stop
    
    pour_indis = indis/total
    pour_indis = pour_indis*100
    pour_dispo = 100 - pour_indis
        
        ###############################
        #frame pour les l'onglet Major
    cell_name = customtkinter.CTkFrame(master=textbox,  border_color="red",corner_radius=2 )
    cell_name.grid(row=0, column=0, sticky="nsew", pady=(5, 5))
        
        
        #label
    cell_name_on = customtkinter.CTkFrame(master=cell_name,  border_width=1)
    cell_name_on.grid(row=0, column=0, sticky="nsew")
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text="Statistique",width=640,  height=50,font=customtkinter.CTkFont(size=14, weight="bold"))
    cell_name_lb.grid(row=0, column=0, sticky="nsew",)
        #
    cell_name_on = customtkinter.CTkFrame(master=cell_name_on,  border_width=1)
    cell_name_on.grid(row=1, column=0, sticky="nsew",)
    
    #####################
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text="Total des sites : ", height=50,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=0, column=0, sticky="w")
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text="Total des sites indisponible : ", height=50,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=1, column=0, sticky="w")
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text="Total des sites fonctionel : ", height=50,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=2, column=0, sticky="w")
    
    ##############################
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"{total}", height=50,font=customtkinter.CTkFont(size=14, weight="bold"))
    cell_name_lb.grid(row=0, column=1, sticky="nsew",padx=(5, 15))
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"{indis}", height=50,font=customtkinter.CTkFont(size=14, weight="bold"))
    cell_name_lb.grid(row=1, column=1, sticky="nsew",padx=(5, 15))
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"{rapport}", height=50,font=customtkinter.CTkFont(size=14, weight="bold"))
    cell_name_lb.grid(row=2, column=1, sticky="nsew",padx=(5, 15))
    
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"Pour une diponiblite de {round(pour_dispo)}%", height=30,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=3, column=0, sticky="w")
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"Pour une inponiblite de {round(pour_indis)}%", height=30,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=4, column=0, sticky="w")
        
        
        
        # self.set_window_icon(new, "icon.png")
        # icon = PhotoImage(file="icon.png")
        # new.iconphoto(False, icon)
        
def mf(self):
    new = customtkinter.CTkToplevel(self)
    new.title("Disponibilite des sites du Mfoundi")
    new.geometry(f"{640}x{320}")
    new.minsize(width=640, height=320)
    new.resizable(FALSE, FALSE)
    new.attributes('-topmost', True)
    new.focus_force()
    # new.iconbitmap("icon.ico")
    
    disponible = pd.read_excel("disponible.xlsx")
    code =  []
    mf = pd.DataFrame()
    for i in range(disponible.index.stop):
         code.append(disponible.loc[i, "MO Name"][:3])
         
    disponible["Tris"] = code
    mf = disponible[disponible["Tris"] == "YDE"]
    mf.to_excel("mf.xlsx")
    mf = pd.read_excel("mf.xlsx")
    

    new.grid_columnconfigure(1, weight=1)
    new.grid_columnconfigure((2, 3), weight=0)
    new.grid_rowconfigure((0, 1, 2), weight=1)
        
    textbox = customtkinter.CTkFrame(new, width=640)
    textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
    # textbox.grid_columnconfigure(1, weight=1)
    # textbox.grid_columnconfigure((1, 2), weight=0)
    # textbox.grid_rowconfigure((0, 0, 1), weight=1)
    global file    
    file =  pd.DataFrame()    
    if os.path.exists("finale.xlsx"):
        try:
            file = pd.read_excel("finale.xlsx")
        
        except:
            pass
        
        ###############################
        #frame pour les l'onglet Major
    cell_name = customtkinter.CTkFrame(master=textbox,  border_color="red",corner_radius=2 )
    cell_name.grid(row=0, column=0, sticky="nsew", pady=(5, 5))
        
        
        #label
    cell_name_on = customtkinter.CTkFrame(master=cell_name,  border_width=1, width=640)
    cell_name_on.grid(row=0, column=0, sticky="nsew")
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text="Statistique",  height=50,font=customtkinter.CTkFont(size=14, weight="bold"))
    cell_name_lb.grid(row=0, column=0, sticky="nsew",)
        #
    cell_name_on = customtkinter.CTkFrame(master=cell_name_on,  border_width=1, width=640)
    cell_name_on.grid(row=1, column=0, sticky="nsew",)
        
        
        
    #     #frame pour les l'onglet site mineur
    # site_name = customtkinter.CTkFrame(master=textbox,  border_color="red", )
    # site_name.grid(row=0, column=1, sticky="nsew",pady=(5, 5), )
        
    #     #label
    # site_name_on = customtkinter.CTkFrame(master=site_name,  border_width=1, height=50)
    # site_name_on.grid(row=0, column=0)
    total = mf.index.stop
    indis =  file.index.stop
    rapport = mf.index.stop - file.index.stop
    
    pour_dispo = indis/100
    pour_dispo = pour_dispo*total
    pour_indis = 100 - pour_dispo
    
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text="Total des sites : ", height=50,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=0, column=0, sticky="w")
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text="Total des sites indisponible : ", height=50,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=1, column=0, sticky="w")
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text="Total des sites fonctionel : ", height=50,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=2, column=0, sticky="w")
    
    ##############################
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"{total}", height=50,font=customtkinter.CTkFont(size=14, weight="bold"))
    cell_name_lb.grid(row=0, column=1, sticky="nsew",padx=(5, 15))
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"{indis}", height=50,font=customtkinter.CTkFont(size=14, weight="bold"))
    cell_name_lb.grid(row=1, column=1, sticky="nsew",padx=(5, 15))
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"{rapport}", height=50,font=customtkinter.CTkFont(size=14, weight="bold"))
    cell_name_lb.grid(row=2, column=1, sticky="nsew",padx=(5, 15))
    
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"Pour une diponiblite de {round(pour_dispo)}%", height=30,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=3, column=0, sticky="w")
    cell_name_lb = customtkinter.CTkLabel(master=cell_name_on, text=f"Pour une inponiblite de {round(pour_indis)}%", height=30,font=customtkinter.CTkFont(size=14, weight="bold"),width=500)
    cell_name_lb.grid(row=4, column=0, sticky="w")
        
    #     #
    # minor_on = customtkinter.CTkFrame(master=site_name_on,  border_width=1, border_color="green")
    # minor_on.grid(row=1, column=0, sticky="nsew",padx=(5, 5), pady=(5, 5))
        
    #     #frame pour les l'onglet warning
    # sr = customtkinter.CTkFrame(master=textbox,  border_color="red", )
    # sr.grid(row=0, column=2, sticky="nsew",pady=(5, 5), )
        
    #     #label
    # sr_on = customtkinter.CTkFrame(master=sr,  border_width=1, height=50)
    # sr_on.grid(row=0, column=0)
    # cell_name_lb = customtkinter.CTkLabel(master=sr_on, text="Warning",width=350,  height=50,font=customtkinter.CTkFont(size=14, weight="bold"))
    # cell_name_lb.grid(row=0, column=0, sticky="nsew")
    
    # warning_on = customtkinter.CTkFrame(master=sr_on,  border_width=1, border_color="yellow")
    # warning_on.grid(row=1, column=0, sticky="nsew",padx=(5, 5), pady=(5, 5))
        
