import asyncio
import pytest

from app.main import app
from app.schemas.users import UserCreate
from app.utils.users import create_user, create_user_token
from app.utils.accounts import create_account
from fastapi.testclient import TestClient


def test_create_account(temp_db):
    user = UserCreate(
        email="vader2@deathstar.com",
        last_name="Vader",
        first_name="Darth",
        patronymic="",
        password="rainbow"
    )
    request_data = {
       "brief": "42301810600000000777",
       "name": "Счет тестовый",
       "fund_id": 2,
       "user_id": 1
    }
    with TestClient(app) as client:
        # Create user and use his token to add new account
        loop = asyncio.get_event_loop()
        user_db = loop.run_until_complete(create_user(user))
        response = client.post(
            "/accounts",
            json=request_data,
            headers={"Authorization": f"Bearer {user_db['token']['token']}"}
        )
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["brief"] == "42301810600000000777"
    assert response.json()["user_id"] == 1


def test_account_get(temp_db):
    with TestClient(app) as client:
        # Create user token to see user info
        loop = asyncio.get_event_loop()
        token = loop.run_until_complete(create_user_token(user_id=1))
        response = client.get(
            "/accounts/1",
            headers={"Authorization": f"Bearer {token['token']}"}
        )
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["brief"] == "42301810600000000777"
    assert response.json()["user_id"] == 1


def test_account_update(temp_db):
    request_data = {
        "id": 1,
        "brief": "42301810600000000888",
        "name": "Имя счета после изменения",
        "fund_id": 2,
        "dateStart": "2023-10-22T11:28:44.077741",
        "dateEnd": "2023-10-22T11:28:44.077744",
        "user_id": 1
    }
    with TestClient(app) as client:
        # Create user token to see user info
        loop = asyncio.get_event_loop()
        token = loop.run_until_complete(create_user_token(user_id=1))
        response = client.put(
            "/accounts/1",
            json=request_data,
            headers={"Authorization": f"Bearer {token['token']}"}
        )
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["brief"] == "42301810600000000888"
    assert response.json()["name"] == "Имя счета после изменения"
    assert response.json()["fund_id"] == 2
    assert response.json()["dateStart"] == "2023-10-22T11:28:44.077741"
    assert response.json()["dateEnd"] == "2023-10-22T11:28:44.077744"
    assert response.json()["user_id"] == 1


def test_account_delete(temp_db):
    with TestClient(app) as client:
        # Create user token to see user info
        loop = asyncio.get_event_loop()
        token = loop.run_until_complete(create_user_token(user_id=1))
        response = client.delete(
            "/accounts/1",
            headers={"Authorization": f"Bearer {token['token']}"}
        )
    assert response.status_code == 204

