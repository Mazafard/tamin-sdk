import datetime
import os

from taminsdk.resources.service \
    import (get_drug_instruction,
            )
from taminsdk.resources.service.exceptions import ServiceException
from taminsdk.resources.service.types import Service
from taminsdk.session import Session


def sample_get_drug_instruction():
    # oauth_token = os.environ.get('OAUTH_TOKEN')
    # url = os.environ.get('URL')
    session = Session(need_token=False)

    try:
        p = get_drug_instruction(session)
    except ServiceException as e:
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
        return None
    else:
        return p


p = sample_get_drug_instruction()
if p:
    print(p)
