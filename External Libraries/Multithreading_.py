# 🔹 4) Multithreading in Python
# Task:
# Write a Python program that:

# Downloads 3 images from URLs (use any free image URLs)

# Uses multithreading to download all images simultaneously

# Prints "Downloaded: image_name" as each download completes

# Hint:

# Use threading.Thread(target=download_function, args=(url,))

# Use requests.get(url) to fetch image

# Use open(filename, 'wb') to save image
import threading, requests

# 3 supercar image URLs
urls = [
   "https://upload.wikimedia.org/wikipedia/commons/f/fd/Lamborghini_Aventador_LP700-4.png",
    "https://upload.wikimedia.org/wikipedia/commons/1/14/Ferrari_488_GT3.png",
    "https://upload.wikimedia.org/wikipedia/commons/4/44/McLaren_P1.png"
]

def download(url):
    name = url.split("/")[-1].split("?")[0] 
    r = requests.get(url)
    with open(name, "wb") as f:
        f.write(r.content)
    print("Downloaded:", name)

# Start threads
threads = []
for u in urls:
    t = threading.Thread(target=download, args=(u,))
    t.start()
    threads.append(t)

for t in threads:
    t.join
