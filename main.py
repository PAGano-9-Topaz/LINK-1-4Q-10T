from pyscript import display, document 
import numpy as np
import logging
import matplotlib.pyplot as plt
logging.getLogger('matplotlib').setLevel(logging.ERROR)

JR = 0
LA = 0
RA = 0
CA = 0
LB = 0
MC = 0
PC = 0
SC = 0
SMC = 0
AD = 0
AE = 0
SE = 0
KE = 0
PG = 0
CG = 0
SK = 0
SO = 0
CR = 0
MS = 0
RS = 0
DT = 0
BV = 0
HY = 0
IZ = 0  

def shinograph(e):
    global JR, LA, RA, CA, LB, MC, PC, SC, SMC
    global AD, AE, SE, KE, PG, CG, SK, SO
    global CR, MS, RS, DT, BV, HY, IZ
    document.getElementById('output').innerHTML = ' '
    selected = document.getElementById("Select").value
    value = document.getElementById("input1").value

    value = int(value)
    
    if selected == "JR":
        JR += value
    elif selected == "LA":
        LA += value
    elif selected == "RA":
        RA += value
    elif selected == "CA":
        CA += value
    elif selected == "LB":
        LB += value
    elif selected == "MC":
        MC += value
    elif selected == "PC":
        PC += value
    elif selected == "SC":
        SC += value
    elif selected == "SMC":
        SMC += value
    elif selected == "AD":
        AD += value
    elif selected == "AE":
        AE += value
    elif selected == "SE":
        SE += value
    elif selected == "KE":
        KE += value
    elif selected == "PG":
        PG += value
    elif selected == "CG":
        CG += value
    elif selected == "SK":
        SK += value
    elif selected == "SO":
        SO += value
    elif selected == "CR":
        CR += value
    elif selected == "MS":
        MS += value
    elif selected == "RS":
        RS += value
    elif selected == "DT":
        DT += value
    elif selected == "BV":
        BV += value
    elif selected == "HY":
        HY += value
    elif selected == "IZ":
        IZ += value

    sasalele = np.array([JR,LA,RA,CA,LB,MC,PC,SC,SMC,AD,AE,SE,KE,PG,CG,SK,SO,CR,MS,RS,DT,BV,HY,IZ])
    days = np.array(['Jalainie','Leona','Renzo','Caleb','Cedric','Martina','Phoebe','Sang-heon','Sean','Allen','AJ','Skyler','Khloe','Shino','Calvin','Simran','Chilli','Carl','Miguel','Ramon','Deryck','Beatrix','Harmony','Ivy'])

    plt.bar(days, sasalele)
    plt.xticks(rotation=90)
    plt.title("Absences Tracker")
    plt.xlabel('Students')
    plt.ylabel('Absences')
    plt.show()
