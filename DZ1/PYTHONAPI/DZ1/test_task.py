import requests
import yaml

from conftest import user_login, post_title

with open('config.yaml', encoding='UTF-8') as f:
    data = yaml.safe_load(f)

session = requests.Session()


def test_t1(user_login):
    result = session.get(url=data['address'],
                         headers={'X-Auth-Token': user_login}
                         ).json()['data']

    send_request = requests.post(url=data['address'],
                                 headers={'X-Auth-Token': user_login},
                                 data={'title': 'new title',
                                       'description': 'some description',
                                       'content': 'some content'})

    print(send_request.json())






def test_t2(user_login, post_title, post_description):
    result = session.get(url=data['address'],
                         headers={'X-Auth-Token': user_login}
                         ).json()['data']
    result_title = [item['title'] for item in result]
    result_description = [item['description'] for item in result]


    assert post_title in result_title, 'test_t2_checktitle FAIL'
    assert post_description in result_description, 'test_t2_checknewpost FAIL'



