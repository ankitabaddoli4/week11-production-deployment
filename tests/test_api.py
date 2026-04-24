def test_home(app):
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200