# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.sddcs.management_vms.
#---------------------------------------------------------------------------

"""


"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class Dns(VapiInterface):
    """
    
    """
    UPDATE_IP_TYPE_PUBLIC = "public"
    """
    Possible value for ``ipType`` of method :func:`Dns.update`.

    """
    UPDATE_IP_TYPE_PRIVATE = "private"
    """
    Possible value for ``ipType`` of method :func:`Dns.update`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.vmc.orgs.sddcs.management_vms.dns'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DnsStub)


    def update(self,
               org,
               sddc,
               management_vm_id,
               ip_type,
               ):
        """
        Update the DNS records of management VMs to use public or private IP
        addresses

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  management_vm_id: :class:`str`
        :param management_vm_id: the management VM ID (required)
        :type  ip_type: :class:`str`
        :param ip_type: the ip type to associate with FQDN in DNS (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
            The sddc is not in a state that's valid for updates or invalid body
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        """
        return self._invoke('update',
                            {
                            'org': org,
                            'sddc': sddc,
                            'management_vm_id': management_vm_id,
                            'ip_type': ip_type,
                            })
class _DnsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'management_vm_id': type.StringType(),
            'ip_type': type.StringType(),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/management-vms/{managementVmId}/dns/{ipType}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'management_vm_id': 'managementVmId',
                'ip_type': 'ipType',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.management_vms.dns',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Dns': Dns,
    }

