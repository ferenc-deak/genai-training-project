import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import seaborn as sns



# 1. Simple self-attention

class SimpleSelfAttention:
    def __init__(self, d_model):
        self.d_model = d_model

        self.Wq = torch.randn(d_model, d_model)
        self.Wk = torch.randn(d_model, d_model)
        self.Wv = torch.randn(d_model, d_model)

    def forward(self, x):
        # x: (seq_len, d_model)

        Q = x @ self.Wq
        K = x @ self.Wk
        V = x @ self.Wv

        scores = Q @ K.T / (self.d_model ** 0.5)
        attn = F.softmax(scores, dim=-1)
        output = attn @ V

        return output, attn



# 2. Tokenization (FIXED)

def tokenize_sentence(sentence, d_model=4):
    words = sentence.lower().split()
    seq_len = len(words)

    # random embeddings instead of one-hot
    x = torch.randn(seq_len, d_model)

    return x, words



# 3. Visualization

def plot_attention(attn, words):
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        attn.detach().numpy(),
        xticklabels=words,
        yticklabels=words,
        cmap="Blues",
        annot=True
    )
    plt.title("Self-Attention Map")
    plt.show()



# 4. Run demo

if __name__ == "__main__":
    sentence = "the server is down because the server crashed"

    x, words = tokenize_sentence(sentence, d_model=4)

    model = SimpleSelfAttention(d_model=4)

    output, attn = model.forward(x)

    print("Attention Matrix:\n", attn)

    plot_attention(attn, words)