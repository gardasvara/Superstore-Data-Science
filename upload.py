import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

DATABASE_URL = (
    f"postgresql+psycopg2://{USER}:{PASSWORD}"
    f"@{HOST}:{PORT}/{DBNAME}?sslmode=require"
)

engine = create_engine(DATABASE_URL)

df = pd.read_csv("data/Superstore.csv")

df.to_sql(
    "superstore",
    engine,
    if_exists="replace",
    index=False
)

print("Upload selesai!")