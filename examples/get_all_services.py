from taminsdk.resources.service import get_all_services
from taminsdk.resources.service.exceptions import ServiceException
from taminsdk.session import Session


def sample_get_all_services():
    # oauth_token = os.environ.get('OAUTH_TOKEN')
    # url = os.environ.get('URL')
    session = Session(need_token=False)

    try:
        p = get_all_services(session)
    except ServiceException as e:
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
        return None
    else:
        return p


p = sample_get_all_services()
if p:
    print(p)
