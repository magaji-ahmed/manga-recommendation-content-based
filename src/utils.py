import pickle
import numpy as np

def read_object(filepath):
    obfile = open(filepath, 'rb')
    object = pickle.load(obfile)
    obfile.close()
    return object

def index_from_title(df,title):
    return df[df['ctitle'] == title].index.values[0]

def title_from_index(df, index):
    return df[df.index == index].title.values[0]

def recommendations(original_title, df, cosine_similarity_matrix, number_of_recommendations):
    index = index_from_title(df, original_title)
    if index:
        similarity_scores = list(enumerate(np.squeeze(np.asarray(cosine_similarity_matrix[index].todense()))))
        # similarity_scores = list(enumerate(cosine_similarity_matrix[index]))
        similarity_scores_sorted = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        recommendations_indices = [t[0] for t in similarity_scores_sorted[1:(number_of_recommendations +1)]]
        return df[['ctitle', 'description']].iloc[recommendations_indices]
    else:
        return 'No valid recommendation'