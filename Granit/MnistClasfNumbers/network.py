from some_tools import plot_predict
import numpy as np
import random
import numpy
import scipy


class MnistNetwork:
    def __init__(self, l_inp_ize, l_hid_size, l_out_size, learning_rate):

        self.__acc = None               # процент точности
        self.mse_for_epoch = []         # mse ошибка
        self.input_size = l_inp_ize     # размеры слоев
        self.hidden_size = l_hid_size
        self.output_size = l_out_size
        self.lr = learning_rate
                                        #нормаль ---- отклонение ----------- размер
        self.w_hid = np.random.normal(0.0, l_inp_ize ** -0.5, (l_hid_size, l_inp_ize))    # веса слоев
        self.w_out = np.random.normal(0.0, l_hid_size ** -0.5, (l_out_size, l_hid_size))

        self.activation_function = lambda x: scipy.special.expit(x)

    def training(self, path, epochs):
        training_data = open(path, 'r').readlines()
        mse = None
        for e in range(epochs):
            for record in training_data:
                all_values = [int(x) for x in record.split(",")]
                inputs = (numpy.array(all_values[1:]) / 255.0 * 0.99) + 0.01  # нормирование
                targets = numpy.zeros(self.output_size) + 0.01  # нули
                targets[all_values[0]] = 0.99  # целевая
                mse = self.predict(inputs, targets)
            self.mse_for_epoch.append(mse)

    def testing(self, path):
        test_data = open(path).readlines()
        accuracy = 0
        for record in test_data:
            all_values =  [int(x) for x in record.split(",")]
            correct = all_values[0]
            inputs = (np.array(all_values[1:]) / 255.0 * 0.99) + 0.01  # нормирование
            answer = numpy.argmax(self.predict(inputs))  # индекс наибольшего элемента в массиве предсказания
            if answer == correct:
                accuracy += 1
        self.__acc =  accuracy / len(test_data)

    def predict(self, inp_list, targ_list=None):
        inputs = numpy.array(inp_list, ndmin=2).T       # транспонируем для умножения матриц

        hid_inputs = self.w_hid @ inputs                # скрытый слой
        hid_outputs = self.activation_function(hid_inputs)

        fin_inputs = self.w_out @ hid_outputs           # слой вывода
        fin_outputs = self.activation_function(fin_inputs)

        if targ_list is None: # тренируем или выводим
            return fin_outputs  # возвращается результат предсказания
        else:
            targets = numpy.array(targ_list, ndmin=2).T
            out_errors = targets - fin_outputs  # подсчет ошибок
            hid_errors = self.w_out.T @ out_errors

            #  меняем веса в зависимости от входов и результата
            self.w_out += self.lr * (out_errors * fin_outputs * (1.0 - fin_outputs)) @ hid_outputs.T  # трансп.
            self.w_hid += self.lr * (hid_errors * hid_outputs * (1.0 - hid_outputs)) @ inputs.T
            return np.mean(out_errors ** 2)  # возвращается ошибка

    def solo_predict(self, path):
        data = open(path).readlines()
        data = random.choice(data).split(",")
        inputs = [int(x) for x in data[1:]]
        predict = str(numpy.argmax(self.predict(inputs)))
        plot_predict(inputs, predict)

    def get_accuracy(self):
        return str(round(self.__acc * 100, 1)) + " %"


