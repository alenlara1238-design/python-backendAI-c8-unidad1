from sqlalchemy import create_engine

DATABASE_URL ="postgresql://postgres:admin123@localhost:5433/products_db"

engine = create_engine(DATABASE_URL)