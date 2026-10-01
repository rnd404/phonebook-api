import pytest

step5 = pytest.mark.skip(reason="step 5: implement authentication and permissions")


@step5
async def test_login_wrong_password_is_401(client):
    r = await client.post("/auth/login", data={"username": "nobody", "password": "wrong-password"})
    assert r.status_code == 401


@step5
async def test_search_requires_token(client):
    assert (await client.get("/contacts", params={"q": "ross"})).status_code == 401


@step5
async def test_read_only_user_cannot_add(client):
    # TODO: create a user with can_write=False, log in, POST /contacts -> 403
    ...
