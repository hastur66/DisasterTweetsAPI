from urllib import response
import pytest
from DisasterTweetsAPI import app

def test_get():
    response = app.test_client().get('/')
    
    assert response.status_code == 200