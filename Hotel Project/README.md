# 🏨 Hotel Bookings Analysis

## 📌 Overview
This project analyzes hotel booking data to uncover insights about **booking behavior, cancellations, revenue trends, and customer demographics** for both city and resort hotels.  
The goal is to identify patterns that can help hotel management improve performance and reduce cancellations.

---

## ⚙️ Steps
1. **Import Libraries**  
2. **Load Data**  
3. **Ask Questions**  
4. **Clean Data**  
5. **Answer the Questions (EDA & Visualization)**  

---

## ❓ Key Questions Explored
- 🏙️ What is the distribution between **City Hotel** and **Resort Hotel** bookings?  
- ❌ How many bookings were **canceled**?  
- 🧾 Who are the **Top 5 booking agents**?  
- 🌍 What are the **Top 5 countries** making bookings?  
- 💶 What is the **total revenue (ADR)**?  
- 📅 How has the **number of bookings changed over time**?  
- 📊 What is the **status distribution**: Checked-Out vs Canceled vs No-Show?  
- ⚠️ What are the **cancellation rates per hotel type**?  
- 💰 How has **revenue changed per year**?

---

## 🧹 Data Cleaning
- Removed duplicates and unused columns (`company`, arrival date details).  
- Filled missing values in:
  - `agent` → *“No agent”*  
  - `country` → *“unknown”*  
  - `children` → *median value*  
- Converted `reservation_status_date` to `datetime` format.

---

## 📊 Visualizations
- **Pie Charts** → Hotel type distribution, booking status.  
- **Bar Charts** → Top 5 agents, Top 5 countries.  
- **Line Charts** → Bookings per year, total revenue per year.  

---

## 🔍 Insights
| # | Insight |
|---|----------|
| 1 | City hotels represent **≈61%** of total bookings. |
| 2 | **~27%** of all bookings were canceled. |
| 3 | The most active booking agent is **Agent 9.0**. |
| 4 | **Portugal (PRT)** contributes the most bookings. |
| 5 | Total average revenue (ADR) ≈ **€9,292,786**. |
| 6 | Bookings **increased in 2016** but declined again in 2017. |
| 7 | **City hotels** have a higher cancellation rate (~28.6%). |
| 8 | About **72.5%** of bookings were successful (checked out). |

---

## 🧩 Tools Used
- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**

---

## 📈 Sample Visuals
- 🥧 Resort vs City Hotel Distribution  
- 📊 Top 5 Booking Agents  
- 🌍 Top 5 Booking Countries  
- 📅 Number of Bookings per Year  
- 💰 Total Revenue per Year  
- 🧾 Booking Status Breakdown  

---

## 👨‍💻 Author
**Mohammed Waleed**  
📧 [mohammed.waleed1121@gmail.com](mailto:mohammed.waleed1121@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/mohammed-waleed-533931375/)  
📅 2025  

---

> 💡 *An end-to-end exploratory data analysis (EDA) project revealing key patterns and revenue insights in hotel bookings.*
