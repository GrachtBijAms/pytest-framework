import allure
import pytest

@allure.feature("User Management")
@allure.story("Get Users")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
def test_get_all_users(user_api):
    # call get_all_users
    response = user_api.get_all_users()
    # assert status code 200
    with allure.step("Verify status code is 200"):
        user_api.assert_status_code(response, expected=200)
    # assert response is a list
    assert isinstance(response.json(), list)
    # assert list is not empty
    assert len(response.json()) > 0

@allure.feature("User Management")
@allure.story("Get Users")
def test_get_single_user(user_api):
    # get user with id 1
    response = user_api.get_user(user_id=1)
    # assert status code 200
    with allure.step("Verify status code is 200"):
        user_api.assert_status_code(response, expected=200)
    # assert id equals 1
    assert response.json()["id"] == 1
    # assert name is not empty
    assert response.json()["name"] != ""

@allure.feature("User Management")
@allure.story("Create User")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_user(user_api):
    # define payload with name, email, username
    payload = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "username": "johndoe"
    }
    # create user
    response = user_api.create_user(payload=payload)
    # assert status code 201
    with allure.step("Verify status code is 201"):
        user_api.assert_status_code(response, expected=201)
    # assert name in response matches payload
    assert response.json()["name"] == payload["name"]

@allure.feature("User Management")
@allure.story("Update User")
def test_update_user(user_api):
    # define payload with updated name
    payload = {
        "name": "Jane Doe"
    }
    # update user with id 1
    response = user_api.update_user(user_id=1, payload=payload)
    # assert status code 200
    with allure.step("Verify status code is 200"):
        user_api.assert_status_code(response, expected=200)
    # assert name in response matches updated name
    assert response.json()["name"] == payload["name"]

@allure.feature("User Management")
@allure.story("Delete User")
def test_delete_user(user_api):
    # delete user with id 1
    response = user_api.delete_user(user_id=1)
    # assert status code 200
    with allure.step("Verify status code is 200"):
        user_api.assert_status_code(response, expected=200)