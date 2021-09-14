# This module will contain helper functions/classes for services
from taminsdk.resources.service import services_endpoint

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


# Make API calls
# ws-services?serviceType=17
def make_get_request(session, endpoint, params_data=None):
    url = f"{session.url}{services_endpoint}{endpoint}"
    return session.session.get(url, params=params_data, verify=True)


def make_post_request(session, endpoint, json_data):
    url = f"{session.url}{services_endpoint}{endpoint}"
    return session.session.post(url, json=json_data, verify=True)


def make_put_request(session, endpoint, headers=None, params_data=None,
                     form_data=None, json_data=None):
    url = f"{session.url}{services_endpoint}{endpoint}"
    return session.session.put(url, headers=headers, params=params_data,
                               data=form_data, json=json_data, verify=True)
