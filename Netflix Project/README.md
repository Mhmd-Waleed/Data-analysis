# 🎬 Netflix Titles Analysis

## 📌 Overview
This project explores the **Netflix Titles Dataset**, which contains information about movies and TV shows available on Netflix.  
The analysis aims to uncover insights about **content types, top-producing countries, top directors, genres, ratings, and content growth over time.**

---

## ⚙️ Steps
1. **Import Libraries**  
2. **Load Data**  
3. **Understand Data**  
4. **Ask Questions**  
5. **Clean Data**  
6. **Answer the Questions (EDA & Visualization)**  

---

## ❓ Key Questions Explored
- 🎥 Who are the **most prolific directors** on Netflix?  
- 🌍 Which **countries** produce the most Netflix titles?  
- 📺 What is the distribution between **Movies and TV Shows**?  
- 🎭 What are the **top 5 genres** on Netflix?  
- ⭐ What is the **distribution of content ratings**?  
- 📅 How has the **number of titles changed over the years**?

---

## 🧹 Data Cleaning
- Filled missing values in:
  - `director`, `cast`, `country`, and `rating` → `"Unknown"`
- Dropped rows missing critical data (`date_added`, `duration`)
- Converted `date_added` column to `datetime`  
- Extracted `year` for time-series analysis  
- Removed duplicate entries  

---

## 📊 Visualizations
| Chart | Description |
|--------|--------------|
| 📊 Bar Chart | Top 5 Directors with most titles |
| 📈 Bar Chart | Top 5 Countries producing content |
| 🎞️ Bar Chart | Distribution of Movies vs TV Shows |
| 🎭 Bar Chart | Top 5 Most Common Genres |
| 🥧 Donut Chart | Content Ratings Distribution |
| 📅 Line Chart | Growth of Movies & TV Shows Over Time |

---

## 🔍 Insights
| # | Insight |
|---|----------|
| 1 | **Rajiv Chilaka** is the most frequent director on Netflix. |
| 2 | The **United States** produces the largest number of Netflix titles. |
| 3 | **Movies** dominate Netflix’s catalog compared to TV Shows. |
| 4 | Top genres include **Dramas**, **Comedies**, and **Documentaries**. |
| 5 | **TV-MA** and **TV-14** are the most common ratings. |
| 6 | Content growth peaked around **2018–2020**, showing Netflix’s expansion phase. |

---

## 🧩 Tools Used
- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

---

## 📈 Sample Visuals
- 🎬 Top Directors by Content  
- 🌎 Top Countries by Titles  
- 🧾 Movie vs TV Show Distribution  
- 🎭 Top Genres  
- ⭐ Ratings Distribution  
- 📅 Movies & TV Shows Over Time  

---

## 👨‍💻 Author
**Mohammed Waleed**  
📧 [mohammed.waleed1121@gmail.com](mailto:mohammed.waleed1121@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/mohammed-waleed-533931375/)  
📅 2025  

---

> 💡 *A clean and insightful EDA project revealing trends and growth patterns of Netflix content worldwide.*
