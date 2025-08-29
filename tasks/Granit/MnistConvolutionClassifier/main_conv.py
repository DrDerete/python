from conv_netwok import CNNetwork

train_path = "mnist_dataset\\mnist_my_con_train.csv"
test_path = "mnist_dataset\\mnist_my_con_test.csv"

if __name__ == '__main__':
    options = {
        "train_path": train_path,
        "test_path": test_path,
        "conv_layer": {  # можно написать функцию, которая будет вычислять input для следующего слоя
            "number_filters": 32,
            "kernel_size": 3,
            "stride": 1,
            "padding": 1,
            "pool_opt": {
                "pool_type": "Max",
                "pool_size": 2,
                "pool_stride": 2
            },
            "activation": "ReLU"
        },
        "full_layer": {
            "input_size": 32 * 14 * 14, # вот сюда
            "output_size": 128,
            "activation": "ReLU"
        },
        "ans_layer": {
            "input_size": 128,
            "output_size": 10,
            "activation": "Linear"
        }
    }
    model = CNNetwork(options)

    model.train(5, 5, 0.001)

    print(model.loss)