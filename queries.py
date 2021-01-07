from time import sleep
import requests

def local_server(login, password):
    response = requests.post('http://127.0.0.1:5000/auth',
                             json={'login': login, 'password': password})
    return response.status_code == 200

