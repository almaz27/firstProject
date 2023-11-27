import nltk
sentence =""" On amending the Constitutional Law of the Kyrgyz Republic“ On the Constitutional Court of the Kyrgyz Republic """
tokens = nltk.word_tokenize(sentence)
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged)
entities = nltk.chunk.ne_chunk(tagged)
print(type(entities))
