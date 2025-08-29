import re
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import matplotlib.pyplot as plt


# Модель RNN
class CharTextGenerator(nn.Module):
    def __init__(self, vocab_size, embedding_dim=128, hidden_dim=256, n_layers=2):
        super(CharTextGenerator, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)
        # Статистика параметров
        self.total_params = sum(p.numel() for p in self.parameters())
        self.trainable_params = sum(p.numel() for p in self.parameters() if p.requires_grad)

    def forward(self, x, hidden=None):
        x = self.embedding(x)
        out, hidden = self.lstm(x, hidden)
        out = self.fc(out[:, -1, :])  # Берем только последний выход
        return out, hidden

    def print_stats(self):
        print("\n" + "=" * 50)
        print("Архитектура сети:")
        print(f"Embedding: {self.embedding.num_embeddings} токенов -> {self.embedding.embedding_dim} dim")
        print(f"LSTM: {self.lstm.input_size} -> {self.lstm.hidden_size} ({self.lstm.num_layers} слоя)")
        print(f"Linear: {self.fc.in_features} -> {self.fc.out_features}")
        print(f"\nВсего параметров: {self.total_params:,}")
        print(f"Обучаемых параметров: {self.trainable_params:,}")
        print("=" * 50 + "\n")


# Создание обучающих примеров
class CharDataset(Dataset):
    def __init__(self, text, seq_length):
        self.seq_length = seq_length
        self.data = torch.tensor([char_to_idx[c] for c in text], dtype=torch.long)

    def __len__(self):
        return len(self.data) - self.seq_length

    def __getitem__(self, idx):
        # преобразуем фрагмент текста в тензор
        input_seq = self.data[idx : idx + self.seq_length]
        # и ставим в соответствие этому фрагменту символ
        target_char = self.data[idx + self.seq_length]
        return input_seq, target_char


# Загрузка данных
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        fresh_text = f.read()
        fresh_text = re.sub(r'\s+', ' ', fresh_text).strip()
    return fresh_text

# Анализ сгенерированного текста
def analyze_generated_text(gen):
    original_words = set(re.findall(r'\w+', text.lower()))
    generated_words = re.findall(r'\w+', gen.lower())

    correct_count = sum(1 for word in generated_words if word in original_words)
    total_words = len(generated_words)

    return (correct_count / total_words * 100) if total_words > 0 else 0.0

# Обучение
def train_model(model, dataloader, epochs=20, temperature=1.0):
    model.to(device)
    model.print_stats()

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    losses = []
    accuracy_history = []

    for epoch in range(1, epochs + 1):
        model.train()
        total_loss = 0

        for batch, (inputs, targets) in enumerate(dataloader):
            inputs, targets = inputs.to(device), targets.to(device)

            optimizer.zero_grad()
            outputs, _ = model(inputs)

            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(dataloader)
        losses.append(avg_loss)

        # Генерация текста и анализ
        generated = generate_text(model, "И ", temp=temperature, length=200)
        accuracy = analyze_generated_text(generated)
        accuracy_history.append(accuracy)

        print(f'Epoch {epoch}, Loss: {avg_loss:.4f}, Правильные слова: {accuracy:.1f}%')
        print(f"Пример: {generated}")

    # Визуализация
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(losses)
    plt.title('График обучения')
    plt.xlabel('Эпоха')
    plt.ylabel('Потери')

    plt.subplot(1, 2, 2)
    plt.plot(accuracy_history)
    plt.title('Качество генерации')
    plt.xlabel('Эпоха')
    plt.ylabel('% правильных слов')

    plt.tight_layout()
    plt.show()


# Генерация текста
def generate_text(model, start_str, temp=1.0, length=1000):
    model.eval()

    # Преобразуем начальную строку в тензор
    input_seq = torch.tensor(
        [char_to_idx[c] for c in start_str],
        dtype=torch.long,
        device=device
    ).unsqueeze(0)  # Добавляем batch dimension

    hidden = None
    generated_text = list(start_str)

    for _ in range(length):
        with torch.no_grad():
            # Подаем текущую последовательность
            output, hidden = model(input_seq, hidden)

            # Применяем температуру
            output = output / temp
            probs = torch.softmax(output, dim=1).cpu()

            # Выбираем следующий символ (с учетом вероятностей)
            next_char_idx = torch.multinomial(probs, num_samples=1).item()
            next_char = idx_to_char[next_char_idx]
            generated_text.append(next_char)

            # Обновляем входную последовательность
            input_seq = torch.tensor(
                [[next_char_idx]],
                dtype=torch.long,
                device=device
            )
    return ''.join(generated_text)



if __name__ == '__main__':
    path = "text_for_train.txt"
    text = load_text(path)
    print(f"Длина текста: {len(text)} символов")

    # Создание словаря
    chars = sorted(list(set(text)))  # 89
    vocab_size = len(chars)
    char_to_idx = {ch: i for i, ch in enumerate(chars)}
    idx_to_char = {i: ch for i, ch in enumerate(chars)}

    # Векторизация текста
    dataset = CharDataset(text, seq_length=30)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    # Обучение
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = CharTextGenerator(vocab_size)
    train_model(model, dataloader)

    # Пример генерации
    print("\nФинальная генерация:")
    print(generate_text(model, "И ", temp=1))