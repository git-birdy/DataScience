#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 17:56:11 2022

@author: katherine vickstrom

dice roll simulator
"""

import numpy as np

def roll():
    dice = np.random.choice(6, 10000) + 1
    return dice

roll1 = roll()
fraction = np.count_nonzero(roll1 == 5) / 10000
print("The fraction of 10000 dice rolls that are 5 is:", fraction)

roll2 = roll() + roll()
fraction = np.count_nonzero(roll2 == 3) / 10000
print("The fraction of 10000 dice rolls that are 3 is:", fraction)
