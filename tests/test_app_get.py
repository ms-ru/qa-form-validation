


def test_get_returns_200(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"Registr" in r.data or b"Regist" in r.data
    