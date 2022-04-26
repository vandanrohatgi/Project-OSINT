import json
from unittest.mock import patch

def test_index(client):
    response=client.get("/")
    assert response.status_code==200

def test_index_response(client):
    response=client.get("/")
    assert response.json["msg"]=="API works!"

@patch('flask_jwt_extended.view_decorators.verify_jwt_in_request')  ### disable jwt_required() (authentication) for this test
def test_auth(mock_jwt_token,client):
    response=client.post("/login",data=json.dumps({"username":"test","password":"test"}),content_type="application/json")
    assert response.status_code==200
    assert 'access_token' in response.json.keys()

    response=client.get("/getScanInfo")
    assert response.status_code == 200

def test_unauth(client):
    response=client.get("/logout")
    assert response.status_code == 401
    response=client.get("/getScanInfo")
    assert response.status_code == 401
    response=client.post("/start")
    assert response.status_code == 401
