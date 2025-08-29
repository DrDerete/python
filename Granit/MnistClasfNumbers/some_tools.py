import numpy as np
import matplotlib.pyplot as plt
import csv
import random

def create_sample(numbers, c_nums,  path="mnist_dataset\\mnist_test.csv"):
    data = open(path).readlines()
    random.shuffle(data)    # перемешать, чтобы каждая выборка отличалась
    data_sample = []        # создание выборки из датасета
    select_control = {num: c_nums for num in numbers}

    for num in data:  # заполнение
        if num[0] in numbers:
            if select_control[num[0]] != 0:
                data_sample.append(num)
                select_control[num[0]] -= 1
                if sum(select_control.values()) == 0:
                    break

    output_path = "mnist_dataset/mnist_dataset" + str(c_nums * len(numbers)) + "(" + "_".join(list(select_control.keys())) + ").csv"
    save_scv(output_path, data_sample)

    data_test = []  # разбиение выборки на train и test (проверить на работоспособность)
    control = {num: int(c_nums/3) for num in numbers}
    while True:
        l = len(data_sample)
        i = random.randint(0, l)
        if control[data_sample[i][0]] != 0:
            control[data_sample[i][0]] -= 1
            data_test.append(data_sample.pop(i))
            if sum(control.values()) == 0:
                break
    data_train = data_sample
    save_scv("mnist_dataset/mnist_my_test.csv", data_test)
    save_scv("mnist_dataset/mnist_my_train.csv", data_train)

def save_scv(path, data):
    with open(path, 'w', newline='') as csvfile:   # сохранение
        for row in data:
            csv.writer(csvfile).writerow(row.strip().split(','))

def plot_dataset(path, cols, rows):   # построение графика
    data = open(path).readlines()
    fig, axes = plt.subplots(rows, cols)
    for i, ax in enumerate(axes.flat):
        row = data[i].split(",")
        image = np.array(row[1:], dtype=np.uint8).reshape(28, 28)
        ax.imshow(image, cmap="gray")
        ax.axis("off")
    plt.show()

def plot_predict(data, predict):
    image = np.array(data, dtype=np.uint8).reshape(28, 28)
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.title("Это цифра " + predict)

def plot_learning(data):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(data)), data)
    plt.title("График обучения")
    plt.xlabel("Эпоха")
    plt.ylabel("MSE")
    plt.grid(True)
    plt.show()
