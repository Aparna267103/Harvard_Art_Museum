from sqlalchemy import create_engine
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_connection():
    engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )
    return engine
