import requests

class APIClient:

    def __init__(self, api_url, token=None):

        self.api_url = api_url
        self.session = requests.Session()

        self.session.headers.update({
            "Content-Type": "application/json"
        })
        if token:
            self.session.headers.update({
                "Authorization": f"Bearer {token}"
            })

    def get(self, endpoint):
        return self.session.get(
            self.api_url + endpoint
        )

    def post(self, endpoint, payload):
        return self.session.post(
            self.api_url + endpoint,
            json=payload
        )

    def put(self, endpoint, payload):
        return self.session.put(
            self.api_url + endpoint,
            json=payload
        )

    def delete(self, endpoint):
        return self.session.delete(
            self.api_url + endpoint
        )