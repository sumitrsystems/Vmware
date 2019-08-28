# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.transport_nodes.
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


class PnicBondStatus(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transport_nodes.pnic_bond_status'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PnicBondStatusStub)


    def list(self,
             node_id,
             ):
        """
        Get high-level summary of a transport node

        :type  node_id: :class:`str`
        :param node_id: ID of transport node (required)
        :rtype: :class:`com.vmware.nsx.model_client.PnicBondStatusListResult`
        :return: com.vmware.nsx.model.PnicBondStatusListResult
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
                            'node_id': node_id,
                            })
class RemoteTransportNodeStatus(VapiInterface):
    """
    
    """
    LIST_BFD_DIAGNOSTIC_CODE_0 = "0"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_NO_DIAGNOSTIC = "NO_DIAGNOSTIC"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_1 = "1"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_CONTROL_DETECTION_TIME_EXPIRED = "CONTROL_DETECTION_TIME_EXPIRED"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_2 = "2"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_ECHO_FUNCTION_FAILED = "ECHO_FUNCTION_FAILED"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_3 = "3"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_NEIGHBOR_SIGNALED_SESSION_DOWN = "NEIGHBOR_SIGNALED_SESSION_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_4 = "4"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_FORWARDING_PLANE_RESET = "FORWARDING_PLANE_RESET"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_5 = "5"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_PATH_DOWN = "PATH_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_6 = "6"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_CONCATENATED_PATH_DOWN = "CONCATENATED_PATH_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_7 = "7"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_ADMINISTRATIVELY_DOWN = "ADMINISTRATIVELY_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_8 = "8"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_REVERSE_CONCATENATED_PATH_DOWN = "REVERSE_CONCATENATED_PATH_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_TUNNEL_STATUS_UP = "UP"
    """
    Possible value for ``tunnelStatus`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """
    LIST_TUNNEL_STATUS_DOWN = "DOWN"
    """
    Possible value for ``tunnelStatus`` of method
    :func:`RemoteTransportNodeStatus.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transport_nodes.remote_transport_node_status'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RemoteTransportNodeStatusStub)


    def list(self,
             node_id,
             bfd_diagnostic_code=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             source=None,
             tunnel_status=None,
             ):
        """
        Read status of all transport nodes with tunnel connections to transport
        node

        :type  node_id: :class:`str`
        :param node_id: ID of transport node (required)
        :type  bfd_diagnostic_code: :class:`str` or ``None``
        :param bfd_diagnostic_code: BFD diagnostic code of Tunnel as defined in RFC 5880 (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :type  tunnel_status: :class:`str` or ``None``
        :param tunnel_status: Tunnel Status (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeStatusListResult`
        :return: com.vmware.nsx.model.TransportNodeStatusListResult
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
                            'node_id': node_id,
                            'bfd_diagnostic_code': bfd_diagnostic_code,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'source': source,
                            'tunnel_status': tunnel_status,
                            })
class State(VapiInterface):
    """
    
    """
    LIST_MM_STATE_ENTERING = "ENTERING"
    """
    Possible value for ``mmState`` of method :func:`State.list`.

    """
    LIST_MM_STATE_ENABLED = "ENABLED"
    """
    Possible value for ``mmState`` of method :func:`State.list`.

    """
    LIST_MM_STATE_EXITING = "EXITING"
    """
    Possible value for ``mmState`` of method :func:`State.list`.

    """
    LIST_MM_STATE_DISABLED = "DISABLED"
    """
    Possible value for ``mmState`` of method :func:`State.list`.

    """
    LIST_STATUS_PENDING = "PENDING"
    """
    Possible value for ``status`` of method :func:`State.list`.

    """
    LIST_STATUS_IN_PROGRESS = "IN_PROGRESS"
    """
    Possible value for ``status`` of method :func:`State.list`.

    """
    LIST_STATUS_SUCCESS = "SUCCESS"
    """
    Possible value for ``status`` of method :func:`State.list`.

    """
    LIST_STATUS_PARTIAL_SUCCESS = "PARTIAL_SUCCESS"
    """
    Possible value for ``status`` of method :func:`State.list`.

    """
    LIST_STATUS_FAILED = "FAILED"
    """
    Possible value for ``status`` of method :func:`State.list`.

    """
    LIST_STATUS_ORPHANED = "ORPHANED"
    """
    Possible value for ``status`` of method :func:`State.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transport_nodes.state'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StateStub)


    def get(self,
            transportnode_id,
            ):
        """
        Returns information about the current state of the transport node
        configuration and information about the associated hostswitch.

        :type  transportnode_id: :class:`str`
        :param transportnode_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeState`
        :return: com.vmware.nsx.model.TransportNodeState
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
                            'transportnode_id': transportnode_id,
                            })

    def list(self,
             mm_state=None,
             status=None,
             vtep_ip=None,
             ):
        """
        Returns a list of transport node states that have realized state as
        provided as query parameter

        :type  mm_state: :class:`str` or ``None``
        :param mm_state: maintenance mode state (optional)
        :type  status: :class:`str` or ``None``
        :param status: Realized state of transport nodes (optional)
        :type  vtep_ip: :class:`str` or ``None``
        :param vtep_ip: Virtual tunnel endpoint ip address of transport node (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeStateListResult`
        :return: com.vmware.nsx.model.TransportNodeStateListResult
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
                            'mm_state': mm_state,
                            'status': status,
                            'vtep_ip': vtep_ip,
                            })
class Status(VapiInterface):
    """
    
    """
    GET_0_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Status.get_0`.

    """
    GET_0_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Status.get_0`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transport_nodes.status'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatusStub)


    def get(self):
        """
        Get high-level summary of all transport nodes. The service layer does
        not support source = realtime or cached.


        :rtype: :class:`com.vmware.nsx.model_client.HeatMapTransportZoneStatus`
        :return: com.vmware.nsx.model.HeatMapTransportZoneStatus
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
        return self._invoke('get', None)

    def get_0(self,
              node_id,
              source=None,
              ):
        """
        Read status of a transport node

        :type  node_id: :class:`str`
        :param node_id: ID of transport node (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TransportNodeStatus`
        :return: com.vmware.nsx.model.TransportNodeStatus
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
        return self._invoke('get_0',
                            {
                            'node_id': node_id,
                            'source': source,
                            })
class Tunnels(VapiInterface):
    """
    
    """
    GET_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Tunnels.get`.

    """
    GET_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Tunnels.get`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_0 = "0"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_NO_DIAGNOSTIC = "NO_DIAGNOSTIC"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_1 = "1"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_CONTROL_DETECTION_TIME_EXPIRED = "CONTROL_DETECTION_TIME_EXPIRED"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_2 = "2"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_ECHO_FUNCTION_FAILED = "ECHO_FUNCTION_FAILED"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_3 = "3"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_NEIGHBOR_SIGNALED_SESSION_DOWN = "NEIGHBOR_SIGNALED_SESSION_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_4 = "4"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_FORWARDING_PLANE_RESET = "FORWARDING_PLANE_RESET"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_5 = "5"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_PATH_DOWN = "PATH_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_6 = "6"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_CONCATENATED_PATH_DOWN = "CONCATENATED_PATH_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_7 = "7"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_ADMINISTRATIVELY_DOWN = "ADMINISTRATIVELY_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_8 = "8"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_BFD_DIAGNOSTIC_CODE_REVERSE_CONCATENATED_PATH_DOWN = "REVERSE_CONCATENATED_PATH_DOWN"
    """
    Possible value for ``bfdDiagnosticCode`` of method :func:`Tunnels.list`.

    """
    LIST_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Tunnels.list`.

    """
    LIST_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Tunnels.list`.

    """
    LIST_STATUS_UP = "UP"
    """
    Possible value for ``status`` of method :func:`Tunnels.list`.

    """
    LIST_STATUS_DOWN = "DOWN"
    """
    Possible value for ``status`` of method :func:`Tunnels.list`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.transport_nodes.tunnels'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TunnelsStub)


    def get(self,
            node_id,
            tunnel_name,
            source=None,
            ):
        """
        Tunnel properties

        :type  node_id: :class:`str`
        :param node_id: ID of transport node (required)
        :type  tunnel_name: :class:`str`
        :param tunnel_name: Tunnel name (required)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TunnelProperties`
        :return: com.vmware.nsx.model.TunnelProperties
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
                            'node_id': node_id,
                            'tunnel_name': tunnel_name,
                            'source': source,
                            })

    def list(self,
             node_id,
             bfd_diagnostic_code=None,
             cursor=None,
             included_fields=None,
             page_size=None,
             remote_node_id=None,
             sort_ascending=None,
             sort_by=None,
             source=None,
             status=None,
             ):
        """
        List of tunnels

        :type  node_id: :class:`str`
        :param node_id: ID of transport node (required)
        :type  bfd_diagnostic_code: :class:`str` or ``None``
        :param bfd_diagnostic_code: BFD diagnostic code of Tunnel as defined in RFC 5880 (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  remote_node_id: :class:`str` or ``None``
        :param remote_node_id: (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :type  status: :class:`str` or ``None``
        :param status: Tunnel status (optional)
        :rtype: :class:`com.vmware.nsx.model_client.TunnelList`
        :return: com.vmware.nsx.model.TunnelList
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
                            'node_id': node_id,
                            'bfd_diagnostic_code': bfd_diagnostic_code,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'remote_node_id': remote_node_id,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'source': source,
                            'status': status,
                            })
class _PnicBondStatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
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
            url_template='/api/v1/transport-nodes/{node-id}/pnic-bond-status',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'PnicBondStatusListResult'),
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
            self, iface_name='com.vmware.nsx.transport_nodes.pnic_bond_status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _RemoteTransportNodeStatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'bfd_diagnostic_code': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'source': type.OptionalType(type.StringType()),
            'tunnel_status': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/transport-nodes/{node-id}/remote-transport-node-status',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
                'bfd_diagnostic_code': 'bfd_diagnostic_code',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'source': 'source',
                'tunnel_status': 'tunnel_status',
            },
            content_type='application/json'
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeStatusListResult'),
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
            self, iface_name='com.vmware.nsx.transport_nodes.remote_transport_node_status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StateStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'transportnode_id': type.StringType(),
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
            url_template='/api/v1/transport-nodes/{transportnode-id}/state',
            path_variables={
                'transportnode_id': 'transportnode-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'mm_state': type.OptionalType(type.StringType()),
            'status': type.OptionalType(type.StringType()),
            'vtep_ip': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/transport-nodes/state',
            path_variables={
            },
            query_parameters={
                'mm_state': 'mm_state',
                'status': 'status',
                'vtep_ip': 'vtep_ip',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeState'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeStateListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.transport_nodes.state',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
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
            url_template='/api/v1/transport-nodes/status',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'source': type.OptionalType(type.StringType()),
        })
        get_0_error_dict = {
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
        get_0_input_value_validator_list = [
        ]
        get_0_output_validator_list = [
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/api/v1/transport-nodes/{node-id}/status',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
                'source': 'source',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'HeatMapTransportZoneStatus'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TransportNodeStatus'),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.transport_nodes.status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TunnelsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'tunnel_name': type.StringType(),
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
            url_template='/api/v1/transport-nodes/{node-id}/tunnels/{tunnel-name}',
            path_variables={
                'node_id': 'node-id',
                'tunnel_name': 'tunnel-name',
            },
            query_parameters={
                'source': 'source',
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
            'bfd_diagnostic_code': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'remote_node_id': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'source': type.OptionalType(type.StringType()),
            'status': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/transport-nodes/{node-id}/tunnels',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
                'bfd_diagnostic_code': 'bfd_diagnostic_code',
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'remote_node_id': 'remote_node_id',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'source': 'source',
                'status': 'status',
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TunnelProperties'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TunnelList'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.transport_nodes.tunnels',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'PnicBondStatus': PnicBondStatus,
        'RemoteTransportNodeStatus': RemoteTransportNodeStatus,
        'State': State,
        'Status': Status,
        'Tunnels': Tunnels,
        'statistics': 'com.vmware.nsx.transport_nodes.statistics_client.StubFactory',
    }

