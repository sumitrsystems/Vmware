# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.
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


class Infra(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx_policy.infra'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InfraStub)


    def get(self,
            filter=None,
            ):
        """
        Read infra. Returns only the infra related properties. Inner object are
        not populated.

        :type  filter: :class:`str` or ``None``
        :param filter: Filter string as java regex (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.Infra`
        :return: com.vmware.nsx_policy.model.Infra
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'filter': filter,
                            })

    def patch(self,
              infra,
              ):
        """
        Update the infra including all the nested entities

        :type  infra: :class:`com.vmware.nsx_policy.model_client.Infra`
        :param infra: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('patch',
                            {
                            'infra': infra,
                            })

    def update(self,
               infra,
               ):
        """
        Update the infra including all the nested entities

        :type  infra: :class:`com.vmware.nsx_policy.model_client.Infra`
        :param infra: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.Infra`
        :return: com.vmware.nsx_policy.model.Infra
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('update',
                            {
                            'infra': infra,
                            })
class _InfraStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra',
            path_variables={
            },
            query_parameters={
                'filter': 'filter',
            },
            content_type='application/json'
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'infra': type.ReferenceType('com.vmware.nsx_policy.model_client', 'Infra'),
        })
        patch_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        patch_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra',
            request_body_parameter='infra',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'infra': type.ReferenceType('com.vmware.nsx_policy.model_client', 'Infra'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        update_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/infra',
            request_body_parameter='infra',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'Infra'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'Infra'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Infra': Infra,
        'infra': 'com.vmware.nsx_policy.infra_client.StubFactory',
        'model': 'com.vmware.nsx_policy.model_client.StubFactory',
    }

