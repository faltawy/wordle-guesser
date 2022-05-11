from typing import Iterable, List, Set
import tqdm

def read(file_name:str)->List[str]:
    with open(f'{file_name}.txt','r') as file:
        lines = file.readlines()
    return [line.strip().lower() for line in lines]

def get_5_only(lines:List[str])->Set[str]:
    words = []
    for word in tqdm.tqdm(lines):
        if len(word) == 5:
            words.append(word)
    return set(words)


def save(iterable:Iterable[str],file_name:str):
    with open(f'{file_name}.txt',"w") as file:
        for i in iterable:
            file.write(i + '\n')



def non_rep_chars(words:List[str]) ->Set:
    __words = {i if len(i) == len(set(i)) else '\r' for i in words}
    return __words

