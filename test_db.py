from sqlalchemy import text

from app.core.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT DATABASE()"))
        print("Connected Successfully")
        print("Database :", result.scalar())

except Exception as e:
    print("Connection Failed")
    print(e)