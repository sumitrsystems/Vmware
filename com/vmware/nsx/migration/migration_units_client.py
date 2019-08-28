# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.migration.migration_units.
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


class AggregateInfo(VapiInterface):
    """
    
    """
    LIST_SELECTION_STATUS_SELECTED = "SELECTED"
    """
    Possible value for ``selectionStatus`` of method :func:`AggregateInfo.list`.

    """
    LIST_SELECTION_STATUS_DESELECTED = "DESELECTED"
    """
    Possible value for ``selectionStatus`` of method :func:`AggregateInfo.list`.

    """
    LIST_SELECTION_STATUS_ALL = "ALL"
    """
    Possible value for ``selectionStatus`` of method :func:`AggregateInfo.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.migration.migration_units.aggregate_info'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _AggregateInfoStub)


    def list(self,
             component_type=None,
             cursor=None,
             group_id=None,
             has_errors=None,
             included_fields=None,
             metadata=None,
             page_size=None,
             selection_status=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Get migration units aggregate-info

        :type  component_type: :class:`str` or ``None``
        :param component_type: Component type based on which migration units to be filtered
            (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  group_id: :class:`str` or ``None``
        :param group_id: Identifier of group based on which migration units to be filtered
            (optional)
        :type  has_errors: :class:`bool` or ``None``
        :param has_errors: Flag to indicate whether to return only migration units with errors
            (optional, default to false)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  metadata: :class:`str` or ``None``
        :param metadata: Metadata about migration unit to filter on (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  selection_status: :class:`str` or ``None``
        :param selection_status: Flag to indicate whether to return only selected, only deselected
            or both type of migration units (optional, default to ALL)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx.model_client.MigrationUnitAggregateInfoListResult`
        :return: com.vmware.nsx.model.MigrationUnitAggregateInfoListResult
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
        return self._invoke('list',
                            {
                            'component_type': component_type,
                            'cursor': cursor,
                            'group_id': group_id,
                            'has_errors': has_errors,
                            'included_fields': included_fields,
                            'metadata': metadata,
                            'page_size': page_size,
                            'selection_status': selection_status,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })
class _AggregateInfoStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'component_type': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'group_id': type.OptionalType(type.StringType()),
            'has_errors': type.OptionalType(type.BooleanType()),
            'included_fields': type.OptionalType(type.StringType()),
            'metadata': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'selection_status': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
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
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/migration/migration-units/aggregate-info',
            path_variables={
            },
            query_parameters={
                'component_type': 'component_type',
                'cursor': 'cursor',
                'group_id': 'group_id',
                'has_errors': 'has_errors',
                'included_fields': 'included_fields',
                'metadata': 'metadata',
                'page_size': 'page_size',
                'selection_status': 'selection_status',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'MigrationUnitAggregateInfoListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.migration.migration_units.aggregate_info',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'AggregateInfo': AggregateInfo,
    }

