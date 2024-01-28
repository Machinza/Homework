# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 21:24:50 2024

@author: Aaron Tragle
"""

import numpy as np
import matplotlib.pyplot as plt

tries = 10000
d1 = 0
d2 = 0
nums = [2,3,4,5,6,7,8,9,10,11,12]
cts = np.zeros(11)

for i in range(0,tries):
    d1 = np.random.randint(1,7)
    d2 = np.random.randint(1,7)
    sumd = d1+d2
    if sumd == 2:
        cts[0]+=1
    if sumd == 3:
        cts[1]+=1
    if sumd == 4:
        cts[2]+=1
    if sumd == 5:
        cts[3]+=1
    if sumd == 6:
        cts[4]+=1
    if sumd == 7:
        cts[5]+=1
    if sumd == 8:
        cts[6]+=1
    if sumd == 9:
        cts[7]+=1
    if sumd == 10:
        cts[8]+=1
    if sumd == 11:
        cts[9]+=1
    if sumd == 12:
        cts[10]+=1
        
norm = max(cts)
for i in range(0,len(cts)):
    cts[i]/=norm
norm2 = min(cts)
for i in range(0,len(cts)):
    cts[i]/=norm2

plt.bar(nums, cts)
plt.title(f"Relative probabilities of rolling 2 D6 die {tries} times")
plt.ylabel("Relative probability")
plt.xlabel("Sum of the 2 D6 die")
plt.ylim(0,7)
plt.show()

#%% Hey, see you're here from the homework. Code for stddev is below

def x_squared(vals, probs, total):
    summation=0
    for i in range(0,len(vals)):
        summation+=vals[i]**2*probs[i]
    return(summation/total)

def x(vals, probs, total):
    summation=0
    for i in range(0,len(vals)):
        summation+=vals[i]*probs[i]
    return(summation/total)

def sigma(val1, val2):
    return np.sqrt(val1-(val2**2))

vals = [2,3,4,5,6,7,8,9,10,11,12]
exp = [1,2,1,2,8,6,4,2,1,1,2]
expct = 30
ideal = [1,2,3,4,5,6,5,4,3,2,1]
idealct = 36
sume=0

# <x> for experimental values
expect_experiment = x(vals, exp, expct)
print(f"Expectation value for experimental data: {expect_experiment}")

# <x> for ideal values
expect_ideal = x(vals, ideal, idealct)
print(f"Expectation value for ideal data: {expect_ideal}")

# <x^2> for experimental 
expect_experiment2 = x_squared(vals, exp, expct)

# <x^2> for ideal 
expect_ideal2 = x_squared(vals, ideal, idealct)

# Finally we can calculate our sigmas

sigma_i = sigma(expect_ideal2, expect_ideal)
print(f"Standard Deviation for ideal distribution is {sigma_i}")
sigma_e = sigma(expect_experiment2, expect_experiment)
print(f"Standard Deviation for experimental distribution is {sigma_e}")

    