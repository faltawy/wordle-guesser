from wordle.utils import (read,save,get_5_only,non_rep_chars)



data = read('words_alpha')
chars_5_only = get_5_only(data)
save(chars_5_only,'5chars')

# we will get 15_920 word
# original list => 370_000 word
# the 5 letter ones => 15_000


# getting non repeated chars words

# data = read('5chars')
# non_rep = non_rep_chars(data)
# save(non_rep,'non_rep')

# we will get 10_175 words

