# Code modified for Code Ocean publication
from simpful import *
#from matplotlib import pyplot as plt

class Fuzzy:
    def __init__(self, cpu_value, mem_value, truput_value):
        self.cpu_val = cpu_value
        self.mem_val = mem_value
        self.truput_val = truput_value
        print("Cpu val "+str(cpu_value)+" Mem Val "+str(mem_value)+" Thruput Val "+ str(truput_value))
        # all input valur in integer
        # input : Cpu Val, RAM mem val, throughput Value
        # cpu val range : 0 - 100%
        # RAM mem val range : 0 - 100%
        # throughput val range : normalized 0 - 100%
        # output : load = load window change
        # load val range = -0.6 - 0.4
        # A simple decision support model
        # Create a fuzzy system object
        FS = FuzzySystem()

        # Define fuzzy sets for the variable CPU
        C1 = FuzzySet(function=Trapezoidal_MF(a=-40, b=-10, c=20, d=60), term="low")
        C2 = FuzzySet(function=Trapezoidal_MF(a=10, b=40, c=60, d=90), term="medium")
        C3 = FuzzySet(function=Trapezoidal_MF(a=40, b=80, c=110, d=140), term="high")
        LV1 = LinguisticVariable([C1,C2,C3], concept="CPU Usage", universe_of_discourse=[0,100])
        FS.add_linguistic_variable("CPU", LV1)
        #LV1.plot()

        # Define fuzzy sets for the variable MEMORY
        M1 = FuzzySet(function=Trapezoidal_MF(a=-40, b=-10, c=20, d=60), term="low")
        M2 = FuzzySet(function=Trapezoidal_MF(a=10, b=40, c=60, d=90), term="medium")
        M3 = FuzzySet(function=Trapezoidal_MF(a=40, b=80, c=110, d=140), term="high")
        LV2 = LinguisticVariable([M1,M2,M3], concept="Memory Usage", universe_of_discourse=[0,100])
        FS.add_linguistic_variable("MEMORY", LV2)
        #LV2.plot()

        # Define fuzzy sets for the variable NETWORK
        N1 = FuzzySet(function=Trapezoidal_MF(a=-40, b=-10, c=20, d=60), term="low")
        N2 = FuzzySet(function=Trapezoidal_MF(a=10, b=40, c=60, d=90), term="medium")
        N3 = FuzzySet(function=Trapezoidal_MF(a=40, b=80, c=110, d=140), term="high")
        LV3 = LinguisticVariable([N1,N2,N3], concept="Network Usage", universe_of_discourse=[0,100])
        FS.add_linguistic_variable("NETWORK", LV3)
        #LV3.plot()

        # Define output fuzzy sets and linguistic variable
        L_1 = FuzzySet(function=Trapezoidal_MF(a=-0.7, b=-0.65, c=-0.55, d=-0.5), term="ed")
        L_2 = FuzzySet(function=Triangular_MF(a=-0.6, b=-0.5, c=-0.4), term="vfd")
        L_3 = FuzzySet(function=Triangular_MF(a=-0.5, b=-0.4, c=-0.3), term="fd")
        L_4 = FuzzySet(function=Triangular_MF(a=-0.4, b=-0.3, c=-0.2), term="d")
        L_5 = FuzzySet(function=Triangular_MF(a=-0.3, b=-0.2, c=-0.1), term="sd")
        L_6 = FuzzySet(function=Triangular_MF(a=-0.2, b=-0.1, c=0), term="vsd")
        L_7 = FuzzySet(function=Triangular_MF(a=-0.1, b=0, c=0.1), term="nc")
        L_8 = FuzzySet(function=Triangular_MF(a=0, b=0.1, c=0.2), term="si")
        L_9 = FuzzySet(function=Triangular_MF(a=0.1, b=0.2, c=0.3), term="i")
        L_10 = FuzzySet(function=Triangular_MF(a=0.2, b=0.3, c=0.4), term="fi")
        L_11 = FuzzySet(function=Trapezoidal_MF(a=0.3, b=0.35, c=0.45, d=0.5), term="vfi")
        #FS.add_linguistic_variable("LoadChange", LinguisticVariable([L_1,L_2,L_3,L_4,L_5,L_6,L_7,L_8,L_9,L_10,L_11], universe_of_discourse=[-0.6,0.4]))
        LV4 = LinguisticVariable([L_1,L_2,L_3,L_4,L_5,L_6,L_7,L_8,L_9,L_10,L_11], concept="Load Window Change", universe_of_discourse=[-0.6,0.4])
        FS.add_linguistic_variable("LoadChange", LV4)

        # =======================================
        # Mamdani (max-min) inference method:
        # * min because of logic 'and' connective.
        # 1) ed_degree <-> loadchange_ed
        # 2) vfd_degree <-> loadchange_vfd
        # 3) fd_degree <-> loadchange_fd
        # 4) dec_degree <-> loadchange_dec
        # 5) sd_degree <-> loadchange_sd
        # 6) vsd_degree <-> loadchange_vsd
        # 7) nc_degree <-> loadchange_nc
        # 8) si_degree <-> loadchange_si
        # 9) inc_degree <-> loadchange_inc
        # 10) fi_degree <-> loadchange_fi
        # 11) vfi_degree <-> loadchange_vfi

        # Define the fuzzy rules
        RULE1 = "IF (CPU IS low) AND (MEMORY IS low) AND (NETWORK IS low) THEN (LoadChange IS vfi)"
        RULE2 = "IF (CPU IS low) AND (MEMORY IS medium) AND (NETWORK IS low) THEN (LoadChange IS fi)"
        RULE3 = "IF (CPU IS low) AND (MEMORY IS high) AND (NETWORK IS high) THEN (LoadChange IS sd)"
        RULE4 = "IF (CPU IS medium) AND (MEMORY IS low) AND (NETWORK IS low) THEN (LoadChange IS i)"
        RULE5 = "IF (CPU IS medium) AND (MEMORY IS medium) AND (NETWORK IS low) THEN (LoadChange IS si)"
        RULE6 = "IF (CPU IS medium) AND (MEMORY IS medium) AND (NETWORK IS medium) THEN (LoadChange IS nc)"
        RULE7 = "IF (CPU IS medium) AND (MEMORY IS high) AND (NETWORK IS high) THEN (LoadChange IS d)"
        RULE8 = "IF (CPU IS high) AND (MEMORY IS low) AND (NETWORK IS high) THEN (LoadChange IS fd)"
        RULE9 = "IF (CPU IS high) AND (MEMORY IS medium) AND (NETWORK IS medium) THEN (LoadChange IS vfd)"
        RULE10 = "IF (CPU IS high) AND (MEMORY IS high) AND (NETWORK IS high) THEN (LoadChange IS ed)"

        # Add fuzzy rules to the fuzzy reasoner object
        FS.add_rules([RULE1,RULE2,RULE3,RULE4,RULE5,RULE6,RULE7,RULE8,RULE9,RULE10])

        # Set antecedent values
        FS.set_variable("CPU", self.cpu_val)
        FS.set_variable("MEMORY", self.mem_val)
        FS.set_variable("NETWORK", self.truput_val)

        # Perform Sugeno inference and print output
        #print(FS.Sugeno_inference(["Sepsis"]))
        # Perform Mamdani inference and print output
        self.outputFuzzy = FS.Mamdani_inference(["LoadChange"])

    def get_fuzzy(self):
        print("Hasil deFuzzy = "+ str(self.outputFuzzy))
        # return float or int
        return self.outputFuzzy
