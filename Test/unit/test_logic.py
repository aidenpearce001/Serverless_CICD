import pytest

def test_sum_correct(logic) -> None:
    assert logic.simple_sum(1, 2) == 4, "Failed"

def test_multiple_correct(logic) -> None:
    assert logic.multiple(2, 2) == 4, "Failed"

def test__correct(logic) -> None:
    assert logic.square_root(9) == 3, "Failed"

StudentA={
    "FullName": "Jane",
    "age": 20,
    "Marks": [
        {
            "skill": "Read",
            "mark": 30
        },
        {
            "skill": "Listening",
            "mark": 67
        },
        {
            "skill": "Speaking",
            "mark": 46
        },
        {
            "skill": "Writting",
            "mark": 54
        },
    ]
}

def test_studentA_rating(Calulator):

    assert(Calulator.rating([_["mark"] for _ in StudentA["Marks"]])) == "C2", "Must Be C2"