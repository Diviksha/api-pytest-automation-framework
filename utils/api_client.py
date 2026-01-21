import requests


class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get_users():
        return requests.get(f"{APIClient.BASE_URL}/users")

    @staticmethod
    def create_post(title, body, user_id=1):
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        return requests.post(f"{APIClient.BASE_URL}/posts", json=payload)
