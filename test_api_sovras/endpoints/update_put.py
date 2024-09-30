import requests
import allure
from test_api_sovras.endpoints.endpoint import Endpoint


class UpdatePut(Endpoint):
    @allure.feature('Editing')
    @allure.story('Edit the object with PUT')
    @allure.title('Verifying updating the record with PUT')
    @allure.step('Sending the PUT request')
    def update_put(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.status_response = self.response.status_code
        return self.response
