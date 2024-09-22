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
    print('\nBefore test')
    yield
    print('\nAfter test')
