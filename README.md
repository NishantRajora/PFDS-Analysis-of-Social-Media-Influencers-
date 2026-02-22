# Influencer Analytics Tool (Python CLI Application)

## Overview

The Influencer Analytics Tool is a command-line application built in Python that enables structured analysis of influencer performance data from 2020 to 2024.

The tool supports data entry, CSV-based persistence, statistical summary generation, and visualization of engagement metrics such as likes, comments, shares, and follower counts.

This project demonstrates practical implementation of:

- Data manipulation using pandas  
- CSV file handling  
- CLI-based interactive systems  
- Visualization using matplotlib  
- Basic analytical reporting  

---

## Project Objectives

- Manage influencer performance data using CSV storage  
- Compute engagement summaries across multiple years  
- Visualize influencer growth and interaction patterns  
- Provide a simple analytical workflow in a CLI environment  

---

## Core Features

### 1. Data Management

- Load influencer data from `influencers.csv`  
- Add new influencer records via interactive input  
- Persist data changes back to CSV  
- Automatically create file if not present  

---

### 2. Analytical Capabilities

- Calculate average likes (2020–2024)  
- Calculate average shares (2020–2024)  
- Calculate average comments (2020–2024)  
- Display tabular summary grouped by influencer  

This enables quick comparative performance evaluation.

---

### 3. Visualizations

- Multi-line graph of likes, comments, and shares over time for a selected influencer  
- Bar chart comparing follower counts across influencers  

The visualization module allows quick identification of engagement trends and growth patterns.

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python 3.x |
| Data Handling | pandas |
| Visualization | matplotlib |
| Numerical Operations | numpy |
| File Storage | CSV |
| Interface | Command Line Interface |

---

## Repository Structure

```
InfluencerAnalytics/
│
├── influencers.csv
└── influencer_analysis.py
```

- `influencers.csv` – Persistent storage file  
- `influencer_analysis.py` – Main application script  

---

## Sample Data Structure

```
influencer_name,platform,follower_count,content_type,post_frequency,
likes_2020,...,likes_2024,
shares_2020,...,shares_2024,
comments_2020,...,comments_2024
```

Each influencer record contains yearly engagement metrics for five years.

---

## Installation and Execution

### Install Dependencies

```
pip install pandas matplotlib numpy
```

### Run the Application

```
python influencer_analysis.py
```

---

## Application Menu

```
1. Show Data
2. Show Summary
3. Add Data
4. Save Data
5. Plot Likes, Comments, and Shares
6. Show Follower Counts
7. Exit
```

---

## Analytical Approach

1. Load dataset into pandas DataFrame  
2. Perform aggregation across yearly columns  
3. Compute averages for engagement metrics  
4. Generate visualizations using matplotlib  
5. Save updated dataset to CSV  

The system ensures persistent storage and repeatable analysis.

---

## Key Insights Enabled by the Tool

- Engagement growth trends across multiple years  
- Comparative influencer performance  
- Relationship between follower count and engagement  
- Identification of high-growth influencers  

---

## Limitations

- Case-sensitive influencer name matching  
- No input validation for negative values  
- No database integration  
- Manual save operation required  
- Basic static visualizations  

This project is intended for academic and learning purposes.

---

## Future Enhancements

- Add data validation and input constraints  
- Implement case-insensitive search  
- Integrate Plotly or Seaborn for advanced visualization  
- Develop web interface using Flask or Django  
- Add predictive analytics for engagement forecasting  
- Integrate SQLite or MySQL database backend  
- Add export to Excel or PDF reporting  

---

## Learning Outcomes

- Practical CSV data management  
- Implementation of CLI-based analytical systems  
- Multi-year data aggregation techniques  
- Visualization of structured datasets  
- Understanding of performance metrics analysis  

---

## Ideal For

- Python programming coursework  
- Data analysis practice projects  
- Beginners learning pandas and matplotlib  
- Academic mini projects  

---

## Author

Nishant Rajora  
