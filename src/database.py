import sqlalchemy as sa
import databases

from src.config import settings

db_client = databases.Database(settings.DATABASE_URL)
metadata = sa.MetaData()
database = db_client

if settings.environment == "production":
    engine = sa.create_engine(settings.DATABASE_URL)
else:
    engine = sa.create_engine(settings.DATABASE_URL, 
                              connect_args={"check_same_thread": False})