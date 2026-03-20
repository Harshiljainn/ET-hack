import os
import logging
import certifi
from dotenv import load_dotenv
from pymongo import ASCENDING, DESCENDING, MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# MongoDB connection string and DB name
MONGODB_URL = os.getenv(
    "MONGODB_URL",
    "mongodb+srv://harshiljain135_db_user:Hello%4012345@cluster0.le9zdwf.mongodb.net/?appName=Cluster0",
)
DATABASE_NAME = os.getenv("DATABASE_NAME", "et-hack")

# -------------------------------
# Mongo Client with TLS support
# -------------------------------
_client: MongoClient | None = None
_database: Database | None = None
_indexes_initialized = False


def _build_client() -> MongoClient:
    if "mongodb+srv://" in MONGODB_URL:
        return MongoClient(
            MONGODB_URL,
            tls=True,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=8000,
            connectTimeoutMS=8000,
        )
    return MongoClient(
        MONGODB_URL,
        serverSelectionTimeoutMS=8000,
        connectTimeoutMS=8000,
    )


def _get_database() -> Database:
    global _client, _database
    if _database is None:
        try:
            _client = _build_client()
            _client.admin.command("ping")
            _database = _client[DATABASE_NAME]
            logger.info("MongoDB connected")
        except (ServerSelectionTimeoutError, OperationFailure) as exc:
            logger.error("MongoDB connection failed: %s", exc)
            raise
    return _database


class LazyCollection:
    def __init__(self, name: str) -> None:
        self._name = name

    def _collection(self) -> Collection:
        database = _get_database()
        return database.get_collection(self._name)

    def __getattr__(self, item):
        return getattr(self._collection(), item)


def get_collection(name: str) -> Collection:
    """Return a typed collection handle."""
    return LazyCollection(name)


# Collections
users_collection: Collection = get_collection("users")
articles_collection: Collection = get_collection("articles")
report_analysis_collection: Collection = get_collection("report_analysis")
financial_analysis_collection: Collection = get_collection("financial_analysis")
market_filings_collection: Collection = get_collection("market_filings")
watchlists_collection: Collection = get_collection("watchlists")
favorite_articles_collection: Collection = get_collection("favorite_articles")
admin_logs_collection: Collection = get_collection("admin_logs")
user_settings_collection: Collection = get_collection("user_settings")
application_settings_collection: Collection = get_collection("application_settings")

def init_indexes() -> None:
    global _indexes_initialized
    if _indexes_initialized:
        return
    try:
        users_collection.create_index([("email", ASCENDING)], unique=True)
        users_collection.create_index([("username", ASCENDING)], unique=True)
        users_collection.create_index([("reset_token", ASCENDING)], unique=True, sparse=True)

        articles_collection.create_index([("link", ASCENDING)], unique=True)
        articles_collection.create_index([("created_at", ASCENDING)])

        report_analysis_collection.create_index([("created_at", ASCENDING)])

        financial_analysis_collection.create_index([("created_at", ASCENDING)])
        financial_analysis_collection.create_index([("file_id", ASCENDING)], unique=True)

        market_filings_collection.create_index(
            [("source", ASCENDING), ("link", ASCENDING)], unique=True
        )
        market_filings_collection.create_index([("created_at", ASCENDING)])

        watchlists_collection.create_index([("user_id", ASCENDING)], unique=True)

        favorite_articles_collection.create_index(
            [("user_id", ASCENDING), ("article_id", ASCENDING)], unique=True
        )
        favorite_articles_collection.create_index([("created_at", ASCENDING)])

        admin_logs_collection.create_index([("created_at", DESCENDING)])
        admin_logs_collection.create_index([("level", ASCENDING), ("created_at", DESCENDING)])

        user_settings_collection.create_index([("user_id", ASCENDING)], unique=True)
        user_settings_collection.create_index([("updated_at", DESCENDING)])

        _indexes_initialized = True
    except Exception as exc:
        logger.error("Index creation failed: %s", exc)
