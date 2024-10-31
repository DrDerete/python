import random
from safe import safe_as_excel

n = 25              # длина сигнала
p = 50              # размер начальной популяции, количество генерируемых наследников
psl = 2             # максимальная высота боковых лепестков
k = 4               # количество наследников, удовлетворяющих psl
pK, pM = 0.85, 0.1  # вероятность скрещивание, вероятность мутации


def generate_cp(cp_i):  # генерация уникального сигнала, тут же происходит и сохранение таблиц

    population, pop_psl_s = generate_population()  # популяция [i] и её psl_s {i: psl}
    fit_data = []
    c = 0

    safe_as_excel(population, pop_psl_s, cp_i, "Zero")

    while True:
        population, pop_psl_s = generic_step(population, pop_psl_s)
        fit_data.append(average_fitness(pop_psl_s))
        cp = check_pop_psl(pop_psl_s)  # i у подходящих
        c += 1
        if c == 3:
            safe_as_excel(population, pop_psl_s, cp_i, "Third")
        if len(cp) > 0:
            break
    safe_as_excel(population, pop_psl_s, cp_i, "Last")
    return population[cp[0]], fit_data


def generate_population(individuals=p):
    pop = []
    pop_psl = {}
    for i in range(individuals):
        sig = generate_signal()
        pop.append(sig)
        pop_psl[i] = count_psl(sig)
    return pop, pop_psl


def generate_signal(length=n):
    signal = []
    while len(signal) != length:
        signal.append((1 if random.random() < 0.5 else -1))
    return signal


def count_psl(signal):
    sums = []
    for i in range(1, n):
        s = 0
        for j in range(i):
            s += signal[j] * signal[-i + j]
        sums.append(s)
    return max(sums)  # подсчет psl особи


def generic_step(pop, psl_s, c_best_ind=int(p / 5) + 1):
    best_psl_i = sorted(psl_s, key= lambda key: psl_s[key])
    descendants = crossing(pop, best_psl_i[:c_best_ind])    # скрещивание
    descendants = mutation(pop+descendants)                 # мутация
    new_pop = roulette_selection(descendants)               # отбор рулеткой
    new_pop_pls = {i: count_psl(new_pop[i]) for i in range(len(new_pop))}
    return new_pop, new_pop_pls

def crossing(pop, best_psl_s, p_cross = pK, length = n, c_des = p):
    descendants = []
    for i in range(len(best_psl_s)):
        for j in range(i+1, len(best_psl_s)):
            if random.random() < p_cross:
                cross_i = int(random.random() * (length-2) + 1) # +1 нужен, чтобы исправить ситуацию с 0, а n-2 для исправления +1 :)
                descendants.append(pop[best_psl_s[i]][:cross_i] + pop[best_psl_s[j]][cross_i:])
                descendants.append(pop[best_psl_s[j]][:cross_i] + pop[best_psl_s[i]][cross_i:])
                if len(descendants) == c_des:
                    return descendants

def mutation(pop, p_mut = pM):
    for individual in pop:
        if random.random() < p_mut:
            mut_i = int(random.random() * (n-1))
            individual[mut_i] = -individual[mut_i]
    return pop

def roulette_selection(pop, sig_len = n, c_survivors = p):
    adaptability = [sig_len / count_psl(ind) for ind in pop]
    survivors = []
    while len(survivors) != c_survivors:
        s = sum(adaptability)
        weighted_adapt = [adapt/s for adapt in adaptability]
        chance = random.random()
        for i in range(1, len(weighted_adapt)):
            if weighted_adapt[i-1] < chance:
                weighted_adapt[i] += weighted_adapt[i-1]
            else:
                survivors.append(pop.pop(i-1))
                adaptability.pop(i-1)
                break
    return survivors


def check_pop_psl(psl_s, need_psl=psl):
    answer = []
    for key in psl_s:
        if psl_s[key] <= need_psl:
            answer.append(key)
    return answer                   # индексы подходящих особей


def average_fitness(map_psl):
    fitness = [n/map_psl[key] for key in map_psl]
    return sum(fitness) / len(fitness)
