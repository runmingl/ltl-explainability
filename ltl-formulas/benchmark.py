import sys
sys.path.append('/home/kgurusha/Documents/CMU/15816/ltl-explainability/src')

from main import *
tl = Ltl2Regex()

import re
import numpy as np
import matplotlib.pyplot as plt

# AAC formulas
aac_file = open('AAC_Communication_Protocol.ltl', 'r')
aac_specs = aac_file.readlines()
aac_ltls = [spec.split(' ', 1)[1] for spec in aac_specs]
print("Found AAC formulas: ", len(aac_ltls))

# RV11 formulas
# tacas08 counter formulas 
base_path = 'ApplicationBenchmarks/AlaskaBenchmarks/tacas08_experiments/counter/'

tacas_counter_ltls = []
for i in range(2, 17):
    f = open(base_path + 'counter_' + str(i) + '.ltl', 'r')
    tacas_counter_ltls.append(f.read())
print("Found TACAS counter formulas: ", len(tacas_counter_ltls), ". Didn't use") # very long formulas, 1000+ chars, not useful

# acacia formulas
base_path = 'ApplicationBenchmarks/acacia_orig_source/acacia/examples/example/'

acacia_ltls = []
for i in range(1,24): 
    f = open(base_path + 'demo-v' + str(i) + '.ltl', 'r')
    lines = f.readlines()
    # strip comments, clause 'assume' tags and '\n's
    lines = [line.split('#', 1)[0].replace('assume', '').strip() for line in lines]
    # formulas are semicolon seperated 
    ltls = " ".join(lines).split(';')[:-1]
    # treat each formula (within examples) as seperate case (is this what we want?) 
    acacia_ltls += ltls 
    
print("Found acacia formulas: ", len(acacia_ltls))


# Boeing formulas
f = open('wbs-ltlspecs.txt', 'r')
lines = f.readlines()
wbs_ltls = [line.split(':= ',1)[1][:-2] for line in lines]
wbs_ltls = list(set(wbs_ltls))

def clean_ltl(ltl):
    ltl = re.sub(r'(\w+)\s*(>|<|>=|<=|=|!=)\s*(\w+)', r'\1_cmp_\3', ltl) # var1 <cmp> var2/num => var1_cmp_var2
    ltl = ltl.replace('next', 'X') 
    ltl = ltl.replace('= rolling', '') # wheel status = rolling is treated as wheel status is true
    ltl = re.sub(r'([\w()]+)\s*=\s*stopped', r'!\1', ltl) # 'stopped' wheel status is false
    return ltl

wbs_ltls = [clean_ltl(ltl) for ltl in wbs_ltls if not re.search(r'\)\s*=\s*(\d+)', ltl)] # give up on making sense of 14 formulas containing <large_exp> = <num>

print("Found Boeing formulas: ", len(wbs_ltls))


# Compute metrics 

ltls = aac_ltls # + acacia_ltls # + wbs_ltls
ltls += [ltl for ltl in acacia_ltls if len(ltl) < 170]  # len > takes too long
# use len < 120 for nice plot, use len < 170 for computable cases that blow up 
ltls = [ltl.strip() for ltl in ltls]

ltllens = [len(re.findall(r'\b\w+\b|[GFXUR]|[&|(->)!]', ltl)) for ltl in ltls] # len(r'\b\w+\b|[GFXUR]|[&|->!]')
regexs = [tl.ltl2regex(ltl) for ltl in ltls]
tllens = [len(wregex) for wregex in regexs]
star_heights = [OmegaRegex.star_height(wregex) for wregex in regexs]

print("\nNumber of formulas: ", len(ltls))
print("\nLTL Formula lengths: ", ltllens)
print("\nTimeline lengths: ", tllens)
print("\nStar heights: ", star_heights)
print("\nMean timeline length: ", np.mean(tllens))

file = open('benchmark-ltls.txt','w')
for ltl in ltls:
	file.write(ltl+"\n")
file.close()
print("\nWrote ltl-formulas to benchmark-ltls.txt")


fig1 = plt.figure()
plt.xlabel('Length of LTL Formula')
plt.ylabel('Star height')
plt.scatter(ltllens, star_heights)
plt.savefig("star-height-graph.png")
print("Saved star height plot to star-height-graph.png")

fig1 = plt.figure()
plt.xlabel('Length of LTL Formula')
plt.ylabel('Timeline lengths')

for idx in range(len(ltls)-2):
    if tllens[idx] > 50000:
        tllens.pop(idx)
        ltllens.pop(idx)
        # use log or other scaling instead
plt.scatter(ltllens, tllens)
plt.savefig("tllens-graph.png")
print("Saved timeline length plot to tllens-graph.png")

#LTL Formula lengths:  [42, 42, 34, 40, 54, 50, 61, 25, 33, 61, 25, 33, 156, 26, 109, 55, 47, 59, 39, 75, 18, 18, 17, 23, 23, 18, 18, 18, 17, 17, 17, 23, 23, 23, 24, 24, 10, 17, 17, 17, 24, 24, 24, 10, 17, 17, 17, 17, 17, 17, 121, 5, 30, 20, 20, 32, 32, 42, 42, 18, 20, 12, 14, 14, 14, 14, 14, 14, 49, 49, 49, 49, 14, 14, 14, 14, 14, 14, 24, 20, 10, 27, 68, 20, 23, 20, 63]
#Timeline lengths:  [5, 9, 1, 5, 5, 5, 41, 9, 21, 113, 9, 21, 86042, 9, 170, 6, 5, 5, 6, 21, 5, 5, 1, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 9, 9, 5, 1, 1, 1, 9, 9, 9, 5, 1, 1, 1, 1, 1, 1, 303958, 2, 9, 5, 9, 9, 9, 9, 9, 1, 5, 5, 1, 1, 1, 1, 1, 1, 113, 113, 113, 113, 1, 1, 1, 1, 1, 1, 2, 1, 5, 9, 69, 5, 5, 9, 7]
#Star heights:  [1, 1, 0, 1, 1, 1, 2, 1, 2, 3, 1, 2, 8, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 8, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1]

#LTL Formula lengths:  [15, 15, 9, 15, 15, 15, 39, 14, 18, 39, 14, 18, 93, 20, 75, 38, 36, 42, 33, 59, 14, 14, 13, 16, 16, 14, 14, 14, 13, 13, 13, 16, 16, 16, 20, 20, 9, 13, 13, 13, 20, 20, 20, 9, 13, 13, 13, 13, 13, 13, 84, 3, 20, 14, 14, 20, 20, 26, 26, 10, 14, 9, 10, 10, 10, 10, 10, 10, 39, 39, 39, 39, 10, 10, 10, 10, 10, 10, 11, 10, 9, 20, 55, 14, 14, 16, 53]

#Timeline lengths:  [5, 9, 1, 5, 5, 5, 41, 9, 21, 113, 9, 21, 86042, 9, 170, 6, 5, 5, 6, 21, 5, 5, 1, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 9, 9, 5, 1, 1, 1, 9, 9, 9, 5, 1, 1, 1, 1, 1, 1, 303958, 2, 9, 5, 9, 9, 9, 9, 9, 1, 5, 5, 1, 1, 1, 1, 1, 1, 113, 113, 113, 113, 1, 1, 1, 1, 1, 1, 2, 1, 5, 9, 69, 5, 5, 9, 7]

#Star heights:  [1, 1, 0, 1, 1, 1, 2, 1, 2, 3, 1, 2, 8, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 8, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1]

