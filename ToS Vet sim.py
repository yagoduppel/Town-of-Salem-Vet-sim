# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 18:19:08 2021

@author: yagod
"""
import random
import numpy as np
from matplotlib import pyplot as plt


def one_game():
    TI = ["Spy", "Lookout", "Investigator", "Sheriff"]
    TP = ["Bodyguard", "Doctor"]
    TK = ["Jailor", "Vigilante", "Veteran"]
    TS = ["Mayor", "Medium", "Retributionist", "Transporter", "Escort"]
    unique_town = ["Jailor", "Mayor", "Veteran", "Retributionist"]
    
    #These are visiting townies who won't be on Jailor
    visiting_town = ["Investigator", "Sheriff", "Transporter"]
    
    all_town_roles = TI+TP+TK+TS
    
    townies = ["Jailor"]
    townies.append(random.choice(TI))
    townies.append(random.choice(TI))
    townies.append(random.choice(TP))
    townies.append("Veteran")
    townies.append(random.choice(TS))
    while len(townies) < 9:
        candidate = random.choice(all_town_roles)
        if not candidate in unique_town:
            townies.append(candidate)
        elif not candidate in townies:
            townies.append(candidate)
    
    dead_townies = []
    for x in townies:
        if x in visiting_town:
            p = random.random()
            if x != "Transporter" and p < 1/13:
                dead_townies.append(x)
            elif x == "Transporter" and p < 2/13:
                dead_townies.append(x)
    
    dead_evils = []
    for i in range(3):
        p = random.random()
        if p < 1/10:
            if i == 0:
                dead_evils.append("Mafioso")
            else:
                dead_evils.append("Random Mafia number {}".format(i))
    
    
    p = random.random()
    if p < 1/13:
        dead_evils.append("Witch")
    
    return len(dead_townies), len(dead_evils)
    
def main(n = 10_000):
    
    data = np.zeros(shape = (n,2), dtype = int)
    for i in range(n):
        data[i, :] = one_game()
    
    
    print("In 1000 games, you will kill about {} townies and {} evils.".format(int(round(data[:,0].mean()*1000)), int(round(data[:,1].mean()*1000))))

if __name__ == '__main__':
    main()