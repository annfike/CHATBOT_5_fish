import requests
import os
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    client_id = os.getenv('MOLTIN_CLIENT_ID')

    #получаем access token
    data = {
        'client_id': client_id,
        'grant_type': 'implicit',
    }
    response = requests.post('https://api.moltin.com/oauth/access_token', data=data)
    moltin_access_token = response.json()['access_token']
    print(moltin_access_token)


    '''
    # получаем инфо о продуктах
    headers = {
        'Authorization': f'Bearer {moltin_access_token}',
    }

    #response = requests.get('https://api.moltin.com/v2/carts/abc', headers=headers)
    response = requests.get('https://api.moltin.com/v2/products', headers=headers)
    print(response.json())


    #добавляем продукт в корзину по его id
    headers = {
        'Authorization': f'Bearer {moltin_access_token}',
        'Content-Type': 'application/json',
    }

    json_data  = {
        'data': {
            'id': '2f0fdfa0-b9e5-4d66-962d-1673e84961f7',
            'type': 'cart_item',
            'quantity': 1,
        },
    }

    response = requests.post('https://api.moltin.com/v2/carts/:reference/items', headers=headers, json=json_data)
    print(response.json())


    #выводим корзину 
    headers = {
        'Authorization': f'Bearer {moltin_access_token}',
    }

    response = requests.get('https://api.moltin.com/v2/carts/:reference', headers=headers)
    print(response.json())
    '''
    #выводим список товаров в корзине
    headers = {
        'Authorization': f'Bearer {moltin_access_token}',
    }

    response = requests.get('https://api.moltin.com/v2/carts/:reference/items', headers=headers) 
    print(response.json())

if __name__ == '__main__':
    main()