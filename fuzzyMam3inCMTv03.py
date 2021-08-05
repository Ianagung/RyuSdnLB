import numpy as np
import skfuzzy as fuzz
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
        x_cpu = np.arange(0, 100, 1)
        x_mem = np.arange(0, 100, 1)
        x_truput = np.arange(0, 100, 1)
        x_load = np.arange(-0.6, 0.4, 0.01)


        # Membership functions
        cpu_low = fuzz.trapmf(x_truput, [-40, -10, 20, 60 ])
        cpu_medium = fuzz.trapmf(x_truput, [10, 40, 60, 90 ])
        cpu_high = fuzz.trapmf(x_truput, [40, 80, 110, 140 ])

        mem_low = fuzz.trapmf(x_truput, [-40, -10, 20, 60 ])
        mem_medium = fuzz.trapmf(x_truput, [10, 40, 60, 90 ])
        mem_high = fuzz.trapmf(x_truput, [40, 80, 110, 140 ])
        
        truput_low = fuzz.trapmf(x_truput, [-40, -10, 20, 60 ])
        truput_medium = fuzz.trapmf(x_truput, [10, 40, 60, 90 ])
        truput_high = fuzz.trapmf(x_truput, [40, 80, 110, 140 ])

        load_extdec = fuzz.trapmf(x_load, [-0.7, -0.65, -0.55, -0.5 ])
        load_veryfastdec = fuzz.trimf(x_load, [ -0.6, -0.5, -0.4 ])
        load_fastdec = fuzz.trimf(x_load, [ -0.5, -0.4, -0.3 ])
        load_dec = fuzz.trimf(x_load, [ -0.4, -0.3, -0.2 ])
        load_smalldec = fuzz.trimf(x_load, [ -0.3, -0.2, -0.1 ])
        load_verysmalldec = fuzz.trimf(x_load, [ -0.2, -0.1, 0 ])
        load_nochange = fuzz.trimf(x_load, [-0.1, 0, 0.1 ])
        load_smallincrease = fuzz.trimf(x_load, [ 0, 0.1, 0.2 ])
        load_increase = fuzz.trimf(x_load, [ 0.1, 0.2, 0.3 ])
        load_fastincrease = fuzz.trimf(x_load, [ 0.2, 0.3, 0.4 ])
        load_veryfastincrease = fuzz.trapmf(x_load, [0.3, 0.35, 0.45, 0.5 ])

        # Input: score
        cpu_score = self.cpu_val 
        mem_score = self.mem_val
        truput_score = self.truput_val

        cpu_low_degree = fuzz.interp_membership(
            x_cpu, cpu_low, cpu_score)
        cpu_medium_degree = fuzz.interp_membership(
            x_cpu, cpu_medium, cpu_score)
        cpu_high_degree = fuzz.interp_membership(
            x_cpu, cpu_high, cpu_score)

        mem_low_degree = fuzz.interp_membership(
            x_mem, mem_low, mem_score)
        mem_medium_degree = fuzz.interp_membership(
            x_mem, mem_medium, mem_score)
        mem_high_degree = fuzz.interp_membership(
            x_mem, mem_high, mem_score)

        thruput_low_degree = fuzz.interp_membership(
            x_truput, truput_low, truput_score)
        thruput_medium_degree = fuzz.interp_membership(
            x_truput, truput_medium, truput_score)
        thruput_high_degree = fuzz.interp_membership(
            x_truput, truput_high, truput_score)

        # Whole config
        #fig_scale_x = 2.0
        #fig_scale_y = 1.5
        #fig = plt.figure(figsize=(6.4 * fig_scale_x, 6.4 * fig_scale_y))
        #row = 3
        #col = 3 

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

        # Apply Fuzzy Rule
        vfi_degree = np.fmax(cpu_low_degree, 
            np.fmax(mem_low_degree, thruput_low_degree))
        fi_degree = np.fmax(cpu_low_degree, 
            np.fmax(mem_medium_degree, thruput_low_degree))
        sd_degree = np.fmax(cpu_low_degree, 
            np.fmax(mem_high_degree, thruput_high_degree))
        inc_degree = np.fmax(cpu_medium_degree, 
            np.fmax(mem_low_degree, thruput_low_degree))
        si_degree = np.fmax(cpu_medium_degree, 
            np.fmax(mem_medium_degree, thruput_low_degree))
        nc_degree = np.fmax(cpu_medium_degree, 
            np.fmax(mem_medium_degree, thruput_medium_degree))
        dec_degree = np.fmax(cpu_medium_degree, 
            np.fmax(mem_high_degree, thruput_high_degree))
        fd_degree = np.fmax(cpu_high_degree, 
            np.fmax(mem_low_degree, thruput_high_degree))
        vfd_degree = np.fmax(cpu_high_degree, 
            np.fmax(mem_medium_degree, thruput_medium_degree))
        ed_degree = np.fmax(cpu_high_degree, 
            np.fmax(mem_high_degree, thruput_high_degree))

        # Apply IMPLICATION or ACTIVATION
        activation_extdec = np.fmin(ed_degree, load_extdec)
        activation_veryfastdec = np.fmin(vfd_degree, load_veryfastdec)
        activation_fastdec = np.fmin(fd_degree, load_fastdec)
        activation_dec = np.fmin(dec_degree, load_dec)
        activation_smalldec = np.fmin(sd_degree, load_smalldec)
        #activation_verysmalldec = np.fmin(vsd_degree, load_verysmalldec)
        activation_nochange = np.fmin(nc_degree, load_nochange)
        activation_smallinc = np.fmin(si_degree, load_smallincrease)
        activation_increase = np.fmin(inc_degree, load_increase)
        activation_fastinc = np.fmin(fi_degree, load_fastincrease)
        activation_veryfastinc = np.fmin(vfi_degree, load_veryfastincrease)

        # AGGREGATION
        # Apply the rules:
        # * max for aggregation, like or the cases
        # aggregated1 = np.fmax(
        #     activation_extdec,
        #     np.fmax(activation_veryfastdec, activation_fastdec))
        # aggregated2 = np.fmax(
        #     activation_dec,
        #     np.fmax(activation_smalldec, activation_verysmalldec))
        # aggregated3 = np.fmax(
        #     activation_nochange,
        #     np.fmax(activation_smallinc, activation_increase))
        # aggregated4 = np.fmax(
        #     activation_fastinc,
        #     np.fmax(activation_veryfastinc, aggregated1))
        # aggregated5 = np.fmax(
        #     aggregated2,
        #     np.fmax(aggregated3, aggregated4))

        aggregated = np.fmax(activation_veryfastinc, np.fmax(activation_fastinc, 
            np.fmax(activation_increase, np.fmax(activation_smallinc, 
            #np.fmax(activation_nochange, np.fmax(activation_verysmalldec, 
            np.fmax(activation_nochange,
            np.fmax(activation_smalldec, np.fmax(activation_dec, 
            np.fmax( activation_fastdec, np.fmax(activation_extdec, activation_veryfastdec)))))))))

        # Defuzzification
        # skfuzzy.defuzz(x, mfx, mode)[source]
        # Parameters:   
        # x : 1d array or iterable, length N

        # Independent variable.
        # mfx : 1d array of iterable, length N

        # Fuzzy membership function.
        # mode : string

        # Controls which defuzzification method will be used. * ‘centroid’: Centroid of area * ‘bisector’: bisector of area * ‘mom’ : mean of maximum * ‘som’ : min of maximum * ‘lom’ : max of maximum
        # Defuzzification of a membership function, returning a defuzzified value of the function at x, using various defuzzification methods.
        # Returns:  u : float or int Defuzzified result.

        self.tip_centroid = fuzz.defuzz(x_load, aggregated, 'centroid')
        self.tip_bisector = fuzz.defuzz(x_load, aggregated, 'bisector')
        self.tip_mom = fuzz.defuzz(x_load, aggregated, "mom")
        self.tip_som = fuzz.defuzz(x_load, aggregated, "som")
        self.tip_lom = fuzz.defuzz(x_load, aggregated, "lom")

        # print(tip_centroid)
        # print(tip_bisector)
        # print(tip_mom)
        # print(tip_som)
        # print(tip_lom)

    def get_fuzzy(self):
        defuzz_val = self.tip_centroid
        print("Hasil deFuzzy = "+ str(self.tip_bisector))
        # return float or int
        return defuzz_val
