import pymongo

if __name__ == "__main__":
    # Connect to MongoDB on localhost with default port 27017
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Create/switch to database named "mydatabase"
    # If database doesn't exist, MongoDB creates it when you first store data
    db = client["mydatabase"]
    
    # Create/switch to collection named "mycollection"
    # Similar to tables in relational databases
    # Collection will be created when you first insert data
    collection = db["mycollection"]
    