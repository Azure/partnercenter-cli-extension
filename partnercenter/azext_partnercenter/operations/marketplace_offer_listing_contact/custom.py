# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from azure.cli.core.azclierror import ResourceNotFoundError
from azext_partnercenter.models.listing_contact import ListingContact


def add_contact(instance, contact_type, email=None, name=None, phone=None, uri=None):
    contact = ListingContact(
        type = contact_type,
        email = email,
        name = name,
        phone = phone,
        uri = uri
    )
    instance.append(contact)
    return instance


def list_contact(client, offer_id):
    listing = client.get_listing(offer_id)
    if listing is None:
        raise ResourceNotFoundError('An Offer was not found with that ID.', 'Please check the value set for parameter --offer-id.')
    return listing.contacts


def delete_contact(client, offer_id, contact_type, email=None, name=None, phone=None, uri=None):
    contact = ListingContact(
        type = contact_type,
        email = email,
        name = name,
        phone = phone,
        uri = uri
    )
    return client.delete_listing_contact(offer_id, contact)
