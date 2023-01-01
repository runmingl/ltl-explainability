import sys
sys.path.append('/home/kgurusha/Documents/CMU/15816/ltl-explainability/src')

from main import Ltl2Regex
tl = Ltl2Regex()

aac_file = open('AAC_Communication_Protocol.ltl', 'r')
specs = aac_file.readlines()
ltls = [spec.split(' ', 1)[1] for spec in specs]
regexs = [tl.ltl2regex(ltl) for ltl in ltls]
tllens = [len(wregex) for wregex in regexs]

print("AAC timeline lengths", tllens)

