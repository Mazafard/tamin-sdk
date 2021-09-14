from taminsdk.resources.service \
    import (get_prescription_type,
            )
from taminsdk.resources.service.exceptions import ServiceException
from taminsdk.session import Session


def sample_get_prescription_type():
    # oauth_token = os.environ.get('OAUTH_TOKEN')
    # url = os.environ.get('URL')
    session = Session(need_token=False)

    try:
        p = get_prescription_type(session)
    except ServiceException as e:
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
        return None
    else:
        return p


p = sample_get_prescription_type()
if p:
    print(p)
