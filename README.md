# 🎬 Movie Recommendation System Using Machine Learning

<img src="demo/banner.png" alt="Movie Recommendation System" width="100%">

## 📌 Project Overview

The **Movie Recommendation System** is a Machine Learning application that recommends movies similar to a user's selected movie. It uses **Content-Based Filtering** with **Cosine Similarity** to identify movies that share similar characteristics such as genres, keywords, cast, crew, and overview.

The application is built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**, providing an interactive and user-friendly interface for movie recommendations.

---

## 🚀 Features

* 🎥 Movie recommendation based on user selection
* ⚡ Fast recommendations using precomputed similarity matrix
* 🎯 Content-Based Filtering algorithm
* 📊 Cosine Similarity for finding similar movies
* 💻 Interactive Streamlit web application
* 📦 Pre-trained model using Joblib
* 🔍 Simple and responsive user interface

---

## 🧠 Machine Learning Approach

This project uses a **Content-Based Recommendation System**.

### Workflow

1. Load the TMDB movie dataset.
2. Perform data cleaning and preprocessing.
3. Combine important features such as:

   * Genres
   * Keywords
   * Cast
   * Crew
   * Overview
4. Convert text into numerical vectors using **CountVectorizer**.
5. Calculate similarity using **Cosine Similarity**.
6. Save the processed data and similarity matrix using Joblib.
7. Build a Streamlit application to generate movie recommendations.

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── movie_list.joblib
├── similarity.joblib
├── notebook.ipynb
├── requirements.txt
├── README.md
└── demo/
    ├── home.png
    ├── recommendation.png
    └── banner.png
```

---

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset**.

Dataset Files:

* tmdb_5000_movies.csv
* tmdb_5000_credits.csv

Source:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

---

## 📦 Saved Model Files

The recommendation engine uses two Joblib files:

### movie_list.joblib

Contains the processed movie dataframe.

```python
joblib.load("movie_list.joblib")
```

### similarity.joblib

Contains the cosine similarity matrix.

```python
joblib.load("similarity.joblib")
```

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

---

## 📐 Algorithm Used

### Content-Based Filtering

Content-Based Filtering recommends movies that have similar characteristics to the movie selected by the user.

### Cosine Similarity

Cosine Similarity measures the similarity between two movie vectors.

The similarity score ranges between:

* **1** → Highly Similar
* **0** → Completely Different

---

## 💻 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Movie-Recommendation-System.git
```

Move into the project directory.

```bash
cd Movie-Recommendation-System
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Recommendation Process

1. Select a movie from the dropdown list.
2. Click the **Recommend Movies** button.
3. The system searches the similarity matrix.
4. The top 5 most similar movies are displayed.

---

## Future Enhancements

* 🎬 Movie Posters using TMDB API
* ⭐ IMDb Ratings
* 🎥 Movie Trailers
* 📅 Release Year
* 🎭 Genre Filtering
* 🔍 Search Functionality
* ❤️ Favorite Movies
* 📱 Mobile-Friendly UI
* 🤖 Hybrid Recommendation System
* ☁️ Cloud Deployment

---

## Author

**Om Yadav**

**Python Developer | Data Scientist**

### Skills

* Python
* Machine Learning
* Data Science
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* TensorFlow
* Flask
* FastAPI

---

## License

This project is developed for learning, portfolio, and demonstration purposes.
