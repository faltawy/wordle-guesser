from wordle.main import WordSet
# lets create none repaeted wordlist chars

from wordle.utils import read,save,non_rep_chars
# save(non_rep_chars(read('wordslist')),'nonrepeatedchars')

wordset = WordSet()
wordset.file_name = 'nonrepeatedchars'
load = wordset.load()
wordset.contains('f').not_contain('i').not_contain('t').not_contain('w').not_contain('s').contains('a').letter_at('f',1).letter_at('e',5).not_contain('l').contains('r').contains('a').letter_at('r',3)
wordset.save('queryset1')