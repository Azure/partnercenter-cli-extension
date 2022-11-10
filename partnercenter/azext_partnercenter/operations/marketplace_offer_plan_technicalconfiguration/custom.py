# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.util import sdk_no_wait
from knack.util import CLIError

# API Operations
# pylint: disable=too-many-locals

def get_technicalconfiguration(client, offer_id, plan_id):
   client.get(offer_id, plan_id)


def update_technicalconfiguration(client, offer_id, plan_id):
   pass
