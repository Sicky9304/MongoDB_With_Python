import pymongo
# YouTube Video Manager using MongoDB
# This script allows users to manage YouTube videos by inserting, viewing, searching, updating, and deleting video records in a MongoDB database.
def insert_video():
    video_id = int(input("Enter the video ID: "))
    title = input("Enter the Video title: ")
    description = input("Enter the video description: ")
    category = input("Enter video category: ")
    upload_date = input("Enter upload date(YYYY-MM-DD): ")
    
    video = {
        "_id": video_id,
        "title":title,
        "description":description,
        "category":category,
        "upload_date":upload_date
    }
    try:
        result = collection.insert_one(video)
        print(f"Video inserted with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error inserting video: {e}")
        return

def view_video():
    videos = collection.find()
    for video in videos:
        try:
            print(f"Title: {video.get('title')}")
            print(f"Description: {video.get('description')}")
            print(f"Category: {video.get('category')}")
            print(f"Upload Date: {video.get('upload_date')}")
            print("-" * 40)
        except Exception as e:
            print(f"Error displaying video: {e}")

def search_video():
    search_term = input("Enter the search term: ")
    videos = collection.find({"title": {"$regex": search_term, "$options": "i"}},{"_id":0,"title": 1, "description": 1, "category": 1, "upload_date": 1})
    
    videos_list = list(videos)
    if len(videos_list) == 0:
        print("No videos found.")
        return
    print(f"Found {len(videos_list)} video(s) matching '{search_term}':")
       
    for video in videos_list:
        try:
            print("-" * 40)
            print(f"Title: {video.get('title')}")
            print(f"Description: {video.get('description')}")
            print(f"Category: {video.get('category')}")
            print(f"Upload Date: {video.get('upload_date')}")
            print("-" * 40)
        except Exception as e:
            print(f"Error displaying video: {e}")


def update_video():
    video_id = input("Enter the video ID to update: ")
    new_title = input("Enter the new title: ")
    new_description = input("Enter the new description: ")
    new_category = input("Enter the new category: ")
    new_upload_date = input("Enter the new upload date (YYYY-MM-DD): ")
    
    updated_video = {
        "title": new_title,
        "description": new_description,
        "category": new_category,
        "upload_date": new_upload_date
    }
    
    result = collection.update_one({"_id": int(video_id)}, {"$set": updated_video})
    
    if result.modified_count > 0:
        print("Video updated successfully.")
    else:
        print("No video found with the specified ID or no changes made.")


def delete_video():
    video_id = input("Enter the video ID to delete: ")
    
    result = collection.delete_one({"_id": int(video_id)})
    
    if result.deleted_count > 0:
        print("Video deleted successfully.")
    else:
        print("No video found with the specified ID.")


def exit():
    print("Exiting Program..")
    import sys
    sys.exit(0)

if __name__ == "__main__":
    
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    
    db = client["YouTube"]
    
    collection = db["youtube_manager"]
    
    print("\nWelcome to YouTube Video Manager")
    while True:
        print("1. Insert Video")
        print("2. View Videos")
        print("3. Search Video")
        print("4. Update Video")
        print("5. Delete Video")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            match (choice):
                case (1):
                    insert_video()
                case (2):
                    view_video()
                case (3):
                    search_video()
                case (4):
                    update_video()
                case (5):
                    delete_video()
                case (6):
                    exit()
                case (_):
                    print("Invalid Choice!...")
                    continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")