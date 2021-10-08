"""
This module contains functions for prescription operations
"""
import datetime
import logging

from taminsdk.resources.service import (
    make_get_request, handle_response,
)
from taminsdk.resources.service.exceptions import (
    ServiceException,
)
from taminsdk.resources.service.types import Service

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

log = logging.getLogger(__name__)


def get_all_services(
        session,
        params_data=None
):
    """
    Get all Services
    """

    # get /api/ws-services
    start_time = datetime.datetime.now()
    response = make_get_request(
        session=session,
        endpoint='ws-services',
        params_data=params_data
    )
    duration = datetime.datetime.now() - start_time
    log.info('Response[%d]: %s, Duration: %s.%ss.' % (
        response.status_code, response.reason, duration.seconds, duration.microseconds))
    return handle_response(response, response.content.decode('utf-8'))


def get_prescription_type(
        session,
        params_data=None
):
    """
    Get prescription_type
    """

    # get /api/get_prescription_type
    start_time = datetime.datetime.now()
    response = make_get_request(
        session=session,
        endpoint='ws-prescription-type',
        params_data=params_data
    )
    duration = datetime.datetime.now() - start_time
    log.info('Response[%d]: %s, Duration: %s.%ss.' % (
        response.status_code, response.reason, duration.seconds, duration.microseconds))
    return handle_response(response, response.content.decode('utf-8'))


def get_paraclinic_taref(
        session,
        params_data=None
):
    """
    Get Paraclinic Taref
    """

    # get /api/ws-par-taref
    start_time = datetime.datetime.now()
    response = make_get_request(
        session=session,
        endpoint='ws-par-taref',
        params_data=params_data
    )
    duration = datetime.datetime.now() - start_time
    log.info('Response[%d]: %s, Duration: %s.%ss.' % (
        response.status_code, response.reason, duration.seconds, duration.microseconds))
    return handle_response(response, response.content.decode('utf-8'))


def get_drug_amount(
        session,
        params_data=None
):
    """
    Get Drug Amount
    """

    # get /api/get_drug_amount
    start_time = datetime.datetime.now()
    response = make_get_request(
        session=session,
        endpoint='ws-drug-amount',
        params_data=params_data
    )
    duration = datetime.datetime.now() - start_time
    log.info('Response[%d]: %s, Duration: %s.%ss.' % (
        response.status_code, response.reason, duration.seconds, duration.microseconds))
    return handle_response(response, response.content.decode('utf-8'))


def get_drug_instruction(
        session,
        params_data=None
):
    """
    Get Drug Amount
    """

    # get /api/ws-drug-instruction
    start_time = datetime.datetime.now()
    response = make_get_request(
        session=session,
        endpoint='ws-drug-instruction',
        params_data=params_data
    )
    duration = datetime.datetime.now() - start_time
    log.info('Response[%d]: %s, Duration: %s.%ss.' % (
        response.status_code, response.reason, duration.seconds, duration.microseconds))
    return handle_response(response, response.content.decode('utf-8'))
