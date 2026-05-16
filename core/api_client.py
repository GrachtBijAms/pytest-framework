import requests
from core.logger import get_logger

class BaseAPIClient:
    def __init__(self, base_url: str, headers: dict = None):
        self.base_url = base_url
        self.headers = headers or {"Content-Type": "application/json"}
        self.logger = get_logger(__name__)
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _log_response(self, response: requests.Response) -> None:
        self.logger.info(
            f"Response: {response.status_code} | "
            f"Time: {response.elapsed.total_seconds()}s"
        )
        if not response.ok:
            self.logger.error(f"Response body: {response.text}")

    def get(self, endpoint: str, params: dict = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"GET {url}")
        response = self.session.get(url, params=params)
        self._log_response(response)
        return response

    def post(self, endpoint: str, payload: dict = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"POST {url} | payload: {payload}")
        response = self.session.post(url, json=payload)
        self._log_response(response)
        return response

    def put(self, endpoint: str, payload: dict = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"PUT {url} | payload: {payload}")
        response = self.session.put(url, json=payload)
        self._log_response(response)
        return response

    def delete(self, endpoint: str) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        self.logger.info(f"DELETE {url}")
        response = self.session.delete(url)
        self._log_response(response)
        return response
    
    def assert_status_code(
            self,
            response: requests.Response,
            expected: int) -> None:
        self.logger.info(
            f"Asserting status code: "
            f"expected={expected}, actual={response.status_code}"
        )
        assert response.status_code == expected, (
            f"Expected {expected} but got {response.status_code}\n"
            f"Response: {response.text}"
        )