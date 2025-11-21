# 🔹 2) Requests Module – Public API (No API Key Needed)
# Task:
# Use the Dog CEO free public API to get and display random dog images.
# Steps:
# Fetch data from 👉 https://dog.ceo/api/breeds/image/random
# Extract the image URL from the JSON response.
# Print:
# The breed name (parsed from the URL)
# The image URL
# Handle any request errors (e.g., network issues).
# Hint:
# response = requests.get("https://dog.ceo/api/breeds/image/random")
# data = response.json()
# print(data)
# Expected Output Example:
# Breed: bulldog
# Image URL: https://image
# s.dog.ceo/breeds/bulldog/n02108422_4635.jpg
import requests

breed = input("Enter Dog Breed Name:-").lower().replace(" ", "")
url = f"https://dog.ceo/api/breed/{breed}/images/random"

response = requests.get(url)
data = response.json()

if data["status"] == "success":
    print(f"Here’s a random image of a {breed.title()}:")
    print(data["message"])
else:
    print("Breed not found! Please try a valid breed name.")
