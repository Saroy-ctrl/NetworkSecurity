import os
import pymongo
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_connection():
    try:
        # 1. Get URL from .env
        mongo_url = os.getenv("MONGO_DB_URL")
        if not mongo_url:
            print("❌ Error: MONGO_DB_URL not found in .env file")
            return

        print(f"Connecting to: {mongo_url[:20]}...")

        # 2. Initialize Client
        # Note: If using Atlas, you might need tlsCAFile=certifi.where()
        client = pymongo.MongoClient(mongo_url)
        
        # 3. Test Server Connection (Ping)
        client.admin.command('ping')
        print("✅ Success: Connection to MongoDB established!")

        # 4. List Databases to verify visibility
        db_names = client.list_database_names()
        print(f"Available Databases: {db_names}")

        # 5. Check specific Database and Collection
        # Change these to match your actual names from your constants
        db_name = "SAANANN_NETWORK_SECURITY" 
        coll_name = "Network_Data"

        if db_name in db_names:
            db = client[db_name]
            collections = db.list_collection_names()
            print(f"✅ Database found. Collections: {collections}")
            
            if coll_name in collections:
                count = db[coll_name].count_documents({})
                print(f"✅ Collection found. Total documents: {count}")
                
                # Preview data
                if count > 0:
                    data = list(db[coll_name].find().limit(5))
                    df = pd.DataFrame(data)
                    print("\n--- Data Preview (First 5 rows) ---")
                    print(df.head())
                else:
                    print("⚠️ Warning: Collection exists but is EMPTY.")
            else:
                print(f"❌ Error: Collection '{coll_name}' not found.")
        else:
            print(f"❌ Error: Database '{db_name}' not found.")

    except Exception as e:
        print(f"❌ Connection Failed: {e}")

if __name__ == "__main__":
    test_connection()