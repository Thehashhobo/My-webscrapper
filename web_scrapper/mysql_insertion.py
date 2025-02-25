import json
import mysql.connector

# Load JSON data (replace with your own file path)
with open("C:\\Users\\Jerry\\PycharmProjects\\mywebscrapper\\data\\mid_out.json", "r", encoding="utf-8") as file:


    recipes = json.load(file)

# Connect to MySQL (replace with your own server details)
try:
    conn = mysql.connector.connect(
        # replace with your own server details
        host="localhost",
        user="root",
        password="C04082015l",
        database="Recipedb",
        charset="utf8mb4"
    )

    cursor = conn.cursor()
    print("✅ Connected to MySQL successfully!")
except mysql.connector.Error as err:
    print(f"❌ MySQL Connection Error: {err}")
    exit(1)  # Stop script if connection fails

# Insert each recipe
for recipe in recipes:
    cursor.execute("""
        INSERT INTO Recipes (id, name, url, time, rating, image_url, overview)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (recipe["id"], recipe["name"], recipe["url"], recipe["time"], float(recipe["rating"]), recipe["imagine_url"], recipe["overview"]))

    # Insert ingredients
    for ingredient in recipe["ingredients"]:
        cursor.execute("""
            INSERT INTO Ingredients (recipe_id, ingredient)
            VALUES (%s, %s)
        """, (recipe["id"], ingredient))

    # Insert instructions
    for step, instruction in enumerate(recipe["instructions"], start=1):
        cursor.execute("""
            INSERT INTO Instructions (recipe_id, step_order, instruction)
            VALUES (%s, %s, %s)
        """, (recipe["id"], step, instruction))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("Data imported successfully!")
