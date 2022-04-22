import pytest

def test_index(client):
    response=client.get("/")
    #print(response.json)
    #assert response.json["msg"]==""
    assert response.status_code==200