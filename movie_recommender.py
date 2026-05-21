import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")


print("Dataset Loaded Successfully!\n")

print("Columns in Dataset:")
print(movies.columns)

print("\nFirst 5 Rows:\n")
print(movies.head())


movies = movies[['movie_id', 'title', 'cast', 'crew']]

movies.fillna('', inplace=True)

movies['tags'] = movies['cast'] + ' ' + movies['crew']
cv = CountVectorizer(max_features=5000, stop_words='english')

vector = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vector)

def recommend(movie_name):

    movie_name = movie_name.lower()

    matched_movies = movies[
        movies['title'].str.lower().str.contains(movie_name)
    ]

    if matched_movies.empty:
        print("\nMovie not found!")
        return
    movie_index = matched_movies.index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    print("\nRecommended Movies:\n")

    count = 0

    for movie in movie_list[1:11]:

        index = movie[0]

        print(movies.iloc[index].title)

        count += 1

        if count == 10:
            break

movie_name = input("\nEnter Movie Name: ")

recommend(movie_name)