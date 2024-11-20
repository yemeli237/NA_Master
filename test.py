import pandas as pd
import  json
import time

#data = pd.read_excel("test.xlsx")   

#data = data.iloc[4:]
#data.columns = data.iloc[0]
#trie = data.iloc[1:]   
#trie.to_excel("test2.xlsx")
filtre = pd.read_excel("test2.xlsx")
alarm = filtre[filtre["Alarm ID"] == 301]
alarm.to_excel("alarm.xlsx")
alarm = pd.read_excel("alarm.xlsx")
hf = pd.DataFrame()

alarm_id = [
    "Major",
    "Minor",
    "Warning"
    ]
dispo = pd.DataFrame()
print(filtre.describe())
stat = filtre.describe()

for i in alarm_id:
    #dispo.append(filtre[filtre["Severity"] == i])    
    dispo = pd.concat([dispo, filtre[filtre["Severity"] == i]], ignore_index=True)
    #print(dispo)

code =  []
codes = [
    "BMY201","MKN138","YDE198","NEB142","NTU141","BZG210","AYS144",
    "ESK258",'MTE206',"MNB213","NGM199","BJK254","YDE200","MBY252","BFA137",
    ]
for i in range(alarm.index.stop):
    code.append(alarm.loc[i, "MO Name"][:6])

alarm["Sites"] = code

#YDE043 = alarm[alarm["Sites"] == "YDE043"]
for i in range(len(codes)):
    hf = pd.concat([hf, alarm[alarm["Sites"] == codes[i]]], ignore_index=True)
    
if hf.empty:
    print("null")
    
        
bon = alarm.drop(['Unnamed: 0.1', 'Unnamed: 0', ' ', 
       'Cleared On (NT)', 'Acknowledged On (ST)', 'Cleared By',
       'Acknowledged By', 'Clearance Status', 'RRU Name',
       'Acknowledgement Status', 'BBU Name', 'eNodeB ID', 'Log Serial Number',
       'User Label', 'Equipment Alarm Serial Number', 'Additional Information',
       'Maintenance Status'], axis=1)
#print(bon[bon["Site"] == "BFA"])    

#print(dispo)       

        
    
        




