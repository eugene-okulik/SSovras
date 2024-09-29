import requests
import allure
from test_api_sovras.endpoints.endpoint import Endpoint


class DeleteObj(Endpoint):
    @allure.feature('Deleting')
    @allure.story('Delete the object')
    @allure.title('Verifying deleting the record')
    @allure.step('Sending the DELETE request')
    def delete_object(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{object_id}',
            headers=headers
        )
        self.status_response = self.response.status_code
        print(object_id)
        return self.response
