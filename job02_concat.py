import pandas as pd
import glob

# data_paths = glob.glob('./crawling_data/reviews_2019_*')
# df = pd.DataFrame()
# for data_path in data_paths:
#     df_temp = pd.read_csv(data_path)
#     df_temp.dropna(inplace=True)
#     df_temp.reset_index(drop=True, inplace=True)
#     # df_temp.columns = ['title', 'reviews']
#     df = pd.concat([df, df_temp], ignore_index=True)
# print(df.head())
# print(df.tail())
# # print(df['title'].value_counts())
# print(df.info())
# df.to_csv('./crawling_data/reviews_{}.csv'.format(2019), index=False)

# data_paths = glob.glob('./crawling_data/reviews_2019_*')
# df = pd.DataFrame()
# for data_path in data_paths:
#     df_temp = pd.read_csv(data_path)
#     df_temp.dropna(inplace=True)
#     df_temp.reset_index(drop=True, inplace=True)
#     # df_temp.columns = ['title', 'reviews']
#     df = pd.concat([df, df_temp], ignore_index=True)
# print(df.head())
# print(df.tail())
# # print(df['title'].value_counts())
# print(df.info())
# df.to_csv('./crawling_data/reviews_{}.csv'.format(2019), index=False)

df = pd.DataFrame()
for i in range(15, 22):
    df_temp = pd.read_csv(
        './crawling_data/reviews_20{}.csv'.format(i))
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    df_temp.columns = ['title','reviews']
    df_temp.to_csv('./crawling/reviews_20{}.csv'.format(i),
                   index=False)
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
df.info()
df.to_csv('./crawling/naver_movie_reviews_2015-2021.csv', index=False)