from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    URL_DATABASE = DATABASE_URL = f"postgresql+asyncpg://{str(os.getenv("PG_USER"))}:{str(os.getenv("PG_PASSWORD"))}@{str(os.getenv("PG_HOST"))}:{str(os.getenv("PG_PORT"))}/{str(os.getenv("PG_DB_NAME"))}"
