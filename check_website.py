import requests

URL = "https://littlegoodwill.org"

def check_website():
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            return f"{URL} is UP (status 200)"
        else:
            return f"{URL} returned status {response.status_code}"
    except Exception as e:
        return f"{URL} check failed: {e}"

if __name__ == "__main__":
    status = check_website()
    print(status)
