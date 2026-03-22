import requests

url = "https://api.github.com/repos/python/cpython"

try:
    
    r = requests.get(url, timeout=10)

    r.raise_for_status()

    data = r.json()

    print("Stars:", data["stargazers_count"])

except requests.exceptions.RequestException as e:
    print("Something went wrong:", e)
