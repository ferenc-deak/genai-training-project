import json

from app.rag.retriever import (
    get_retriever,
    search_docs
)


DATASET_PATH = "evaluation/rag_dataset.jsonl"


def load_dataset():

    dataset = []

    with open(DATASET_PATH, "r") as file:
        for line in file:
            if line.strip():
               dataset.append(json.loads(line))

    return dataset


# -------------------------
# Baseline retrieval
# -------------------------

def baseline_search(query, k=5):

    db = get_retriever()

    return db.similarity_search(
        query,
        k=k
    )


# -------------------------
# Recall@K metric
# -------------------------

def calculate_recall(search_function, k=5):

    dataset = load_dataset()

    correct = 0

    for item in dataset:

        docs = search_function(
            item["query"],
            k
        )

        sources = [
            doc.metadata.get("source")
            for doc in docs
        ]

        if item["expected_source"] in sources:
            correct += 1


    return correct / len(dataset)



if __name__ == "__main__":

    baseline = calculate_recall(
        baseline_search,
        k=5
    )

    hybrid = calculate_recall(
        search_docs,
        k=5
    )


    print("====================")
    print("RAG Evaluation")
    print("====================")

    print(
        f"Baseline Recall@5: {baseline:.2f}"
    )

    print(
        f"Hybrid Recall@5: {hybrid:.2f}"
    )

    print(
        f"Improvement: {(hybrid - baseline):.2f}"
    )