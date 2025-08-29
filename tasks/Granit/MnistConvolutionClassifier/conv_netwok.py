from GranitElectron.MnistConvolutionClassifier.plotting import plot_acr_and_loss, plot_con_matrix
from smt import create_dataset_from_csv, batch_loader
from torch.utils.data import DataLoader
from layers import Conv, Dense

import torch.nn.functional as f
import torch.nn as nn
import numpy as np
import torch

class CNNetwork:
    def __init__(self, option):
        self.tr_p = option["train_path"]
        self.te_p = option["test_path"]

        self.conv_l = Conv(option["conv_layer"])
        self.full_l = Dense(option["full_layer"])
        self.end_l = Dense(option["ans_layer"])

        self.loss = None

    def train(self, epoches, batches_size, learning_rate):
        train_data = create_dataset_from_csv(self.tr_p, ",", 28)
        for i in range(epoches):                                                # по эпохам
            for images, numbers in batch_loader(batches_size, train_data):      # по батчам
                conv_out = self.conv_l.step(images)                             # проход по слоям
                full_out = self.full_l.step(conv_out.reshape(images.shape[0], -1))
                final_out = self.end_l.step(full_out)

                grad = self.__loss_and_gradients(final_out, numbers)

                err_end = self.end_l.backward(grad, learning_rate)
                err_full = self.full_l.backward(err_end, learning_rate)
                self.conv_l.backward(err_full.reshape(conv_out.shape), learning_rate)
            print("epoches: " + str(i))

    def __loss_and_gradients(self, final_out, numbers):
        exponents = np.exp(final_out - np.max(final_out, axis=1, keepdims=True))   # e^(массив-max)
        scores = exponents / np.sum(exponents, axis=1, keepdims=True)              # softmax
        log_scores = -np.log(scores[range(len(numbers)), numbers])                 # логарифм правдоподобия
        self.loss = np.sum(log_scores) / len(numbers)                              # перекрестная энтропия

        grad = scores.copy()
        grad[range(len(numbers)), numbers] -= 1
        grad /= len(numbers)                                                       # нормализация

        return grad

    def predict(self, x):
        x = self.conv_l.step(x).reshape(x.shape[0], -1)
        x = self.full_l.step(x)
        x = self.end_l.step(x)
        return x







class CNNTorch(nn.Module):
    def __init__(self, train_data, test_data):
        super(CNNTorch, self).__init__()
        self.tr_d = train_data
        self.te_d = test_data
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(32 * 14 * 14, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(f.relu(self.conv1(x)))
        x = x.view(-1, 32 * 14 * 14)
        x = f.relu(self.fc1(x))
        x = self.fc2(x)
        return x

    def train_module(self, loss_f, opt, epochs):
        train_losses = []
        train_accuracies = []

        self.train()
        batch_size = 30
        train_loader = DataLoader(self.tr_d, batch_size, True)

        for epoch in range(epochs):
            running_loss = 0.0
            epoch_correct = 0.0

            for images, numbers in train_loader:
                opt.zero_grad()
                output = self(images)
                loss = loss_f(output, numbers)
                loss.backward()
                opt.step()

                running_loss += loss.item()
                _, predict = torch.max(output.data, 1)
                batch_correct = torch.eq(predict, numbers).sum().item()
                epoch_correct += torch.eq(predict, numbers).sum().item()

                train_losses.append(loss.item())
                train_accuracies.append(round(100 * batch_correct / batch_size, 3))

            epoch_loss = round(running_loss / len(train_loader), 5)
            epoch_acr = round(100 * epoch_correct / len(train_loader) / batch_size, 3)

            print(f"Epoch {epoch + 1}, Loss: {epoch_loss}, Accuracy: {epoch_acr}%")

        plot_acr_and_loss(train_losses, train_accuracies)

    def test_module(self):
        self.eval()
        batch_size = 28
        test_loader = DataLoader(self.te_d, batch_size, False)

        all_predicts = []
        all_labels = []

        for images, numbers in test_loader:
            output = self(images)
            _, predicted = torch.max(output.data, 1)
            all_predicts.extend(predicted)
            all_labels.extend(numbers)

        correct = sum([1 if all_labels[i] == all_predicts[i] else 0 for i in range(len(all_labels))])
        total = len(all_labels)
        print(f'Accuracy of the model on the test images: {100 * correct / total:.2f}%')

        plot_con_matrix(all_labels, all_predicts)
