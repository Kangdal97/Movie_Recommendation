import pandas as pd

df = pd.read_csv('crawling/naver_movie_reviews_2015-2021.csv')
one_sentences = []

for title in df['title'].unique():
    temp = df[df['title'] == title]
    temp = temp['reviews']
    one_sentence = ' '.join(temp)
    one_sentences.append(one_sentence)
df_one_sentence = pd.DataFrame({'titles': df['title'].unique(), 'reviews': one_sentences})
print(df_one_sentence.head())
df_one_sentence.to_csv('./crawling/naver_movie_reviews_onesentence_2015-2021.csv', index=False)
