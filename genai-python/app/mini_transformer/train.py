import torch
import torch.nn as nn
from torch.optim import Adam
from torch.utils.data import DataLoader

from dataset import TextDataset
from model import TinyTransformer


# --------------------------
# Configuration
# --------------------------

DATASET_PATH = "data.txt"

D_MODEL = 32

EPOCHS = 200

LEARNING_RATE = 0.001


# --------------------------
# Load dataset
# --------------------------

dataset = TextDataset(DATASET_PATH)

print(f"Vocabulary size: {dataset.vocab_size}")
print(f"Training samples: {len(dataset)}")


# --------------------------
# DataLoader
# --------------------------

# batch_size=1 because our input sequences
# have different lengths.
loader = DataLoader(
    dataset,
    batch_size=1,
    shuffle=True
)


# --------------------------
# Create model
# --------------------------

model = TinyTransformer(
    vocab_size=dataset.vocab_size,
    d_model=D_MODEL
)


# --------------------------
# Loss function
# --------------------------

criterion = nn.CrossEntropyLoss()


# --------------------------
# Optimizer
# --------------------------

optimizer = Adam(
    model.parameters(),
    lr=LEARNING_RATE
)


# --------------------------
# Training Loop
# --------------------------

for epoch in range(EPOCHS):

    total_loss = 0

    for inputs, target in loader:

        # Remove batch dimension
        inputs = inputs.squeeze(0)
        target = target.long()

        # ----------------------
        # Forward pass
        # ----------------------

        logits, attention = model(inputs)

        # logits shape:
        # (vocab_size)

        # CrossEntropyLoss expects:
        #
        # (batch_size, classes)
        #
        logits = logits.unsqueeze(0)

        loss = criterion(logits, target)

        # ----------------------
        # Backpropagation
        # ----------------------

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    average_loss = total_loss / len(loader)

    print(
        f"Epoch {epoch + 1}/{EPOCHS} "
        f"Loss: {average_loss:.4f}"
    )


# --------------------------
# Save model
# --------------------------

torch.save(
    {
        "model_state_dict": model.state_dict(),
        "word_to_idx": dataset.word_to_idx,
        "idx_to_word": dataset.idx_to_word,
        "d_model": D_MODEL
    },
    "tiny_transformer.pth"
)

print("\nTraining finished!")

print("Model saved as tiny_transformer.pth")