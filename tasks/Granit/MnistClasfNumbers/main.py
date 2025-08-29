from some_tools import plot_learning
from network import MnistNetwork

if __name__ == '__main__':
    input_nodes = 784
    hidden_nodes = 200
    output_nodes = 10
    learning_rate = 0.1

    n = MnistNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

    n.training("mnist_dataset/mnist_my_train.csv", 5)

    n.solo_predict("mnist_dataset\\mnist_dataset90(0_2_8).csv")

    n.testing("mnist_dataset\\mnist_my_test.csv")
    print("Процент точности на тестовой выборке = ", n.get_accuracy())

    n.testing("mnist_dataset\\mnist_my_train.csv")
    print("Процент точности на тренировочной выборке = ", n.get_accuracy())

    plot_learning(n.mse_for_epoch)

