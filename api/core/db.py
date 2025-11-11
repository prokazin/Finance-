import os
from sqlalchemy import create_engine, Table, Column, Integer, String, Float, Date, MetaData
import datetime

DATABASE_URL = os.environ.get("DATABASE_URL","sqlite:///local.db")
engine = create_engine(DATABASE_URL, echo=False, future=True)
metadata = MetaData()

users = Table("users", metadata, Column("id", Integer, primary_key=True), Column("chat_id", String, unique=True))
incomes = Table("incomes", metadata, Column("id", Integer, primary_key=True), Column("chat_id", String), Column("amount", Float), Column("category", String), Column("date", Date, default=datetime.date.today))
expenses = Table("expenses", metadata, Column("id", Integer, primary_key=True), Column("chat_id", String), Column("amount", Float), Column("category", String), Column("date", Date, default=datetime.date.today))

def init_db():
    metadata.create_all(engine)
