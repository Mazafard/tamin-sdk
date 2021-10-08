# This module will contain helper functions/classes for services
import json

from taminsdk import exceptions
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


def handle_response(response, content):
    """Validate HTTP response
    """
    status = response.status_code
    if status in (301, 302, 303, 307):
        raise exceptions.Redirection(response, content)
    elif 200 <= status <= 299:
        return json.loads(content) if content else {}
    elif status == 400:
        raise exceptions.BadRequest(response, content)
    elif status == 401:
        raise exceptions.UnauthorizedAccess(response, content)
    elif status == 403:
        raise exceptions.ForbiddenAccess(response, content)
    elif status == 404:
        raise exceptions.ResourceNotFound(response, content)
    elif status == 405:
        raise exceptions.MethodNotAllowed(response, content)
    elif status == 409:
        raise exceptions.ResourceConflict(response, content)
    elif status == 410:
        raise exceptions.ResourceGone(response, content)
    elif status == 422:
        raise exceptions.ResourceInvalid(response, content)
    elif 401 <= status <= 499:
        raise exceptions.ClientError(response, content)
    elif 500 <= status <= 599:
        raise exceptions.ServerError(response, content)
    else:
        raise exceptions.ConnectionError(
            response, content, "Unknown response code: #{response.code}")
