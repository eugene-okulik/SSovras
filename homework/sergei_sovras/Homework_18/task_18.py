import requests


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


def obj_clearing(obj_id):
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'
    requests.delete(f'{url}/{obj_id}', headers=headers)


def create_object():
    data = {
        "name": "Apple MacBook Pro 16",
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
    obj_clearing(response.json()['id'])


def put_editing():
    obj_id = obj_creating()
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
    obj_clearing(obj_id)


def patch_editing():
    obj_id = obj_creating()
    data = {
        "name": "Updated Name",
    }
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'
    response = requests.patch(f'{url}/{obj_id}', json=data, headers=headers)
    assert response.status_code == 200, "The request isn't sent"
    assert response.json()['id'] == obj_id
    obj_clearing(obj_id)


def delete_object():
    obj_id = obj_creating()
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'
    response = requests.delete(f'{url}/{obj_id}', headers=headers)
    assert response.status_code == 200, "The request isn't sent"


create_object()
put_editing()
patch_editing()
delete_object()
