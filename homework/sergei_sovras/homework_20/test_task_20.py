import pytest
import requests
import allure


@allure.feature('Creating')
@allure.story('Create an object')
@allure.title('Verifying creating a new record')
@pytest.mark.critical
@pytest.mark.parametrize('name_param', ['Name_1', 'Name_2', 'Name_3'])
def test_create_object(name_param, messages_for_each_session, messages_for_each_test):
    data = {
        "name": name_param,
        "data": {
            "year": 2024,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    url = 'https://api.restful-api.dev/objects'
    headers = {'Content-Type': 'application/json'}
    with allure.step('Sending the post request'):
        response = requests.post(url, json=data, headers=headers)
    with allure.step('Verifying the status code'):
        assert response.status_code == 200, "The request isn't sent"
    with allure.step('Sending the delete request'):
        requests.delete(f'{url}/{response.json()["id"]}', headers=headers)


@allure.feature('Editing')
@allure.story('Edit the object with PUT')
@allure.title('Verifying updating the record with PUT')
@pytest.mark.medium
def test_put_editing(obj_creating_and_deleting, messages_for_each_session, messages_for_each_test):
    with allure.step('Sending the post request'):
        obj_id = obj_creating_and_deleting
    data = {
        "name": "Apple MacBook Pro 16 UPDATED",
        "data": {
            "year": 1990,
            "price": 201145,
            "CPU model": "Intel Core i9 UPDATED",
            "Hard disk size": "1 TB UPDATED"
        }
    }
    url = 'https://api.restful-api.dev/objects'
    headers = {'Content-Type': 'application/json'}
    with allure.step('Sending the put request'):
        response = requests.put(f'{url}/{obj_id}', json=data, headers=headers)
    with allure.step('Verifying the status code'):
        assert response.status_code == 200, "The request isn't sent"
    with allure.step('Verifying the id value'):
        assert response.json()['id'] == obj_id


@allure.feature('Editing')
@allure.story('Edit the object with PATCH')
@allure.title('Verifying updating the record with PATCH')
@pytest.mark.low
def test_patch_editing(obj_creating_and_deleting, messages_for_each_session, messages_for_each_test):
    with allure.step('Sending the post request'):
        obj_id = obj_creating_and_deleting
    data = {
        "name": "Updated Name",
    }
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'
    response = requests.patch(f'{url}/{obj_id}', json=data, headers=headers)
    with allure.step('Verifying the status code'):
        assert response.status_code == 200, "The request isn't sent"
    with allure.step('Verifying the id value'):
        assert response.json()['id'] == obj_id


@allure.feature('Deleting')
@allure.story('Delete the object')
@allure.title('Verifying deleting the record')
@pytest.mark.medium
def test_delete_object(obj_creating, messages_for_each_session, messages_for_each_test):
    with allure.step('Verifying the status code'):
        obj_id = obj_creating
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'
    with allure.step('Sending the delete request'):
        response = requests.delete(f'{url}/{obj_id}', headers=headers)
    with allure.step('Verifying the status code'):
        assert response.status_code == 200, "The request isn't sent"
