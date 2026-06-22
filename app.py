import streamlit as st
import pickle
import requests
# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="MovieRecc",
    page_icon="🎬",
    layout="wide"
)

# ---------------- LOAD DATA ----------------

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
st.markdown("""
<h1 style='text-align:center; font-size:60px;'>
🎬 MovieRecc
</h1>

<p style='text-align:center; font-size:22px;'>
Discover movies you'll love
</p>
""", unsafe_allow_html=True)
st.info(
    "Select a movie and click Recommend to discover similar movies."
)

# ---------------- CSS ----------------

st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #0E1117;
}

/* All Text */
html, body, [class*="css"] {
    color: white;
}

/* Headings */
h1, h2, h3 {
    color: white !important;
}

/* Selectbox Label */
label {
    color: white !important;
    font-weight: bold;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #161B22;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Metric */
[data-testid="stMetricValue"] {
    color: white !important;
}

[data-testid="stMetricLabel"] {
    color: white !important;
}

/* Recommended Movie Cards */
div[data-testid="column"] {
    background-color: #161B22;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

/* Button */
.stButton > button {
    background-color: #1F6FEB;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    width: 100%;
}

.stButton > button:hover {
    background-color: #388BFD;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- RECOMMEND FUNCTION ----------------

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies

# ---------------- HEADER ----------------

st.title("🎬 MovieRecc")
st.subheader("Find Your Next Favorite Movie")

# ---------------- SEARCH SECTION ----------------

col1, col2 = st.columns([3,1])

with col1:
    selected_movie = st.selectbox(
        "Search Movie",
        movie_list
    )

with col2:
    st.metric("Movies Available", "4800+")

# ---------------- BUTTON ----------------

# ---------------- BUTTON ----------------

if st.button("Recommend"):

    with st.spinner("Finding great movies for you..."):

        recommendations = recommend(selected_movie)

    st.subheader("Recommended For You")

    cols = st.columns(5)

    for idx, movie in enumerate(recommendations):

        with cols[idx]:

            st.info(movie, icon="🎬")
# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
    """
    <center style="color:white;">
        Built with ❤️ using Python, Pandas and Streamlit
    </center>
    """,
    unsafe_allow_html=True
)