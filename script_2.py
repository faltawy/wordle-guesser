from wordle.main import WordSet



wordset = WordSet()
load = wordset.load()
wordset.letter_at('a',2).letter_at('r',3).contains('e').contains('c').not_contain('t')
wordset.save('queryset')