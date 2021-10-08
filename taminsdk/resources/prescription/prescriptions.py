"""
This module contains functions for prescription operations
"""
import datetime
import logging

from taminsdk.resources.prescription import (
    make_get_request, make_post_request, )
from taminsdk.resources.prescription.types import (DocEprsc
                                                   )
from taminsdk.resources.service import handle_response

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

log = logging.getLogger(__name__)


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
    start_time = datetime.datetime.now()
    response = make_post_request(session, '', json_data=prescription_data)
    duration = datetime.datetime.now() - start_time
    log.info('Response[%d]: %s, Duration: %s.%ss.' % (
        response.status_code, response.reason, duration.seconds, duration.microseconds))
    return handle_response(response, response.content.decode('utf-8'))


def get_prescription_detail(
        session,
        params_data=None
):
    """
    Get prescription_detail
    """

    # get /api/ws-services
    start_time = datetime.datetime.now()

    response = make_get_request(
        session=session,
        endpoint='',
        params_data=params_data
    )
    duration = datetime.datetime.now() - start_time
    log.info('Response[%d]: %s, Duration: %s.%ss.' % (
        response.status_code, response.reason, duration.seconds, duration.microseconds))
    return handle_response(response, response.content.decode('utf-8'))
