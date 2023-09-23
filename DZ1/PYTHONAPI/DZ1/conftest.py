import pytest
import requests
import yaml

session = requests.Session()

with open('config.yaml', encoding='UTF-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def user_login():
    result = session.post(url=data['url'],
                          data={'username': data['login'],
                                'password': data['password']})
    response = result.json()
    return response['token']


@pytest.fixture()
def post_title():
    return 'new title'


@pytest.fixture()
def post_description():
    return 'some description'


@pytest.fixture()
def create_post(user_login):
    send_request = requests.post(url=data['address'],
                                 headers={'X-Auth-Token': user_login},
                                 data={'title': 'new title',
                                       'description': 'some description',
                                       'content': 'some content'})
    print(send_request.json)

