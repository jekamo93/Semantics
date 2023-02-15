import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Write a note about what you found interesting about the similarities
# between cat, monkey and banana and think of an example of your own.
# cat and monkey are similar because they are both animals
# monkey and banana are quite similar because monkeys eat bananas
# cat and banana are not similar because cats don't eat bananas
# below is my example
# moose and elephant are similar because they are both animals
# moose and africa are not similar because mooses don't live in africa
# elephant and africa are more similar because elephants live in africa

my_tokens = nlp("moose elephant africa")
for token1 in my_tokens:
    for token2 in my_tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# Run the example file with the simpler language model ‘en_core_web_sm’
# and write a note on what you notice is different from the model
# 'en_core_web_md'
# the difference is that with 'en_core_web_md' similarity numbers are lower

