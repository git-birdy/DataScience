#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:05:51 2022

@author: katherine
"""

import numpy as np

child1 = np.random.randint(1,3,10000)
child2 = np.random.randint(1,3,10000)

one_girl = np.sum((child1 == 2) | (child2 == 2))
both_girls = np.sum((child1 == 2) & (child2 == 2))
probability = both_girls / one_girl

elder_girl = np.sum(child1 == 2)
probability2 = both_girls / elder_girl
