import numpy as np

class Conv:
    def __init__(self, option):
        self.n_f = option["number_filters"]
        self.k_s = option["kernel_size"]
        self.srd = option["stride"]
        self.pad = option["padding"]
        self.pl_o = option["pool_opt"]
        self.ac = option["activation"]
        self.input = None
        self.weights = np.random.randn(self.n_f, self.k_s, self.k_s) / (self.k_s ** 2)
        self.bias = np.zeros((self.n_f, 1))

    def step(self, input_data):
        self.input = input_data
        data = self.__convolution(input_data)   # свертка
        data = self.__activation(data)          # активация
        data = self.__pooling(data)             # пулинг
        return data

    def __convolution(self, in_data):
        batch_size, input_height, input_width = in_data.shape  # инфо о data
        # для вывода, надо знать размер свернутого изображения
        out_h = (input_height - self.k_s + 2 * self.pad) // self.srd + 1
        out_w = (input_width - self.k_s + 2 * self.pad) // self.srd + 1
        # количество свободных ячеек, делённое на страйд + начальная ячейка;
        out_data = np.zeros((batch_size, self.n_f, out_h, out_w))  # массив выходных данных
        # для каждого batch, для каждого ядра свертки, свое изображение[h][w]
        padded_input = np.pad(in_data, ((0, 0), (self.pad, self.pad), (self.pad, self.pad)))
        # заполнение output массива
        for b in range(batch_size):
            for f in range(self.n_f):
                for i in range(out_h):
                    for j in range(out_w):
                        out_data[b, f, i, j] = np.sum(
                            padded_input[  # массив из padded_input * ядро свертки
                            b,
                            (i * self.srd):(i * self.srd + self.k_s),
                            (j * self.srd):(j * self.srd + self.k_s)
                            ] * self.weights[f]
                        ) + self.bias[f]
        return out_data

    def __pooling(self, in_data):
        batch_size, n_f, input_height, input_width = in_data.shape
        p_s = self.pl_o["pool_size"]   # входные данные
        s = self.pl_o["pool_stride"]

        out_h = (input_height - p_s) // s + 1  # для вывода
        out_w = (input_width - p_s) // s + 1

        out_data = np.zeros((batch_size, n_f, out_h, out_w))

        match self.pl_o["pool_type"]:
            case "Max":
                for b in range(batch_size):
                    for f in range(n_f):
                        for i in range(out_h):
                            for j in range(out_w):
                                out_data[b, f, i, j] = np.max(
                                    in_data[b, f, (i * s):(i * s + p_s), (j * s):(j * s + p_s)]
                                )
            case _:
                raise ValueError(f"Unsupported pool type: {self.pl_o["pool_type"]}")
        return out_data

    def __activation(self, data):
        match self.ac:
            case "ReLU":
                return np.maximum(data, 0)
            case "Sigmoid":
                return 1 / (1 + np.exp(-data))
            case "Linear":
                return data
            case _:
                raise ValueError(f"Unsupported activation function: {self.ac}")

    def backward(self, d_output, lr):
        batch_size, input_height, input_width = self.input.shape
        _, out_h, out_w = d_output.shape[1:]

        grad_w = np.zeros_like(self.weights)    # инициализация, позже заполнение
        grad_b = np.zeros_like(self.bias)
        grad_inp = np.zeros_like(self.input)

        padded_input = np.pad(self.input, ((0, 0), (self.pad, self.pad), (self.pad, self.pad)))

        for b in range(batch_size):     # вычисление смещений
            for f in range(self.n_f):
                for i in range(out_h):
                    for j in range(out_w):
                        window = padded_input[
                                 b,
                                 (i * self.srd):(i * self.srd + self.k_s),
                                 (j * self.srd):(j * self.srd + self.k_s)
                                 ]
                        grad_w[f] += window * d_output[b, f, i, j]
                        grad_b[f] += d_output[b, f, i, j]
                        grad_inp[
                            b,
                            (i * self.srd):(i * self.srd + self.k_s),
                            (j * self.srd):(j * self.srd + self.k_s)
                        ] += self.weights[f] * d_output[b, f, i, j]

        self.weights -= lr * grad_w     # обновление весов
        self.bias -= lr * grad_b

        if self.pad > 0:                # удаление паддинга
            grad_inp = grad_inp[:, self.pad:-self.pad, self.pad:-self.pad]

        return grad_inp



class Dense:
    def __init__(self, option):
        self.input = None
        self.inp = option["input_size"]
        self.out = option["output_size"]
        self.ac = option["activation"]

        self.weights = np.random.randn(self.inp, self.out) / self.inp ** 2
        self.bias = np.zeros((1, self.out))

    def step(self, in_data):
        self.input = in_data
        out_data = in_data @ self.weights + self.bias
        return self.__activation(out_data)

    def __activation(self, data):
        match self.ac:
            case "ReLU":
                return np.maximum(data, 0)
            case "Sigmoid":
                return 1 / (1 + np.exp(-data))
            case "Linear":
                return data
            case _:
                raise ValueError(f"Unsupported activation function: {self.ac}")

    def backward(self, grad_out, lr):
        grad_w = self.input.T @ grad_out
        grad_b = np.sum(grad_out, axis=0, keepdims=True)
        grad_inp = grad_out @ self.weights.T
        self.weights -= lr * grad_w
        self.bias -= lr * grad_b
        return grad_inp

