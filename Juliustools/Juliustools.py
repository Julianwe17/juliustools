import requests
from typing import Dict, Optional

class APIError(Exception):
    def __init__(self, message, status_code=None, response=None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)

class JuliusToolsAPI:
    def __init__(self, api_key: str, base_url: str = "http://localhost:25568"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {"X-API-Key": self.api_key}

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 403:
                error_message = "Invalid API key. Please check your API key and try again."
            else:
                error_message = f"HTTP error occurred: {http_err}"
            raise APIError(error_message, status_code=response.status_code, response=response)
        except requests.exceptions.ConnectionError as conn_err:
            error_message = f"Error connecting to the API: {conn_err}"
            raise APIError(error_message)
        except requests.exceptions.Timeout as timeout_err:
            error_message = f"Timeout error: {timeout_err}"
            raise APIError(error_message)
        except requests.exceptions.RequestException as req_err:
            error_message = f"An error occurred while making the request: {req_err}"
            raise APIError(error_message)
        except ValueError as json_err:
            error_message = f"Error decoding JSON response: {json_err}"
            raise APIError(error_message)

    def get_status(self) -> Dict:
        return self._make_request("GET", "/v1/status")

    def crypto_operation(self, text: str, operation: str, key: Optional[str] = None) -> Dict:
        data = {"text": text, "operation": operation, "key": key}
        return self._make_request("POST", "/v1/crypto", data)

    def get_random_quote(self) -> Dict:
        return self._make_request("GET", "/v1/quote")

    def get_random_joke(self) -> Dict:
        return self._make_request("GET", "/v1/joke")

    def add_content(self, content: str, content_type: str) -> Dict:
        data = {"content": content, "content_type": content_type}
        return self._make_request("POST", "/v1/add_content", data)