def test_get_returns_200(client):
    """
    Test that a GET request to the root URL ("/") works correctly.
    - Expects a 200 OK status code
    - Checks that the response contains the word "Registr" (German "Registrierung")
      or "Regist" (covers possible encoding/truncation cases)
    """
    # Send a GET request to the homepage
    r = client.get("/")

    # The response should be successful (HTTP 200)
    assert r.status_code == 200

    # The HTML should contain text related to "Registration"
    assert b"Registr" in r.data or b"Regist" in r.data
             