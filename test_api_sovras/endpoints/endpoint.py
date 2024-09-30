import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None
    status_response = None
    obj_id = None

    @allure.step('Check that response is 200')
    def verifying_status_code_200(self):
        assert self.status_response == 200

    @allure.step('Check that name is the same as sent')
    def verifying_response_title_is_correct(self, name):
        assert self.json['name'] == name
