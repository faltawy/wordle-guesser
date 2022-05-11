from typing import Counter, List

from typing_extensions import Self

from .utils import read,save


class Word:
    def __init__(self,word:str):
        _word =word.strip().lower()
        if len(_word) != 5 :
            raise Exception('Word {} must be 5 chars'.format(_word))

        else:
            self.__word = _word


    def __str__(self) -> str:
        return 'word=' + self.__word

    @property
    def counter(self):
        return Counter(self.__word)

    def contains(self,letter:str):
        return self.__word.__contains__(letter)
    
    @property
    def letters(self):
        return list(self.__word)
    
    @property
    def word(self):
        return self.__word
    
    def get_index(self,index:int)->str:
        "get letter by it's index"
        if index > 5 or index < 1:
            raise Exception('index must be from 1 to 5')
        else:
            return self.__word[index-1]
    

class WordSet:
    def __init__(self,file_name:str='wordslist') -> None:
        self.__words:List[Word]
        self.file_name = 'wordslist'
    
    def __load(self):
        return read(self.file_name)

    def load(self) -> Self:
        words = self.__load()
        self.__words = [Word(word) for word in words]
        return self
    
    def not_contain(self,letter:str):
        words = []
        for word in self.__words:
            if not word.contains(letter.lower()):
                words.append(word)
        self.__words = list(set(words))
        return self

    def letter_at(self,letter:str,index:int):
        words = []
        for word in self.__words:
            if word.get_index(index) == letter.lower():
                words.append(word)
        self.__words = words
        return self

    def contains(self,letter:str):
        words = []
        for word in self.__words:
            if word.contains(letter.lower()):
                words.append(word)
        self.__words  = words
        return self

    def save(self,file_name):
        if self.__words != None:
            save([word.word for word in self.__words],file_name)
    
    @property
    def get_most_repeated_chars(self):
        return sorted(self.counter_all)


    @property    
    def words(self) ->List[Word]:
        return self.__words

    @property
    def count(self) ->int:
        return len(self.__words)
    
    @property
    def counter_all(self)->List[Counter]:
        return [i.counter for i in self.__words]
    
    def __str__(self) -> str:
        return f'words = {self.count} from {self.file_name}'