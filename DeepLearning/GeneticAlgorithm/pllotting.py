import numpy as np
import matplotlib.pyplot as plt

def plot_fitness(data_plot):

    fig, axis = plt.subplots(2, 2)

    for i in range(len(data_plot)):

        x = np.arange(0, len(data_plot[i]))
        y = np.array(data_plot[i])

        axis[int(i / 2), i % 2].plot(x, y, color="red")
        axis[int(i / 2), i % 2].set_title("Fitness function " +str(i))
        axis[int(i / 2), i % 2].set_xlabel("Generation")
        axis[int(i / 2), i % 2].set_ylabel("Length/PSL")

    fig.tight_layout()
    plt.show()

def plot_akf(data_plots, needed_psl = 2):

    n = len(data_plots[0])
    fig, axis = plt.subplots(2, 2)

    for plot_i in range(len(data_plots)):
        akf_s = []
        for i in range(1, n):
            s = 0
            for j in range(i):
                s += data_plots[plot_i][j] * data_plots[plot_i][-i + j]
            akf_s.append(s)

        x = np.arange(-n + 1, n)
        y = akf_s + [len(akf_s)] + list(reversed(akf_s))

        axis[int(plot_i / 2), plot_i % 2].plot(x, y)
        axis[int(plot_i / 2), plot_i % 2].axhline(needed_psl, color="red")
        axis[int(plot_i / 2), plot_i % 2].set_title("AKF for " + str(plot_i))

    fig.tight_layout()
    plt.show()