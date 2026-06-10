import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
movies = pd.read_csv(r"D:\VS_CODE\movie_dataset\Movie-Rating.csv")

# Rename columns exactly like notebook
movies.columns = [
    'Film',
    'Genre',
    'CriticRating',
    'AudienceRating',
    'BudgetMillions',
    'Year'
]

movies['Genre'] = movies['Genre'].astype('category')
movies['Year'] = movies['Year'].astype('category')

st.title("🎬 Movie Rating Analytics Dashboard")
st.subheader("Miss Swati Jadhav - Seaborn Bootcamp")

st.dataframe(movies.head())

graph = st.sidebar.selectbox(
    "Select Graph",
    [
        "Joint Plot",
        "Hex Plot",
        "Histogram",
        "Genre Histogram",
        "Stacked Histogram",
        "LM Plot",
        "Genre LM Plot",
        "KDE Plot",
        "Filled KDE Plot",
        "Box Plot",
        "Violin Plot",
        "Drama Box Plot",
        "Drama Violin Plot",
        "FacetGrid Scatter",
        "FacetGrid Histogram"
    ]
)

if graph == "Joint Plot":
    j = sns.jointplot(
        data=movies,
        x='CriticRating',
        y='AudienceRating'
    )
    st.pyplot(j.figure)

elif graph == "Hex Plot":
    j = sns.jointplot(
        data=movies,
        x='CriticRating',
        y='AudienceRating',
        kind='hex'
    )
    st.pyplot(j.figure)

elif graph == "Histogram":
    fig, ax = plt.subplots()
    sns.histplot(
        movies['AudienceRating'],
        bins=15,
        kde=True,
        ax=ax
    )
    st.pyplot(fig)

elif graph == "Genre Histogram":
    fig, ax = plt.subplots()
    plt.hist(
        movies[movies.Genre == 'Drama'].BudgetMillions
    )
    st.pyplot(fig)

elif graph == "Stacked Histogram":
    fig, ax = plt.subplots()

    plt.hist([
        movies[movies.Genre == 'Action'].BudgetMillions,
        movies[movies.Genre == 'Drama'].BudgetMillions,
        movies[movies.Genre == 'Thriller'].BudgetMillions,
        movies[movies.Genre == 'Comedy'].BudgetMillions
    ],
    bins=20,
    stacked=True)

    plt.legend(['Action','Drama','Thriller','Comedy'])
    st.pyplot(fig)

elif graph == "LM Plot":
    g = sns.lmplot(
        data=movies,
        x='CriticRating',
        y='AudienceRating',
        fit_reg=False
    )
    st.pyplot(g.figure)

elif graph == "Genre LM Plot":
    g = sns.lmplot(
        data=movies,
        x='CriticRating',
        y='AudienceRating',
        fit_reg=False,
        hue='Genre'
    )
    st.pyplot(g.figure)

elif graph == "KDE Plot":
    fig, ax = plt.subplots()

    sns.kdeplot(
        data=movies,
        x='CriticRating',
        y='AudienceRating',
        ax=ax
    )

    st.pyplot(fig)

elif graph == "Filled KDE Plot":
    fig, ax = plt.subplots()

    sns.kdeplot(
        data=movies,
        x='CriticRating',
        y='AudienceRating',
        fill=True,
        cmap='Reds',
        ax=ax
    )

    st.pyplot(fig)

elif graph == "Box Plot":
    fig, ax = plt.subplots(figsize=(10,5))

    sns.boxplot(
        data=movies,
        x='Genre',
        y='CriticRating',
        ax=ax
    )

    plt.xticks(rotation=45)
    st.pyplot(fig)

elif graph == "Violin Plot":
    fig, ax = plt.subplots(figsize=(10,5))

    sns.violinplot(
        data=movies,
        x='Genre',
        y='CriticRating',
        ax=ax
    )

    plt.xticks(rotation=45)
    st.pyplot(fig)

elif graph == "Drama Box Plot":
    fig, ax = plt.subplots()

    sns.boxplot(
        data=movies[movies.Genre=='Drama'],
        x='Year',
        y='CriticRating',
        ax=ax
    )

    st.pyplot(fig)

elif graph == "Drama Violin Plot":
    fig, ax = plt.subplots()

    sns.violinplot(
        data=movies[movies.Genre=='Drama'],
        x='Year',
        y='CriticRating',
        ax=ax
    )

    st.pyplot(fig)

elif graph == "FacetGrid Scatter":
    g = sns.FacetGrid(
        movies,
        row='Genre',
        col='Year',
        hue='Genre'
    )

    g.map(
        plt.scatter,
        'CriticRating',
        'AudienceRating'
    )

    st.pyplot(g.figure)

elif graph == "FacetGrid Histogram":
    g = sns.FacetGrid(
        movies,
        row='Genre',
        col='Year',
        hue='Genre'
    )

    g.map(
        plt.hist,
        'BudgetMillions'
    )

    st.pyplot(g.figure)