import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']=['Times New Roman'] + plt.rcParams['font.serif']
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size']=25

color_names = list(mcolors.XKCD_COLORS)

cm = 1/2.54

# File designed to recover and plot results in order to study cavitation onset and collapse with the two interaction models
# This test case is inspired by https://doi.org/10.1063/1.3265547

######### Step 1 : Recovering data ##################################################################################################################

inttype_list = ["NI", "IC", "QA"]

dic_2_bubbles = {}

working_path = os.getcwd()

for inttype in inttype_list :
    if inttype not in list(dic_2_bubbles.keys()) :
        dic_2_bubbles[inttype] = {}

    inttype_path = os.path.join(working_path, inttype)
    inttype_path = os.path.join(inttype_path, "results")

    for file in os.listdir(inttype_path) :
        file_path = os.path.join(inttype_path, file)
        file_results = open(file_path, "r")
        lines = file_results.readlines()
        file_results.close()

        first_line = lines[0].split(" ")
        count = int(first_line[0])
        png = float(first_line[5])
        size = float(first_line[7])

        if png not in list(dic_2_bubbles[inttype].keys()) :
            dic_2_bubbles[inttype][png] = {}
        if size not in list(dic_2_bubbles[inttype][png].keys()) :
            dic_2_bubbles[inttype][png][size] = []
        
        dic_data = dic_2_bubbles[inttype][png][size]
        
        second_line = lines[1].split(" ")
        for i in range(count) :
            init_radius = float(second_line[i+1])
            # list format : for each bubble, [R0, t_list, R_list, Pt_list]
            dic_data.append([init_radius, [], [], []])
            if (inttype == "IC" or inttype == "QA") :
                dic_data[-1].append([])
                dic_data[-1].append([])
                dic_data[-1].append([])
        
        for line in lines[3:] :
            data = line.split(" ")
            t = float(data[0])
            for i in range(count) :
                r = float(data[1 + i])
                pt = float(data[1 + count + i])
                dic_data[i][1].append(t)
                dic_data[i][2].append(r)
                dic_data[i][3].append(pt)
                if (inttype == "IC" or inttype == "QA") :
                    a = float(data[1 + 2 * count + i])
                    dp = float(data[1 + 3 * count + i])
                    u = float(data[1 + 4 * count + i])
                    dic_data[i][4].append(a)
                    dic_data[i][5].append(dp)
                    dic_data[i][6].append(u)

######### Step 2 : Plotting results #################################################################################################################

######### Initial parameters ####################

T = 10.0e-06
P0 = 0.1013e06
sigma = 0.0728

######### Cavitation inception with interactions with varying distance between 2 bubbles ##########

nrow = 1
ncol = 2

fig, axs = plt.subplots(nrow, ncol, figsize=((ncol*20*cm, nrow*12.5*cm)))
plt.subplots_adjust(wspace=0.35*cm, hspace=0.5*cm)

dist_list = [10, 12, 12.1, 12.5, 15, 20]

axs[0].set_title(r"Incompressible interactions", y=1.025)
axs[0].set_xlabel(r"$t$ [$\mu$s]", fontsize=27.5)
axs[0].set_xlim(xmin=0.0, xmax=60.0)
axs[0].set_ylabel(r"$R$ [$\mu$m]", fontsize=27.5)
axs[0].set_ylim(ymin=-5.0, ymax=80.0)
axs[0].grid()

for dist in dist_list :
    t_list = np.array(dic_2_bubbles["IC"][-25325][dist][0][1]) * 1.0e6
    r_list = np.array(dic_2_bubbles["IC"][-25325][dist][0][2]) * 1.0e6

    axs[0].plot(t_list, r_list, color="blue", linewidth=2.5)

t_list = np.array(dic_2_bubbles["NI"][-25325][15.0][0][1]) * 1.0e6
r_list = np.array(dic_2_bubbles["NI"][-25325][15.0][0][2]) * 1.0e6
axs[0].plot(t_list, r_list, color="blue", linewidth=2.5)

t_list = np.array(dic_2_bubbles["NI"][-25325][15.0][1][1]) * 1.0e6
r_list = np.array(dic_2_bubbles["NI"][-25325][15.0][1][2]) * 1.0e6
axs[0].plot(t_list, r_list, color="magenta", linestyle="dashed", linewidth=2.5)

axs[0].text(0.5, 5.0, r"$R_{1,0}$", color="blue")
axs[0].text(0.5, 25.0, r"$R_{2,0}$", color="magenta")

axs[0].text(36.5, 73.5, r"$\infty$", color="blue")
axs[0].text(42.5, 73.5, r"20", color="blue")
axs[0].text(54.0, 73.5, r"15", color="blue")
axs[0].text(47.0, 54.0, r"12.5", color="blue")
axs[0].text(45.0, 17.0, r"12.1", color="blue")
axs[0].text(41.0, 6.75, r"12", color="blue")
axs[0].text(25.0, -2.5, r"10", color="blue")

dist_list = [10, 11.9, 12, 15, 20]

axs[1].set_title(r"Quasi-acoustic interactions", y=1.025)
axs[1].set_xlabel(r"$t$ [$\mu$s]", fontsize=27.5)
axs[1].set_xlim(xmin=0.0, xmax=60.0)
axs[1].set_ylim(ymin=-5.0, ymax=80.0)
axs[1].grid()

for dist in dist_list :
    t_list = np.array(dic_2_bubbles["QA"][-25325][dist][0][1]) * 1.0e6
    r_list = np.array(dic_2_bubbles["QA"][-25325][dist][0][2]) * 1.0e6

    axs[1].plot(t_list, r_list, color="blue", linewidth=2.5)

t_list = np.array(dic_2_bubbles["NI"][-25325][15.0][0][1]) * 1.0e6
r_list = np.array(dic_2_bubbles["NI"][-25325][15.0][0][2]) * 1.0e6
axs[1].plot(t_list, r_list, color="blue", linewidth=2.5)

t_list = np.array(dic_2_bubbles["NI"][-25325][15.0][1][1]) * 1.0e6
r_list = np.array(dic_2_bubbles["NI"][-25325][15.0][1][2]) * 1.0e6
axs[1].plot(t_list, r_list, color="magenta", linestyle="dashed", linewidth=2.5)

axs[1].text(0.5, 5.0, r"$R_{1,0}$", color="blue")
axs[1].text(0.5, 25.0, r"$R_{2,0}$", color="magenta")

axs[1].text(36.5, 73.5, r"$\infty$", color="blue")
axs[1].text(42.5, 73.5, r"20", color="blue")
axs[1].text(54.0, 73.5, r"15", color="blue")
axs[1].text(51.0, 36.0, r"12", color="blue")
axs[1].text(40.0, 10.0, r"11.9", color="blue")
axs[1].text(25.0, -2.5, r"10", color="blue")

fig.savefig("cavitationonset_varyingdistance.pdf", bbox_inches='tight',pad_inches=0.35)

######### Cavitation inception with interactions with varying pressure between 2 bubbles ##########

nrow = 1
ncol = 2

fig, axs = plt.subplots(nrow, ncol, figsize=((ncol*20*cm, nrow*12.5*cm)))
plt.subplots_adjust(wspace=0.35*cm, hspace=0.5*cm)

png_list = [-25325, -27351, -27654.9, -27958.8, -29377]

axs[0].set_title(r"Incompressible interactions", y=1.025)
axs[0].set_xlabel(r"$t$ [$\mu$s]", fontsize=27.5)
axs[0].set_xlim(xmin=0.0, xmax=60.0)
axs[0].set_ylabel(r"$R_{1}$ [$\mu$m]", fontsize=27.5)
axs[0].set_ylim(ymin=0.0, ymax=40.0)
axs[0].grid()

for png in png_list :
    t_list = np.array(dic_2_bubbles["IC"][png][10.0][0][1]) * 1.0e6
    r_list = np.array(dic_2_bubbles["IC"][png][10.0][0][2]) * 1.0e6

    axs[0].plot(t_list, r_list, color="blue", linewidth=2.5)

axs[0].text(0.5, 3.0, r"$R_{1,0}$", color="blue")

axs[0].text(32.0, 37.5, r"-0.29", color="blue")
axs[0].text(45.0, 28.5, r"-0.276", color="blue")
axs[0].text(43.0, 17.5, r"-0.273", color="blue") 
axs[0].text(30.0, 8.0, r"-0.27", color="blue")
axs[0].text(23.0, 0.5, r"-0.25", color="blue")

png_list = [-25325, -27351, -27958.8, -27654.9, -29377]

axs[1].set_title(r"Quasi-acoustic interactions", y=1.025)
axs[1].set_xlabel(r"$t$ [$\mu$s]", fontsize=27.5)
axs[1].set_xlim(xmin=0.0, xmax=60.0)
axs[1].set_ylim(ymin=0.0, ymax=40.0)
axs[1].grid()

for png in png_list :
    t_list = np.array(dic_2_bubbles["QA"][png][10.0][0][1]) * 1.0e6
    r_list = np.array(dic_2_bubbles["QA"][png][10.0][0][2]) * 1.0e6

    axs[1].plot(t_list, r_list, color="blue", linewidth=2.5)

axs[1].text(0.5, 3.0, r"$R_{1,0}$", color="blue")

axs[1].text(30.5, 37.5, r"-0.29", color="blue")
axs[1].text(48.5, 37.5, r"-0.276", color="blue")
axs[1].text(50.0, 28.0, r"-0.273", color="blue")
axs[1].text(36.5, 8.0, r"-0.27", color="blue")
axs[1].text(25.0, 0.5, r"-0.25", color="blue")

fig.savefig("cavitationonset_varyingpressure.pdf", bbox_inches='tight',pad_inches=0.35)

##### Pressure differences between the two interactions models evolution ######

nrow = 2
ncol = 1

fig, axs = plt.subplots(nrow, ncol, figsize=((ncol*20*cm, nrow*12.5*cm)), sharex=True)
plt.subplots_adjust(wspace=1.5*cm, hspace=0.25*cm)

png_list = [-25325, -27654.9]
dist_list = [12.0, 10.0]

for i in range(nrow) :
    png = png_list[i]
    dist = dist_list[i]

    if (i == 1) :
        axs[i].set_xlabel(r"$t$ [$\mu$s]", fontsize=27.5)
    axs[i].set_ylabel(r"$p_{\infty, 1} / p_{0}$", fontsize=27.5)
    axs[i].set_xlim(xmin=10.0, xmax=60.0)
    axs[i].grid()

    secyax = axs[i].twinx()
    secyax.yaxis.label.set_color("blue")
    secyax.spines["right"].set_color("blue")
    secyax.tick_params("y", colors="blue")
    secyax.spines["right"].set_edgecolor("blue")
    secyax.set_ylabel(r"$(p_{\infty, 1, \mathrm{QA}} - p_{\infty, 1, \mathrm{IC}}) / p_{0}$", fontsize=27.5)
    secyax.grid(linestyle="dashed")

    sec_bis_yaxis = axs[i].twinx()
    sec_bis_yaxis.set_yticks([])

    t_list_IC = np.array(dic_2_bubbles["IC"][png][dist][0][1]) * 1.0e6
    p_list_IC = np.array(dic_2_bubbles["IC"][png][dist][0][3]) / P0

    t_list_QA = np.array(dic_2_bubbles["QA"][png][dist][0][1]) * 1.0e6
    p_list_QA = np.array(dic_2_bubbles["QA"][png][dist][0][3]) / P0

    p_list_QA_new = []
    for j in range(9, len(p_list_QA), 10) :
        p_list_QA_new.append(p_list_QA[j])

    diff_p = np.array(p_list_QA_new) - p_list_IC

    axs[i].plot(t_list_IC, p_list_IC, color="red", linewidth=3.0, linestyle="solid", label="IC")
    axs[i].plot(t_list_QA, p_list_QA, color="black", linewidth=3.0, linestyle="dashed", label="QA")
    secyax.plot(t_list_IC, diff_p, color="blue", linewidth=3.0, linestyle="dotted", label=r"$\Delta p_{\infty, 1} / p_{0}$ (QA - IC)")
    sec_bis_yaxis.plot(t_list_IC, p_list_IC, color="red", linewidth=3.0, linestyle="solid", label="IC")
    sec_bis_yaxis.plot(t_list_QA, p_list_QA, color="black", linewidth=3.0, linestyle="dashed", label="QA")

    t_IC = t_list_IC[dic_2_bubbles["IC"][png][10.0][0][2].index(np.max(dic_2_bubbles["IC"][png][10.0][0][2]))]
    t_QA = t_list_QA[dic_2_bubbles["QA"][png][10.0][0][2].index(np.max(dic_2_bubbles["QA"][png][10.0][0][2]))]

    secyax.set_ylim(ymin=-0.005, ymax=0.005)
    secyax.set_yticks([-0.005, 0.0, 0.005])

    if (i == 0) :
        sec_bis_yaxis.legend(bbox_to_anchor=(0.5, 1.15), loc="center", ncol=2, frameon=False)
        secyax.legend(bbox_to_anchor=(0.5, 1.05), loc="center", ncol=1, frameon=False)
    
    axs[i].text(25.0, 0.85, r"$\Delta x_{12}^{*}=$" + " {:.1f}".format(dist), horizontalalignment="center", fontsize=27.5)
    axs[i].text(25.0, 0.65, r"$p_{\mathrm{ng}}^{*}=$" + " {:.3f}".format(png/P0), horizontalalignment="center", fontsize=27.5)

fig.savefig("cavitationonset_pressuredifferences.pdf", bbox_inches='tight',pad_inches=0.35)

#### Ambient pressure during collapse evolution ####

png = -27351
dist = 10.0

nrow = 2
ncol = 2

fig, axs = plt.subplots(nrow, ncol, figsize=((ncol*18.75*cm, nrow*9.375*cm)), sharex=True)
plt.subplots_adjust(wspace=0.45*cm, hspace=0.25*cm)

axs[0, 0].set_title("Incompressible interactions", y=1.025)
axs[0, 1].set_title("Quasi-acoustic interactions", y=1.025)

for i in range(nrow) :
    for j in range(ncol) :
        axs[i, j].grid()

axs[nrow - 1, 0].set_xlabel(r"$t$ [$\mu$s]")
axs[nrow - 1, 1].set_xlabel(r"$t$ [$\mu$s]")

axs[0, 0].set_ylabel(r"$R/R_{0}$")
axs[nrow - 1, 0].set_ylabel(r"$p_{\infty} / p_{0}$")

axs[1, 0].set_xlim(xmin=30.0, xmax=50.0)
axs[0, 0].set_ylim(ymin=0.0, ymax=10.0)
axs[0, 1].set_ylim(ymin=0.0, ymax=10.0)
axs[nrow - 1, 0].set_ylim(ymin=-0.3, ymax=0.0)
axs[nrow - 1, 1].set_ylim(ymin=-0.3, ymax=0.0)

# IC
r0 = dic_2_bubbles["IC"][png][dist][0][0]
t_list = np.array(dic_2_bubbles["IC"][png][dist][0][1]) * 1.0e6
r_list = np.array(dic_2_bubbles["IC"][png][dist][0][2]) / r0
p_list = np.array(dic_2_bubbles["IC"][png][dist][0][3]) / P0
dp_list = dic_2_bubbles["IC"][png][dist][0][5]

axs[0, 0].plot(t_list, r_list, color="blue", linewidth=2.5, label=r"$R_{0}=2.0$ $\mu$m")
axs[nrow - 1, 0].plot(t_list, p_list, color="blue", linewidth=2.5)

r0 = dic_2_bubbles["IC"][png][dist][1][0]
t_list = np.array(dic_2_bubbles["IC"][png][dist][1][1]) * 1.0e6
r_list = np.array(dic_2_bubbles["IC"][png][dist][1][2]) / r0
p_list = np.array(dic_2_bubbles["IC"][png][dist][1][3]) / P0
dp_list = dic_2_bubbles["IC"][png][dist][1][5]

axs[0, 0].plot(t_list, r_list, color="magenta", linestyle="dashed", linewidth=2.5, label=r"$R_{0}=20.0$ $\mu$m")
axs[nrow - 1, 0].plot(t_list, p_list, color="magenta", linestyle="dashed", linewidth=2.5)

# QA
r0 = dic_2_bubbles["QA"][png][dist][0][0]
t_list = np.array(dic_2_bubbles["QA"][png][dist][0][1]) * 1.0e6
r_list = np.array(dic_2_bubbles["QA"][png][dist][0][2]) / r0
p_list = np.array(dic_2_bubbles["QA"][png][dist][0][3]) / P0
dp_list = dic_2_bubbles["QA"][png][dist][0][5]

axs[0, 1].plot(t_list, r_list, color="blue", linewidth=2.5)
axs[nrow - 1, 1].plot(t_list, p_list, color="blue", linewidth=2.5)

r0 = dic_2_bubbles["QA"][png][dist][1][0]
t_list = np.array(dic_2_bubbles["QA"][png][dist][1][1]) * 1.0e6
r_list = np.array(dic_2_bubbles["QA"][png][dist][1][2]) / r0
p_list = np.array(dic_2_bubbles["QA"][png][dist][1][3]) / P0
dp_list = dic_2_bubbles["QA"][png][dist][1][5]

axs[0, 1].plot(t_list, r_list, color="magenta", linestyle="dashed", linewidth=2.5)
axs[nrow - 1, 1].plot(t_list, p_list, color="magenta", linestyle="dashed", linewidth=2.5)

axs[0, 0].legend(bbox_to_anchor=(1.05, 1.05), loc="lower center", ncol=2, frameon=False, fontsize=27.5)
fig.savefig("cavitationonset_collapse.pdf", bbox_inches='tight',pad_inches=0.35)

#### Unstable radius ####

nrow = 2
ncol = 2

fig, axs = plt.subplots(nrow, ncol, figsize=((ncol*15*cm, nrow*9.375*cm)), sharey=True, sharex=True)
plt.subplots_adjust(wspace=0.14*cm, hspace=0.25*cm)

for i in range(nrow) :
    for j in range(ncol) :
        axs[i, j].grid()
        if j == 0 :
            axs[i, j].set_ylabel(r"$R$ [$\mu$m]", fontsize=27.5)
            axs[i, j].set_ylim(ymin=0.0, ymax=40.0)
        if i == nrow - 1 :
            axs[i, j].set_xlabel(r"$t$ [$\mu$s]", fontsize=27.5)
            axs[i, j].set_xlim(xmin=0.0, xmax=60.0)
            axs[i, j].set_xticks([10, 30, 50], [10, 30, 50])

axs[0, 0].set_title(r"Incompressible interactions", y=1.025)
axs[0, 1].set_title(r"Quasi-acoustic interactions", y=1.025)

png_list = [-25325, -27654.9]
dist_list = [12.0, 10.0]

for l in range(nrow) :
    png = png_list[l]
    dist = dist_list[l]

    # IC
    t_list = np.array(dic_2_bubbles["IC"][png][dist][0][1])
    r_list = np.array(dic_2_bubbles["IC"][png][dist][0][2])
    p_list = np.array(dic_2_bubbles["IC"][png][dist][0][3])

    axs[l, 0].text(31.0, 30.0, r"$p_{\mathrm{ng}}^{*}=$" + " {:.3f}".format(png/P0), horizontalalignment="center", fontsize=26)
    axs[l, 0].text(31.0, 35.0, r"$\Delta x_{12}^{*}=$" + " {:.1f}".format(dist), horizontalalignment="center", fontsize=26)

    R0 = r_list[0]
    pG0 = P0 + (2 * sigma / R0)

    r_unstable_list = []
    for i in range(len(t_list)) :
        p = np.polynomial.Polynomial([-pG0 * (R0**3), 0, 2 * sigma, p_list[i]])
        roots = p.roots()
        r_unstable_list.append(float(np.real(roots[-1])))
    
    if (l == 0) :
        axs[l, 0].plot(t_list*1e6, r_list*1e6, color="blue", linewidth=3.0, label=r"$R_{1}$")
        axs[l, 0].plot(t_list*1e6, np.array(r_unstable_list)*1e6, linestyle="solid", color="red", marker="o", markevery=500, linewidth=2.5, label=r"$R_{\mathrm{Ue}}$")
    else :
        axs[l, 0].plot(t_list*1e6, r_list*1e6, color="blue", linewidth=3.0)
        axs[l, 0].plot(t_list*1e6, np.array(r_unstable_list)*1e6, linestyle="solid", color="red", marker="o", markevery=500, linewidth=2.5)

    # QA
    t_list = np.array(dic_2_bubbles["QA"][png][dist][0][1])
    r_list = np.array(dic_2_bubbles["QA"][png][dist][0][2])
    p_list = np.array(dic_2_bubbles["QA"][png][dist][0][3])

    axs[l, 1].text(31.0, 30.0, r"$p_{\mathrm{ng}}^{*}=$" + " {:.3f}".format(png/P0), horizontalalignment="center", fontsize=26)
    axs[l, 1].text(31.0, 35.0, r"$\Delta x_{12}^{*}=$" + " {:.1f}".format(dist), horizontalalignment="center", fontsize=26)

    R0 = r_list[0]
    pG0 = P0 + (2 * sigma / R0)

    r_unstable_list = []
    for i in range(len(t_list)) :
        p = np.polynomial.Polynomial([-pG0 * (R0**3), 0, 2 * sigma, p_list[i]])
        roots = p.roots()
        r_unstable_list.append(float(np.real(roots[-1])))

    axs[l, 1].plot(t_list*1e6, r_list*1e6, color="blue", linewidth=3.0)
    axs[l, 1].plot(t_list*1e6, np.array(r_unstable_list)*1e6, linestyle="solid", color="red", marker="o", markevery=5000,  linewidth=2.5)

axs[0, 0].legend(bbox_to_anchor=(1.05, 1.05), loc="lower center", ncol=2, frameon=False, fontsize=27.5)
fig.savefig("cavitationonset_unstableradius.pdf", bbox_inches='tight',pad_inches=0.35)