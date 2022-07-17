from typing import Iterable, List, Set

def read(file_name: str) -> List[str]:
    with open(f"{file_name}.txt", "r") as file:
        lines = file.readlines()
    return [line.strip().lower() for line in lines]


def get_5_only(words: List[str]) -> Set[str]:
    return set(list(filter(lambda line: len(line) == 5, words)))


def save(iterable: Iterable[str], file_name: str):
    with open(f"{file_name}.txt", "w") as file:
        for i in iterable:
            file.write(i + "\n")


def non_rep_chars(words: List[str]) -> Set:
    return set(list(filter(lambda word: len(word) == len(set(word)), words)))




