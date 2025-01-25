import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    posts = response.json()
    for post in posts[:10]:
        print(post['title'])
else:
    print(f"Помилка запиту: {response.status_code}")
