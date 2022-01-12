import pandas as pd
from gensim.models import Word2Vec  # conda install -c conda-forge python-levenshtein
#
# review_word = pd.read_csv('crawling/cleaned_review_2015-2021.csv')
# review_word.info()
#
# cleaned_token_review = list(review_word['cleaned_sentences'])
#
# cleaned_tokens = []
#
# for sentence in cleaned_token_review:
#     token = sentence.split()
#     cleaned_tokens.append(token)
# # print(cleaned_tokens)
#
# embedding_model = Word2Vec(cleaned_tokens,
#                            size=100, window=4, min_count=20,
#                            workers=6, sg=1, iter=100)
# embedding_model.save('./models/word2VecModel_2015-2021.model')
embedding_model = Word2Vec.load('./models/word2VecModel_2015-2021.model')
print(embedding_model.wv.vocab.keys())
print(len(embedding_model.wv.vocab.keys()))
