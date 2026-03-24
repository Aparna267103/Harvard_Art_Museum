import requests
import streamlit as st
import pandas as pd
from config import API_KEY,  CLASSIFICATION_URL, OBJECT_URL
from db_connection import get_connection
from sql_queries import queries
from transform import transform_objects
from load import create_tables,insert_metadata, insert_media, insert_colors

st.title("Harvard Art Museum Collection")

# 🔹 Step 1: Create Tables
if st.button("Create Tables"):
    create_tables()
    st.success("✅ Tables created!")

# -----------------------------
# Step 1 : Get classifications with objectcount >= 2500
# -----------------------------
@st.cache_data
def get_big_classifications(min_objects=2500):
    classifications = []
    page = 1
    while True:
        params = {
            "apikey": API_KEY, 
            "size": 100, 
            "page": page
            }
        
        response = requests.get(CLASSIFICATION_URL, params=params)
        data = response.json()

        if not data.get("records"):
            break
        # Filter only objectcount >= min_objects
        for cls in data["records"]:
            if cls.get("objectcount", 0) >= 2500:
                classifications.append(cls["name"])
        # Check if more pages exist
        if not data.get("info", {}).get("next"):
            break

        page += 1
    return classifications

big_classifications = get_big_classifications()

# -----------------------------
# Step 2: Streamlit selectbox for 5 classifications
# -----------------------------
selected_classes = st.multiselect(
    "Select up to 5 classifications (objectcount >= 2500):",
    options=big_classifications,
    max_selections=5
)

# -----------------------------
# Step 3: Collect up to 2500 objects per selected classification
# -----------------------------
def collect_artifacts(class_name, limit=2500):
    records = []
    page = 1
    while len(records) < limit:
        params = {
            "apikey": API_KEY, 
            "classification": class_name, 
            "size": 100, 
            "page": page
            }
        response = requests.get(OBJECT_URL, params=params)
        data = response.json()
        if "records" not in data or not data["records"]:
            break
        records.extend(data["records"])
        page += 1
    return records[:limit]

if st.button("Collect Data"):
    all_data = {}
    for cls in selected_classes:
        st.write(f"Collecting objects for: {cls}")
        objects = collect_artifacts(cls, limit=2500)
        all_data[cls] = objects
        st.write(f"{len(objects)} records collected for {cls}")

    # 🔹 Store collected data in session_state
    st.session_state.data = all_data

    total_records = sum(len(v) for v in all_data.values())
    st.success(f"Total {total_records} records collected from {len(selected_classes)} classifications")
    st.success("Data collected successfully!")

# -------------------------------------------------
#           Show data
# -------------------------------------------------  

if st.button("Show data"):
    if not st.session_state.data:
        st.warning("Please collect data first")

    else:
        for cls, df in st.session_state.data.items():

            st.subheader(f"{cls} Records")

            st.dataframe(df)
# -------------------------------------------------
# Insert Data to MySQL
# -------------------------------------------------


if st.button("Insert Data to MySQL"):

    if not st.session_state.data:
        st.warning("No data to insert. Please collect data first.")
    else:
        try:
            all_objects = []

            for cls, records_list in st.session_state.data.items():
                # records_list is already a list of dicts
                all_objects.extend(records_list)

            df_metadata, df_media, df_colors = transform_objects(all_objects)

            insert_metadata(df_metadata)
            insert_media(df_media)
            insert_colors(df_colors)

            st.success("✅ Data inserted successfully!")

        except Exception as e:
            st.error(f"Error inserting data: {e}")

# -------------------------------------------------
# SQL Queries Section
# -------------------------------------------------

st.subheader("Run SQL Queries")

selected_query = st.selectbox(
    "Choose a Query",
    list(queries.keys())
)

engine = get_connection()

if st.button("Run Query"):
    selected_query = queries[selected_query]   
    df = pd.read_sql(selected_query, engine)
    st.dataframe(df)
