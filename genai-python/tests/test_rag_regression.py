from app.rag.rag import ask_question


def test_rag_python():

    result = ask_question("What is Python?")

    answer = result["answer"].lower()

    assert "programming language" in answer

    assert len(result["sources"]) > 0


def test_rag_fastapi():

    result = ask_question("What is FastAPI?")

    answer = result["answer"].lower()

    assert "web framework" in answer

    assert len(result["sources"]) > 0


def test_rag_rag():

    result = ask_question(
        "What is Retrieval Augmented Generation?"
    )

    answer = result["answer"].lower()

    assert "retrieval" in answer

    assert len(result["sources"]) > 0


def test_unknown_question():

    result = ask_question(
        "Who won the FIFA World Cup in 1998?"
    )

    answer = result["answer"].lower()

    assert (
        "don't know" in answer
        or "not in context" in answer
    )