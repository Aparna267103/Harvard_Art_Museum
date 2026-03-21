# 🏛️ Harvard Artifacts Data Pipeline Project

### ETL • SQL Analytics • Streamlit Dashboard

---

## 📌 Overview

This project is a complete **end-to-end data pipeline** built using the **Harvard Art Museums API**.

It allows users to:

* 📥 Collect large-scale artifact data
* 🔄 Clean and transform raw JSON data
* 🗄️ Store structured data in a database
* 🧠 Run SQL queries for analysis
* 📊 Explore insights through a Streamlit dashboard

---

## 🚀 Key Features

* 📦 Collect **2500+ artifacts per classification**
* 🔄 ETL pipeline (Extract → Transform → Load)
* 🧹 Clean and structured datasets
* 🗄️ MySQL database integration
* 🧠 20+ SQL queries for analysis
* 💻 Interactive Streamlit UI

---

## 🏗️ Architecture

API → Data Extraction → Data Cleaning → Database → Streamlit UI → SQL Analysis

---

## 🧰 Tech Stack

* 🐍 Python
* 🌐 Requests
* 🐼 Pandas
* 🗄️ MySQL
* 🔗 SQLAlchemy
* 🎛️ Streamlit

---

## 🗄️ Database Tables

### 📄 artifact_metadata

Stores main artifact details:

* id (Primary Key)
* title, culture, period
* century, medium
* department, classification

### 🖼️ artifact_media

Stores media-related details:

* objectid (FK)
* imagecount, mediacount
* datebegin, dateend

### 🎨 artifact_colors

Stores color information:

* objectid (FK)
* color, spectrum
* hue, percent

---

## 📁 Project Structure

```
Harvard_Art_Project/
│
├── app.py            # Streamlit application
├── extract.py        # API data collection
├── transform.py      # Data cleaning
├── load.py           # Database insertion
├── db_connection.py  # DB connection
├── sql_queries.py    # SQL queries
├── config.py         # API key
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```

---

## ⚙️ Setup Instructions

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🧭 Application Workflow

1. 🔽 Select classification
2. 📥 Collect artifact data
3. 📋 Preview dataset
4. 🗄️ Store in database
5. 🧠 Run SQL queries
6. 📊 View results

---

## 🧠 SQL Analysis

Includes queries like:

* 📊 Artifacts by classification
* 🌍 Culture-based analysis
* 🕰️ Century-based filtering
* 🎨 Color distribution

---

## 📸 Screenshots

*Add your Streamlit screenshots here*

---

## ❗ Challenges

* Handling API pagination
* Managing large datasets
* Cleaning nested JSON
* SQL debugging

---

## 👩‍💻 Author

**Aparna V**

---

## ⭐ Summary

This project showcases:

* 🔄 Data pipeline development
* 🧠 SQL analytics skills
* 📊 Dashboard building

🚀 Ideal for **Data Analyst / Data Engineer portfolio**
