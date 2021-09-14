"""
This module contains functions for prescription operations
"""

from taminsdk.resources.service import (
    make_get_request,
)
from taminsdk.resources.service.exceptions import (
    ServiceException,
)

from taminsdk.resources.service.types import Service

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


def get_all_services(
        session,
        params_data=None
):
    """
    Get all Services
    """

    # get /api/ws-services
    response = make_get_request(
        session=session,
        endpoint='ws-services',
        params_data=params_data
    )
    json_data = response.json()
    if response.status_code == 200:
        services_data = json_data['data']
        return Service(services_data)
    else:
        raise ServiceException(
            message=json_data['data'],
            error_code=json_data['error_code'],

        )


def get_prescription_type(
        session,
        params_data=None
):
    """
    Get prescription_type
    """

    # get /api/get_prescription_type
    response = make_get_request(
        session=session,
        endpoint='ws-prescription-type',
        params_data=params_data
    )
    json_data = response.json()
    if response.status_code == 200:
        services_data = json_data['data']
        return Service(services_data)
    else:
        raise ServiceException(
            message=json_data['data'],
            error_code=json_data['error_code'],

        )

def get_paraclinic_taref(
        session,
        params_data=None
):
    """
    Get Paraclinic Taref
    """

    # get /api/ws-par-taref
    response = make_get_request(
        session=session,
        endpoint='ws-par-taref',
        params_data=params_data
    )
    json_data = response.json()
    if response.status_code == 200:
        services_data = json_data['data']
        return Service(services_data)
    else:
        raise ServiceException(
            message=json_data['data'],
            error_code=json_data['error_code'],

        )


def get_drug_amount(
        session,
        params_data=None
):
    """
    Get Drug Amount
    """

    # get /api/get_drug_amount
    response = make_get_request(
        session=session,
        endpoint='ws-drug-amount',
        params_data=params_data
    )
    json_data = response.json()
    if response.status_code == 200:
        services_data = json_data['data']
        return Service(services_data)
    else:
        raise ServiceException(
            message=json_data['data'],
            error_code=json_data['error_code'],

        )


def get_drug_instruction(
        session,
        params_data=None
):
    """
    Get Drug Amount
    """

    # get /api/ws-drug-instruction
    response = make_get_request(
        session=session,
        endpoint='ws-drug-instruction',
        params_data=params_data
    )
    json_data = response.json()
    if response.status_code == 200:
        services_data = json_data['data']
        return Service(services_data)
    else:
        raise ServiceException(
            message=json_data['data'],
            error_code=json_data['error_code'],

        )

