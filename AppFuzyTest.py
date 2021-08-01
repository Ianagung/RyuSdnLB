#!/usr/bin/env python3

sys.path.append(".")
from fuzzyMam3inCMT import Fuzzy

#do fuzzy untuk setiap server  
myFuzzy = Fuzzy(cpu_val, mem_val, truput_val)
delta_ld_window = myFuzzy.get_fuzzy()

print("Perubahan Load Window Server- is %.2f" % (delta_ld_window))