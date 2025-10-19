"""Seed the MongoDB with example activities for local development.

Run:

    python -m src.seed_db

It reads MONGO_URL and DB_NAME from the environment (same as the app).
"""
import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DB_NAME", "mergington")

SAMPLE_ACTIVITIES = [
    {
        "name": "Chess Club",
        "description": "Weekly chess club for beginners and advanced players.",
        "schedule": "Wednesdays 15:30",
        "max_participants": 20,
        "participants": ["alice@example.com"],
    },
    {
        "name": "Programming Class",
        "description": "Hands-on Python programming class.",
        "schedule": "Mondays 16:00",
        "max_participants": 25,
        "participants": [],
    },
    {
        "name": "Gym Class",
        "description": "Competitive and recreational sports activities.",
        "schedule": "Fridays 14:00",
        "max_participants": 30,
        "participants": [],
    },
]


async def seed():
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    activities = db["activities"]
    # Ensure index
    await activities.create_index("name", unique=True)
    # Upsert sample activities
    for a in SAMPLE_ACTIVITIES:
        await activities.update_one({"name": a["name"]}, {"$set": a}, upsert=True)
    print(f"Seeded {len(SAMPLE_ACTIVITIES)} activities into {DB_NAME} @ {MONGO_URL}")
    client.close()


if __name__ == "__main__":
    asyncio.run(seed())
"""
Seed MongoDB with initial activities used by the app if they don't exist.

Usage: run this once after MongoDB is available.
Environment variables respected:
- MONGO_URL (default: mongodb://localhost:27017)
- DB_NAME (default: mergington)
"""

import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.environ.get("DB_NAME", "mergington")

INITIAL_ACTIVITIES = [
    {
        "name": "Chess Club",
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
    },
    {
        "name": "Programming Class",
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
    },
    {
        "name": "Gym Class",
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"],
    },
    {
        "name": "Soccer Team",
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"],
    },
    {
        "name": "Basketball Team",
        "description": "Practice and play basketball with the school team",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"],
    },
    {
        "name": "Art Club",
        "description": "Explore your creativity through painting and drawing",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"],
    },
    {
        "name": "Drama Club",
        "description": "Act, direct, and produce plays and performances",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "scarlett@mergington.edu"],
    },
    {
        "name": "Math Club",
        "description": "Solve challenging problems and participate in math competitions",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"],
    },
    {
        "name": "Debate Team",
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu", "henry@mergington.edu"],
    },
]


async def main():
    client = AsyncIOMotorClient(MONGO_URL)
    try:
        db = client[DB_NAME]
        col = db["activities"]
        await col.create_index("name", unique=True)
        for act in INITIAL_ACTIVITIES:
            existing = await col.find_one({"name": act["name"]})
            if not existing:
                await col.insert_one(act)
                print(f"Inserted: {act['name']}")
            else:
                print(f"Skipped (exists): {act['name']}")
    finally:
        client.close()


if __name__ == "__main__":
    asyncio.run(main())
