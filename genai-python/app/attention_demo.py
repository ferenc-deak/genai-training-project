import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import seaborn as sns


# -----------------------------
# 1. Simple toy self-attention
# -----------------------------
class SimpleSelfAttention:
    def __init__(self, d_model=4):
        self.d_model = d_model

        # random weights (toy example)
        self.Wq = torch.randn(d_model, d_model)
        self.Wk = torch.randn(d_model, d_model)
        self.Wv = torch.randn(d_model, d_model)

    def forward(self, x):
        Q = x @ self.Wq
        K = x @ self.Wk
        V = x @ self.Wv

        scores = Q @ K.T / (self.d_model ** 0.5)
        attn = F.softmax(scores, dim=-1)
        output = attn @ V

        return output, attn


# -----------------------------
# 2. Tokenize simple input
# -----------------------------
def tokenize_sentence(sentence):
    words = sentence.lower().split()
    vocab = {w: i for i, w in enumerate(set(words))}

    x = torch.eye(len(vocab))  # one-hot vectors
    tokens = [vocab[w] for w in words]

    return x[tokens], words


# -----------------------------
# 3. Visualization
# -----------------------------
def plot_attention(attn, words):
    plt.figure(figsize=(6, 5))
    sns.heatmap(attn.detach().numpy(),
                xticklabels=words,
                yticklabels=words,
                cmap="Blues",
                annot=True)
    plt.title("Self-Attention Map")
    plt.show()


# -----------------------------
# 4. Run demo
# -----------------------------
if __name__ == "__main__":
    sentence = "the server is down because the server crashed"

    x, words = tokenize_sentence(sentence)

    model = SimpleSelfAttention(d_model=len(words))
    output, attn = model.forward(x)

    print("Attention Matrix:\n", attn)

    plot_attention(attn, words)