import requests
import os
from dotenv import load_dotenv


def get_token(client_id):
    data = {
        'client_id': client_id,
        'grant_type': 'implicit',
    }
    response = requests.post('https://api.moltin.com/oauth/access_token', data=data)
    moltin_access_token = response.json()['access_token']
    return moltin_access_token


def get_products(client_id):
    moltin_access_token = get_token(client_id)
    headers = {
        'Authorization': f'Bearer {moltin_access_token}',
    }
    response = requests.get('https://api.moltin.com/v2/products', headers=headers)
    return response.json()['data']


def get_product_details(client_id, product_id):
    moltin_access_token = get_token(client_id)
    headers = {
        'Authorization': f'Bearer {moltin_access_token}',
    }
    response = requests.get(f'https://api.moltin.com/v2/products/{product_id}', headers=headers)
    return response.json()['data']


def main() -> None:
    load_dotenv()
    client_id = os.getenv('MOLTIN_CLIENT_ID')
        

    '''
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
    
    #выводим список товаров в корзине
    headers = {
        'Authorization': f'Bearer {moltin_access_token}',
    }

    response = requests.get('https://api.moltin.com/v2/carts/:reference/items', headers=headers) 
    print(response.json())
    '''

    

if __name__ == '__main__':
    main()