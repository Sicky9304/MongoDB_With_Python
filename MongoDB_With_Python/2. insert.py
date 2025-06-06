import pymongo

if __name__ == "__main__":
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Create or switch to a database
    db = client["mydatabase"]
    
    # Create or switch to a collection
    collection = db["mycollection"]
    
    # # Insert One document into the collection
    
    # document = {"name": "Alice", "age": 30}
    # collection.insert_one(document)
    
    # document = {"name": "Bob", "age": 25}
    # collection.insert_one(document)
    
    # Insert Many document into the collection

    insertThis = {
        "_id": 1,
        "name": "Charlie",
        "age": 28,
        "city": "New York",
        "skills": ["Python", "MongoDB", "Data Analysis"],
        "isActive": True,
    },{
        "_id": 2,
        "name": "Diana",
        "age": 32,
        "city": "Los Angeles",
        "skills": ["JavaScript", "React", "Node.js"],
        "isActive": False,
    },{
        "_id": 3,
        "name": "Ethan",
        "age": 26,
        "city": "Chicago",
        "skills": ["Java", "Spring", "Hibernate"],
        "isActive": True,
    },{
        "_id": 4,
        "name": "Fiona",
        "age": 29,
        "city": "San Francisco",
        "skills": ["Ruby", "Rails", "PostgreSQL"],
        "isActive": True,
    }
    # Insert Many document into the collection
    collection.insert_many(insertThis)
    
    
    print("Document inserted successfully.")
    
    