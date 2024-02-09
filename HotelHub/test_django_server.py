import requests


def test_basic_auth():
    response = requests.get('http://127.0.0.1:8000/api/guests/',)
    
    print(response.status_code)
    print(response.json())
    
    response = requests.get('http://127.0.0.1:8000/api/guests/',auth=('dima','123'))
    
    print(response.status_code)
    print(response.json())


def test_token_auth():
    response = requests.post('http://127.0.0.1:8000/api/auth/',json={'username':'test_user7','password':'test_user'})
     
    print(response.status_code)
    print(response.json())
    
    token = response.json()['token']
    
    
    response = requests.get('http://127.0.0.1:8000/api',headers={'Authorization':f'Token {token}'})
    
    print(response.status_code)
    print(response.json())
    
    
def test_registration_view():
    
    registration_data = {
        'username': 'test_user7',
        'password': 'test_user',
    }

    response = requests.post('http://127.0.0.1:8000/api/register/', json=registration_data)
  

    
    print(response.status_code)
    print(response.json())
   

if __name__ == '__main__':
    test_token_auth()
    # test_registration_view()
    # test_basic_auth()