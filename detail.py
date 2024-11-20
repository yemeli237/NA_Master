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
from datetime import datetime
# from docx import Document

def detail(self, find,):
    new = customtkinter.CTkToplevel(self)
    new.title("Suivie de releve du site")
    new.geometry(f"{1080}x{460}")
    new.minsize(width=1080, height=460)
    new.resizable(False, False)
    new.attributes('-topmost', True)
    new.focus_force()
    # new.iconbitmap("icon.ico")
    new.grid_columnconfigure(1, weight=1)
    new.grid_columnconfigure((2, 3), weight=0)
    new.grid_rowconfigure((0, 1, 2), weight=1)
    date1_str = find.loc["First Occurred (NT)"]
    date2_str = find.loc["Last Occurred (NT)"]
    etat_reseau = []
    responsable = None
    observations = None
    causes = None
    
    
    head = customtkinter.CTkFrame(master=new, border_color="#1492E6", width=1070, border_width=1)
    head.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
    site = customtkinter.CTkFrame(master=head)
    site.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        
        
    site_label = customtkinter.CTkLabel(master=site, text="Site de: ", width=250, font=customtkinter.CTkFont(size=18, weight="bold"))
    site_label.grid(row=0, column=0, sticky="nsew")
    
    text = find.loc["MO Name"]
    text = text[7:]
    site_nom = customtkinter.CTkLabel(master=site, text=f"{text}", width=250, font=customtkinter.CTkFont(size=16))
    site_nom.grid(row=1, column=0, sticky="nsew",pady=(25, 5), )
        ###
    local_label = customtkinter.CTkLabel(master=site, text="Localisation: ", width=300, font=customtkinter.CTkFont(size=18, weight="bold"))
    local_label.grid(row=0, column=1, sticky="nsew")
    local_nom = customtkinter.CTkLabel(master=site, text=f"{find.loc["Location Information"][7:15]}", width=300,font=customtkinter.CTkFont(size=16))
    local_nom.grid(row=1, column=1, sticky="nsew",pady=(25, 5),)
        ###
    date_label = customtkinter.CTkLabel(master=site, text="Date et heure de coupure: ", width=250,font=customtkinter.CTkFont(size=18, weight="bold"))
    date_label.grid(row=0, column=2, sticky="nsew")
    date = customtkinter.CTkLabel(master=site, text=f"{date2_str}", width=250,font=customtkinter.CTkFont(size=16))
    date.grid(row=1, column=2, sticky="nsew",pady=(25, 5),)
        ###
    dure_label = customtkinter.CTkLabel(master=site, text="Duree de coupure: ", width=250,font=customtkinter.CTkFont(size=18, weight="bold"))
    dure_label.grid(row=0, column=3, sticky="nsew")
    
    date1 = datetime.now()
    date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
    difference = date2 - date1
    
    dure = customtkinter.CTkLabel(master=site, text=f"{difference}", width=250,font=customtkinter.CTkFont(size=16))
    dure.grid(row=1, column=3, sticky="nsew",pady=(25, 5),)
        
        ########################################################################
    confi = customtkinter.CTkFrame(master=new, border_color="#1492E6", width=1070, border_width=1)
    confi.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
    manip = customtkinter.CTkFrame(master=confi)
    manip.grid(row=1, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        
    entete = customtkinter.CTkFrame(master=confi, height=60, fg_color="#1492E6")
    entete.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="news")
    cause_label = customtkinter.CTkLabel(master=entete, text="Cause", width=345,font=customtkinter.CTkFont(size=18, weight="bold"))
    cause_label.grid(row=0, column=0, sticky="news", padx=(5, 5), pady=(5, 5))
    observation_label = customtkinter.CTkLabel(master=entete, text="Observation",width=345, font=customtkinter.CTkFont(size=18, weight="bold"))
    observation_label.grid(row=0, column=1, sticky="news", padx=(5, 5), pady=(5, 5))
    respon_label = customtkinter.CTkLabel(master=entete, text="Responsable",width=345, font=customtkinter.CTkFont(size=18, weight="bold"))
    respon_label.grid(row=0, column=2, sticky="news", padx=(5, 5), pady=(5, 5))
        ###
    cause = customtkinter.CTkOptionMenu(master=manip,width=345, fg_color="#3340F2",font=customtkinter.CTkFont(size=18), height=40,
                                        values=["Sinistre", "Energie","Vandalisme", "Diagnostique en cours","Transmission"],
                                        command=lambda causes : choix_cause(causes)
                                        )
    observation = customtkinter.CTkTextbox(master=manip,width=345,text_color="#1492E6",font=customtkinter.CTkFont(size=18), height=40)
    respon = customtkinter.CTkOptionMenu(master=manip,width=345,fg_color="#3340F2",font=customtkinter.CTkFont(size=18), height=40,
                                         values=["ENEO/CEEY", "CRARY", "BUM/CART", "CERTUY/EMIRY", "DRCM", "CTT Obala", "CTT Ayos","CTTY"],
                                        #  command=respo()
                                        command=lambda responsable : choix_responsable(responsable)
                                         )
    cause.grid(row=0, column=0,sticky="news", padx=(5, 5), pady=(5, 5))
    observation.grid(row=0, column=1,sticky="news", padx=(5, 5), pady=(5, 5))
    respon.grid(row=0, column=2,sticky="news", padx=(5, 5), pady=(5, 5))
        
        #################################
    ctl = customtkinter.CTkFrame(master=new, border_color=None, width=1070, border_width=1,)
    ctl.grid(row=2, column=0, padx=(5, 5), pady=(5, 5),sticky="n")
    site = customtkinter.CTkButton(master=ctl, height=40, text="Soumetre",font=customtkinter.CTkFont(size=18,  weight="bold"), command=lambda:create(observation))
    site.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="n")
    
    def choix_cause(choice):
        causes = choice
        try:
            with open("cause.json", "w") as cause:
                json.dump(causes, cause)
        except:
            pass
    def choix_responsable(choice):
        responsable = choice
        try:
            with open("responsable.json", "w") as f:
                json.dump(responsable, f)
        except:
            pass
    
    def create(observation):
        dateheure = date2_str
        site = text
        local = find.loc["Location Information"][7:15]
        with open("cause.json", "r") as f:
            causes = json.load(f)
        f.close()
        with open("responsable.json", "r") as f:
            responsable = json.load(f)
        f.close()
        observation = observation.get(0.0, "end")
        valeur = {
            "Site" : f"{site}",
                # "Localisation" : f"{local}",
                "Date et Heure" : f"{dateheure}",
                "Cause" : causes,
                "Responsable" : responsable,
                # "Observation" : observations,
                
                
            }
        
        if os.path.exists("etat.xlsx"):
            data = pd.read_excel("etat.xlsx")
            etat_reseau.append(valeur)
            new_data = pd.DataFrame(etat_reseau)
            data = pd.concat([data, new_data], ignore_index=True)
            data.to_excel("etat.xlsx", index=False)
        else:
            etat_reseau.append(valeur)
            data = pd.DataFrame(etat_reseau)
            data.to_excel("etat.xlsx", index=False)

        # if os.path.exists("etat.json"):
        #     try:
                
                
        #         # with open("etat.txt", "+a") as f:
        #         #     f.write(",")
        #         # with open("etat.txt", "+a") as file:
        #         #     file.write(str(valeur))
                
        #         #########################
                
        #         with open("etat.json", "+a") as file:
        #             data = json.load(file)
        #         etat_reseau.append(data)
        #         # etat_reseau.append(valeur)
        #         print(etat_reseau)
                
        #         # with open("etat.json", "w") as file:
        #         #     json.dump(etat_reseau, file, indent=4)
        #         # pass
                    
        #         ###############################    
                    
        #         # with open("etat.json", "+a") as file:
        #         #     data = json.load(file)
        #         # etat_reseau = valeur
        #         # etat_reseau.popitem(data)
                
        #         # with open("etat.json", "w") as file:
        #         #     json.dump(etat_reseau, file, indent=4)
            
        #     except Exception as e :
        #         print(e)
                
        # else:
        #    with open("etat.json", "w") as file:
        #        json.dump(valeur, file, indent=4)
            
        new.destroy()
        

    

    
        # self.set_window_icon(new, "icon.png")
        # icon = PhotoImage(file="icon.png")
        # new.iconphoto(False, icon)