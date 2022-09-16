# -*- coding: utf-8 -*-
"""
Created on Thu May 27 08:31:03 2021

@author: mathieu
"""
import os
import time
import numpy as np
from matplotlib import pyplot as plt
import progressbar

def import_config(nom_fichier):
    fichier = open(nom_fichier, "r")
    l = fichier.readline()
    n = int(l)
    l = fichier.readline()
    c = int(l)
    weight=[]
    for i in range(n):
        l = fichier.readline()
        weight.append(int(l))
    fichier.close()
    return (n, c, weight)

########J'ai rajouté ce commentaire
############################################################## NextFit
def nextfit(weight, c):
    if (len(weight)==0):
        return 0
    res = 1
    rem = c
    for _ in range(len(weight)):
        if rem >= weight[_]:
            rem = rem - weight[_]
        else:
            res += 1
            rem = c - weight[_]
    return res

#############################################################First Fit


def firstfit(weight,c):
    
    if (len(weight)==0):
        return 0
   
    boites=[c - weight[0]] #on crée une boite avec le 1er élément déjà à l'intérieur
    for i in range(1,len(weight)):
        
        
        for j in range(len(boites)):
            
            if boites[j] >= weight[i]:
                boites[j]+= -weight[i]
                break
            elif j == (len(boites) - 1) :
                
                boites.append(c-weight[i])

    return len(boites)


############################################################# Best fit
def bestfit(weight,c):
    
    if (len(weight)==0):
        return 0
   
    boites=[c - weight[0]] #on crée une boite avec le 1er élément déjà à l'intérieur
    for i in range(1,len(weight)):
        
        mini=c
        indice=None
        for j in range(len(boites)):
            
            
            if mini >= boites[j] and boites[j] >= weight[i] : #recherche de la boite la plus remplis et pouvant contenir l'objet i
                indice = j
                mini = boites[j]
        
        
        #print((indice,weight[i])) test
        
        if indice==None:
            boites.append(c-weight[i])
        else:
            boites[indice]+= - weight[i]
          

    return len(boites)


############################################################# Worst fit
def worstfit(weight,c):
    
    if (len(weight)==0):
        return 0
  
    boites=[c - weight[0]] #on crée une boite avec le 1er élément déjà à l'intérieur
    for i in range(1,len(weight)):
        
        mini=0
        indice=None
        for j in range(len(boites)):
            
            
            if mini <= boites[j] and boites[j] >= weight[i] : #recherche de la boite la plus remplis et pouvant contenir l'objet i
                indice = j
                mini = boites[j]
        
        if indice==None:
            boites.append(c-weight[i])
        else:
            boites[indice]+= - weight[i]
            

    return len(boites)



#############################################################

def BF_decreaseing(weight,c):
    
    weight.sort()
    weight = weight[::-1]
   
    

    return bestfit(weight, c)



#############################################################

def FF_decreaseing(weight,c):
    
    weight.sort()
    weight = weight[::-1]
   
    

    return firstfit(weight, c)



#############################################################

#%% 

np.random.seed(0)
nmaxi=2920 #nombre de boites maximale
nminim=2900 # nombre de boites minimale
NF=[[],[],[]]
FF=[[],[],[]]
BF=[[],[],[]]
WF=[[],[],[]]
BFD=[[],[],[]]
FFD=[[],[],[]]
c=100 # capacité des boites

for i in progressbar.progressbar(range(nminim,nmaxi)):
       
    weight = np.random.randint(1,c,size=i)
    
    
    start=time.time()
    res=nextfit(weight, c)
    delta =time.time() - start
    NF[0].append(res)
    NF[1].append(delta)
    NF[2].append(delta*res)
    
    start=time.time()
    res=firstfit(weight, c)
    delta =time.time() - start
    FF[0].append(res)
    FF[1].append(delta)
    FF[2].append(delta*res)
    
    start=time.time()
    res=bestfit(weight, c)
    delta =time.time() - start
    BF[0].append(res)
    BF[1].append(delta)
    BF[2].append(delta*res)
    
    start=time.time()
    res=worstfit(weight, c)
    delta =time.time() - start
    WF[0].append(res)
    WF[1].append(delta)
    WF[2].append(delta*res)
    
    start=time.time()
    res=BF_decreaseing(weight, c)
    delta =time.time() - start
    BFD[0].append(res)
    BFD[1].append(delta)
    BFD[2].append(delta*res)

    start=time.time()
    res=FF_decreaseing(weight, c)
    delta =time.time() - start
    FFD[0].append(res)
    FFD[1].append(delta)
    FFD[2].append(delta*res)
    
N = np.arange(nminim,nmaxi) 



plt.title("Comparaison résultat") 
plt.xlabel("Nombre d'objet") 
plt.ylabel("Nombre de boites") 
plt.plot(N,NF[0]) 
plt.plot(N,FF[0]) 
plt.plot(N,BF[0]) 
plt.plot(N,WF[0]) 
plt.plot(N,BFD[0]) 
plt.plot(N,FFD[0]) 
plt.legend(["Next fit", " First fit ","Best fit", " Worst fit ","BFD","FFD"])

plt.show()

plt.title("Comparaison temps d'éxecution") 
plt.xlabel("Nombre d'objet") 
plt.ylabel("Temps") 
plt.plot(N,NF[1]) 
plt.plot(N,FF[1]) 
plt.plot(N,BF[1]) 
plt.plot(N,WF[1]) 
plt.plot(N,BFD[1]) 
plt.plot(N,FFD[1]) 
plt.legend(["Next fit", " First fit ","Best fit", " Worst fit ","BFD","FFD"])

plt.show()

"""
plt.title("Comparaison rapport temps*nombre de boites") 
plt.xlabel("Nombre d'objet") 
plt.ylabel("Rapport temps*nombre de boites") 
plt.plot(N,NF[2]) 
plt.plot(N,FF[2]) 
plt.plot(N,BF[2]) 
plt.plot(N,WF[2]) 
plt.plot(N,BFD[2]) 
plt.plot(N,FFD[2]) 
plt.legend(["Next fit", " First fit ","Best fit", " Worst fit ","BFD","FFD"])

plt.show()
"""
#%%
def main():
    # weight = [2, 5, 4, 7, 1, 3, 8]
    # c = 10
    #c=11
    print(os.getcwd())
    [_, c, weight] = import_config("binpack_001.in")
    start=time.time()
    print("Our data == capacity :", c, "weights :", weight, "\n\n")
    print("Number of bins required in Next Fit :",
                               bestfit(weight, c))
    print(time.time()-start)

    




if __name__ == "__main__":
    main()
