import numpy as np
import skfuzzy as fuzz
from matplotlib import pyplot as plt

def fuzzy_mamdani(cpu_val, mem_val, rsp_time_val)
    # Problem: from service quality and food quality to tip amount
    x_cpu = np.arange(0, 1.01, 0.1)
    x_mem = np.arange(0, 1.01, 0.1)
    x_rsptmstddev = np.arange(0, 1.01, 0.1)
    x_load = np.arange(-0.6, 0.4, 0.1)


    # Membership functions
    cpu_verylow = fuzz.trapmf(x_cpu, [-0.2, -0.1, 0.1, 0.4 ])
    cpu_low = fuzz.trapmf(x_cpu, [-0.1, 0.2, 0.3, 0.6 ])
    cpu_medium = fuzz.trapmf(x_cpu, [0.1, 0.45, 0.55, 0.9 ])
    cpu_high = fuzz.trapmf(x_cpu, [0.4, 0.7, 0.8, 1.1 ])
    cpu_veryhigh = fuzz.trapmf(x_cpu, [0.6, 0.95, 1.05, 1.4 ])

    mem_verylow = fuzz.trapmf(x_mem, [-0.2, -0.1, 0.1, 0.4 ])
    mem_low = fuzz.trapmf(x_mem, [-0.1, 0.2, 0.3, 0.6 ])
    mem_medium = fuzz.trapmf(x_mem, [0.1, 0.45, 0.55, 0.9 ])
    mem_high = fuzz.trapmf(x_mem, [0.4, 0.7, 0.8, 1.1 ])
    mem_veryhigh = fuzz.trapmf(x_mem, [0.6, 0.95, 1.05, 1.4 ])

    rsptmstddev_low = fuzz.trapmf(x_rsptmstddev, [-0.1, -0.01, 0.2, 0.6 ])
    rsptmstddev_medium = fuzz.trapmf(x_rsptmstddev, [0.1, 0.4, 0.6, 1 ])
    rsptmstddev_high = fuzz.trapmf(x_rsptmstddev, [0.5, 0.8, 1, 1.3 ])

    load_extdec = fuzz.trapmf(x_load, [-0.7, -0.65, 0.55, 0.5 ])
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

    # Input: service score and food score
    cpu_score = cpu_val / 100
    mem_score = mem_val / 100
    rsptime_score = rsp_time_val

    cpu_verylow_degree = fuzz.interp_membership(
        x_cpu, cpu_verylow, cpu_score)
    cpu_low_degree = fuzz.interp_membership(
        x_cpu, cpu_low, cpu_score)
    cpu_medium_degree = fuzz.interp_membership(
        x_cpu, cpu_medium, cpu_score)
    cpu_high_degree = fuzz.interp_membership(
        x_cpu, cpu_high, cpu_score)
    cpu_veryhigh_degree = fuzz.interp_membership(
        x_cpu, cpu_veryhigh, cpu_score)

    mem_verylow_degree = fuzz.interp_membership(
        x_cpu, mem_verylow, cpu_score)
    mem_low_degree = fuzz.interp_membership(
        x_cpu, mem_low, cpu_score)
    mem_medium_degree = fuzz.interp_membership(
        x_cpu, mem_medium, cpu_score)
    mem_high_degree = fuzz.interp_membership(
        x_cpu, mem_high, cpu_score)
    mem_veryhigh_degree = fuzz.interp_membership(
        x_cpu, mem_veryhigh, cpu_score)

    rsptmstddev_low_degree = fuzz.interp_membership(
        x_rsptmstddev, rsptmstddev_low, cpu_score)
    rsptmstddev_medium_degree = fuzz.interp_membership(
        x_rsptmstddev, rsptmstddev_medium, cpu_score)
    rsptmstddev_high_degree = fuzz.interp_membership(
        x_rsptmstddev, rsptmstddev_high, cpu_score)


    # Whole config
    fig_scale_x = 2.0
    fig_scale_y = 1.5
    fig = plt.figure(figsize=(6.4 * fig_scale_x, 6.4 * fig_scale_y))
    row = 3
    col = 3

    plt.subplot(row, col, 1)
    plt.title("CPU Usage")
    plt.plot(x_cpu, cpu_verylow, label="verylow", marker=".")
    plt.plot(x_cpu, cpu_low, label="low", marker=".")
    plt.plot(x_cpu, cpu_medium, label="medium", marker=".")
    plt.plot(x_cpu, cpu_high, label="high", marker=".")
    plt.plot(x_cpu, cpu_veryhigh, label="veryhigh", marker=".")
    plt.plot(cpu_score, 0.0, label="cpu_score", marker="D")
    plt.plot(cpu_score, cpu_verylow_degree,
             label="verylow degree", marker="o")
    plt.plot(cpu_score, cpu_low_degree,
             label="low degree", marker="o")
    plt.plot(cpu_score, cpu_medium_degree,
             label="medium degree", marker="o")
    plt.plot(cpu_score, cpu_high_degree,
             label="high degree", marker="o")
    plt.plot(cpu_score, cpu_veryhigh_degree,
             label="veryhigh degree", marker="o")
    plt.legend(loc="upper left")

    plt.subplot(row, col, 2)
    plt.title("Memory Usage")
    plt.plot(x_mem, mem_verylow, label="verylow", marker=".")
    plt.plot(x_mem, mem_low, label="low", marker=".")
    plt.plot(x_mem, mem_medium, label="medium", marker=".")
    plt.plot(x_mem, mem_high, label="high", marker=".")
    plt.plot(x_mem, mem_veryhigh, label="veryhigh", marker=".")
    plt.plot(mem_score, 0.0, label="memory_score", marker="D")
    plt.plot(mem_score, mem_verylow_degree,
             label="verylow degree", marker="o")
    plt.plot(mem_score, mem_low_degree,
             label="low degree", marker="o")
    plt.plot(mem_score, mem_medium_degree,
             label="medium degree", marker="o")
    plt.plot(mem_score, mem_high_degree,
             label="high degree", marker="o")
    plt.plot(mem_score, mem_veryhigh_degree,
             label="veryhigh degree", marker="o")
    plt.legend(loc="upper left")

    plt.subplot(row, col, 3)
    plt.title("Respon Time Standar Deviation")
    plt.plot(x_rsptmstddev, rsptmstddev_low, label="low", marker=".")
    plt.plot(x_rsptmstddev, rsptmstddev_medium, label="medium", marker=".")
    plt.plot(x_rsptmstddev, rsptmstddev_high, label="high", marker=".")
    plt.plot(rsptime_score, 0.0, label="respontime_score", marker="D")
    plt.plot(rsptime_score, rsptmstddev_low_degree,
             label="low degree", marker="o")
    plt.plot(rsptime_score, rsptmstddev_medium_degree,
             label="medium degree", marker="o")
    plt.plot(rsptime_score, rsptmstddev_high_degree,
             label="high degree", marker="o")
    plt.legend(loc="upper left")

    plt.subplot(row, col, 4)
    plt.title("Change Load Window")
    plt.plot(x_load, load_extdec, label="extdecrease", marker=".")
    plt.plot(x_load, load_veryfastdec, label="veryfastdecrease", marker=".")
    plt.plot(x_load, load_fastdec, label="fastdecrease", marker=".")
    plt.plot(x_load, load_dec, label="decrease", marker=".")
    plt.plot(x_load, load_smalldec, label="smalldecrease", marker=".")
    plt.plot(x_load, load_verysmalldec, label="verysmalldecrease", marker=".")
    plt.plot(x_load, load_nochange, label="nochange", marker=".")
    plt.plot(x_load, load_smallincrease, label="smallincrease", marker=".")
    plt.plot(x_load, load_increase, label="increase", marker=".")
    plt.plot(x_load, load_fastincrease, label="fastincrease", marker=".")
    plt.plot(x_load, load_veryfastincrease, label="veryfastincrease", marker=".")
    plt.legend(loc="upper left")   

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

    #extremely decrease load window value change
    ed_degree = np.fmax(cpu_veryhigh_degree,np.fmax(mem_veryhigh_degree, rsptmstddev_high_degree))
    #very fast decrease load window value change
    vfd_degree = np.fmax(cpu_high_degree,np.fmax(mem_veryhigh_degree, rsptmstddev_high_degree))
    #fast decrease load window value change
    fd_degree = np.fmax(cpu_veryhigh_degree,np.fmax(mem_medium, rsptmstddev_medium))
    #decrease load window value change
    dec_degree = np.fmax(cpu_high_degree,np.fmax(mem_medium_degree, rsptmstddev_medium_degree))
    #small decrease load window value change
    sd_degree = np.fmax(cpu_low_degree,np.fmax(mem_high_degree, rsptmstddev_medium_degree))
    #very small decrease load window value change
    vsd_degree = np.fmax(cpu_high_degree,np.fmax(mem_verylow_degree, rsptmstddev_low_degree))
    #no change load window value change
    nc_degree = np.fmax(cpu_medium_degree,np.fmax(mem_medium_degree, rsptmstddev_medium_degree))
    #small increase load window value change
    si_degree = np.fmax(cpu_low_degree,np.fmax(mem_medium_degree, rsptmstddev_medium_degree))
    #increase load window value change
    inc_degree = np.fmax(cpu_low_degree,np.fmax(mem_low_degree, rsptmstddev_low_degree))
    #fast increase load window value change
    fi_degree = np.fmax(cpu_verylow_degree,np.fmax(mem_low_degree, rsptmstddev_low_degree))
    #very fast increase load window value change
    vfi_degree = np.fmax(cpu_verylow_degree,np.fmax(mem_verylow_degree, rsptmstddev_low_degree))

    plt.subplot(row, col, 5)
    plt.title("Some Fuzzy Rules")
    t = (   "ed_degree <-> loadchange_ed\n"
            "vfd_degree <-> loadchange_vfd\n"
            "fd_degree <-> loadchange_fd\n"
            "dec_degree <-> loadchange_dec\n"
            "sd_degree <-> loadchange_sd\n"
            "vsd_degree <-> loadchange_vsd\n"
            "nc_degree <-> loadchange_nc\n"
            "si_degree <-> loadchange_si\n"
            "inc_degree <-> loadchange_inc\n"
            "fi_degree <-> loadchange_fi\n"
            "vfi_degree <-> loadchange_vfi")
    plt.text(0.1, 0.5, t)

    activation_extdec = np.fmin(ed_degree, load_extdec)
    activation_veryfastdec = np.fmin(vfd_degree, load_veryfastdec)
    activation_fastdec = np.fmin(fd_degree, load_fastdec)
    activation_dec = np.fmin(dec_degree, load_dec)
    activation_smalldec = np.fmin(sd_degree, load_smalldec)
    activation_verysmalldec = np.fmin(vsd_degree, load_verysmalldec)
    activation_nochange = np.fmin(nc_degree, load_nochange)
    activation_smallinc = np.fmin(si_degree, load_smallincrease)
    activation_increase = np.fmin(inc_degree, load_increase)
    activation_fastinc = np.fmin(fi_degree, load_fastincrease)
    activation_veryfastinc = np.fmin(vfi_degree, load_veryfastincrease)

    plt.subplot(row, col, 6)
    plt.title("Tip Activation: Mamdani Inference Method")

    plt.plot(x_load, activation_extdec, label="load change ext decrease", marker=".")
    plt.plot(x_load, activation_veryfastdec, label="load change very fast ext decrease", marker=".")
    plt.plot(x_load, activation_fastdec, label="load change fast decrease", marker=".")
    plt.plot(x_load, activation_dec, label="load change decrease", marker=".")
    plt.plot(x_load, activation_smalldec, label="load change small decrease", marker=".")
    plt.plot(x_load, activation_verysmalldec, label="load change very small decrease", marker=".")
    plt.plot(x_load, activation_nochange, label="load change nochange", marker=".")
    plt.plot(x_load, activation_smallinc, label="load change small increase", marker=".")
    plt.plot(x_load, activation_increase, label="load change increase", marker=".")
    plt.plot(x_load, activation_fastinc, label="load change fast increase", marker=".")
    plt.plot(x_load, activation_veryfastinc, label="load change very fast increase", marker=".")
    plt.legend(loc="upper left")

    # Apply the rules:
    # * max for aggregation, like or the cases
    aggregated1 = np.fmax(
        activation_extdec,
        np.fmax(activation_veryfastdec, activation_fastdec))
    aggregated2 = np.fmax(
        activation_dec,
        np.fmax(activation_smalldec, activation_verysmalldec))
    aggregated3 = np.fmax(
        activation_nochange,
        np.fmax(activation_smallinc, activation_increase))
    aggregated4 = np.fmax(
        activation_fastinc,
        np.fmax(activation_veryfastinc, aggregated1))
    aggregated5 = np.fmax(
        aggregated2,
        np.fmax(aggregated3, aggregated4))

    # Defuzzification
    tip_centroid = fuzz.defuzz(x_load, aggregated5, 'centroid')
    tip_bisector = fuzz.defuzz(x_load, aggregated5, 'bisector')
    tip_mom = fuzz.defuzz(x_load, aggregated5, "mom")
    tip_som = fuzz.defuzz(x_load, aggregated5, "som")
    tip_lom = fuzz.defuzz(x_load, aggregated5, "lom")

    print(tip_centroid)
    print(tip_bisector)
    print(tip_mom)
    print(tip_som)
    print(tip_lom)

    plt.subplot(row, col, 6)
    plt.title("Aggregation and Defuzzification")
    plt.plot(x_load, aggregated5, label="fuzzy result", marker=".")
    plt.plot(tip_centroid, 0.0, label="centroid", marker="o")
    plt.plot(tip_bisector, 0.0, label="bisector", marker="o")
    plt.plot(tip_mom, 0.0, label="mom", marker="o")
    plt.plot(tip_som, 0.0, label="som", marker="o")
    plt.plot(tip_lom, 0.0, label="lom", marker="o")
    plt.legend(loc="upper left")

    plt.savefig("7-tipping-problem-mamdani.png")
    plt.show()