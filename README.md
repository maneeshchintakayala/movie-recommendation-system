# 🎬 Movie Recommendation System

A simple **Content-Based Movie Recommendation System** built using **Python, Pandas, and Scikit-learn**. The system recommends similar movies based on cast and crew information by calculating text similarity using **CountVectorizer** and **Cosine Similarity**.

---

# 📌 Project Overview

The Movie Recommendation System suggests movies that are similar to a movie entered by the user. Instead of using user ratings, this project uses a **content-based filtering approach**, where movie metadata (cast and crew) is analyzed to find similar movies.

This project demonstrates the basics of recommendation systems and Natural Language Processing (NLP).

---

# ✨ Features

- ✅ Load movie dataset from CSV
- ✅ Display dataset information
- ✅ Handle missing values
- ✅ Combine cast and crew information
- ✅ Convert text into numerical vectors using CountVectorizer
- ✅ Calculate similarity using Cosine Similarity
- ✅ Recommend the Top 10 similar movies
- ✅ Supports partial movie name search

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning |
| CountVectorizer | Text Feature Extraction |
| Cosine Similarity | Recommendation Engine |

---

# 📂 Project Structure

```
Movie-Recommendation-System/
│
├── movie_recommender.py
├── movies.csv
├── README.md
└── screenshots/
    ├── dataset.png
    └── recommendation.png
```

---

# 📊 Dataset

The project uses a CSV dataset containing movie information.

### Required Columns

| Column | Description |
|---------|-------------|
| movie_id | Unique Movie ID |
| title | Movie Title |
| cast | Cast Members |
| crew | Crew Members |

Example:

| movie_id | title | cast | crew |
|----------|-------|------|------|
| 1 | Avatar | Sam Worthington... | James Cameron... |

---

# ⚙️ How It Works

1. Load the movie dataset.
2. Select the required columns.
3. Replace missing values with empty strings.
4. Combine the **cast** and **crew** columns into a single **tags** column.
5. Convert text into numerical vectors using **CountVectorizer**.
6. Compute similarity scores using **Cosine Similarity**.
7. Accept a movie name as input.
8. Find the closest matching movie.
9. Display the **Top 10 recommended movies**.

---

# ▶️ Installation

## Step 1

Clone the repository

```bash
git clone https://github.com/yourusername/Movie-Recommendation-System.git
```

## Step 2

Navigate into the project

```bash
cd Movie-Recommendation-System
```

## Step 3

Install the required libraries

```bash
pip install pandas scikit-learn
```

## Step 4

Run the project

```bash
python movie_recommender.py
```

---

# ▶️ Usage

After running the program, enter a movie name when prompted.

Example:

```text
Enter Movie Name: Avatar
```

Output:

```text
Recommended Movies:

Avatar: The Way of Water
Titanic
Aliens
The Abyss
Terminator 2: Judgment Day
True Lies
...
```

The system displays up to **10 movies** that are most similar based on cast and crew information.

---

# 🔄 Project Workflow

```
Start Program
        │
        ▼
Load Dataset
        │
        ▼
Select Required Columns
        │
        ▼
Handle Missing Values
        │
        ▼
Create Tags (Cast + Crew)
        │
        ▼
Convert Text into Vectors
        │
        ▼
Calculate Cosine Similarity
        │
        ▼
User Enters Movie Name
        │
        ▼
Find Similar Movies
        │
        ▼
Display Top 10 Recommendations
```

---

# 🧠 Machine Learning Concepts Used

### Content-Based Filtering

Recommendations are generated based on movie metadata rather than user ratings.

### CountVectorizer

Converts textual information (cast and crew) into numerical feature vectors.

### Cosine Similarity

Measures how similar two movies are by comparing their feature vectors.

---

# 🎯 Learning Outcomes

This project helps in understanding:

- Data preprocessing with Pandas
- Text feature extraction
- Natural Language Processing (NLP)
- CountVectorizer
- Cosine Similarity
- Recommendation Systems
- Content-Based Filtering
- Data manipulation in Python

---

# 🚀 Future Enhancements

Potential improvements include:

- Use movie genres, keywords, and overview for better recommendations
- Add movie posters
- Create a GUI using Tkinter
- Build a web application using Flask or Streamlit
- Recommend movies based on user ratings (Collaborative Filtering)
- Hybrid recommendation system
- Display movie details such as release year, rating, and overview
- Add fuzzy matching for improved search accuracy

---

# 📸 Screenshots

Store screenshots inside the `screenshots` folder.

Example:

```
screenshots/
    dataset.png
    recommendation.png
```

---

# 📋 Requirements

- Python 3.8 or above
- Pandas
- Scikit-learn

Install dependencies:

```bash
pip install pandas scikit-learn
```

---

# 👨‍💻 Author

**Maneesh Chintakayala**

Python Developer | Machine Learning Enthusiast | Data Science Enthusiast

---

# 📄 License

This project is developed for educational and learning purposes. You are free to use, modify, and enhance it for personal or academic use.

---

# ⭐ Support

If you found this project helpful:

- ⭐ Star the repository
- 🍴 Fork the repository
- 💡 Contribute improvements
- 🐞 Report issues through GitHub Issues

---

# 📌 Project Status

✅ Completed