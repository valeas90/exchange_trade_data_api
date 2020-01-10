"""Model and database related things package."""
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import DESCENDING
from pymongo import ASCENDING


async def setup_databases(app):
    """Set databases up."""
    app['mongo'] = AsyncIOMotorClient(app['config'].get('mongo', 'uri'))
    app['mongo_db'] = app['mongo'].get_database()
