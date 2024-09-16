import pytest
import requests


@pytest.fixture()
def obj_creating_and_deleting():
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'
    response = requests.post(url, json=data, headers=headers)
    yield response.json()['id']
    requests.delete(f'{url}/{response.json()["id"]}', headers=headers)


@pytest.fixture()
def obj_creating():
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2024,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'
    response = requests.post(url, json=data, headers=headers)
    return response.json()['id']


@pytest.fixture(scope='session')
def messages_for_each_session():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def messages_for_each_test():
    print('\nbefore test')
    yield
    print('\nafter test')


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
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 200, "The request isn't sent"
    requests.delete(f'{url}/{response.json()["id"]}', headers=headers)


def test_put_editing(obj_creating_and_deleting, messages_for_each_session, messages_for_each_test):
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
    response = requests.put(f'{url}/{obj_id}', json=data, headers=headers)
    assert response.status_code == 200, "The request isn't sent"
    assert response.json()['id'] == obj_id


@pytest.mark.critical
def test_patch_editing(obj_creating_and_deleting, messages_for_each_session, messages_for_each_test):
    obj_id = obj_creating_and_deleting
    data = {
        "name": "Updated Name",
    }
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'
    response = requests.patch(f'{url}/{obj_id}', json=data, headers=headers)
    assert response.status_code == 200, "The request isn't sent"
    assert response.json()['id'] == obj_id


@pytest.mark.medium
def test_delete_object(obj_creating, messages_for_each_session, messages_for_each_test):
    obj_id = obj_creating
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'
    response = requests.delete(f'{url}/{obj_id}', headers=headers)
    assert response.status_code == 200, "The request isn't sent"
