import sys
sys.path.append('/home/kgurusha/Documents/CMU/15816/ltl-explainability/src')

from main import Ltl2Regex
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
print("Found TACAS counter formulas: ", len(tacas_counter_ltls)) # very long formulas, 1000+ chars

# acacia formulas
base_path = 'ApplicationBenchmarks/acacia_orig_source/acacia/examples/example/'

acacia_ltls = []
for i in range(1,24):
    f = open(base_path + 'demo-v' + str(i) + '.ltl', 'r')
    acacia_ltls.append(f.read())
print("Found acacia formulas: ", len(acacia_ltls))


ltls = aac_ltls #+ acacia_ltls (needs formatting) #+ tacas_counter_ltls (takes too long to compute)
regexs = [tl.ltl2regex(ltl) for ltl in ltls]
tllens = [len(wregex) for wregex in regexs]

print("\n")
print("Number of formulas: ", len(ltls))
print("Mean timeline length: ", np.mean(tllens))


