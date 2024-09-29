import requests
import allure
from test_api_sovras.endpoints.endpoint import Endpoint


class UpdatePatch(Endpoint):
    @allure.feature('Editing')
    @allure.story('Edit the object with PATCH')
    @allure.title('Verifying updating the record with PATCH')
    @allure.step('Sending the PATCH request')
    def update_patch(self, object_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
