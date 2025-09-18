import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}")
    response = requests.get(url)
    print(f"Finished download from {url} with status code {response.status_code} and {len(response.content)} bytes")

urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.reddit.com"
]

start = time.time()
threads = []

for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()

print(f"All downloads completed in {end - start} seconds.")