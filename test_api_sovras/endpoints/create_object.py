import requests
import allure
from test_api_sovras.endpoints.endpoint import Endpoint


class CreateObj(Endpoint):
    @allure.feature('Creating')
    @allure.story('Create an object')
    @allure.title('Verifying creating a new record')
    @allure.step('Sending the POST request')
    def create_new_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.status_response = self.response.status_code
        self.obj_id = self.json["id"]
        return self.response
