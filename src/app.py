import pickle
import pandas as pd
import streamlit as st
from streamlit import session_state as session
from utils import recommendations, read_object

@st.cache_data(persist=True, show_spinner=False)
def load_data():
    cos_simi_mat_desc = read_object('artifacts/cosine_similarity_desc.pkl')
    df_manga_rel = pd.read_csv('artifacts/manga_clean.csv', index_col='manga_id')

    return cos_simi_mat_desc, df_manga_rel

simi_mat, df = load_data()

dataframe = None

st.title("""
Manga Recommendation System
""")
         
st.text('')
st.text('')
st.text('')
st.text('')

session.options = st.multiselect('select movies', options=df['ctitle'])

st.text('')
st.text('')

session.slider_count = st.slider('movie count', min_value=5, max_value=30)

st.text('')
st.text('')

buf1, col1, buf3 = st.columns([1.45, 1, 1])

is_clicked = st.button('Recommend')

if is_clicked:
    # print(session.options[0])
    # print(session.slider_count)
    dataframe = recommendations(session.options[0], df, simi_mat, session.slider_count)

st.text('')
st.text('')
st.text('')
st.text('')

if dataframe is not None:
    st.table(dataframe)