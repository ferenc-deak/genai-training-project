import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import seaborn as sns



# 1. Tokenizer

def tokenize(sentence):
    words = sentence.lower().split()
    vocab = {w: i for i, w in enumerate(set(words))}

    tokens = torch.tensor([vocab[w] for w in words])
    return tokens, words, vocab



# 2. Mini Transformer

class MiniTransformer(nn.Module):
    def __init__(self, vocab_size, d_model=16):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, d_model)

        self.Wq = nn.Linear(d_model, d_model)
        self.Wk = nn.Linear(d_model, d_model)
        self.Wv = nn.Linear(d_model, d_model)

        self.fc = nn.Linear(d_model, d_model)

    def forward(self, x):
        x = self.embedding(x)

        Q = self.Wq(x)
        K = self.Wk(x)
        V = self.Wv(x)

        scores = Q @ K.transpose(-2, -1)
        scores = scores / (x.shape[-1] ** 0.5)

        attn = F.softmax(scores, dim=-1)
        out = attn @ V

        return self.fc(out), attn



# 3. Visualization

def plot_attention(attn, words):
    import numpy as np

    attn = attn.detach().numpy()

    plt.figure(figsize=(8, 6))
    sns.heatmap(
        attn,
        xticklabels=words,
        yticklabels=words,
        cmap="Blues"
    )
    plt.title("Self-Attention Map")
    plt.show()



# 4. RUN EVERYTHING

if __name__ == "__main__":

    sentence = "server server server crashed"

    tokens, words, vocab = tokenize(sentence)

    model = MiniTransformer(len(vocab))

    output, attn = model(tokens)

    print("\nWords:", words)
    print("\nAttention Matrix:\n", attn)

    plot_attention(attn, words)