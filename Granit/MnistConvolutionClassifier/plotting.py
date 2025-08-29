from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns

def plot_acr_and_loss(data_loss, data_acr):
    plt.figure(figsize=(10, 5))
    # График потерь
    plt.plot(data_loss, label="Loss", color='blue')
    # График точности
    plt.plot(data_acr, label="Accuracy", color='red')
    plt.xlabel("Batch")
    plt.ylabel("Value")
    plt.title("Training Loss and Accuracy")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_con_matrix(labels, predicts):
    cm = confusion_matrix(labels, predicts)

    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()