# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_vmc_app.model.
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


class AdvertisedRoute(VapiStruct):
    """
    Advertised BGP route

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    ADVERTISEMENT_STATE_SUCCESS = "SUCCESS"
    """


    """
    ADVERTISEMENT_STATE_FAILED = "FAILED"
    """


    """



    _canonical_to_pep_names = {
                            'advertisement_state': 'advertisement_state',
                            'ipv4_cidr': 'ipv4_cidr',
                            }

    def __init__(self,
                 advertisement_state=None,
                 ipv4_cidr=None,
                ):
        """
        :type  advertisement_state: :class:`str`
        :param advertisement_state: Possible values are: 
            
            * :attr:`AdvertisedRoute.ADVERTISEMENT_STATE_SUCCESS`
            * :attr:`AdvertisedRoute.ADVERTISEMENT_STATE_FAILED`
            
             State of advertisement
        :type  ipv4_cidr: :class:`str`
        :param ipv4_cidr: The route that is advertised to on-premise datacenter via Direct
            Connect format: ipv4-cidr-block
        """
        self.advertisement_state = advertisement_state
        self.ipv4_cidr = ipv4_cidr
        VapiStruct.__init__(self)


AdvertisedRoute._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.advertised_route', {
        'advertisement_state': type.StringType(),
        'ipv4_cidr': type.StringType(),
    },
    AdvertisedRoute,
    False,
    None))



class ApiError(VapiStruct):
    """
    Detailed information about an API Error

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'details': 'details',
                            'error_code': 'error_code',
                            'error_data': 'error_data',
                            'error_message': 'error_message',
                            'module_name': 'module_name',
                            'related_errors': 'related_errors',
                            }

    def __init__(self,
                 details=None,
                 error_code=None,
                 error_data=None,
                 error_message=None,
                 module_name=None,
                 related_errors=None,
                ):
        """
        :type  details: :class:`str` or ``None``
        :param details: Further details about the error
        :type  error_code: :class:`long` or ``None``
        :param error_code: A numeric error code format: int64
        :type  error_data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param error_data: Additional data about the error
        :type  error_message: :class:`str` or ``None``
        :param error_message: A description of the error
        :type  module_name: :class:`str` or ``None``
        :param module_name: The module name where the error occurred
        :type  related_errors: :class:`list` of :class:`RelatedApiError` or ``None``
        :param related_errors: Other errors related to this error
        """
        self.details = details
        self.error_code = error_code
        self.error_data = error_data
        self.error_message = error_message
        self.module_name = module_name
        self.related_errors = related_errors
        VapiStruct.__init__(self)


ApiError._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.api_error', {
        'details': type.OptionalType(type.StringType()),
        'error_code': type.OptionalType(type.IntegerType()),
        'error_data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'error_message': type.OptionalType(type.StringType()),
        'module_name': type.OptionalType(type.StringType()),
        'related_errors': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'RelatedApiError'))),
    },
    ApiError,
    False,
    None))



class BGPAdvertisedRoutes(VapiStruct):
    """
    Advertised bgp routes

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'advertised_routes': 'advertised_routes',
                            'failed_advertised_routes': 'failed_advertised_routes',
                            }

    def __init__(self,
                 advertised_routes=None,
                 failed_advertised_routes=None,
                ):
        """
        :type  advertised_routes: :class:`list` of :class:`AdvertisedRoute` or ``None``
        :param advertised_routes: Routes advertised to on-premise datacenter via Direct Connect
        :type  failed_advertised_routes: :class:`long` or ``None``
        :param failed_advertised_routes: Number of routes failed to advertise format: int32
        """
        self.advertised_routes = advertised_routes
        self.failed_advertised_routes = failed_advertised_routes
        VapiStruct.__init__(self)


BGPAdvertisedRoutes._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.BGP_advertised_routes', {
        'advertised_routes': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'AdvertisedRoute'))),
        'failed_advertised_routes': type.OptionalType(type.IntegerType()),
    },
    BGPAdvertisedRoutes,
    False,
    None))



class BGPLearnedRoutes(VapiStruct):
    """
    Learned bgp routes

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'ipv4_cidr': 'ipv4_cidr',
                            }

    def __init__(self,
                 ipv4_cidr=None,
                ):
        """
        :type  ipv4_cidr: :class:`list` of :class:`str` or ``None``
        :param ipv4_cidr: The route that is learned from BGP via Direct Connect format:
            ipv4-cidr-block
        """
        self.ipv4_cidr = ipv4_cidr
        VapiStruct.__init__(self)


BGPLearnedRoutes._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.BGP_learned_routes', {
        'ipv4_cidr': type.OptionalType(type.ListType(type.StringType())),
    },
    BGPLearnedRoutes,
    False,
    None))



class ConnectedServiceListResult(VapiStruct):
    """
    A list of status of 'Enabled/Disabled' for a service connected to a linked
    vpc

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`ConnectedServiceStatus`
        :param results: Connected service status list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


ConnectedServiceListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.connected_service_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.ListType(type.ReferenceType(__name__, 'ConnectedServiceStatus')),
    },
    ConnectedServiceListResult,
    False,
    None))



class ConnectedServiceStatus(VapiStruct):
    """
    Status of 'Enabled/Disabled' for a service connected to a linked vpc

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'enabled': 'enabled',
                            'name': 'name',
                            }

    def __init__(self,
                 enabled=None,
                 name=None,
                ):
        """
        :type  enabled: :class:`bool` or ``None``
        :param enabled: status of service
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  name: :class:`str` or ``None``
        :param name: service name
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.enabled = enabled
        self.name = name
        VapiStruct.__init__(self)


ConnectedServiceStatus._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.connected_service_status', {
        'enabled': type.OptionalType(type.BooleanType()),
        'name': type.OptionalType(type.StringType()),
    },
    ConnectedServiceStatus,
    False,
    None))



class DirectConnectBgpInfo(VapiStruct):
    """
    Direct Connect BGP related information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    ROUTE_PREFERENCE_DX_PREFERED_OVER_VPN = "DX_PREFERED_OVER_VPN"
    """


    """
    ROUTE_PREFERENCE_VPN_PREFERED_OVER_DX = "VPN_PREFERED_OVER_DX"
    """


    """



    _canonical_to_pep_names = {
                            'local_as_num': 'local_as_num',
                            'mtu': 'mtu',
                            'route_preference': 'route_preference',
                            }

    def __init__(self,
                 local_as_num=None,
                 mtu=None,
                 route_preference=None,
                ):
        """
        :type  local_as_num: :class:`str` or ``None``
        :param local_as_num: The ASN paired with the VGW attached to the VPC. AWS allowed
            private BGP ASN range - [64512, 65534] and [4200000000,
            4294967294]. If omitted in the payload, BGP ASN will not be
            modified.
        :type  mtu: :class:`long` or ``None``
        :param mtu: Maximum transmission unit allowed by the VIF format: int32
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  route_preference: :class:`str` or ``None``
        :param route_preference: Possible values are: 
            
            *
              :attr:`DirectConnectBgpInfo.ROUTE_PREFERENCE_DX_PREFERED_OVER_VPN`
            *
              :attr:`DirectConnectBgpInfo.ROUTE_PREFERENCE_VPN_PREFERED_OVER_DX`
            
            Direct connect route preference over VPN routes. If omitted in the
            payload, route preference will not be modified.
        """
        self.local_as_num = local_as_num
        self.mtu = mtu
        self.route_preference = route_preference
        VapiStruct.__init__(self)


DirectConnectBgpInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.direct_connect_bgp_info', {
        'local_as_num': type.OptionalType(type.StringType()),
        'mtu': type.OptionalType(type.IntegerType()),
        'route_preference': type.OptionalType(type.StringType()),
    },
    DirectConnectBgpInfo,
    False,
    None))



class DiscoveredResource(VapiStruct):
    """
    Base class for resources that are discovered and automatically updated

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            '_last_sync_time': 'last_sync_time',
                            'description': 'description',
                            'display_name': 'display_name',
                            'resource_type': 'resource_type',
                            'tags': 'tags',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 last_sync_time=None,
                 description=None,
                 display_name=None,
                 resource_type=None,
                 tags=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  last_sync_time: :class:`long` or ``None``
        :param last_sync_time: Timestamp of last modification format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  description: :class:`str` or ``None``
        :param description: Description of this resource
        :type  display_name: :class:`str` or ``None``
        :param display_name: Defaults to ID if not set
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: The type of this resource.
        :type  tags: :class:`list` of :class:`Tag` or ``None``
        :param tags: Opaque identifiers meaningful to the API user
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.last_sync_time = last_sync_time
        self.description = description
        self.display_name = display_name
        self.resource_type = resource_type
        self.tags = tags
        VapiStruct.__init__(self)


DiscoveredResource._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.discovered_resource', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        '_last_sync_time': type.OptionalType(type.IntegerType()),
        'description': type.OptionalType(type.StringType()),
        'display_name': type.OptionalType(type.StringType()),
        'resource_type': type.OptionalType(type.StringType()),
        'tags': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Tag'))),
    },
    DiscoveredResource,
    False,
    None))



class EmbeddedResource(VapiStruct):
    """
    Base class for resources that are embedded in other resources

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            '_revision': 'revision',
                            '_owner': 'owner',
                            'description': 'description',
                            'display_name': 'display_name',
                            'id': 'id',
                            'resource_type': 'resource_type',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 revision=None,
                 owner=None,
                 description=None,
                 display_name=None,
                 id=None,
                 resource_type=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  revision: :class:`long` or ``None``
        :param revision: The _revision property describes the current revision of the
            resource. To prevent clients from overwriting each other's changes,
            PUT operations must include the current _revision of the resource,
            which clients should obtain by issuing a GET operation. If the
            _revision provided in a PUT request is missing or stale, the
            operation will be rejected. format: int32
        :type  owner: :class:`OwnerResourceLink` or ``None``
        :param owner: Owner of this resource
        :type  description: :class:`str` or ``None``
        :param description: Description of this resource
        :type  display_name: :class:`str` or ``None``
        :param display_name: Defaults to ID if not set
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: The type of this resource.
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.revision = revision
        self.owner = owner
        self.description = description
        self.display_name = display_name
        self.id = id
        self.resource_type = resource_type
        VapiStruct.__init__(self)


EmbeddedResource._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.embedded_resource', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        '_revision': type.OptionalType(type.IntegerType()),
        '_owner': type.OptionalType(type.ReferenceType(__name__, 'OwnerResourceLink')),
        'description': type.OptionalType(type.StringType()),
        'display_name': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'resource_type': type.OptionalType(type.StringType()),
    },
    EmbeddedResource,
    False,
    None))



class HostEni(VapiStruct):
    """
    Host elastic network interface (ENI)

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'associated_public_ips': 'associated_public_ips',
                            'description': 'description',
                            'interface_id': 'interface_id',
                            'interface_mac': 'interface_mac',
                            'primary_ip': 'primary_ip',
                            'subnet_id': 'subnet_id',
                            'vdr_type': 'vdr_type',
                            }

    def __init__(self,
                 associated_public_ips=None,
                 description=None,
                 interface_id=None,
                 interface_mac=None,
                 primary_ip=None,
                 subnet_id=None,
                 vdr_type=None,
                ):
        """
        :type  associated_public_ips: :class:`list` of :class:`str` or ``None``
        :param associated_public_ips: List of associated public IPs. format: ipv4
        :type  description: :class:`str` or ``None``
        :param description: Description
        :type  interface_id: :class:`str` or ``None``
        :param interface_id: Interface id
        :type  interface_mac: :class:`str` or ``None``
        :param interface_mac: Interface mac
        :type  primary_ip: :class:`str` or ``None``
        :param primary_ip: Primary IP format: ipv4
        :type  subnet_id: :class:`str` or ``None``
        :param subnet_id: Subnet ID
        :type  vdr_type: :class:`str` or ``None``
        :param vdr_type: Virtual distributed router (VDR) type
        """
        self.associated_public_ips = associated_public_ips
        self.description = description
        self.interface_id = interface_id
        self.interface_mac = interface_mac
        self.primary_ip = primary_ip
        self.subnet_id = subnet_id
        self.vdr_type = vdr_type
        VapiStruct.__init__(self)


HostEni._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.host_eni', {
        'associated_public_ips': type.OptionalType(type.ListType(type.StringType())),
        'description': type.OptionalType(type.StringType()),
        'interface_id': type.OptionalType(type.StringType()),
        'interface_mac': type.OptionalType(type.StringType()),
        'primary_ip': type.OptionalType(type.StringType()),
        'subnet_id': type.OptionalType(type.StringType()),
        'vdr_type': type.OptionalType(type.StringType()),
    },
    HostEni,
    False,
    None))



class HostStatus(VapiStruct):
    """
    Host status

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    VMCD_STATUS_GREEN = "GREEN"
    """


    """
    VMCD_STATUS_RED = "RED"
    """


    """
    VMCD_STATUS_UNKNOWN = "UNKNOWN"
    """


    """



    _canonical_to_pep_names = {
                            'eni': 'eni',
                            'host_id': 'host_id',
                            'host_ip': 'host_ip',
                            'issues': 'issues',
                            'vdr': 'vdr',
                            'vmcd_status': 'vmcd_status',
                            }

    def __init__(self,
                 eni=None,
                 host_id=None,
                 host_ip=None,
                 issues=None,
                 vdr=None,
                 vmcd_status=None,
                ):
        """
        :type  eni: :class:`list` of :class:`HostEni` or ``None``
        :param eni: List of ENIs
        :type  host_id: :class:`str` or ``None``
        :param host_id: Host UUID
        :type  host_ip: :class:`str` or ``None``
        :param host_ip: Host ip format: ipv4
        :type  issues: :class:`list` of :class:`str` or ``None``
        :param issues: issues with the host
        :type  vdr: :class:`list` of :class:`HostVdr` or ``None``
        :param vdr: List of VDRs
        :type  vmcd_status: :class:`str` or ``None``
        :param vmcd_status: Possible values are: 
            
            * :attr:`HostStatus.VMCD_STATUS_GREEN`
            * :attr:`HostStatus.VMCD_STATUS_RED`
            * :attr:`HostStatus.VMCD_STATUS_UNKNOWN`
            
             Status of vmcd, a service running on host
        """
        self.eni = eni
        self.host_id = host_id
        self.host_ip = host_ip
        self.issues = issues
        self.vdr = vdr
        self.vmcd_status = vmcd_status
        VapiStruct.__init__(self)


HostStatus._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.host_status', {
        'eni': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'HostEni'))),
        'host_id': type.OptionalType(type.StringType()),
        'host_ip': type.OptionalType(type.StringType()),
        'issues': type.OptionalType(type.ListType(type.StringType())),
        'vdr': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'HostVdr'))),
        'vmcd_status': type.OptionalType(type.StringType()),
    },
    HostStatus,
    False,
    None))



class HostStatusListResult(VapiStruct):
    """
    Host status list result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`HostStatus`
        :param results: Connected service status list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


HostStatusListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.host_status_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.ListType(type.ReferenceType(__name__, 'HostStatus')),
    },
    HostStatusListResult,
    False,
    None))



class HostVdr(VapiStruct):
    """
    Host virtual distributed router (VDR)

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'lifs': 'lifs',
                            'routes': 'routes',
                            'type': 'type',
                            }

    def __init__(self,
                 lifs=None,
                 routes=None,
                 type=None,
                ):
        """
        :type  lifs: :class:`list` of :class:`VdrLif` or ``None``
        :param lifs: List of VDR lifs
        :type  routes: :class:`list` of :class:`VdrRoute` or ``None``
        :param routes: List of VDR routes
        :type  type: :class:`str` or ``None``
        :param type: VDR type
        """
        self.lifs = lifs
        self.routes = routes
        self.type = type
        VapiStruct.__init__(self)


HostVdr._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.host_vdr', {
        'lifs': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VdrLif'))),
        'routes': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VdrRoute'))),
        'type': type.OptionalType(type.StringType()),
    },
    HostVdr,
    False,
    None))



class InterfaceStatistics(VapiStruct):
    """
    Statistics for a network interface

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'rx_bytes': 'rx_bytes',
                            'rx_errors': 'rx_errors',
                            'rx_packets': 'rx_packets',
                            'tx_bytes': 'tx_bytes',
                            'tx_errors': 'tx_errors',
                            'tx_packets': 'tx_packets',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 rx_bytes=None,
                 rx_errors=None,
                 rx_packets=None,
                 tx_bytes=None,
                 tx_errors=None,
                 tx_packets=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  rx_bytes: :class:`long` or ``None``
        :param rx_bytes: Count of bytes received on this port format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  rx_errors: :class:`long` or ``None``
        :param rx_errors: Count of receive errors occurring on this port format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  rx_packets: :class:`long` or ``None``
        :param rx_packets: Count of packets received on this port format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  tx_bytes: :class:`long` or ``None``
        :param tx_bytes: Count of bytes transmitted on this port format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  tx_errors: :class:`long` or ``None``
        :param tx_errors: Count of transmit errors occurring on this port format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  tx_packets: :class:`long` or ``None``
        :param tx_packets: Count of packets transmitted on this port format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.rx_bytes = rx_bytes
        self.rx_errors = rx_errors
        self.rx_packets = rx_packets
        self.tx_bytes = tx_bytes
        self.tx_errors = tx_errors
        self.tx_packets = tx_packets
        VapiStruct.__init__(self)


InterfaceStatistics._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.interface_statistics', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'rx_bytes': type.OptionalType(type.IntegerType()),
        'rx_errors': type.OptionalType(type.IntegerType()),
        'rx_packets': type.OptionalType(type.IntegerType()),
        'tx_bytes': type.OptionalType(type.IntegerType()),
        'tx_errors': type.OptionalType(type.IntegerType()),
        'tx_packets': type.OptionalType(type.IntegerType()),
    },
    InterfaceStatistics,
    False,
    None))



class IpAttachmentPair(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'attachment_id': 'attachment_id',
                            'ip': 'ip',
                            }

    def __init__(self,
                 attachment_id=None,
                 ip=None,
                ):
        """
        :type  attachment_id: :class:`str`
        :param attachment_id: Attachment id which maps to management VM IP
        :type  ip: :class:`str`
        :param ip: Management VM IP Address format: ipv4
        """
        self.attachment_id = attachment_id
        self.ip = ip
        VapiStruct.__init__(self)


IpAttachmentPair._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.ip_attachment_pair', {
        'attachment_id': type.StringType(),
        'ip': type.StringType(),
    },
    IpAttachmentPair,
    False,
    None))



class LinkedSubnetInfo(VapiStruct):
    """
    Infromation related to a subnet where linked ENIs were created.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'availability_zone': 'availability_zone',
                            'cidr': 'cidr',
                            'id': 'id',
                            }

    def __init__(self,
                 availability_zone=None,
                 cidr=None,
                 id=None,
                ):
        """
        :type  availability_zone: :class:`str`
        :param availability_zone: Linked subnet availability zone
        :type  cidr: :class:`str`
        :param cidr: Linked subnet CIDR format: ipv4-cidr-block
        :type  id: :class:`str`
        :param id: Linked subnet identifier
        """
        self.availability_zone = availability_zone
        self.cidr = cidr
        self.id = id
        VapiStruct.__init__(self)


LinkedSubnetInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.linked_subnet_info', {
        'availability_zone': type.StringType(),
        'cidr': type.StringType(),
        'id': type.StringType(),
    },
    LinkedSubnetInfo,
    False,
    None))



class LinkedVpcInfo(VapiStruct):
    """
    Linked VPC info

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'active_eni': 'active_eni',
                            'arn_role': 'arn_role',
                            'external_id': 'external_id',
                            'linked_account': 'linked_account',
                            'linked_vpc_addresses': 'linked_vpc_addresses',
                            'linked_vpc_id': 'linked_vpc_id',
                            'linked_vpc_nat_ips': 'linked_vpc_nat_ips',
                            'linked_vpc_subnets': 'linked_vpc_subnets',
                            'route_table_ids': 'route_table_ids',
                            'service_arn_role': 'service_arn_role',
                            }

    def __init__(self,
                 active_eni=None,
                 arn_role=None,
                 external_id=None,
                 linked_account=None,
                 linked_vpc_addresses=None,
                 linked_vpc_id=None,
                 linked_vpc_nat_ips=None,
                 linked_vpc_subnets=None,
                 route_table_ids=None,
                 service_arn_role=None,
                ):
        """
        :type  active_eni: :class:`str` or ``None``
        :param active_eni: Active network interface used for linked vpc traffic
        :type  arn_role: :class:`str`
        :param arn_role: ARN role for linked VPC operations
        :type  external_id: :class:`str`
        :param external_id: External identifier for ARN role
        :type  linked_account: :class:`str`
        :param linked_account: Linked VPC account number
        :type  linked_vpc_addresses: :class:`list` of :class:`str`
        :param linked_vpc_addresses: Linked VPC CIDRs format: ipv4-cidr-block
        :type  linked_vpc_id: :class:`str` or ``None``
        :param linked_vpc_id: Linked VPC identifier
        :type  linked_vpc_nat_ips: :class:`list` of :class:`str`
        :param linked_vpc_nat_ips: The IPs of linked VPC NAT rule for service access. format: ipv4
        :type  linked_vpc_subnets: :class:`list` of :class:`LinkedSubnetInfo`
        :param linked_vpc_subnets: Infromation related to the subnets where linked ENIs were created.
        :type  route_table_ids: :class:`list` of :class:`str`
        :param route_table_ids: The identifiers of route tables to be dynamically updated with SDDC
            networks
        :type  service_arn_role: :class:`str` or ``None``
        :param service_arn_role: service ARN role
        """
        self.active_eni = active_eni
        self.arn_role = arn_role
        self.external_id = external_id
        self.linked_account = linked_account
        self.linked_vpc_addresses = linked_vpc_addresses
        self.linked_vpc_id = linked_vpc_id
        self.linked_vpc_nat_ips = linked_vpc_nat_ips
        self.linked_vpc_subnets = linked_vpc_subnets
        self.route_table_ids = route_table_ids
        self.service_arn_role = service_arn_role
        VapiStruct.__init__(self)


LinkedVpcInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.linked_vpc_info', {
        'active_eni': type.OptionalType(type.StringType()),
        'arn_role': type.StringType(),
        'external_id': type.StringType(),
        'linked_account': type.StringType(),
        'linked_vpc_addresses': type.ListType(type.StringType()),
        'linked_vpc_id': type.OptionalType(type.StringType()),
        'linked_vpc_nat_ips': type.ListType(type.StringType()),
        'linked_vpc_subnets': type.ListType(type.ReferenceType(__name__, 'LinkedSubnetInfo')),
        'route_table_ids': type.ListType(type.StringType()),
        'service_arn_role': type.OptionalType(type.StringType()),
    },
    LinkedVpcInfo,
    False,
    None))



class LinkedVpcsListResult(VapiStruct):
    """
    Linked VPC list query result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`LinkedVpcInfo` or ``None``
        :param results: Linked VPCs list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


LinkedVpcsListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.linked_vpcs_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'LinkedVpcInfo'))),
    },
    LinkedVpcsListResult,
    False,
    None))



class ListResult(VapiStruct):
    """
    Base class for list results from collections

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        VapiStruct.__init__(self)


ListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
    },
    ListResult,
    False,
    None))



class ManagedResource(VapiStruct):
    """
    Base type for resources that are managed by API clients

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            '_revision': 'revision',
                            '_create_time': 'create_time',
                            '_create_user': 'create_user',
                            '_last_modified_time': 'last_modified_time',
                            '_last_modified_user': 'last_modified_user',
                            '_protection': 'protection',
                            '_system_owned': 'system_owned',
                            'description': 'description',
                            'display_name': 'display_name',
                            'id': 'id',
                            'resource_type': 'resource_type',
                            'tags': 'tags',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 revision=None,
                 create_time=None,
                 create_user=None,
                 last_modified_time=None,
                 last_modified_user=None,
                 protection=None,
                 system_owned=None,
                 description=None,
                 display_name=None,
                 id=None,
                 resource_type=None,
                 tags=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  revision: :class:`long` or ``None``
        :param revision: The _revision property describes the current revision of the
            resource. To prevent clients from overwriting each other's changes,
            PUT operations must include the current _revision of the resource,
            which clients should obtain by issuing a GET operation. If the
            _revision provided in a PUT request is missing or stale, the
            operation will be rejected. format: int32
        :type  create_time: :class:`long` or ``None``
        :param create_time: Timestamp of resource creation format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  create_user: :class:`str` or ``None``
        :param create_user: ID of the user who created this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  last_modified_time: :class:`long` or ``None``
        :param last_modified_time: Timestamp of last modification format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  last_modified_user: :class:`str` or ``None``
        :param last_modified_user: ID of the user who last modified this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  protection: :class:`str` or ``None``
        :param protection: Protection status is one of the following: PROTECTED - the client
            who retrieved the entity is not allowed to modify it. NOT_PROTECTED
            - the client who retrieved the entity is allowed to modify it
            REQUIRE_OVERRIDE - the client who retrieved the entity is a super
            user and can modify it, but only when providing the request header
            X-Allow-Overwrite=true. UNKNOWN - the _protection field could not
            be determined for this entity.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  system_owned: :class:`bool` or ``None``
        :param system_owned: Indicates system owned resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  description: :class:`str` or ``None``
        :param description: Description of this resource
        :type  display_name: :class:`str` or ``None``
        :param display_name: Defaults to ID if not set
        :type  id: :class:`str` or ``None``
        :param id: Unique identifier of this resource
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: The type of this resource.
        :type  tags: :class:`list` of :class:`Tag` or ``None``
        :param tags: Opaque identifiers meaningful to the API user
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.revision = revision
        self.create_time = create_time
        self.create_user = create_user
        self.last_modified_time = last_modified_time
        self.last_modified_user = last_modified_user
        self.protection = protection
        self.system_owned = system_owned
        self.description = description
        self.display_name = display_name
        self.id = id
        self.resource_type = resource_type
        self.tags = tags
        VapiStruct.__init__(self)


ManagedResource._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.managed_resource', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        '_revision': type.OptionalType(type.IntegerType()),
        '_create_time': type.OptionalType(type.IntegerType()),
        '_create_user': type.OptionalType(type.StringType()),
        '_last_modified_time': type.OptionalType(type.IntegerType()),
        '_last_modified_user': type.OptionalType(type.StringType()),
        '_protection': type.OptionalType(type.StringType()),
        '_system_owned': type.OptionalType(type.BooleanType()),
        'description': type.OptionalType(type.StringType()),
        'display_name': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'resource_type': type.OptionalType(type.StringType()),
        'tags': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Tag'))),
    },
    ManagedResource,
    False,
    None))



class MgmtServiceEntry(VapiStruct):
    """
    A service entry describes the detail of a network service.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'display_name': 'display_name',
                            'path': 'path',
                            }

    def __init__(self,
                 display_name=None,
                 path=None,
                ):
        """
        :type  display_name: :class:`str` or ``None``
        :param display_name: Display name for this service
        :type  path: :class:`str` or ``None``
        :param path: Service path should refer to a valid service in the system. Service
            can be system defined or user defined.
        """
        self.display_name = display_name
        self.path = path
        VapiStruct.__init__(self)


MgmtServiceEntry._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.mgmt_service_entry', {
        'display_name': type.OptionalType(type.StringType()),
        'path': type.OptionalType(type.StringType()),
    },
    MgmtServiceEntry,
    False,
    None))



class MgmtVmInfo(VapiStruct):
    """
    Management VM access information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'display_name': 'display_name',
                            'group_path': 'group_path',
                            'id': 'id',
                            'ip_attachment_pairs': 'ip_attachment_pairs',
                            'ips': 'ips',
                            'services': 'services',
                            }

    def __init__(self,
                 display_name=None,
                 group_path=None,
                 id=None,
                 ip_attachment_pairs=None,
                 ips=None,
                 services=None,
                ):
        """
        :type  display_name: :class:`str` or ``None``
        :param display_name: Management VM name
        :type  group_path: :class:`str` or ``None``
        :param group_path: For each management VM, a dedicated policy group will be created.
            This property will reflect its group path.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  id: :class:`str` or ``None``
        :param id: Management VM identifier
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  ip_attachment_pairs: :class:`list` of :class:`IpAttachmentPair` or ``None``
        :param ip_attachment_pairs: IP address and attachment id pairs for tagging managment VM
        :type  ips: :class:`list` of :class:`str` or ``None``
        :param ips: Local IPs of a management VM format: address-or-block-or-range
        :type  services: :class:`list` of :class:`MgmtServiceEntry` or ``None``
        :param services: Details services path and display name.
        """
        self.display_name = display_name
        self.group_path = group_path
        self.id = id
        self.ip_attachment_pairs = ip_attachment_pairs
        self.ips = ips
        self.services = services
        VapiStruct.__init__(self)


MgmtVmInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.mgmt_vm_info', {
        'display_name': type.OptionalType(type.StringType()),
        'group_path': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'ip_attachment_pairs': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'IpAttachmentPair'))),
        'ips': type.OptionalType(type.ListType(type.StringType())),
        'services': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'MgmtServiceEntry'))),
    },
    MgmtVmInfo,
    False,
    None))



class MgmtVmsListResult(VapiStruct):
    """
    Management VM list query result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`MgmtVmInfo` or ``None``
        :param results: Management VMs list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


MgmtVmsListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.mgmt_vms_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'MgmtVmInfo'))),
    },
    MgmtVmsListResult,
    False,
    None))



class NetworkStatusEntry(VapiStruct):
    """
    Network status entry

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'host_ips': 'host_ips',
                            'ip_address': 'ip_address',
                            'issues': 'issues',
                            'issues_found': 'issues_found',
                            }

    def __init__(self,
                 host_ips=None,
                 ip_address=None,
                 issues=None,
                 issues_found=None,
                ):
        """
        :type  host_ips: :class:`list` of :class:`str` or ``None``
        :param host_ips: IPs of hosts that store this entry format: ipv4
        :type  ip_address: :class:`str` or ``None``
        :param ip_address: IP address programmed with the entry format: ipv4
        :type  issues: :class:`list` of :class:`str` or ``None``
        :param issues: Known issues detected with the entry
        :type  issues_found: :class:`bool` or ``None``
        :param issues_found: Indicate whether issues is a non-empty array
        """
        self.host_ips = host_ips
        self.ip_address = ip_address
        self.issues = issues
        self.issues_found = issues_found
        VapiStruct.__init__(self)


NetworkStatusEntry._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.network_status_entry', {
        'host_ips': type.OptionalType(type.ListType(type.StringType())),
        'ip_address': type.OptionalType(type.StringType()),
        'issues': type.OptionalType(type.ListType(type.StringType())),
        'issues_found': type.OptionalType(type.BooleanType()),
    },
    NetworkStatusEntry,
    False,
    None))



class NetworkStatusKey(VapiStruct):
    """
    Key used to group network status inquiry results.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    CONTEXT_INVALID_NETWORK = "INVALID_NETWORK"
    """


    """
    CONTEXT_MANAGEMENT = "MANAGEMENT"
    """


    """
    CONTEXT_PUBLIC = "PUBLIC"
    """


    """
    CONTEXT_CONNECTED_VPC = "CONNECTED_VPC"
    """


    """
    CONTEXT_DIRECT_CONNECT = "DIRECT_CONNECT"
    """


    """
    NETWORK_TYPE_DNS = "DNS"
    """


    """
    NETWORK_TYPE_VPN = "VPN"
    """


    """
    NETWORK_TYPE_MANAGEMENT = "MANAGEMENT"
    """


    """
    NETWORK_TYPE_NAT = "NAT"
    """


    """
    NETWORK_TYPE_LOGICAL = "LOGICAL"
    """


    """
    NETWORK_TYPE_INFRA = "INFRA"
    """


    """



    _canonical_to_pep_names = {
                            'context': 'context',
                            'network_type': 'network_type',
                            }

    def __init__(self,
                 context=None,
                 network_type=None,
                ):
        """
        :type  context: :class:`str`
        :param context: Possible values are: 
            
            * :attr:`NetworkStatusKey.CONTEXT_INVALID_NETWORK`
            * :attr:`NetworkStatusKey.CONTEXT_MANAGEMENT`
            * :attr:`NetworkStatusKey.CONTEXT_PUBLIC`
            * :attr:`NetworkStatusKey.CONTEXT_CONNECTED_VPC`
            * :attr:`NetworkStatusKey.CONTEXT_DIRECT_CONNECT`
            
             The context that the entry is used in
        :type  network_type: :class:`str`
        :param network_type: Possible values are: 
            
            * :attr:`NetworkStatusKey.NETWORK_TYPE_DNS`
            * :attr:`NetworkStatusKey.NETWORK_TYPE_VPN`
            * :attr:`NetworkStatusKey.NETWORK_TYPE_MANAGEMENT`
            * :attr:`NetworkStatusKey.NETWORK_TYPE_NAT`
            * :attr:`NetworkStatusKey.NETWORK_TYPE_LOGICAL`
            * :attr:`NetworkStatusKey.NETWORK_TYPE_INFRA`
            
             Network type in the network status pair.
        """
        self.context = context
        self.network_type = network_type
        VapiStruct.__init__(self)


NetworkStatusKey._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.network_status_key', {
        'context': type.StringType(),
        'network_type': type.StringType(),
    },
    NetworkStatusKey,
    False,
    None))



class NetworkStatusKeyValuePair(VapiStruct):
    """
    List of network status

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'key': 'key',
                            'values': 'values',
                            }

    def __init__(self,
                 key=None,
                 values=None,
                ):
        """
        :type  key: :class:`NetworkStatusKey` or ``None``
        :param key: Network status key
        :type  values: :class:`list` of :class:`NetworkStatusEntry` or ``None``
        :param values: Network status value
        """
        self.key = key
        self.values = values
        VapiStruct.__init__(self)


NetworkStatusKeyValuePair._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.network_status_key_value_pair', {
        'key': type.OptionalType(type.ReferenceType(__name__, 'NetworkStatusKey')),
        'values': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'NetworkStatusEntry'))),
    },
    NetworkStatusKeyValuePair,
    False,
    None))



class NetworkStatusListResult(VapiStruct):
    """
    List of network status

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'issues': 'issues',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 issues=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  issues: :class:`list` of :class:`str` or ``None``
        :param issues: List of overall issues encountered during the inquiry
        :type  results: :class:`list` of :class:`NetworkStatusKeyValuePair`
        :param results: List of network status key value pairs.
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.issues = issues
        self.results = results
        VapiStruct.__init__(self)


NetworkStatusListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.network_status_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'issues': type.OptionalType(type.ListType(type.StringType())),
        'results': type.ListType(type.ReferenceType(__name__, 'NetworkStatusKeyValuePair')),
    },
    NetworkStatusListResult,
    False,
    None))



class OwnerResourceLink(VapiStruct):
    """
    The server will populate this field when returing the resource. Ignored on
    PUT and POST.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'action': 'action',
                            'href': 'href',
                            'rel': 'rel',
                            }

    def __init__(self,
                 action=None,
                 href=None,
                 rel=None,
                ):
        """
        :type  action: :class:`str` or ``None``
        :param action: Optional action
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  href: :class:`str` or ``None``
        :param href: Link to resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  rel: :class:`str` or ``None``
        :param rel: Custom relation type (follows RFC 5988 where appropriate
            definitions exist)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.action = action
        self.href = href
        self.rel = rel
        VapiStruct.__init__(self)


OwnerResourceLink._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.owner_resource_link', {
        'action': type.OptionalType(type.StringType()),
        'href': type.OptionalType(type.StringType()),
        'rel': type.OptionalType(type.StringType()),
    },
    OwnerResourceLink,
    False,
    None))



class PrefixInfo(VapiStruct):
    """
    Service IP prefixes information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'display_name': 'display_name',
                            'prefixes': 'prefixes',
                            }

    def __init__(self,
                 display_name=None,
                 prefixes=None,
                ):
        """
        :type  display_name: :class:`str` or ``None``
        :param display_name: Display name
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  prefixes: :class:`list` of :class:`str`
        :param prefixes: Service IP prefixes format: ipv4-cidr-block
        """
        self.display_name = display_name
        self.prefixes = prefixes
        VapiStruct.__init__(self)


PrefixInfo._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.prefix_info', {
        'display_name': type.OptionalType(type.StringType()),
        'prefixes': type.ListType(type.StringType()),
    },
    PrefixInfo,
    False,
    None))



class PrefixesListResult(VapiStruct):
    """
    Service Prefix list query result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`PrefixInfo` or ``None``
        :param results: Service Prefixes list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


PrefixesListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.prefixes_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'PrefixInfo'))),
    },
    PrefixesListResult,
    False,
    None))



class PublicIp(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'display_name': 'display_name',
                            'id': 'id',
                            'ip': 'ip',
                            }

    def __init__(self,
                 display_name=None,
                 id=None,
                 ip=None,
                ):
        """
        :type  display_name: :class:`str` or ``None``
        :param display_name: 
        :type  id: :class:`str` or ``None``
        :param id: Public IP identifier
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  ip: :class:`str` or ``None``
        :param ip: IPv4 address format: ipv4
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.display_name = display_name
        self.id = id
        self.ip = ip
        VapiStruct.__init__(self)


PublicIp._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.public_ip', {
        'display_name': type.OptionalType(type.StringType()),
        'id': type.OptionalType(type.StringType()),
        'ip': type.OptionalType(type.StringType()),
    },
    PublicIp,
    False,
    None))



class PublicIpsListResult(VapiStruct):
    """
    Public IP list

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`PublicIp` or ``None``
        :param results: Public IP list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


PublicIpsListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.public_ips_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'PublicIp'))),
    },
    PublicIpsListResult,
    False,
    None))



class RelatedApiError(VapiStruct):
    """
    Detailed information about a related API error

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'details': 'details',
                            'error_code': 'error_code',
                            'error_data': 'error_data',
                            'error_message': 'error_message',
                            'module_name': 'module_name',
                            }

    def __init__(self,
                 details=None,
                 error_code=None,
                 error_data=None,
                 error_message=None,
                 module_name=None,
                ):
        """
        :type  details: :class:`str` or ``None``
        :param details: Further details about the error
        :type  error_code: :class:`long` or ``None``
        :param error_code: A numeric error code format: int64
        :type  error_data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param error_data: Additional data about the error
        :type  error_message: :class:`str` or ``None``
        :param error_message: A description of the error
        :type  module_name: :class:`str` or ``None``
        :param module_name: The module name where the error occurred
        """
        self.details = details
        self.error_code = error_code
        self.error_data = error_data
        self.error_message = error_message
        self.module_name = module_name
        VapiStruct.__init__(self)


RelatedApiError._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.related_api_error', {
        'details': type.OptionalType(type.StringType()),
        'error_code': type.OptionalType(type.IntegerType()),
        'error_data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
        'error_message': type.OptionalType(type.StringType()),
        'module_name': type.OptionalType(type.StringType()),
    },
    RelatedApiError,
    False,
    None))



class Resource(VapiStruct):
    """
    Base class for resources

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        VapiStruct.__init__(self)


Resource._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.resource', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
    },
    Resource,
    False,
    None))



class ResourceLink(VapiStruct):
    """
    A link to a related resource

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'action': 'action',
                            'href': 'href',
                            'rel': 'rel',
                            }

    def __init__(self,
                 action=None,
                 href=None,
                 rel=None,
                ):
        """
        :type  action: :class:`str` or ``None``
        :param action: Optional action
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  href: :class:`str` or ``None``
        :param href: Link to resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  rel: :class:`str` or ``None``
        :param rel: Custom relation type (follows RFC 5988 where appropriate
            definitions exist)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.action = action
        self.href = href
        self.rel = rel
        VapiStruct.__init__(self)


ResourceLink._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.resource_link', {
        'action': type.OptionalType(type.StringType()),
        'href': type.OptionalType(type.StringType()),
        'rel': type.OptionalType(type.StringType()),
    },
    ResourceLink,
    False,
    None))



class RevisionedResource(VapiStruct):
    """
    A base class for types that track revisions

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            '_revision': 'revision',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 revision=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  revision: :class:`long` or ``None``
        :param revision: The _revision property describes the current revision of the
            resource. To prevent clients from overwriting each other's changes,
            PUT operations must include the current _revision of the resource,
            which clients should obtain by issuing a GET operation. If the
            _revision provided in a PUT request is missing or stale, the
            operation will be rejected. format: int32
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.revision = revision
        VapiStruct.__init__(self)


RevisionedResource._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.revisioned_resource', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        '_revision': type.OptionalType(type.IntegerType()),
    },
    RevisionedResource,
    False,
    None))



class SddcUserConfiguration(VapiStruct):
    """
    SDDC configuration parameters for users. User-level addresses/CIDRs are
    provided.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'all_uplink_interface_label': 'all_uplink_interface_label',
                            'all_vpn_interface_label': 'all_vpn_interface_label',
                            'cgw_snat_ip': 'cgw_snat_ip',
                            'compute_gateway': 'compute_gateway',
                            'dx_interface_label': 'dx_interface_label',
                            'linked_vpc_interface_label': 'linked_vpc_interface_label',
                            'management_gateway': 'management_gateway',
                            'management_gateway_label': 'management_gateway_label',
                            'mgmt_subnet': 'mgmt_subnet',
                            'mgw_snat_ip': 'mgw_snat_ip',
                            'provider_name': 'provider_name',
                            'public_interface_label': 'public_interface_label',
                            'sddc_infra_subnet': 'sddc_infra_subnet',
                            'vpn_dx_ips': 'vpn_dx_ips',
                            'vpn_internet_ips': 'vpn_internet_ips',
                            }

    def __init__(self,
                 all_uplink_interface_label=None,
                 all_vpn_interface_label=None,
                 cgw_snat_ip=None,
                 compute_gateway=None,
                 dx_interface_label=None,
                 linked_vpc_interface_label=None,
                 management_gateway=None,
                 management_gateway_label=None,
                 mgmt_subnet=None,
                 mgw_snat_ip=None,
                 provider_name=None,
                 public_interface_label=None,
                 sddc_infra_subnet=None,
                 vpn_dx_ips=None,
                 vpn_internet_ips=None,
                ):
        """
        :type  all_uplink_interface_label: :class:`str`
        :param all_uplink_interface_label: All uplink interfaces label name
        :type  all_vpn_interface_label: :class:`str`
        :param all_vpn_interface_label: All VPN interfaces label name
        :type  cgw_snat_ip: :class:`str` or ``None``
        :param cgw_snat_ip: CGW SNAT ip address format: ipv4
        :type  compute_gateway: :class:`str`
        :param compute_gateway: Compute gateway name
        :type  dx_interface_label: :class:`str`
        :param dx_interface_label: DirectConnect interface label name
        :type  linked_vpc_interface_label: :class:`str`
        :param linked_vpc_interface_label: Linked VPC interface label name
        :type  management_gateway: :class:`str`
        :param management_gateway: Management gateway name
        :type  management_gateway_label: :class:`str`
        :param management_gateway_label: Management gateway label name
        :type  mgmt_subnet: :class:`list` of :class:`str`
        :param mgmt_subnet: Management VMs CIDRs format: ipv4-cidr-block
        :type  mgw_snat_ip: :class:`str` or ``None``
        :param mgw_snat_ip: MGW SNAT ip address format: ipv4
        :type  provider_name: :class:`str`
        :param provider_name: Provider Name
        :type  public_interface_label: :class:`str`
        :param public_interface_label: Public interface label name
        :type  sddc_infra_subnet: :class:`list` of :class:`str`
        :param sddc_infra_subnet: SDDC Infra CIDRs format: ipv4-cidr-block
        :type  vpn_dx_ips: :class:`list` of :class:`str` or ``None``
        :param vpn_dx_ips: Local IPs for VPN tunnel over Direct Connect format: ipv4
        :type  vpn_internet_ips: :class:`list` of :class:`str` or ``None``
        :param vpn_internet_ips: Public IPs for VPN tunnel over internet format: ipv4
        """
        self.all_uplink_interface_label = all_uplink_interface_label
        self.all_vpn_interface_label = all_vpn_interface_label
        self.cgw_snat_ip = cgw_snat_ip
        self.compute_gateway = compute_gateway
        self.dx_interface_label = dx_interface_label
        self.linked_vpc_interface_label = linked_vpc_interface_label
        self.management_gateway = management_gateway
        self.management_gateway_label = management_gateway_label
        self.mgmt_subnet = mgmt_subnet
        self.mgw_snat_ip = mgw_snat_ip
        self.provider_name = provider_name
        self.public_interface_label = public_interface_label
        self.sddc_infra_subnet = sddc_infra_subnet
        self.vpn_dx_ips = vpn_dx_ips
        self.vpn_internet_ips = vpn_internet_ips
        VapiStruct.__init__(self)


SddcUserConfiguration._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.sddc_user_configuration', {
        'all_uplink_interface_label': type.StringType(),
        'all_vpn_interface_label': type.StringType(),
        'cgw_snat_ip': type.OptionalType(type.StringType()),
        'compute_gateway': type.StringType(),
        'dx_interface_label': type.StringType(),
        'linked_vpc_interface_label': type.StringType(),
        'management_gateway': type.StringType(),
        'management_gateway_label': type.StringType(),
        'mgmt_subnet': type.ListType(type.StringType()),
        'mgw_snat_ip': type.OptionalType(type.StringType()),
        'provider_name': type.StringType(),
        'public_interface_label': type.StringType(),
        'sddc_infra_subnet': type.ListType(type.StringType()),
        'vpn_dx_ips': type.OptionalType(type.ListType(type.StringType())),
        'vpn_internet_ips': type.OptionalType(type.ListType(type.StringType())),
    },
    SddcUserConfiguration,
    False,
    None))



class SelfResourceLink(VapiStruct):
    """
    The server will populate this field when returing the resource. Ignored on
    PUT and POST.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'action': 'action',
                            'href': 'href',
                            'rel': 'rel',
                            }

    def __init__(self,
                 action=None,
                 href=None,
                 rel=None,
                ):
        """
        :type  action: :class:`str` or ``None``
        :param action: Optional action
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  href: :class:`str` or ``None``
        :param href: Link to resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  rel: :class:`str` or ``None``
        :param rel: Custom relation type (follows RFC 5988 where appropriate
            definitions exist)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.action = action
        self.href = href
        self.rel = rel
        VapiStruct.__init__(self)


SelfResourceLink._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.self_resource_link', {
        'action': type.OptionalType(type.StringType()),
        'href': type.OptionalType(type.StringType()),
        'rel': type.OptionalType(type.StringType()),
    },
    SelfResourceLink,
    False,
    None))



class Tag(VapiStruct):
    """
    Arbitrary key-value pairs that may be attached to an entity

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'scope': 'scope',
                            'tag': 'tag',
                            }

    def __init__(self,
                 scope=None,
                 tag=None,
                ):
        """
        :type  scope: :class:`str` or ``None``
        :param scope: Tag searches may optionally be restricted by scope
        :type  tag: :class:`str` or ``None``
        :param tag: Identifier meaningful to user
        """
        self.scope = scope
        self.tag = tag
        VapiStruct.__init__(self)


Tag._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.tag', {
        'scope': type.OptionalType(type.StringType()),
        'tag': type.OptionalType(type.StringType()),
    },
    Tag,
    False,
    None))



class TaskProperties(VapiStruct):
    """
    Task properties

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    STATUS_RUNNING = "running"
    """


    """
    STATUS_ERROR = "error"
    """


    """
    STATUS_SUCCESS = "success"
    """


    """
    STATUS_CANCELING = "canceling"
    """


    """
    STATUS_CANCELED = "canceled"
    """


    """
    STATUS_KILLED = "killed"
    """


    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'async_response_available': 'async_response_available',
                            'cancelable': 'cancelable',
                            'description': 'description',
                            'end_time': 'end_time',
                            'id': 'id',
                            'message': 'message',
                            'progress': 'progress',
                            'request_method': 'request_method',
                            'request_uri': 'request_uri',
                            'start_time': 'start_time',
                            'status': 'status',
                            'user': 'user',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 async_response_available=None,
                 cancelable=None,
                 description=None,
                 end_time=None,
                 id=None,
                 message=None,
                 progress=None,
                 request_method=None,
                 request_uri=None,
                 start_time=None,
                 status=None,
                 user=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  async_response_available: :class:`bool` or ``None``
        :param async_response_available: True if response for asynchronous request is available
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  cancelable: :class:`bool` or ``None``
        :param cancelable: True if this task can be canceled
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  description: :class:`str` or ``None``
        :param description: Description of the task
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  end_time: :class:`long` or ``None``
        :param end_time: The end time of the task in epoch milliseconds format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  id: :class:`str` or ``None``
        :param id: Identifier for this task
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  message: :class:`str` or ``None``
        :param message: A message describing the disposition of the task
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  progress: :class:`long` or ``None``
        :param progress: Task progress if known, from 0 to 100 format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  request_method: :class:`str` or ``None``
        :param request_method: HTTP request method
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  request_uri: :class:`str` or ``None``
        :param request_uri: URI of the method invocation that spawned this task
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  start_time: :class:`long` or ``None``
        :param start_time: The start time of the task in epoch milliseconds format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  status: :class:`str` or ``None``
        :param status: Possible values are: 
            
            * :attr:`TaskProperties.STATUS_RUNNING`
            * :attr:`TaskProperties.STATUS_ERROR`
            * :attr:`TaskProperties.STATUS_SUCCESS`
            * :attr:`TaskProperties.STATUS_CANCELING`
            * :attr:`TaskProperties.STATUS_CANCELED`
            * :attr:`TaskProperties.STATUS_KILLED`
            
             Current status of the task
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  user: :class:`str` or ``None``
        :param user: Name of the user who created this task
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.async_response_available = async_response_available
        self.cancelable = cancelable
        self.description = description
        self.end_time = end_time
        self.id = id
        self.message = message
        self.progress = progress
        self.request_method = request_method
        self.request_uri = request_uri
        self.start_time = start_time
        self.status = status
        self.user = user
        VapiStruct.__init__(self)


TaskProperties._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.task_properties', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'async_response_available': type.OptionalType(type.BooleanType()),
        'cancelable': type.OptionalType(type.BooleanType()),
        'description': type.OptionalType(type.StringType()),
        'end_time': type.OptionalType(type.IntegerType()),
        'id': type.OptionalType(type.StringType()),
        'message': type.OptionalType(type.StringType()),
        'progress': type.OptionalType(type.IntegerType()),
        'request_method': type.OptionalType(type.StringType()),
        'request_uri': type.OptionalType(type.StringType()),
        'start_time': type.OptionalType(type.IntegerType()),
        'status': type.OptionalType(type.StringType()),
        'user': type.OptionalType(type.StringType()),
    },
    TaskProperties,
    False,
    None))



class TraceflowAction(VapiStruct):
    """
    A component that processed the packet injected by traceflow

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    COMPONENT_SUB_TYPE_EDGE_UPLINK = "EDGE_UPLINK"
    """


    """
    COMPONENT_SUB_TYPE_VDR = "VDR"
    """


    """
    COMPONENT_SUB_TYPE_ENI = "ENI"
    """


    """
    COMPONENT_SUB_TYPE_AWS_GATEWAY = "AWS_GATEWAY"
    """


    """
    COMPONENT_TYPE_VMC = "VMC"
    """


    """



    _canonical_to_pep_names = {
                            'component_name': 'component_name',
                            'component_sub_type': 'component_sub_type',
                            'component_type': 'component_type',
                            'reason': 'reason',
                            'resource_type': 'resource_type',
                            }

    def __init__(self,
                 component_name=None,
                 component_sub_type=None,
                 component_type=None,
                 reason=None,
                 resource_type=None,
                ):
        """
        :type  component_name: :class:`str` or ``None``
        :param component_name: Name of a component instance
        :type  component_sub_type: :class:`str` or ``None``
        :param component_sub_type: Possible values are: 
            
            * :attr:`TraceflowAction.COMPONENT_SUB_TYPE_EDGE_UPLINK`
            * :attr:`TraceflowAction.COMPONENT_SUB_TYPE_VDR`
            * :attr:`TraceflowAction.COMPONENT_SUB_TYPE_ENI`
            * :attr:`TraceflowAction.COMPONENT_SUB_TYPE_AWS_GATEWAY`
            
             Subtype of component
        :type  component_type: :class:`str` or ``None``
        :param component_type: Possible values are: 
            
            * :attr:`TraceflowAction.COMPONENT_TYPE_VMC`
            
             Type of component
        :type  reason: :class:`str` or ``None``
        :param reason: Reason to drop or reject packet if it is not forwarded
        :type  resource_type: :class:`str` or ``None``
        :param resource_type: Action taken by the component to process the packet
        """
        self.component_name = component_name
        self.component_sub_type = component_sub_type
        self.component_type = component_type
        self.reason = reason
        self.resource_type = resource_type
        VapiStruct.__init__(self)


TraceflowAction._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.traceflow_action', {
        'component_name': type.OptionalType(type.StringType()),
        'component_sub_type': type.OptionalType(type.StringType()),
        'component_type': type.OptionalType(type.StringType()),
        'reason': type.OptionalType(type.StringType()),
        'resource_type': type.OptionalType(type.StringType()),
    },
    TraceflowAction,
    False,
    None))



class TraceflowActionListResults(VapiStruct):
    """
    A list containing all traceflow actions that have been taken to process the
    packet

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`TraceflowAction` or ``None``
        :param results: Result containing all traceflow actions that have processed the
            packet
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


TraceflowActionListResults._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.traceflow_action_list_results', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'TraceflowAction'))),
    },
    TraceflowActionListResults,
    False,
    None))



class VMCAccounts(VapiStruct):
    """
    Shadow account and linked VPC account

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'linked_vpc_account': 'linked_vpc_account',
                            'shadow_account': 'shadow_account',
                            }

    def __init__(self,
                 linked_vpc_account=None,
                 shadow_account=None,
                ):
        """
        :type  linked_vpc_account: :class:`str` or ``None``
        :param linked_vpc_account: linked VPC account number
        :type  shadow_account: :class:`str`
        :param shadow_account: Shadow VPC account number
        """
        self.linked_vpc_account = linked_vpc_account
        self.shadow_account = shadow_account
        VapiStruct.__init__(self)


VMCAccounts._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.VMC_accounts', {
        'linked_vpc_account': type.OptionalType(type.StringType()),
        'shadow_account': type.StringType(),
    },
    VMCAccounts,
    False,
    None))



class VdrLif(VapiStruct):
    """
    Virtual distributed router (VDR) LIF

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'id': 'id',
                            'ip': 'ip',
                            'netmask': 'netmask',
                            'vlan_id': 'vlan_id',
                            }

    def __init__(self,
                 id=None,
                 ip=None,
                 netmask=None,
                 vlan_id=None,
                ):
        """
        :type  id: :class:`str` or ``None``
        :param id: VDR LIF ID
        :type  ip: :class:`str` or ``None``
        :param ip: VDR LIF IP format: ipv4
        :type  netmask: :class:`str` or ``None``
        :param netmask: VDR LIF subnet mask format: ipv4
        :type  vlan_id: :class:`long` or ``None``
        :param vlan_id: VDR LIF VLAN ID format: int64
        """
        self.id = id
        self.ip = ip
        self.netmask = netmask
        self.vlan_id = vlan_id
        VapiStruct.__init__(self)


VdrLif._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vdr_lif', {
        'id': type.OptionalType(type.StringType()),
        'ip': type.OptionalType(type.StringType()),
        'netmask': type.OptionalType(type.StringType()),
        'vlan_id': type.OptionalType(type.IntegerType()),
    },
    VdrLif,
    False,
    None))



class VdrRoute(VapiStruct):
    """
    Virtual Distributed Router (VDR) route entry

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'destination': 'destination',
                            'gateway': 'gateway',
                            'lif_id': 'lif_id',
                            }

    def __init__(self,
                 destination=None,
                 gateway=None,
                 lif_id=None,
                ):
        """
        :type  destination: :class:`str` or ``None``
        :param destination: Destination IP CIDR Block format: ipv4-cidr-block
        :type  gateway: :class:`str` or ``None``
        :param gateway: Outgoing gateway
        :type  lif_id: :class:`str` or ``None``
        :param lif_id: Outgoing Lif ID
        """
        self.destination = destination
        self.gateway = gateway
        self.lif_id = lif_id
        VapiStruct.__init__(self)


VdrRoute._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vdr_route', {
        'destination': type.OptionalType(type.StringType()),
        'gateway': type.OptionalType(type.StringType()),
        'lif_id': type.OptionalType(type.StringType()),
    },
    VdrRoute,
    False,
    None))



class VifsListResult(VapiStruct):
    """
    Direct Connect VIFs (Virtual Interface) list query result

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            '_links': 'links',
                            '_schema': 'schema',
                            '_self': 'self_',
                            'cursor': 'cursor',
                            'result_count': 'result_count',
                            'sort_ascending': 'sort_ascending',
                            'sort_by': 'sort_by',
                            'results': 'results',
                            }

    def __init__(self,
                 links=None,
                 schema=None,
                 self_=None,
                 cursor=None,
                 result_count=None,
                 sort_ascending=None,
                 sort_by=None,
                 results=None,
                ):
        """
        :type  links: :class:`list` of :class:`ResourceLink` or ``None``
        :param links: The server will populate this field when returing the resource.
            Ignored on PUT and POST.
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  schema: :class:`str` or ``None``
        :param schema: Schema for this resource
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  self_: :class:`SelfResourceLink` or ``None``
        :param self_: Link to this resource
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page)
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  result_count: :class:`long` or ``None``
        :param result_count: Count of results found (across all pages), set only on first page
            format: int64
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: If true, results are sorted in ascending order
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  results: :class:`list` of :class:`VirtualInterface` or ``None``
        :param results: VIFs list
        """
        self.links = links
        self.schema = schema
        self.self_ = self_
        self.cursor = cursor
        self.result_count = result_count
        self.sort_ascending = sort_ascending
        self.sort_by = sort_by
        self.results = results
        VapiStruct.__init__(self)


VifsListResult._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vifs_list_result', {
        '_links': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'ResourceLink'))),
        '_schema': type.OptionalType(type.StringType()),
        '_self': type.OptionalType(type.ReferenceType(__name__, 'SelfResourceLink')),
        'cursor': type.OptionalType(type.StringType()),
        'result_count': type.OptionalType(type.IntegerType()),
        'sort_ascending': type.OptionalType(type.BooleanType()),
        'sort_by': type.OptionalType(type.StringType()),
        'results': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VirtualInterface'))),
    },
    VifsListResult,
    False,
    None))



class VirtualInterface(VapiStruct):
    """


    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    BGP_STATUS_UP = "UP"
    """


    """
    BGP_STATUS_DOWN = "DOWN"
    """


    """
    STATE_CONFIRMING = "CONFIRMING"
    """


    """
    STATE_VERIFYING = "VERIFYING"
    """


    """
    STATE_PENDING = "PENDING"
    """


    """
    STATE_AVAILABLE = "AVAILABLE"
    """


    """
    STATE_DOWN = "DOWN"
    """


    """
    STATE_DELETING = "DELETING"
    """


    """
    STATE_DELETED = "DELETED"
    """


    """
    STATE_REJECTED = "REJECTED"
    """


    """
    STATE_ATTACHED = "ATTACHED"
    """


    """
    STATE_ATTACHING = "ATTACHING"
    """


    """
    STATE_ERROR = "ERROR"
    """


    """



    _canonical_to_pep_names = {
                            'bgp_status': 'bgp_status',
                            'direct_connect_id': 'direct_connect_id',
                            'id': 'id',
                            'local_ip': 'local_ip',
                            'mtu': 'mtu',
                            'name': 'name',
                            'remote_asn': 'remote_asn',
                            'remote_ip': 'remote_ip',
                            'state': 'state',
                            }

    def __init__(self,
                 bgp_status=None,
                 direct_connect_id=None,
                 id=None,
                 local_ip=None,
                 mtu=None,
                 name=None,
                 remote_asn=None,
                 remote_ip=None,
                 state=None,
                ):
        """
        :type  bgp_status: :class:`str`
        :param bgp_status: Possible values are: 
            
            * :attr:`VirtualInterface.BGP_STATUS_UP`
            * :attr:`VirtualInterface.BGP_STATUS_DOWN`
            
             BGP status
        :type  direct_connect_id: :class:`str`
        :param direct_connect_id: Identifier for the Direct Connect
        :type  id: :class:`str`
        :param id: Identifier for the virtual interface
        :type  local_ip: :class:`str` or ``None``
        :param local_ip: amazon side address format: ipv4
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  mtu: :class:`long` or ``None``
        :param mtu: Maximum transmission unit allowed by the VIF format: int32
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  name: :class:`str`
        :param name: VIF name
        :type  remote_asn: :class:`str` or ``None``
        :param remote_asn: Remote autonomous system number of vif
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  remote_ip: :class:`str` or ``None``
        :param remote_ip: customer address format: ipv4
            This attribute may be present in responses from the server, but if
            it is present in a request to server it will be ignored.
        :type  state: :class:`str`
        :param state: Possible values are: 
            
            * :attr:`VirtualInterface.STATE_CONFIRMING`
            * :attr:`VirtualInterface.STATE_VERIFYING`
            * :attr:`VirtualInterface.STATE_PENDING`
            * :attr:`VirtualInterface.STATE_AVAILABLE`
            * :attr:`VirtualInterface.STATE_DOWN`
            * :attr:`VirtualInterface.STATE_DELETING`
            * :attr:`VirtualInterface.STATE_DELETED`
            * :attr:`VirtualInterface.STATE_REJECTED`
            * :attr:`VirtualInterface.STATE_ATTACHED`
            * :attr:`VirtualInterface.STATE_ATTACHING`
            * :attr:`VirtualInterface.STATE_ERROR`
            
             VIF State
        """
        self.bgp_status = bgp_status
        self.direct_connect_id = direct_connect_id
        self.id = id
        self.local_ip = local_ip
        self.mtu = mtu
        self.name = name
        self.remote_asn = remote_asn
        self.remote_ip = remote_ip
        self.state = state
        VapiStruct.__init__(self)


VirtualInterface._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.virtual_interface', {
        'bgp_status': type.StringType(),
        'direct_connect_id': type.StringType(),
        'id': type.StringType(),
        'local_ip': type.OptionalType(type.StringType()),
        'mtu': type.OptionalType(type.IntegerType()),
        'name': type.StringType(),
        'remote_asn': type.OptionalType(type.StringType()),
        'remote_ip': type.OptionalType(type.StringType()),
        'state': type.StringType(),
    },
    VirtualInterface,
    False,
    None))



class VmcConsolidatedRealizedStatus(VapiStruct):
    """
    Represents aggregated realized status for intent entity across associated
    realized entities.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'consolidated_status': 'consolidated_status',
                            'consolidated_status_per_object': 'consolidated_status_per_object',
                            'intent_path': 'intent_path',
                            }

    def __init__(self,
                 consolidated_status=None,
                 consolidated_status_per_object=None,
                 intent_path=None,
                ):
        """
        :type  consolidated_status: :class:`VmcConsolidatedStatus` or ``None``
        :param consolidated_status: Consolidated state of objects for a given intent entity.
        :type  consolidated_status_per_object: :class:`list` of :class:`VmcConsolidatedStatusPerObject` or ``None``
        :param consolidated_status_per_object: Aggregated consolidated status by enforcement point.
        :type  intent_path: :class:`str` or ``None``
        :param intent_path: Intent path of the object representing this consolidated state.
        """
        self.consolidated_status = consolidated_status
        self.consolidated_status_per_object = consolidated_status_per_object
        self.intent_path = intent_path
        VapiStruct.__init__(self)


VmcConsolidatedRealizedStatus._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_consolidated_realized_status', {
        'consolidated_status': type.OptionalType(type.ReferenceType(__name__, 'VmcConsolidatedStatus')),
        'consolidated_status_per_object': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'VmcConsolidatedStatusPerObject'))),
        'intent_path': type.OptionalType(type.StringType()),
    },
    VmcConsolidatedRealizedStatus,
    False,
    None))



class VmcConsolidatedStatus(VapiStruct):
    """
    Consolidated status of an object.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    CONSOLIDATED_STATUS_IN_PROGRESS = "IN_PROGRESS"
    """


    """
    CONSOLIDATED_STATUS_SUCCESS = "SUCCESS"
    """


    """
    CONSOLIDATED_STATUS_ERROR = "ERROR"
    """


    """
    CONSOLIDATED_STATUS_UNAVAILABLE = "UNAVAILABLE"
    """


    """



    _canonical_to_pep_names = {
                            'consolidated_status': 'consolidated_status',
                            'status_message': 'status_message',
                            }

    def __init__(self,
                 consolidated_status=None,
                 status_message=None,
                ):
        """
        :type  consolidated_status: :class:`str` or ``None``
        :param consolidated_status: Possible values are: 
            
            * :attr:`VmcConsolidatedStatus.CONSOLIDATED_STATUS_IN_PROGRESS`
            * :attr:`VmcConsolidatedStatus.CONSOLIDATED_STATUS_SUCCESS`
            * :attr:`VmcConsolidatedStatus.CONSOLIDATED_STATUS_ERROR`
            * :attr:`VmcConsolidatedStatus.CONSOLIDATED_STATUS_UNAVAILABLE`
            
            Possible values could be IN_PROGRESS, SUCCESS, ERROR, UNAVAILABLE.
            IN_PROGRESS - The object realization is in progress. ERROR - The
            object realization fails or is caught in an error. SUCCESS - The
            realization succeeds. UNAVAILABLE - The object realization status
            is unavailable.
        :type  status_message: :class:`str` or ``None``
        :param status_message: Help message for the current status regarding an object, providing
            information for each state.
        """
        self.consolidated_status = consolidated_status
        self.status_message = status_message
        VapiStruct.__init__(self)


VmcConsolidatedStatus._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_consolidated_status', {
        'consolidated_status': type.OptionalType(type.StringType()),
        'status_message': type.OptionalType(type.StringType()),
    },
    VmcConsolidatedStatus,
    False,
    None))



class VmcConsolidatedStatusPerObject(VapiStruct):
    """
    Realized status consolidated by individual objects.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """



    _canonical_to_pep_names = {
                            'consolidated_status': 'consolidated_status',
                            'object_id': 'object_id',
                            }

    def __init__(self,
                 consolidated_status=None,
                 object_id=None,
                ):
        """
        :type  consolidated_status: :class:`VmcConsolidatedStatus` or ``None``
        :param consolidated_status: Detailed consolidated realized status for an intent object.
        :type  object_id: :class:`str`
        :param object_id: Object id used to consolidate state. This can be a particular
            backend task/job, etc.
        """
        self.consolidated_status = consolidated_status
        self.object_id = object_id
        VapiStruct.__init__(self)


VmcConsolidatedStatusPerObject._set_binding_type(type.StructType(
    'com.vmware.nsx_vmc_app.model.vmc_consolidated_status_per_object', {
        'consolidated_status': type.OptionalType(type.ReferenceType(__name__, 'VmcConsolidatedStatus')),
        'object_id': type.StringType(),
    },
    VmcConsolidatedStatusPerObject,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

