import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:gardasvarascience@db.pcagjhiefuxoqnydjrzb.supabase.co:5432/postgres"

engine = create_engine(DATABASE_URL)

df = pd.read_csv("data/Superstore.csv")

df.to_sql(
    "superstore",
    engine,
    if_exists="replace",
    index=False
)

print("Upload selesai!")