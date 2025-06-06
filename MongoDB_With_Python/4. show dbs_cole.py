import pymongo

if __name__ == "__main__":
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Show all databases
    databases = client.list_database_names()
    print("Databases:")
    for db_name in databases:
        print(f"- {db_name}")
        
    # Show all collections in each database
    for db_name in databases:
        db = client[db_name]
        collections = db.list_collection_names()
        print(f"Collections in {db_name}:")
        for collection_name in collections:
            print(f"  - {collection_name}")
        
    
    
    