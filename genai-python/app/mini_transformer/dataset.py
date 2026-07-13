import torch
from torch.utils.data import Dataset


class TextDataset(Dataset):

    def __init__(self, filename):

        with open(filename, "r", encoding="utf8") as f:
            self.sentences = [
                line.strip().lower()
                for line in f
                if line.strip()
            ]

        # --------------------------
        # Build vocabulary
        # --------------------------

        words = []

        for sentence in self.sentences:
            words.extend(sentence.split())

        unique_words = sorted(set(words))

        self.word_to_idx = {
            word: idx
            for idx, word in enumerate(unique_words)
        }

        self.idx_to_word = {
            idx: word
            for word, idx in self.word_to_idx.items()
        }

        self.vocab_size = len(self.word_to_idx)

        # --------------------------
        # Build training samples
        # --------------------------

        self.samples = []

        for sentence in self.sentences:

            tokens = [
                self.word_to_idx[word]
                for word in sentence.split()
            ]

            for i in range(1, len(tokens)):

                input_tokens = tokens[:i]

                target = tokens[i]

                self.samples.append(
                    (
                        torch.tensor(input_tokens),
                        torch.tensor(target)
                    )
                )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):

        return self.samples[idx]