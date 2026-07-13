import torch
import torch.nn as nn
import torch.nn.functional as F


class TinyTransformer(nn.Module):

    def __init__(self, vocab_size, d_model):

        super().__init__()

        self.d_model = d_model

        # Trainable word embeddings
        self.embedding = nn.Embedding(vocab_size, d_model)

        # Trainable Query, Key and Value projections
        self.Wq = nn.Linear(d_model, d_model, bias=False)
        self.Wk = nn.Linear(d_model, d_model, bias=False)
        self.Wv = nn.Linear(d_model, d_model, bias=False)

        # Predict next word
        self.output_layer = nn.Linear(d_model, vocab_size)

    def forward(self, x):

        # x shape:
        # (sequence_length)

        embeddings = self.embedding(x)

        # (sequence_length, d_model)

        Q = self.Wq(embeddings)
        K = self.Wk(embeddings)
        V = self.Wv(embeddings)

        scores = torch.matmul(Q, K.transpose(0, 1))
        scores = scores / (self.d_model ** 0.5)

        attention = F.softmax(scores, dim=-1)

        context = torch.matmul(attention, V)

        # Only use the last token
        last_token = context[-1]

        logits = self.output_layer(last_token)

        return logits, attention