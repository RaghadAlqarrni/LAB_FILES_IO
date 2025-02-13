import os
import json
from datetime import datetime

def todo_program():
    while True:
        user_input = input("Do you want to add a new To-Do item? y or n: ").strip().lower()
        
        if user_input == "y":
            title = input("Please type in your new To-Do item: ")
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            todo_item = {
                "title": title,
                "date_time": now,
                "done": False
            }
            with open("to_do.json", "r", encoding="utf-8") as file:
                items = json.load(file)
  
            items.append(todo_item)
       
            with open("to_do.json", "w", encoding="utf-8") as file:
                json.dump(items, file, indent=4)
        
        elif user_input == "n":
            list_input = input("Do you want to list your To-Do items? y or n: ").strip().lower()
            if list_input == "y":
                if os.path.exists("to_do.json"):
                    with open("to_do.json", "r", encoding="utf-8") as file:
                        items = json.load(file)
                    if items:  # Check if there are any items
                        print("Your To-Do items:")
                        for done, item in enumerate(items, start=1):
                            status = "✔️" if item['done'] else "❌"
                            print(f"{done}. {item['title']} (Added on: {item['date_time']}, Status: {status})")

        elif user_input == "exit":
            print("Thank you for using the To-Do program, come back again soon!")
            break
todo_program()