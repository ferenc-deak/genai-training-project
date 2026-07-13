import torch
import matplotlib.pyplot as plt
import seaborn as sns

from model import TinyTransformer


# --------------------------
# Load saved model
# --------------------------

checkpoint = torch.load("tiny_transformer.pth")

word_to_idx = checkpoint["word_to_idx"]
idx_to_word = checkpoint["idx_to_word"]
d_model = checkpoint["d_model"]

vocab_size = len(word_to_idx)


# --------------------------
# Recreate model
# --------------------------

model = TinyTransformer(
    vocab_size=vocab_size,
    d_model=d_model
)

model.load_state_dict(checkpoint["model_state_dict"])

model.eval()


# --------------------------
# Sentence to visualize
# --------------------------

sentence = "the server crashed"

words = sentence.lower().split()

token_ids = []

for word in words:

    if word not in word_to_idx:
        raise ValueError(f"Unknown word: {word}")

    token_ids.append(word_to_idx[word])

x = torch.tensor(token_ids)


# --------------------------
# Run model
# --------------------------

with torch.no_grad():

    logits, attention = model(x)


# --------------------------
# Predict next word
# --------------------------

predicted_index = torch.argmax(logits).item()

predicted_word = idx_to_word[predicted_index]

print()

print("Input sentence:")
print(sentence)

print()

print("Predicted next word:")
print(predicted_word)

print()

print("Attention matrix:")
print(attention)


# --------------------------
# Plot attention
# --------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
    attention.numpy(),
    xticklabels=words,
    yticklabels=words,
    cmap="Blues",
    annot=True,
    fmt=".2f"
)

plt.title("Learned Self-Attention")

plt.xlabel("Key")

plt.ylabel("Query")

plt.show()