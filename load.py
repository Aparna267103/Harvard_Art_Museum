from db_connection import get_connection
from sqlalchemy import text

engine = get_connection()

artifact_metadata = """
CREATE TABLE IF NOT EXISTS artifact_metadata (
    id INT NOT NULL,
    title TEXT,
    culture TEXT,
    period TEXT,
    century TEXT,
    medium TEXT,
    dimensions TEXT,
    description TEXT,
    department TEXT,
    classification TEXT,
    accessionyear INT,
    accessionmethod TEXT,
    PRIMARY KEY (id)
)
"""

artifact_media = """
CREATE TABLE IF NOT EXISTS artifact_media (
    objectid INT NOT NULL,
    imagecount INT,
    mediacount INT,
    colorcount INT,
    artifact_rank INT,
    datebegin INT,
    dateend INT,
    FOREIGN KEY (objectid) REFERENCES artifact_metadata(id)
)
"""

artifact_colors = """
CREATE TABLE IF NOT EXISTS artifact_colors (
    objectid INT NOT NULL,
    color VARCHAR(20),
    spectrum VARCHAR(20),
    hue VARCHAR(50),
    percent FLOAT,
    css3 VARCHAR(20),
    FOREIGN KEY (objectid) REFERENCES artifact_metadata(id)
)
"""
# ------------------ CREATE TABLE FUNCTION ------------------

def create_tables():
    engine = get_connection()

    with engine.connect() as conn:
        # Create tables
        conn.execute(text(artifact_metadata))
        conn.execute(text(artifact_media))
        conn.execute(text(artifact_colors))
    print("✅ Tables created successfully!")

# ------------------ INSERT FUNCTIONS ------------------

def insert_metadata(df):
    engine = get_connection()

    with engine.connect() as conn:
        for _, row in df.iterrows():
            query = text("""
                INSERT IGNORE INTO artifact_metadata VALUES (
                    :id, :title, :culture, :period, :century,
                    :medium, :dimensions, :description,
                    :department, :classification,
                    :accessionyear, :accessionmethod
                )
            """)

            conn.execute(query, {
                "id": row["id"],
                "title": row["title"],
                "culture": row["culture"],
                "period": row["period"],
                "century": row["century"],
                "medium": row["medium"],
                "dimensions": row["dimensions"],
                "description": row["description"],
                "department": row["department"],
                "classification": row["classification"],
                "accessionyear": row["accessionyear"],
                "accessionmethod": row["accessionmethod"]
            })

        conn.commit()

    print("✅ Metadata inserted")


def insert_media(df):
    engine = get_connection()

    with engine.connect() as conn:
        for _, row in df.iterrows():
            query = text("""
                INSERT IGNORE INTO artifact_media VALUES (
                    :objectid, :imagecount, :mediacount,
                    :colorcount, :artifact_rank,
                    :datebegin, :dateend
                )
            """)

            conn.execute(query, {
                "objectid": row["objectid"],
                "imagecount": row["imagecount"],
                "mediacount": row["mediacount"],
                "colorcount": row["colorcount"],
                "artifact_rank": row["rank"],
                "datebegin": row["datebegin"],
                "dateend": row["dateend"]
            })

        conn.commit()

    print("✅ Media inserted")


def insert_colors(df):
    engine = get_connection()

    with engine.connect() as conn:
        for _, row in df.iterrows():
            query = text("""
                INSERT IGNORE INTO artifact_colors VALUES (
                    :objectid, :color, :spectrum,
                    :hue, :percent, :css3
                )
            """)

            conn.execute(query, {
                "objectid": row["objectid"],
                "color": row["color"],
                "spectrum": row["spectrum"],
                "hue": row["hue"],
                "percent": row["percent"],
                "css3": row["css3"]
            })

        conn.commit()

    print("✅ Colors inserted")