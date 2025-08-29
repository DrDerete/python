import numpy as np
from torch.utils.data import TensorDataset
import torch
import random
import csv

def create_sample(numbers, c_train, c_test, path):
    data = open(path).readlines()
    random.shuffle(data)                            # для разнообразия
    control_train = {n: c_train for n in numbers}
    control_test = {n: c_test for n in numbers}
    train_sample = []
    test_sample = []

    for num in data:                                # создание train и test выборок
        if control_train[num[0]] != 0:
            train_sample.append(num.strip().split(","))
            control_train[num[0]] -= 1
        elif control_test[num[0]] != 0:
            test_sample.append(num.strip().split(","))
            control_test[num[0]] -= 1
        if sum(list(control_test.values()) + list(control_train.values())) == 0:
            break

    safe_csv("mnist_dataset\\mnist_my_con_train.csv", train_sample)
    safe_csv("mnist_dataset\\mnist_my_con_test.csv", test_sample)

def safe_csv(path, data):
    with open(path, "w", newline="") as csvfile:    # открытие файла для записи
        csv.writer(csvfile).writerows(data)         # csv.writer помоги

def tensor_from_data(path):                         # тензор, круто, но для pytorch надо images = (batch_size, in_channels(каналы_изображения), height, width)
    data = open(path).readlines()                   # можно переделать, но сделал по другому
    data = torch.tensor([[int(num) for num in row.strip().split(",")] for row in data])
    images = data[:, 1:].view(-1, 28, 28) / 255
    numbers = data[:, :1].view(-1)
    return TensorDataset(images, numbers)

def create_dataset_from_csv(path, delimiter, size):
    images = []
    numbers = []
    with open(path) as file:                            # открыть в режиме чтения(по умолчанию)
        reader = csv.reader(file, delimiter=delimiter)  # создание ридера
        for row in reader:
            row = list(map(int, row))
            numbers.append(row[0])
            image = np.zeros((size, size))
            non_zeros_idx = np.nonzero(row[1:])[0]
            image[non_zeros_idx // size, non_zeros_idx % size] = np.array(row[1:])[non_zeros_idx] / 255
            images.append(image)
    return np.array(images), np.array(numbers)

def batch_loader(b_size, data):
    images, numbers = data
    indices = np.arange(len(images))
    np.random.shuffle(indices)
    for start_idx in range(0, len(images), b_size):
        end_idx = min(start_idx + b_size, len(images))
        batch_indices = indices[start_idx:end_idx]
        batch_images = images[batch_indices]
        batch_numbers = numbers[batch_indices]
        yield batch_images, batch_numbers



