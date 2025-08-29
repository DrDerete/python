from pllotting import plot_fitness, plot_akf
from generic import generate_cp

if __name__ == '__main__':

    generated_signals = []  # сгенерированные сигналы
    fit_of_gen = []  # данные для построения графика фит функция от поколения(натолкнуло на мысль, что имеет смысл начинать генерацию заново)

    for i in range(4):
        gen, fit = generate_cp(i)
        generated_signals.append(gen)
        fit_of_gen.append(fit)

    plot_akf(generated_signals)
    plot_fitness(fit_of_gen)