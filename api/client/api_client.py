import time

import requests

from utilities.custom_logger import LogMaker

logger = LogMaker.log_gen("API")

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
        url = self.api_url + endpoint

        logger.info("=" * 80)
        logger.info(f"GET Request: {url}")

        start_time = time.perf_counter()

        response = self.session.get(url)

        end_time = time.perf_counter()

        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Time: {(end_time - start_time):.3f} seconds")
        logger.info(f"Response Body: {response.text}")

        return response

    def post(self, endpoint, payload):
        url = self.api_url + endpoint

        logger.info("=" * 80)
        logger.info(f"POST Request: {url}")
        logger.info(f"Request payload: {payload}")

        start_time = time.perf_counter()

        response = self.session.post(
            url,
            json=payload
        )

        end_time = time.perf_counter()

        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Time: {(end_time - start_time):.3f} seconds")
        logger.info(f"Response Body: {response.text}")

        return response

    def put(self, endpoint, payload):
        url = self.api_url + endpoint

        logger.info("=" * 80)
        logger.info(f"PUT Request: {url}")
        logger.info(f"Request payload: {payload}")

        start_time = time.perf_counter()

        response = self.session.put(
            url,
            json=payload
        )

        end_time = time.perf_counter()

        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Time: {(end_time - start_time):.3f} seconds")
        logger.info(f"Response Body: {response.text}")

        return response


    def delete(self, endpoint):
        url = self.api_url + endpoint

        logger.info("=" * 80)
        logger.info(f"DELETE Request: {url}")

        start_time = time.perf_counter()

        response = self.session.delete(url)

        end_time = time.perf_counter()

        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Time: {(end_time - start_time):.3f} seconds")
        logger.info(f"Response Body: {response.text}")

        return response
