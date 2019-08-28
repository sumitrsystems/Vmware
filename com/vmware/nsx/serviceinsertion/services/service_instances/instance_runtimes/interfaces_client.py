# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.serviceinsertion.services.service_instances.instance_runtimes.interfaces.
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


class Statistics(VapiInterface):
    """
    
    """
    GET_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Statistics.get`.

    """
    GET_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Statistics.get`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.services.service_instances.instance_runtimes.interfaces.statistics'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatisticsStub)


    def get(self,
            service_id,
            service_instance_id,
            instance_runtime_id,
            interface_index,
            source=None,
            ):
        """
        Returns statistics of a specified interface via associated logical
        port. If the logical port is attached to a logical router port, query
        parameter \"source=realtime\" is not supported.

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
        :type  instance_runtime_id: :class:`str`
        :param instance_runtime_id: (required)
        :type  interface_index: :class:`str`
        :param interface_index: (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.RuntimeInterfaceStatistics`
        :return: com.vmware.nsx.model.RuntimeInterfaceStatistics
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
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            'instance_runtime_id': instance_runtime_id,
                            'interface_index': interface_index,
                            'source': source,
                            })
class Status(VapiInterface):
    """
    
    """
    GET_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Status.get`.

    """
    GET_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Status.get`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.serviceinsertion.services.service_instances.instance_runtimes.interfaces.status'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatusStub)


    def get(self,
            service_id,
            service_instance_id,
            instance_runtime_id,
            interface_index,
            source=None,
            ):
        """
        Returns operational status of a specified interface

        :type  service_id: :class:`str`
        :param service_id: (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: (required)
        :type  instance_runtime_id: :class:`str`
        :param instance_runtime_id: (required)
        :type  interface_index: :class:`str`
        :param interface_index: (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.RuntimeInterfaceOperationalStatus`
        :return: com.vmware.nsx.model.RuntimeInterfaceOperationalStatus
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
                            'service_id': service_id,
                            'service_instance_id': service_instance_id,
                            'instance_runtime_id': instance_runtime_id,
                            'interface_index': interface_index,
                            'source': source,
                            })
class _StatisticsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'instance_runtime_id': type.StringType(),
            'interface_index': type.StringType(),
            'source': type.OptionalType(type.StringType()),
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
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes/{instance-runtime-id}/interfaces/{interface_index}/statistics',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
                'instance_runtime_id': 'instance-runtime-id',
                'interface_index': 'interface_index',
            },
            query_parameters={
                'source': 'source',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'RuntimeInterfaceStatistics'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.services.service_instances.instance_runtimes.interfaces.statistics',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'instance_runtime_id': type.StringType(),
            'interface_index': type.StringType(),
            'source': type.OptionalType(type.StringType()),
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
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/serviceinsertion/services/{service-id}/service-instances/{service-instance-id}/instance-runtimes/{instance-runtime-id}/interfaces/{interface_index}/status',
            path_variables={
                'service_id': 'service-id',
                'service_instance_id': 'service-instance-id',
                'instance_runtime_id': 'instance-runtime-id',
                'interface_index': 'interface_index',
            },
            query_parameters={
                'source': 'source',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'RuntimeInterfaceOperationalStatus'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.serviceinsertion.services.service_instances.instance_runtimes.interfaces.status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Statistics': Statistics,
        'Status': Status,
    }

