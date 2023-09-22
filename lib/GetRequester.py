import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        try:
            # Decode the bytes to a string and then parse it as JSON
            data = json.loads(response_body.decode('utf-8'))
            return data
        except json.JSONDecodeError:
            # Handle the case where the response is not valid JSON
            return None