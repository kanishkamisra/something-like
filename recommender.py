import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel

products = pd.read_csv('data/sample-data.csv')

tfidf = TfidfVectorizer(analyzer = 'word', ngram_range = (1,3), min_df = 0, stop_words = 'english')
tfidf_matrix = tfidf.fit_transform(products.description)

cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

similarities = {}

for index, row in products.iterrows():
    similar_indices = cosine_similarities[index].argsort()[:-100:-1]
    # add product title after you separate it!
    similar_items = [(cosine_similarities[index][i], products['id'][i]) for i in similar_indices]
    similarities[row['id']] = similar_items[1:]

def query_item(item_id):
    return products.loc[products['id'] == item_id]['description'].tolist()[0].split(' - ')[0]

def recommend(item_id, n):
    print(str(n) + " products similar to " + query_item(item_id) + " :")
    print("------------------")
    recommendations = similarities[item_id][:n]
    for r in recommendations:
        print(query_item(r[1]) + " (score:" + str(r[0]) + ")")


