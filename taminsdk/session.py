from urllib.parse import urljoin

import requests

from taminsdk.exceptions import UserLoginException


class Session():
    """
    This class will manage a HTTP session to the tamin.ir API
    """

    def __init__(self, oauth_token=None, url=None, username=None, password=None, need_token=True):
        self.session = requests.Session()
        if url is not None:
            self.url = url
        else:

            self.url = 'https://ep-test.tamin.ir/api/'
        print(self.url)
        if need_token:
            if not oauth_token:
                oauth_token = self._login(username, password)

            # Set default headers
            default_headers = {
                'Authorization': f'Bearer {oauth_token}',
            }
            self.session.headers.update(default_headers)

    def _login(self, user, password):
        json_data = {
            'client_id': user,
            'secret': password
        }
        url = urljoin(self.url, f'ws/api/auth/login')
        response = self.session.post(url, json=json_data, verify=True)
        json_data = response.json()
        if response.status_code == 200:
            return json_data['data']
        else:
            raise UserLoginException(
                data=json_data['data'],
                status=json_data['status'],
                family=json_data['family'],
                reason=json_data['reason'])
