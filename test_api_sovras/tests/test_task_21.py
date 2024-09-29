import pytest


@pytest.mark.critical
@pytest.mark.parametrize('name_param', ['Name_1', 'Name_2', 'Name_3'])
def test_create_object(name_param, create_obj_endpoint, delete_object):
    data = {
        "name": name_param,
        "data": {
            "year": 2024,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_obj_endpoint.create_new_object(payload=data)
    create_obj_endpoint.verifying_status_code_200()
    create_obj_endpoint.verifying_response_title_is_correct(data['name'])


@pytest.mark.low
def test_patch_editing(new_object, update_patch_obj_endpoint, delete_object):
    data = {"name": "Updated Name"}
    update_patch_obj_endpoint.update_patch(new_object, payload=data, )
    update_patch_obj_endpoint.verifying_status_code_200()
    update_patch_obj_endpoint.verifying_response_title_is_correct(data['name'])


@pytest.mark.medium
def test_put_editing(new_object, update_put_obj_endpoint, delete_object):
    data = {
        "name": "Apple MacBook Pro 16 UPDATED",
        "data": {
            "year": 1990,
            "price": 201145,
            "CPU model": "Intel Core i9 UPDATED",
            "Hard disk size": "1 TB UPDATED"
        }
    }
    update_put_obj_endpoint.update_put(new_object, payload=data,)
    update_put_obj_endpoint.verifying_status_code_200()
    update_put_obj_endpoint.verifying_response_title_is_correct(data['name'])


@pytest.mark.medium
def test_delete_object(new_object, delete_obj_endpoint):
    delete_obj_endpoint.delete_object(new_object)
    delete_obj_endpoint.verifying_status_code_200()
