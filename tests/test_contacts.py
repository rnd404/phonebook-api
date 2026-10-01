import pytest

step3 = pytest.mark.skip(reason="step 3: implement create/get/delete with the database")
step4 = pytest.mark.skip(reason="step 4: implement search and pagination")

PERSON = {"kind": "person", "name": "Mario", "surname": "Rossi", "phone": "333 1234567"}
COMPANY = {"kind": "company", "name": "Acme Srl", "phone": "06 1234567"}


# --- already passing: validation lives in the schema, before our code runs ---
async def test_person_without_surname_is_rejected(client):
    r = await client.post("/contacts", json={"kind": "person", "name": "Mario", "phone": "3331234567"})
    assert r.status_code == 422


async def test_invalid_phone_is_rejected(client):
    r = await client.post("/contacts", json={**PERSON, "phone": "abc"})
    assert r.status_code == 422


# --- to unlock step by step: remove the skip marker when you implement the endpoint ---
@step3
async def test_create_and_get(client):
    created = (await client.post("/contacts", json=PERSON)).json()
    assert created["id"] > 0 and created["surname"] == "Rossi"
    r = await client.get(f"/contacts/{created['id']}")
    assert r.status_code == 200 and r.json() == created


@step3
async def test_get_missing_returns_404(client):
    assert (await client.get("/contacts/999")).status_code == 404


@step3
async def test_delete(client):
    cid = (await client.post("/contacts", json=COMPANY)).json()["id"]
    assert (await client.delete(f"/contacts/{cid}")).status_code == 204
    assert (await client.get(f"/contacts/{cid}")).status_code == 404


@step4
async def test_search_is_case_insensitive_substring(client):
    await client.post("/contacts", json=PERSON)
    await client.post("/contacts", json=COMPANY)
    r = await client.get("/contacts", params={"q": "ROSS"})
    assert [c["surname"] for c in r.json()] == ["Rossi"]


@step4
async def test_pagination(client):
    for i in range(5):
        await client.post("/contacts", json={**COMPANY, "name": f"Acme {i}"})
    r = await client.get("/contacts", params={"limit": 2, "offset": 2})
    assert len(r.json()) == 2
