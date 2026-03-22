import pandas as pd
import numpy as np

# ------------------ SAFE FUNCTIONS ------------------

def safe_int(value):
    return int(value) if pd.notna(value) else 0

def safe_float(value):
    return float(value) if pd.notna(value) else 0.0

# ------------------ MEDIA  ------------------

def transform_media(obj):
    return {
        "objectid": obj.get("objectid"),
        "imagecount": int(obj.get("imagecount") or 0),
        "mediacount": int(obj.get("mediacount") or 0),
        "colorcount": int(obj.get("colorcount") or 0),
        "rank": int(obj.get("rank") or 0),
        "datebegin": int(obj.get("datebegin") or 0),
        "dateend": int(obj.get("dateend") or 0)
    }

# ------------------ COLORS  ------------------

def transform_colors(obj, c):
    return {
        "objectid": obj.get("objectid"),
        "color": c.get("color") or "#000000",
        "spectrum": c.get("spectrum") or "#000000",
        "hue": c.get("hue") or "Unknown",
        "percent": float(c.get("percent") or 0.0),
        "css3": c.get("css3") or "#000000"
    }

# ------------------ MAIN TRANSFORM ------------------

def transform_objects(objects):
    metadata_rows = []
    media_rows = [] 
    color_rows = []

    for obj in objects:
        # Metadata
        metadata_rows.append({
            "id": safe_int(obj.get("objectid")),
            "title": (obj.get("title") or "").strip(),
            "culture": obj.get("culture") or "Unknown",
            "period": obj.get("period") or "Unknown",
            "century": obj.get("century") or "Unknown",
            "medium": obj.get("medium") or "Unknown",
            "dimensions": obj.get("dimensions") or "Unknown",
            "description": obj.get("description") or "",
            "department": obj.get("department") or "Unknown",
            "classification": obj.get("classification") or "Unknown",
            "accessionyear": safe_int(obj.get("accessionyear")),
            "accessionmethod": obj.get("accessionmethod") or "Unknown"
        })

        # Media
        media_rows.append(transform_media(obj))

        # Colors
        colors = obj.get("colors")
        if isinstance(colors, list):
            for c in colors:
                color_rows.append(transform_colors(obj, c))

    df_metadata = pd.DataFrame(metadata_rows).drop_duplicates(subset=["id"])
    df_media = pd.DataFrame(media_rows).drop_duplicates(subset=["objectid"])
    df_colors = pd.DataFrame(color_rows).drop_duplicates()

    # ✅ Replace NaN with None for SQLAlchemy compatibility
    df_metadata = df_metadata.replace({np.nan: None})
    df_media = df_media.replace({np.nan: None})
    df_colors = df_colors.replace({np.nan: None})


    return df_metadata, df_media, df_colors