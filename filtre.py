import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import json
import time

def main():
    filtre()
    
    
def filtre():
    url = "test.xlsx"
    data = pd.read_excel(url)
    data = data.iloc[4:]
    data  = data.iloc[0]
    data = data.iloc[1:]
    print(data)
    
    
    

    
    
    
if __name__ == "__main__":
    main()
    