import sys
sys.path.append('/home/kgurusha/Documents/CMU/15816/ltl-explainability/src')

from main import *
tl = Ltl2Regex()

import numpy as np

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

# acacsia formulas
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

ltls = aac_ltls # + tacas_counter_ltls (takes too long to compute)
ltls += [ltl for ltl in acacia_ltls if len(ltl) < 170] # len > takes too long
# use len < 120 for nice plot, use len < 170 for computable cases that blow up

ltllens = [len(ltl.strip()) for ltl in ltls]
regexs = [tl.ltl2regex(ltl) for ltl in ltls]
tllens = [len(wregex) for wregex in regexs]
star_heights = [OmegaRegex.star_height(wregex) for wregex in regexs]

print("\nNumber of formulas: ", len(ltls))
print("\nLTL Formula lengths: ", ltllens)
print("\nTimeline lengths: ", tllens)
print("\nStar heights: ", star_heights)
print("\nMean timeline length: ", np.mean(tllens))

#LTL Formula lengths:  [42, 42, 34, 40, 54, 50, 61, 25, 33, 61, 25, 33, 156, 26, 109, 55, 47, 59, 39, 75, 18, 18, 17, 23, 23, 18, 18, 18, 17, 17, 17, 23, 23, 23, 24, 24, 10, 17, 17, 17, 24, 24, 24, 10, 17, 17, 17, 17, 17, 17, 121, 5, 30, 20, 20, 32, 32, 42, 42, 18, 20, 12, 14, 14, 14, 14, 14, 14, 49, 49, 49, 49, 14, 14, 14, 14, 14, 14, 24, 20, 10, 27, 68, 20, 23, 20, 63]
#Timeline lengths:  [5, 9, 1, 5, 5, 5, 41, 9, 21, 113, 9, 21, 86042, 9, 170, 6, 5, 5, 6, 21, 5, 5, 1, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 9, 9, 5, 1, 1, 1, 9, 9, 9, 5, 1, 1, 1, 1, 1, 1, 303958, 2, 9, 5, 9, 9, 9, 9, 9, 1, 5, 5, 1, 1, 1, 1, 1, 1, 113, 113, 113, 113, 1, 1, 1, 1, 1, 1, 2, 1, 5, 9, 69, 5, 5, 9, 7]
#Star heights:  [1, 1, 0, 1, 1, 1, 2, 1, 2, 3, 1, 2, 8, 1, 3, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 8, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 1, 1, 1, 1]

