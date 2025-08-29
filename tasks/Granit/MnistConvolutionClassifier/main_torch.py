from torchvision import datasets, transforms
from conv_netwok import CNNTorch
import torch.optim as optim
import torch.nn as nn

if __name__ == '__main__':

    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

    model = CNNTorch(train_dataset, test_dataset)

    loss_f = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    epochs = 5

    model.train_module(loss_f, optimizer, epochs)

    model.test_module()
