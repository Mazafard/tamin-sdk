"""
This module contains functions for prescription operations
"""
import datetime

from taminsdk.resources.prescription import (
    make_get_request, make_post_request, make_put_request,
)
from taminsdk.resources.prescription.exceptions import (
    PrescriptionNotCreatedException,
)
from taminsdk.resources.prescription.types import (Prescription, DocEprsc
)

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


def create_prescription(
        session,
        patient: str,
        mobile: str,
        doctor: DocEprsc,  # doc_eprc,
        doc_id: str,
        presc_date: datetime,
        doc_national_code: str,
        doc_mobile_no: str,
        presc_type: object,  # presc_type,
        comments: str,
        note_detail_eprscs: [object],  # note_detail_eprsc[],

):
    """
    Create a prescription
    """
    prescription_data = {

        'patient': patient,
        'mobile': mobile,
        'doctor': doctor,
        'doc_id': doc_id,
        'presc_date': presc_date,
        'doc_national_code': doc_national_code,
        'doc_mobile_no': doc_mobile_no,
        'presc_type': presc_type,
        'comments': comments,
        'note_detail_eprscs': note_detail_eprscs,
    }

    # POST /interface/epresc/SendEpresc
    response = make_post_request(session, '', json_data=prescription_data)
    json_data = response.json()
    if response.status_code == 200:
        prescription_data = json_data['data']
        return Prescription(prescription_data)
    else:
        raise PrescriptionNotCreatedException(
            message=json_data['message'],
            error_code=json_data['error_code'],
        )



def get_prescription_detail(
        session,
        params_data=None
):
    """
    Get prescription_detail
    """

    # get /api/ws-services
    response = make_get_request(
        session=session,
        endpoint='',
        params_data=params_data
    )
    json_data = response.json()
    if response.status_code == 200:
        prescription_data = json_data['data']
        return Prescription(prescription_data)
    else:
        raise PrescriptionNotCreatedException(
            message=json_data['data'],
            error_code=json_data['error_code'],

        )
