from app import app

def test_addition():
    c = app.test_client()
    r = c.post("/", data={
        "a": "10", "b": "5", "op": "add"
    })
    assert r.status_code == 200
    assert "15.0" in r.get_data(as_text=True)

def test_subtraction():
    c = app.test_client()
    r = c.post("/", data={
        "a": "10", "b": "5", "op": "sub"
    })
    assert r.status_code == 200
    assert "5.0" in r.get_data(as_text=True)