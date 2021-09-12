import datetime
import os

from taminsdk.resources.prescription \
    import (create_prescription, PrescriptionNotCreatedException,
            )
from taminsdk.resources.prescription.types import PrescriptionType, DocEprsc
from taminsdk.session import Session


def sample_create_prescription():
    oauth_token = os.environ.get('OAUTH_TOKEN')
    # url = os.environ.get('URL')
    session = Session(oauth_token=oauth_token, url=None, username='username', password='password')

    prescription_data = {

        'patient': 'Mazafard',
        'mobile': '09222222222',
        'doctor': DocEprsc(),
        'doc_id': '1111111111',
        'presc_date': datetime.datetime.now().timestamp(),
        'doc_national_code': '1111111111',
        'doc_mobile_no': '09121111111111',
        'presc_type': PrescriptionType.VISIT,
        # 'comments': 'comments',
        # 'note_detail_eprscs': 'note_detail_eprscs',
    }

    try:
        p = create_prescription(session, **prescription_data)
    except PrescriptionNotCreatedException as e:
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
        return None
    else:
        return p


p = sample_create_prescription()
if p:
    print(("Project created: %s" % p.url))
