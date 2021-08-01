#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import numpy as np
import skfuzzy as fuzz
import multitimer
import time
from matplotlib import pyplot as plt

sys.path.append(".")
from fuzzyMam3inCMT import Fuzzy

#do fuzzy untuk setiap server
cpu_val = 50
mem_val = 50
truput_val = 50 
myFuzzy = Fuzzy(cpu_val, mem_val, truput_val)
delta_ld_window = myFuzzy.get_fuzzy()

print("Perubahan Load Window Server- is %.2f" % (delta_ld_window))