# 📊 Influencer Analytics Tool (Python CLI App)

A **command-line tool** built in **Python** that allows users to analyze influencer data including likes, comments, shares, and follower counts from **2020 to 2024**. The application supports **data entry, CSV persistence, summary generation, and visualization using matplotlib**.

---

## 🧰 Features

### 📂 Data Management
- Load influencer data from a CSV file (`influencers.csv`)
- Add new influencer records through interactive CLI input
- Save updated data to CSV for future use

### 📊 Analytics & Summaries
- Compute average likes, shares, and comments from 2020–2024
- Generate tabular summaries by influencer

### 📈 Visualizations
- Plot **likes, comments, and shares** over years for a selected influencer
- Bar chart of **follower counts** for all influencers

---

## 🧑‍💻 Technologies Used

| Feature           | Library           |
|-------------------|-------------------|
| Data Handling     | `pandas`          |
| Visualization     | `matplotlib`      |
| Numerical Ops     | `numpy` (optional but imported) |
| File Format       | `.csv`            |
| Input/Output      | CLI + CSV         |

---

## 📁 Project Structure

```
📦 InfluencerAnalytics/
├── influencers.csv         # CSV data file (auto-created if missing)
└── influencer_analysis.py  # Main Python script
```

---

## 📝 Sample `influencers.csv` Format

```csv
influencer_name,platform,follower_count,content_type,post_frequency,likes_2020,likes_2021,likes_2022,likes_2023,likes_2024,shares_2020,shares_2021,shares_2022,shares_2023,shares_2024,comments_2020,comments_2021,comments_2022,comments_2023,comments_2024
nishant123,Instagram,150000,Fashion,30,1200,1500,1700,1800,2000,300,350,400,420,450,250,300,310,320,350
```

---

## ▶️ How to Run

### 🔧 Prerequisites

Install dependencies using pip:

```bash
pip install pandas matplotlib numpy
```

### 🚀 Execute

Run the script:

```bash
python influencer_analysis.py
```

---

## 🧑‍💻 User Menu Options

```
1. Show Data                         -> View full data from CSV
2. Show Summary                     -> View average likes, shares, comments
3. Add Data                         -> Add a new influencer interactively
4. Save Data                        -> Save changes to influencers.csv
5. Plot Likes, Comments, and Shares -> Line graph for a chosen influencer
6. Show Follower Counts             -> Bar chart for all influencers
7. Exit                             -> Close the program
```

---

## 📊 Example Visualizations

### Likes, Comments, Shares (2020–2024)
![line chart example](https://via.placeholder.com/500x250?text=Line+Chart+Example)

### Follower Count Bar Graph
![bar chart example](https://via.placeholder.com/500x250?text=Bar+Chart+Example)

*(Replace these images with real screenshots from your project when uploading to GitHub)*

---

## ⚠️ Notes

- The file `influencers.csv` is auto-created if not found.
- Data is saved manually via the **Save Data** option.
- Case-sensitive matching is used when entering influencer names.

---

## 🌱 Future Enhancements

- ✅ Add data validation (e.g., restrict negative numbers)
- 📊 Use interactive charts via `plotly` or `seaborn`
- 🌐 Web interface using Flask or Django
- 🔐 Password protection for editing or adding records

---

## 🧑‍🏫 Built for

> 📚 **Python Programming** | Semester Project  
> 🎓 Ideal for students learning **data visualization**, **file handling**, and **data analysis** in Python.
