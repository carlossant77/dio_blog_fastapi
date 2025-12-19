import sqlalchemy as sa
import databases

DATABASE_URL = "sqlite:///./blog.db"
db_client = databases.Database(DATABASE_URL)
database = db_client
metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL, connect_args={
                          "check_same_thread": False})