from django.test import client

def test_status_code(client:client):
     resp = client.get('/')
     assert resp.status_code == 200

