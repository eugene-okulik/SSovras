from test_api_sovras.endpoints.create_object import CreateObj
from test_api_sovras.endpoints.update_put import UpdatePut
from test_api_sovras.endpoints.update_patch import UpdatePatch
from test_api_sovras.endpoints.delete_object import DeleteObj

import pytest


@pytest.fixture()
def create_obj_endpoint():
    return CreateObj()


@pytest.fixture()
def update_put_obj_endpoint():
    return UpdatePut()


@pytest.fixture()
def update_patch_obj_endpoint():
    return UpdatePatch()


@pytest.fixture()
def delete_obj_endpoint():
    return DeleteObj()


@pytest.fixture()
def new_object(create_obj_endpoint):
    data = {
        "name": 'name_param',
        "data": {
            "year": 2024,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    create_obj_endpoint.create_new_object(payload=data)
    yield create_obj_endpoint.obj_id


@pytest.fixture()
def delete_object(delete_obj_endpoint):
    yield True
    delete_obj_endpoint.delete_object(new_object)
