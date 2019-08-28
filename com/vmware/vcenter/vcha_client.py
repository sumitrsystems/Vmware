# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.vcha.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.vcha_client`` module provides classes for deploying
and monitoring a vCenter High Availability (VCHA) Cluster.

"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from com.vmware.cis_client import Tasks
from vmware.vapi.stdlib.client.task import Task
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

class IpFamily(Enum):
    """
    The ``IpFamily`` class defines the Ip address family. This enumeration was
    added in vSphere API 6.7.1.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    IPV4 = None
    """
    IPV4 address family. This class attribute was added in vSphere API 6.7.1.

    """
    IPV6 = None
    """
    IPv6 address family. This class attribute was added in vSphere API 6.7.1.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`IpFamily` instance.
        """
        Enum.__init__(string)

IpFamily._set_values([
    IpFamily('IPV4'),
    IpFamily('IPV6'),
])
IpFamily._set_binding_type(type.EnumType(
    'com.vmware.vcenter.vcha.ip_family',
    IpFamily))



class NetworkType(Enum):
    """
    The ``NetworkType`` class defines the type of a vCenter Server network.
    This enumeration was added in vSphere API 6.7.1.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    STANDARD_PORTGROUP = None
    """
    vSphere standard portgroup network. This class attribute was added in
    vSphere API 6.7.1.

    """
    DISTRIBUTED_PORTGROUP = None
    """
    Distributed virtual switch. This class attribute was added in vSphere API
    6.7.1.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`NetworkType` instance.
        """
        Enum.__init__(string)

NetworkType._set_values([
    NetworkType('STANDARD_PORTGROUP'),
    NetworkType('DISTRIBUTED_PORTGROUP'),
])
NetworkType._set_binding_type(type.EnumType(
    'com.vmware.vcenter.vcha.network_type',
    NetworkType))




class CertificateInfo(VapiStruct):
    """
    The ``CertificateInfo`` Class contains information about the SSL
    certificate for a management vCenter server. This class was added in
    vSphere API 6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 ssl_thumbprint=None,
                ):
        """
        :type  ssl_thumbprint: :class:`str`
        :param ssl_thumbprint: The SHA-256 thumbprint of the SSL certificate for a management
            vCenter server. This attribute was added in vSphere API 6.7.1.
        """
        self.ssl_thumbprint = ssl_thumbprint
        VapiStruct.__init__(self)


CertificateInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.certificate_info', {
        'ssl_thumbprint': type.StringType(),
    },
    CertificateInfo,
    False,
    None))



class ConnectionSpec(VapiStruct):
    """
    The ``ConnectionSpec`` class contains information required to connect to a
    vCenter server. The connection to the vCenter server always uses the HTTPS
    protocol. This class was added in vSphere API 6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 hostname=None,
                 port=None,
                 ssl_thumbprint=None,
                 username=None,
                 password=None,
                ):
        """
        :type  hostname: :class:`str`
        :param hostname: IP Address or DNS of the vCenter. This attribute was added in
            vSphere API 6.7.1.
        :type  port: :class:`long` or ``None``
        :param port: Port number. This attribute was added in vSphere API 6.7.1.
            If None, port 443 will be used.
        :type  ssl_thumbprint: :class:`str` or ``None``
        :param ssl_thumbprint: SHA1 hash of the server SSL certificate. This attribute was added
            in vSphere API 6.7.1.
            If None, empty ssl thumbprint is assumed.
        :type  username: :class:`str` or ``None``
        :param username: Username to access the server. This attribute was added in vSphere
            API 6.7.1.
            This attribute is currently required. If None, an error is
            returned. In the future, if this attribute is None, the system will
            attempt to identify the user. If a user cannot be identified, then
            the requested operation will fail.
        :type  password: :class:`str` or ``None``
        :param password: Password for the specified user. This attribute was added in
            vSphere API 6.7.1.
            This attribute is currently required. If None, an empty password is
            assumed. In the future, if this attribute is None, the system will
            attempt to authenticate the user. If a user cannot be identified,
            then the requested operation will fail.
        """
        self.hostname = hostname
        self.port = port
        self.ssl_thumbprint = ssl_thumbprint
        self.username = username
        self.password = password
        VapiStruct.__init__(self)


ConnectionSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.connection_spec', {
        'hostname': type.StringType(),
        'port': type.OptionalType(type.IntegerType()),
        'ssl_thumbprint': type.OptionalType(type.StringType()),
        'username': type.OptionalType(type.StringType()),
        'password': type.OptionalType(type.SecretType()),
    },
    ConnectionSpec,
    False,
    None))



class CredentialsSpec(VapiStruct):
    """
    The ``CredentialsSpec`` class contains information to connect to the
    vCenter server managing the VCHA nodes. This class was added in vSphere API
    6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 active_location=None,
                ):
        """
        :type  active_location: :class:`ConnectionSpec`
        :param active_location: Connection information for the management vCenter Server of the
            Active Node in a VCHA Cluster. This attribute was added in vSphere
            API 6.7.1.
        """
        self.active_location = active_location
        VapiStruct.__init__(self)


CredentialsSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.credentials_spec', {
        'active_location': type.ReferenceType(__name__, 'ConnectionSpec'),
    },
    CredentialsSpec,
    False,
    None))



class DiskInfo(VapiStruct):
    """
    The ``DiskInfo`` class contains information to describe the storage
    configuration of a vCenter virtual machine. This class was added in vSphere
    API 6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 datastore=None,
                 datastore_name=None,
                ):
        """
        :type  datastore: :class:`str`
        :param datastore: The identifier of the datastore to put all the virtual disks on.
            This attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``Datastore:VCenter``. When methods return a value of this class as
            a return value, the attribute will be an identifier for the
            resource type: ``Datastore:VCenter``.
        :type  datastore_name: :class:`str`
        :param datastore_name: The name of the datastore. This attribute was added in vSphere API
            6.7.1.
        """
        self.datastore = datastore
        self.datastore_name = datastore_name
        VapiStruct.__init__(self)


DiskInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.disk_info', {
        'datastore': type.IdType(resource_types='Datastore:VCenter'),
        'datastore_name': type.StringType(),
    },
    DiskInfo,
    False,
    None))



class DiskSpec(VapiStruct):
    """
    The ``DiskSpec`` class contains information to describe the storage
    configuration of a vCenter virtual machine. This class was added in vSphere
    API 6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 datastore=None,
                ):
        """
        :type  datastore: :class:`str` or ``None``
        :param datastore: The identifier of the datastore to put all the virtual disks on.
            This attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``Datastore:VCenter``. When methods return a value of this class as
            a return value, the attribute will be an identifier for the
            resource type: ``Datastore:VCenter``.
            This field needs to be set. If None, then see
            vim.vm.RelocateSpec.datastore.
        """
        self.datastore = datastore
        VapiStruct.__init__(self)


DiskSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.disk_spec', {
        'datastore': type.OptionalType(type.IdType()),
    },
    DiskSpec,
    False,
    None))



class IpSpec(VapiStruct):
    """
    The ``IpSpec`` class contains IP information used to configure a network
    interface. This class was added in vSphere API 6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'ip_family',
            {
                'IPV4' : [('ipv4', True)],
                'IPV6' : [('ipv6', True)],
            }
        ),
    ]



    def __init__(self,
                 ip_family=None,
                 ipv4=None,
                 ipv6=None,
                 default_gateway=None,
                 dns_servers=None,
                ):
        """
        :type  ip_family: :class:`IpFamily`
        :param ip_family: Family of the IP address to configure the interface. This attribute
            was added in vSphere API 6.7.1.
        :type  ipv4: :class:`Ipv4Spec`
        :param ipv4: If the family of the ip is IPV4, then this will point to IPv4
            address specification. This attribute was added in vSphere API
            6.7.1.
            This attribute is optional and it is only relevant when the value
            of ``ipFamily`` is :attr:`IpFamily.IPV4`.
        :type  ipv6: :class:`Ipv6Spec`
        :param ipv6: If the family of the ip is IPV6, then this will point to IPv6
            address specification. This attribute was added in vSphere API
            6.7.1.
            This attribute is optional and it is only relevant when the value
            of ``ipFamily`` is :attr:`IpFamily.IPV6`.
        :type  default_gateway: :class:`str` or ``None``
        :param default_gateway: The IP address of the Gateway for this interface. This attribute
            was added in vSphere API 6.7.1.
            If None, gateway will not be used for the network interface.
        :type  dns_servers: :class:`list` of :class:`str` or ``None``
        :param dns_servers: The list of IP addresses of the DNS servers for this interface.
            This list is a comma separated list. This attribute was added in
            vSphere API 6.7.1.
            If None, DNS servers will not be used for the network interface.
        """
        self.ip_family = ip_family
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.default_gateway = default_gateway
        self.dns_servers = dns_servers
        VapiStruct.__init__(self)


IpSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.ip_spec', {
        'ip_family': type.ReferenceType(__name__, 'IpFamily'),
        'ipv4': type.OptionalType(type.ReferenceType(__name__, 'Ipv4Spec')),
        'ipv6': type.OptionalType(type.ReferenceType(__name__, 'Ipv6Spec')),
        'default_gateway': type.OptionalType(type.StringType()),
        'dns_servers': type.OptionalType(type.ListType(type.StringType())),
    },
    IpSpec,
    False,
    None))



class Ipv4Spec(VapiStruct):
    """
    The ``Ipv4Spec`` class contains IPV4 information used to configure a
    network interface. This class was added in vSphere API 6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 address=None,
                 subnet_mask=None,
                 prefix=None,
                ):
        """
        :type  address: :class:`str`
        :param address: IPV4 address to be used to configure the interface. This attribute
            was added in vSphere API 6.7.1.
        :type  subnet_mask: :class:`str` or ``None``
        :param subnet_mask: The subnet mask for the interface. This attribute was added in
            vSphere API 6.7.1.
            If None and the ``prefix`` attribute is None, then an error will be
            reported.
            If None and the ``prefix`` attribute is set, then the ``prefix``
            attribute will be used to create a subnet mask whose first prefix
            bits are 1 and the remaining bits 0.
            If both the ``subnetMask`` attribute and the ``prefix`` attribute
            are set and they do not represent the same value, then an error
            will be reported.
        :type  prefix: :class:`long` or ``None``
        :param prefix: The CIDR prefix for the interface. This attribute was added in
            vSphere API 6.7.1.
            If None and the ``subnetMask`` attribute is None, this an error
            will be reported.
            If None and the ``subnetMask`` attribute is set, then the
            ``subnetMask`` attribute will be used.
            If both the ``subnetMask`` attribute and the ``prefix`` attribute
            are set and they do not represent the same value, then an error
            will be reported.
        """
        self.address = address
        self.subnet_mask = subnet_mask
        self.prefix = prefix
        VapiStruct.__init__(self)


Ipv4Spec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.ipv4_spec', {
        'address': type.StringType(),
        'subnet_mask': type.OptionalType(type.StringType()),
        'prefix': type.OptionalType(type.IntegerType()),
    },
    Ipv4Spec,
    False,
    None))



class Ipv6Spec(VapiStruct):
    """
    The ``Ipv6Spec`` class contains IPV6 information used to configure a
    network interface. This class was added in vSphere API 6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 address=None,
                 prefix=None,
                ):
        """
        :type  address: :class:`str`
        :param address: IPv6 address to be used to configure the interface. This attribute
            was added in vSphere API 6.7.1.
        :type  prefix: :class:`long`
        :param prefix: The CIDR prefix for the interface. This attribute was added in
            vSphere API 6.7.1.
        """
        self.address = address
        self.prefix = prefix
        VapiStruct.__init__(self)


Ipv6Spec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.ipv6_spec', {
        'address': type.StringType(),
        'prefix': type.IntegerType(),
    },
    Ipv6Spec,
    False,
    None))



class PlacementInfo(VapiStruct):
    """
    The ``PlacementInfo`` class contains information to describe the inventory
    placement of a single node of a VCHA cluster.
    The active node's management vCenter server credentials are required to
    populate all attributes except biosUuid. This class was added in vSphere
    API 6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 management_vcenter_name=None,
                 vm_name=None,
                 datacenter=None,
                 datacenter_name=None,
                 host=None,
                 host_name=None,
                 cluster=None,
                 cluster_name=None,
                 ha_network=None,
                 ha_network_name=None,
                 ha_network_type=None,
                 management_network=None,
                 management_network_name=None,
                 management_network_type=None,
                 storage=None,
                 bios_uuid=None,
                ):
        """
        :type  management_vcenter_name: :class:`str`
        :param management_vcenter_name: The hostname of the vCenter server that is managing the VCHA node.
            This attribute was added in vSphere API 6.7.1.
        :type  vm_name: :class:`str`
        :param vm_name: The virtual machine name of the VCHA node. This attribute was added
            in vSphere API 6.7.1.
        :type  datacenter: :class:`str`
        :param datacenter: The identifier of the datacenter of the VCHA node. This attribute
            was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``Datacenter:VCenter``. When methods return a value of this class
            as a return value, the attribute will be an identifier for the
            resource type: ``Datacenter:VCenter``.
        :type  datacenter_name: :class:`str`
        :param datacenter_name: The name of the datacenter of the VCHA node. This attribute was
            added in vSphere API 6.7.1.
        :type  host: :class:`str`
        :param host: The identifier of the host of the VCHA node. This attribute was
            added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``HostSystem:VCenter``. When methods return a value of this class
            as a return value, the attribute will be an identifier for the
            resource type: ``HostSystem:VCenter``.
        :type  host_name: :class:`str`
        :param host_name: The name of the host of the VCHA node. This attribute was added in
            vSphere API 6.7.1.
        :type  cluster: :class:`str` or ``None``
        :param cluster: The identifier of the cluster of which ``host`` is member. This
            attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``ClusterComputeResource:VCenter``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``ClusterComputeResource:VCenter``.
            If None, ``host`` is a standalone host.
        :type  cluster_name: :class:`str` or ``None``
        :param cluster_name: The name of the cluster of which ``host`` is member. This attribute
            was added in vSphere API 6.7.1.
            If None, ``host`` is a standalone host.
        :type  ha_network: :class:`str` or ``None``
        :param ha_network: The identifier of the Network object used for the HA network. This
            attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``Network:VCenter``. When methods return a value of this class as a
            return value, the attribute will be an identifier for the resource
            type: ``Network:VCenter``.
            If None, the information is currently unavailable or the haNetwork
            is not configured.
        :type  ha_network_name: :class:`str` or ``None``
        :param ha_network_name: The name of the Network object used for the HA network. This
            attribute was added in vSphere API 6.7.1.
            If None, the information is currently unavailable or the haNetwork
            is not configured.
        :type  ha_network_type: :class:`NetworkType` or ``None``
        :param ha_network_type: The type of the Network object used for the HA network. This
            attribute was added in vSphere API 6.7.1.
            If None, the information is currently unavailable or the haNetwork
            is not configured.
        :type  management_network: :class:`str`
        :param management_network: The identifier of the Network object used for the Management
            network. This attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``Network:VCenter``. When methods return a value of this class as a
            return value, the attribute will be an identifier for the resource
            type: ``Network:VCenter``.
        :type  management_network_name: :class:`str`
        :param management_network_name: The name of the Network object used for the Management network.
            This attribute was added in vSphere API 6.7.1.
        :type  management_network_type: :class:`NetworkType`
        :param management_network_type: The type of the Network object used for the Management network.
            This attribute was added in vSphere API 6.7.1.
        :type  storage: :class:`DiskInfo`
        :param storage: The storage information of the VCHA node. This attribute was added
            in vSphere API 6.7.1.
        :type  bios_uuid: :class:`str` or ``None``
        :param bios_uuid: BIOS UUID for the node. This attribute was added in vSphere API
            6.7.1.
            If None, the information is currently unavailable.
        """
        self.management_vcenter_name = management_vcenter_name
        self.vm_name = vm_name
        self.datacenter = datacenter
        self.datacenter_name = datacenter_name
        self.host = host
        self.host_name = host_name
        self.cluster = cluster
        self.cluster_name = cluster_name
        self.ha_network = ha_network
        self.ha_network_name = ha_network_name
        self.ha_network_type = ha_network_type
        self.management_network = management_network
        self.management_network_name = management_network_name
        self.management_network_type = management_network_type
        self.storage = storage
        self.bios_uuid = bios_uuid
        VapiStruct.__init__(self)


PlacementInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.placement_info', {
        'management_vcenter_name': type.StringType(),
        'vm_name': type.StringType(),
        'datacenter': type.IdType(resource_types='Datacenter:VCenter'),
        'datacenter_name': type.StringType(),
        'host': type.IdType(resource_types='HostSystem:VCenter'),
        'host_name': type.StringType(),
        'cluster': type.OptionalType(type.IdType()),
        'cluster_name': type.OptionalType(type.StringType()),
        'ha_network': type.OptionalType(type.IdType()),
        'ha_network_name': type.OptionalType(type.StringType()),
        'ha_network_type': type.OptionalType(type.ReferenceType(__name__, 'NetworkType')),
        'management_network': type.IdType(resource_types='Network:VCenter'),
        'management_network_name': type.StringType(),
        'management_network_type': type.ReferenceType(__name__, 'NetworkType'),
        'storage': type.ReferenceType(__name__, 'DiskInfo'),
        'bios_uuid': type.OptionalType(type.StringType()),
    },
    PlacementInfo,
    False,
    None))



class PlacementSpec(VapiStruct):
    """
    The ``PlacementSpec`` class contains information to describe the inventory
    placement of a single node of a VCHA cluster. This class was added in
    vSphere API 6.7.1.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 folder=None,
                 host=None,
                 resource_pool=None,
                 ha_network_type=None,
                 ha_network=None,
                 management_network_type=None,
                 management_network=None,
                 storage=None,
                ):
        """
        :type  name: :class:`str`
        :param name: The name of the VCHA node to be used for the virtual machine name.
            This attribute was added in vSphere API 6.7.1.
        :type  folder: :class:`str`
        :param folder: The identifier of the folder to deploy the VCHA node to. This
            attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``Folder:VCenter``. When methods return a value of this class as a
            return value, the attribute will be an identifier for the resource
            type: ``Folder:VCenter``.
        :type  host: :class:`str` or ``None``
        :param host: The identifier of the host to deploy the VCHA node to. This
            attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``HostSystem:VCenter``. When methods return a value of this class
            as a return value, the attribute will be an identifier for the
            resource type: ``HostSystem:VCenter``.
            If None, see vim.vm.RelocateSpec.host.
        :type  resource_pool: :class:`str` or ``None``
        :param resource_pool: The identifier of the resource pool to deploy the VCHA node to.
            This attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``ResourcePool:VCenter``. When methods return a value of this class
            as a return value, the attribute will be an identifier for the
            resource type: ``ResourcePool:VCenter``.
            If None, then the active node's resource pool will be used.
        :type  ha_network_type: :class:`NetworkType` or ``None``
        :param ha_network_type: The type of the Network object used by the HA network.
            If the :attr:`PlacementSpec.ha_network` attribute is set, then the
            :attr:`PlacementSpec.ha_network_type` field must be set.
            If the :attr:`PlacementSpec.ha_network` attribute is None, then the
            :attr:`PlacementSpec.ha_network_type` attribute is ignored. This
            attribute was added in vSphere API 6.7.1.
            If None and the :attr:`PlacementSpec.ha_network` attribute is
            unset, then the same network present on the Active node virtual
            machine is used to deploy the virtual machine with an assumption
            that the network is present on the destination.
            If None and the :attr:`PlacementSpec.ha_network` attribute is set,
            then an error is reported.
        :type  ha_network: :class:`str` or ``None``
        :param ha_network: The identifier of the Network object used for the HA network.
            If the :attr:`PlacementSpec.ha_network` attribute is set, then the
            {#link #haNetworkType} attribute must be set.
            If the :attr:`PlacementSpec.ha_network` attribute is None, then the
            :attr:`PlacementSpec.ha_network_type` attribute is ignored. This
            attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``Network:VCenter``. When methods return a value of this class as a
            return value, the attribute will be an identifier for the resource
            type: ``Network:VCenter``.
            If None and the :attr:`PlacementSpec.ha_network_type` attribute is
            unset, then the same network present on the Active node virtual
            machine is used to deploy the virtual machine with an assumption
            that the network is present on the destination.
        :type  management_network_type: :class:`NetworkType` or ``None``
        :param management_network_type: The type of the Network object used by the Management network.
            If the :attr:`PlacementSpec.management_network` attribute is set,
            then the {#link #managementNetworkType} field must be set.
            If the :attr:`PlacementSpec.management_network` attribute is None,
            then the :attr:`PlacementSpec.management_network_type` attribute is
            ignored. This attribute was added in vSphere API 6.7.1.
            If None and the :attr:`PlacementSpec.management_network` attribute
            is unset, then the same network present on the Active node virtual
            machine is used to deploy the virtual machine with an assumption
            that the network is present on the destination.
            If None and the :attr:`PlacementSpec.management_network` attribute
            is set, then an error is reported.
        :type  management_network: :class:`str` or ``None``
        :param management_network: The identifier of the Network object used for the Management
            network. If the :attr:`PlacementSpec.management_network` attribute
            is set, then the :attr:`PlacementSpec.management_network_type`
            attribute must be set.
            If the :attr:`PlacementSpec.management_network` attribute is None,
            then the :attr:`PlacementSpec.management_network_type` attribute is
            ignored. This attribute was added in vSphere API 6.7.1.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``Network:VCenter``. When methods return a value of this class as a
            return value, the attribute will be an identifier for the resource
            type: ``Network:VCenter``.
            If None and the :attr:`PlacementSpec.management_network_type`
            attribute is unset, then the same network present on the Active
            node virtual machine is used to deploy the virtual machine with an
            assumption that the network is present on the destination.
        :type  storage: :class:`DiskSpec` or ``None``
        :param storage: The storage specification to deploy the VCHA node to. This
            attribute was added in vSphere API 6.7.1.
            If None, see vim.vm.RelocateSpec.datastore.
        """
        self.name = name
        self.folder = folder
        self.host = host
        self.resource_pool = resource_pool
        self.ha_network_type = ha_network_type
        self.ha_network = ha_network
        self.management_network_type = management_network_type
        self.management_network = management_network
        self.storage = storage
        VapiStruct.__init__(self)


PlacementSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vcha.placement_spec', {
        'name': type.StringType(),
        'folder': type.IdType(resource_types='Folder:VCenter'),
        'host': type.OptionalType(type.IdType()),
        'resource_pool': type.OptionalType(type.IdType()),
        'ha_network_type': type.OptionalType(type.ReferenceType(__name__, 'NetworkType')),
        'ha_network': type.OptionalType(type.IdType()),
        'management_network_type': type.OptionalType(type.ReferenceType(__name__, 'NetworkType')),
        'management_network': type.OptionalType(type.IdType()),
        'storage': type.OptionalType(type.ReferenceType(__name__, 'DiskSpec')),
    },
    PlacementSpec,
    False,
    None))



class Cluster(VapiInterface):
    """
    The ``Cluster`` class provides methods to deploy and undeploy a vCenter
    High Availability (VCHA) cluster, failover from the active VCHA node to the
    passive VCHA node, and retrieve the status of the VCHA cluster. This class
    was added in vSphere API 6.7.1.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.vcha.cluster'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterStub)

    class Type(Enum):
        """
        The ``Cluster.Type`` class defines the possible deployment types for a VCHA
        Cluster. This enumeration was added in vSphere API 6.7.1.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        AUTO = None
        """
        Passive and witness nodes are cloned automatically. This class attribute
        was added in vSphere API 6.7.1.

        """
        MANUAL = None
        """
        Passive and witness nodes are not cloned automatically. After deployment,
        the customer should clone the passive and witness virtual machines. This
        class attribute was added in vSphere API 6.7.1.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('AUTO'),
        Type('MANUAL'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vcha.cluster.type',
        Type))


    class ClusterMode(Enum):
        """
        The ``Cluster.ClusterMode`` class defines the possible modes for a VCHA
        Cluster. This enumeration was added in vSphere API 6.7.1.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        ENABLED = None
        """
        VCHA Cluster is enabled. State replication between the Active and Passive
        node is enabled and automatic failover is allowed. This class attribute was
        added in vSphere API 6.7.1.

        """
        DISABLED = None
        """
        VCHA Cluster is disabled. State replication between the Active and Passive
        node is disabled and automatic failover is not allowed. This class
        attribute was added in vSphere API 6.7.1.

        """
        MAINTENANCE = None
        """
        VCHA Cluster is in maintenance mode. State replication between the Active
        and Passive node is enabled but automatic failover is not allowed. This
        class attribute was added in vSphere API 6.7.1.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ClusterMode` instance.
            """
            Enum.__init__(string)

    ClusterMode._set_values([
        ClusterMode('ENABLED'),
        ClusterMode('DISABLED'),
        ClusterMode('MAINTENANCE'),
    ])
    ClusterMode._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vcha.cluster.cluster_mode',
        ClusterMode))


    class ClusterState(Enum):
        """
        The ``Cluster.ClusterState`` class defines the possible for a VCHA Cluster.
        This enumeration was added in vSphere API 6.7.1.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        HEALTHY = None
        """
        All three nodes in a VCHA Cluster are healthy and connected. State
        replication between Active and Passive node is working and both nodes are
        in sync. This class attribute was added in vSphere API 6.7.1.

        """
        DEGRADED = None
        """
        A VCHA Cluster is said to be in a degraded state for either or all of the
        following reasons: 
        
        * There is a node loss.
        * State replication between the Active and Passive node fails.
        
        . This class attribute was added in vSphere API 6.7.1.

        """
        ISOLATED = None
        """
        All three nodes are isolated from each other. This class attribute was
        added in vSphere API 6.7.1.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ClusterState` instance.
            """
            Enum.__init__(string)

    ClusterState._set_values([
        ClusterState('HEALTHY'),
        ClusterState('DEGRADED'),
        ClusterState('ISOLATED'),
    ])
    ClusterState._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vcha.cluster.cluster_state',
        ClusterState))


    class NodeState(Enum):
        """
        The ``Cluster.NodeState`` class defines possible state a node can be in a
        VCHA Cluster. This enumeration was added in vSphere API 6.7.1.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        UP = None
        """
        Node is up and has joined the VCHA Cluster. This class attribute was added
        in vSphere API 6.7.1.

        """
        DOWN = None
        """
        Node is down and has left the VCHA Cluster. This class attribute was added
        in vSphere API 6.7.1.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`NodeState` instance.
            """
            Enum.__init__(string)

    NodeState._set_values([
        NodeState('UP'),
        NodeState('DOWN'),
    ])
    NodeState._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vcha.cluster.node_state',
        NodeState))


    class NodeRole(Enum):
        """
        The ``Cluster.NodeRole`` class defines the role node can be in a VCHA
        Cluster. This enumeration was added in vSphere API 6.7.1.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        ACTIVE = None
        """
        Node is having a role of Active. In this role, node runs a vCenter Server
        that serves client requests. This class attribute was added in vSphere API
        6.7.1.

        """
        PASSIVE = None
        """
        Node is having a role of Passive. In this role node, runs as a standby for
        the Active vCenter Server and receives state updates. This node takes over
        the role of Active vCenter Server upon failover. This class attribute was
        added in vSphere API 6.7.1.

        """
        WITNESS = None
        """
        Node is having a role of Witness. In this role, node acts as a quorum node
        for avoiding the classic split-brain problem. This class attribute was
        added in vSphere API 6.7.1.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`NodeRole` instance.
            """
            Enum.__init__(string)

    NodeRole._set_values([
        NodeRole('ACTIVE'),
        NodeRole('PASSIVE'),
        NodeRole('WITNESS'),
    ])
    NodeRole._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vcha.cluster.node_role',
        NodeRole))


    class ConfigState(Enum):
        """
        The ``Cluster.ConfigState`` class defines the VCHA configuration state.
        This enumeration was added in vSphere API 6.7.1.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        CONFIGURED = None
        """
        VCHA cluster is configured. This class attribute was added in vSphere API
        6.7.1.

        """
        NOTCONFIGURED = None
        """
        VCHA cluster is not configured. This class attribute was added in vSphere
        API 6.7.1.

        """
        INVALID = None
        """
        VCHA cluster is in an invalid/dirty state. This class attribute was added
        in vSphere API 6.7.1.

        """
        PREPARED = None
        """
        vCenter server appliance has been prepared for VCHA cluster configuration.
        This class attribute was added in vSphere API 6.7.1.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ConfigState` instance.
            """
            Enum.__init__(string)

    ConfigState._set_values([
        ConfigState('CONFIGURED'),
        ConfigState('NOTCONFIGURED'),
        ConfigState('INVALID'),
        ConfigState('PREPARED'),
    ])
    ConfigState._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vcha.cluster.config_state',
        ConfigState))


    class IpFamily(Enum):
        """
        The ``Cluster.IpFamily`` class defines the IP address family. This
        enumeration was added in vSphere API 6.7.1.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        IPV4 = None
        """
        IPV4 address family. This class attribute was added in vSphere API 6.7.1.

        """
        IPV6 = None
        """
        IPV6 address family. This class attribute was added in vSphere API 6.7.1.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`IpFamily` instance.
            """
            Enum.__init__(string)

    IpFamily._set_values([
        IpFamily('IPV4'),
        IpFamily('IPV6'),
    ])
    IpFamily._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vcha.cluster.ip_family',
        IpFamily))


    class ActiveSpec(VapiStruct):
        """
        The ``Cluster.ActiveSpec`` class contains the deploy specification for the
        Active Node of the VCHA cluster. This class was added in vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     ha_network_type=None,
                     ha_network=None,
                     ha_ip=None,
                    ):
            """
            :type  ha_network_type: :class:`NetworkType` or ``None``
            :param ha_network_type: The type of the Network object used by the HA network.
                If the :attr:`Cluster.ActiveSpec.ha_network` attribute is set, then
                the :attr:`Cluster.ActiveSpec.ha_network_type` field must be set.
                If the :attr:`Cluster.ActiveSpec.ha_network` attribute is None,
                then the :attr:`Cluster.ActiveSpec.ha_network_type` attribute is
                ignored. This attribute was added in vSphere API 6.7.1.
                If None and the :attr:`Cluster.ActiveSpec.ha_network` attribute is
                unset, then the second NIC is assumed to be already configured.
                If None and the :attr:`Cluster.ActiveSpec.ha_network` attribute is
                set, then an error is reported.
            :type  ha_network: :class:`str` or ``None``
            :param ha_network: The identifier of the Network object used for the HA network.
                If the :attr:`Cluster.ActiveSpec.ha_network` attribute is set, then
                the :attr:`Cluster.ActiveSpec.ha_network_type` attribute must be
                set.
                If the :attr:`Cluster.ActiveSpec.ha_network` attribute is None,
                then the :attr:`Cluster.ActiveSpec.ha_network_type` attribute is
                ignored. This attribute was added in vSphere API 6.7.1.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Network:VCenter``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Network:VCenter``.
                If None and the :attr:`Cluster.ActiveSpec.ha_network_type`
                attribute is unset, then the second NIC is assumed to be already
                configured.
                If None and the :attr:`Cluster.ActiveSpec.ha_network` attribute is
                set, then an error is reported.
            :type  ha_ip: :class:`IpSpec`
            :param ha_ip: IP specification for the HA network. This attribute was added in
                vSphere API 6.7.1.
            """
            self.ha_network_type = ha_network_type
            self.ha_network = ha_network
            self.ha_ip = ha_ip
            VapiStruct.__init__(self)


    ActiveSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.active_spec', {
            'ha_network_type': type.OptionalType(type.ReferenceType(__name__, 'NetworkType')),
            'ha_network': type.OptionalType(type.IdType()),
            'ha_ip': type.ReferenceType(__name__, 'IpSpec'),
        },
        ActiveSpec,
        False,
        None))


    class PassiveSpec(VapiStruct):
        """
        The ``Cluster.PassiveSpec`` class contains the deploy specification for the
        Passive Node of the VCHA cluster. This class was added in vSphere API
        6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     placement=None,
                     ha_ip=None,
                     failover_ip=None,
                    ):
            """
            :type  placement: :class:`PlacementSpec` or ``None``
            :param placement: Contains the placement configuration of the node. This attribute
                was added in vSphere API 6.7.1.
                If None, then the it is assumed that the clone will be done
                manually by the customer. In this case, the placement configuration
                for the witness node should also be omitted. Only the network
                configuration will be setup. Once the passive and witness nodes are
                cloned from the active node, the VCHA high availability is turned
                on.
            :type  ha_ip: :class:`IpSpec`
            :param ha_ip: IP specification for the HA network. This attribute was added in
                vSphere API 6.7.1.
            :type  failover_ip: :class:`IpSpec` or ``None``
            :param failover_ip: IP specification for the management network. This attribute was
                added in vSphere API 6.7.1.
                If None, then it will assume the public IP address of the Active
                vCenter Server.
            """
            self.placement = placement
            self.ha_ip = ha_ip
            self.failover_ip = failover_ip
            VapiStruct.__init__(self)


    PassiveSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.passive_spec', {
            'placement': type.OptionalType(type.ReferenceType(__name__, 'PlacementSpec')),
            'ha_ip': type.ReferenceType(__name__, 'IpSpec'),
            'failover_ip': type.OptionalType(type.ReferenceType(__name__, 'IpSpec')),
        },
        PassiveSpec,
        False,
        None))


    class WitnessSpec(VapiStruct):
        """
        The ``Cluster.WitnessSpec`` class contains the deploy specification for the
        Witness Node of the VCHA cluster. This class was added in vSphere API
        6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     placement=None,
                     ha_ip=None,
                    ):
            """
            :type  placement: :class:`PlacementSpec` or ``None``
            :param placement: Contains the placement configuration of the node. This attribute
                was added in vSphere API 6.7.1.
                If None, then it is assumed that the clone will be done manually by
                the customer. In this case, the placement configuration for the
                witness node should also be omitted. Only the network configuration
                will be setup. Once the passive and witness nodes are cloned from
                the active node, the VCHA high availability is turned on.
            :type  ha_ip: :class:`IpSpec`
            :param ha_ip: IP specification for the HA network. This attribute was added in
                vSphere API 6.7.1.
            """
            self.placement = placement
            self.ha_ip = ha_ip
            VapiStruct.__init__(self)


    WitnessSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.witness_spec', {
            'placement': type.OptionalType(type.ReferenceType(__name__, 'PlacementSpec')),
            'ha_ip': type.ReferenceType(__name__, 'IpSpec'),
        },
        WitnessSpec,
        False,
        None))


    class DeploySpec(VapiStruct):
        """
        The ``Cluster.DeploySpec`` class contains the deploy specification for the
        three nodes of a VCHA cluster. This class was added in vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vc_spec=None,
                     deployment=None,
                     active=None,
                     passive=None,
                     witness=None,
                    ):
            """
            :type  vc_spec: :class:`CredentialsSpec` or ``None``
            :param vc_spec: Contains the active node's management vCenter server credentials.
                This attribute was added in vSphere API 6.7.1.
                If None, then the active vCenter Server instance is assumed to be
                either self-managed or else in enhanced linked mode and managed by
                a linked vCenter Server instance.
            :type  deployment: :class:`Cluster.Type`
            :param deployment: Contains the deployment type. This attribute was added in vSphere
                API 6.7.1.
            :type  active: :class:`Cluster.ActiveSpec`
            :param active: Contains the active node's network configuration. This attribute
                was added in vSphere API 6.7.1.
            :type  passive: :class:`Cluster.PassiveSpec`
            :param passive: Contains the passive node's placement configuration. This attribute
                was added in vSphere API 6.7.1.
            :type  witness: :class:`Cluster.WitnessSpec`
            :param witness: Contains the witness node's placement configuration. This attribute
                was added in vSphere API 6.7.1.
            """
            self.vc_spec = vc_spec
            self.deployment = deployment
            self.active = active
            self.passive = passive
            self.witness = witness
            VapiStruct.__init__(self)


    DeploySpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.deploy_spec', {
            'vc_spec': type.OptionalType(type.ReferenceType(__name__, 'CredentialsSpec')),
            'deployment': type.ReferenceType(__name__, 'Cluster.Type'),
            'active': type.ReferenceType(__name__, 'Cluster.ActiveSpec'),
            'passive': type.ReferenceType(__name__, 'Cluster.PassiveSpec'),
            'witness': type.ReferenceType(__name__, 'Cluster.WitnessSpec'),
        },
        DeploySpec,
        False,
        None))


    class NodeRuntimeInfo(VapiStruct):
        """
        The ``Cluster.NodeRuntimeInfo`` class describes a node's runtime
        information in a VCHA Cluster. This class was added in vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     state=None,
                     role=None,
                     placement=None,
                    ):
            """
            :type  state: :class:`Cluster.NodeState` or ``None``
            :param state: Last known state of the node.
                The active node's management vCenter server credentials are not
                required to populate :attr:`Cluster.NodeRuntimeInfo.state`. This
                attribute was added in vSphere API 6.7.1.
                If None, then information is unavailable or the passive and witness
                nodes are not cloned yet.
            :type  role: :class:`Cluster.NodeRole` or ``None``
            :param role: Last known role of the node.
                The active node's management vCenter server credentials are not
                required to populate :attr:`Cluster.NodeRuntimeInfo.role`. This
                attribute was added in vSphere API 6.7.1.
                If None, then information is unavailable or the passive and witness
                nodes are not cloned yet.
            :type  placement: :class:`PlacementInfo` or ``None``
            :param placement: Placement information of the node.
                The active node's management vCenter server credentials are
                required to populate most attributes of
                :attr:`Cluster.NodeRuntimeInfo.placement`. This attribute was added
                in vSphere API 6.7.1.
                If None, then the information is unavailable or the specified
                Active vCenter server management credentials are invalid or the
                node is not cloned yet or the VCHA cluster was deployed in a manual
                fashion.
            """
            self.state = state
            self.role = role
            self.placement = placement
            VapiStruct.__init__(self)


    NodeRuntimeInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.node_runtime_info', {
            'state': type.OptionalType(type.ReferenceType(__name__, 'Cluster.NodeState')),
            'role': type.OptionalType(type.ReferenceType(__name__, 'Cluster.NodeRole')),
            'placement': type.OptionalType(type.ReferenceType(__name__, 'PlacementInfo')),
        },
        NodeRuntimeInfo,
        False,
        None))


    class Ipv4Info(VapiStruct):
        """
        The ``Cluster.Ipv4Info`` class contains attributes to describe IPV4
        information of the configured network interface. This class was added in
        vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     address=None,
                     subnet_mask=None,
                     prefix=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: IP address of the configured network interface. This attribute was
                added in vSphere API 6.7.1.
            :type  subnet_mask: :class:`str`
            :param subnet_mask: The subnet mask of the interface. This attribute was added in
                vSphere API 6.7.1.
            :type  prefix: :class:`long` or ``None``
            :param prefix: The CIDR prefix of the interface. This attribute was added in
                vSphere API 6.7.1.
                If None , then the subnet mask is invalid.
            """
            self.address = address
            self.subnet_mask = subnet_mask
            self.prefix = prefix
            VapiStruct.__init__(self)


    Ipv4Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.ipv4_info', {
            'address': type.StringType(),
            'subnet_mask': type.StringType(),
            'prefix': type.OptionalType(type.IntegerType()),
        },
        Ipv4Info,
        False,
        None))


    class Ipv6Info(VapiStruct):
        """
        The ``Cluster.Ipv6Info`` class contains attributes to describe IPV6
        information of the configured network interface. This class was added in
        vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     address=None,
                     prefix=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: IP address of the configured network interface. This attribute was
                added in vSphere API 6.7.1.
            :type  prefix: :class:`long`
            :param prefix: The CIDR prefix of the interface. This attribute was added in
                vSphere API 6.7.1.
            """
            self.address = address
            self.prefix = prefix
            VapiStruct.__init__(self)


    Ipv6Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.ipv6_info', {
            'address': type.StringType(),
            'prefix': type.IntegerType(),
        },
        Ipv6Info,
        False,
        None))


    class IpInfo(VapiStruct):
        """
        The ``Cluster.IpInfo`` class contains attributes related to an ip. This
        class was added in vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'ip_family',
                {
                    'IPV4' : [('ipv4', True)],
                    'IPV6' : [('ipv6', True)],
                }
            ),
        ]



        def __init__(self,
                     ip_family=None,
                     ipv4=None,
                     ipv6=None,
                     gateway_ip=None,
                    ):
            """
            :type  ip_family: :class:`Cluster.IpFamily`
            :param ip_family: Family of the ip. This attribute was added in vSphere API 6.7.1.
            :type  ipv4: :class:`Cluster.Ipv4Info`
            :param ipv4: If the type of the ip family is IPV4, then this will point to IPv4
                address specification. This attribute was added in vSphere API
                6.7.1.
                This attribute is optional and it is only relevant when the value
                of ``ipFamily`` is :attr:`Cluster.IpFamily.IPV4`.
            :type  ipv6: :class:`Cluster.Ipv6Info`
            :param ipv6: If the type of the ip family is IPV6, then this will point to IPv6
                address specification. This attribute was added in vSphere API
                6.7.1.
                This attribute is optional and it is only relevant when the value
                of ``ipFamily`` is :attr:`Cluster.IpFamily.IPV6`.
            :type  gateway_ip: :class:`str` or ``None``
            :param gateway_ip: Gateway IP address. This attribute was added in vSphere API 6.7.1.
                If None, no gateway is specified.
            """
            self.ip_family = ip_family
            self.ipv4 = ipv4
            self.ipv6 = ipv6
            self.gateway_ip = gateway_ip
            VapiStruct.__init__(self)


    IpInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.ip_info', {
            'ip_family': type.ReferenceType(__name__, 'Cluster.IpFamily'),
            'ipv4': type.OptionalType(type.ReferenceType(__name__, 'Cluster.Ipv4Info')),
            'ipv6': type.OptionalType(type.ReferenceType(__name__, 'Cluster.Ipv6Info')),
            'gateway_ip': type.OptionalType(type.StringType()),
        },
        IpInfo,
        False,
        None))


    class NodeInfo(VapiStruct):
        """
        The ``Cluster.NodeInfo`` class defines the configuration information for
        the active and passive nodes in the cluster. This class was added in
        vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     failover_ip=None,
                     ha_ip=None,
                     runtime=None,
                    ):
            """
            :type  failover_ip: :class:`Cluster.IpInfo` or ``None``
            :param failover_ip: Failover IP address that this node will assume after the failover
                to serve client requests. Each failover node can have a different
                failover IP address.
                The active node's management vCenter server credentials are not
                required to populate :attr:`Cluster.NodeInfo.failover_ip`. This
                attribute was added in vSphere API 6.7.1.
                If None, then it will assume the public IP address of the Active
                vCenter Server.
            :type  ha_ip: :class:`Cluster.IpInfo`
            :param ha_ip: VCHA Cluster network configuration of the node. All cluster
                communication (state replication, heartbeat, cluster messages)
                happens over this network.
                The active node's management vCenter server credentials are not
                required to populate this :attr:`Cluster.NodeInfo.ha_ip`. This
                attribute was added in vSphere API 6.7.1.
            :type  runtime: :class:`Cluster.NodeRuntimeInfo` or ``None``
            :param runtime: Runtime information for the node in the VCHA Cluster.
                The active node's management vCenter server credentials are
                required to populate some attributes of
                :attr:`Cluster.NodeInfo.runtime`. This attribute was added in
                vSphere API 6.7.1.
                If None, then the information is unavailable or the specified
                Active vCenter server management credentials are invalid or the
                node is not cloned yet.
            """
            self.failover_ip = failover_ip
            self.ha_ip = ha_ip
            self.runtime = runtime
            VapiStruct.__init__(self)


    NodeInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.node_info', {
            'failover_ip': type.OptionalType(type.ReferenceType(__name__, 'Cluster.IpInfo')),
            'ha_ip': type.ReferenceType(__name__, 'Cluster.IpInfo'),
            'runtime': type.OptionalType(type.ReferenceType(__name__, 'Cluster.NodeRuntimeInfo')),
        },
        NodeInfo,
        False,
        None))


    class WitnessInfo(VapiStruct):
        """
        The ``Cluster.WitnessInfo`` class defines the configuration and runtime
        information for the witness node in the cluster. This class was added in
        vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     ha_ip=None,
                     runtime=None,
                    ):
            """
            :type  ha_ip: :class:`Cluster.IpInfo`
            :param ha_ip: VCHA Cluster network configuration of the node. All cluster
                communication (state replication, heartbeat, cluster messages)
                happens over this network.
                The active node's management vCenter server credentials are not
                required to populate :attr:`Cluster.WitnessInfo.ha_ip`. This
                attribute was added in vSphere API 6.7.1.
            :type  runtime: :class:`Cluster.NodeRuntimeInfo` or ``None``
            :param runtime: Runtime information for the node in the VCHA Cluster.
                The active node's management vCenter server credentials are
                required to populate some attributes of
                :attr:`Cluster.WitnessInfo.runtime`. This attribute was added in
                vSphere API 6.7.1.
                If None, then the information is unavailable or the node is not
                cloned yet.
            """
            self.ha_ip = ha_ip
            self.runtime = runtime
            VapiStruct.__init__(self)


    WitnessInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.witness_info', {
            'ha_ip': type.ReferenceType(__name__, 'Cluster.IpInfo'),
            'runtime': type.OptionalType(type.ReferenceType(__name__, 'Cluster.NodeRuntimeInfo')),
        },
        WitnessInfo,
        False,
        None))


    class ErrorCondition(VapiStruct):
        """
        The ``Cluster.ErrorCondition`` class contains an error condition and a
        recommendation to handle the error condition. This class was added in
        vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     error=None,
                     recommendation=None,
                    ):
            """
            :type  error: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param error: Contains an error condition. This attribute was added in vSphere
                API 6.7.1.
            :type  recommendation: :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
            :param recommendation: Contains a recommendation on handling the error condition. This
                attribute was added in vSphere API 6.7.1.
                If None, there is no tip for the error condition.
            """
            self.error = error
            self.recommendation = recommendation
            VapiStruct.__init__(self)


    ErrorCondition._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.error_condition', {
            'error': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'recommendation': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        ErrorCondition,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Cluster.Info`` class contains the configuration and health
        information of the three nodes in a VCHA Cluster. This class was added in
        vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     config_state=None,
                     node1=None,
                     node2=None,
                     witness=None,
                     mode=None,
                     health_state=None,
                     health_exception=None,
                     health_warnings=None,
                     manual_failover_allowed=None,
                     auto_failover_allowed=None,
                    ):
            """
            :type  config_state: :class:`Cluster.ConfigState` or ``None``
            :param config_state: Configuration state of the VCHA cluster.
                The active node's management vCenter server credentials are not
                required to populate this attribute. This attribute was added in
                vSphere API 6.7.1.
                If None, then the information is unavailable.
            :type  node1: :class:`Cluster.NodeInfo` or ``None``
            :param node1: Node configuration information for the VCHA cluster. This attribute
                was added in vSphere API 6.7.1.
                If None, then the information is unavailable.
            :type  node2: :class:`Cluster.NodeInfo` or ``None``
            :param node2: Node configuration information for the VCHA cluster. This attribute
                was added in vSphere API 6.7.1.
                If None, then the information is unavailable or the node is not
                cloned yet.
            :type  witness: :class:`Cluster.WitnessInfo` or ``None``
            :param witness: Node configuration information for the VCHA cluster. This attribute
                was added in vSphere API 6.7.1.
                If None, then the information is unavailable or the node is not
                cloned yet.
            :type  mode: :class:`Cluster.ClusterMode` or ``None``
            :param mode: Operational mode of the VCHA Cluster. This attribute was added in
                vSphere API 6.7.1.
                If None, then the information is unavailable or the node is not
                cloned yet.
            :type  health_state: :class:`Cluster.ClusterState` or ``None``
            :param health_state: Last known state of the VCHA Cluster. This attribute was added in
                vSphere API 6.7.1.
                If None, then the information is unavailable or the node is not
                cloned yet.
            :type  health_exception: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
            :param health_exception: Health warning messages if the health information is unavailable.
                This attribute was added in vSphere API 6.7.1.
                If None, then the cluster is in a healthy state.
            :type  health_warnings: :class:`list` of :class:`Cluster.ErrorCondition` or ``None``
            :param health_warnings: A collection of messages describing the reason for a non-healthy
                Cluster. This attribute was added in vSphere API 6.7.1.
                If None, then the cluster is in a healthy state.
            :type  manual_failover_allowed: :class:`bool` or ``None``
            :param manual_failover_allowed: Specifies if manual failover is allowed. This attribute was added
                in vSphere API 6.7.1.
                If None, then the cluster state healthy and manual failover
                allowance in accordance with the cluster mode.
            :type  auto_failover_allowed: :class:`bool` or ``None``
            :param auto_failover_allowed: Specifies if automatic failover is allowed. This attribute was
                added in vSphere API 6.7.1.
                If None, then the cluster state healthy and automatic failover
                allowance in accordance with the cluster mode.
            """
            self.config_state = config_state
            self.node1 = node1
            self.node2 = node2
            self.witness = witness
            self.mode = mode
            self.health_state = health_state
            self.health_exception = health_exception
            self.health_warnings = health_warnings
            self.manual_failover_allowed = manual_failover_allowed
            self.auto_failover_allowed = auto_failover_allowed
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.info', {
            'config_state': type.OptionalType(type.ReferenceType(__name__, 'Cluster.ConfigState')),
            'node1': type.OptionalType(type.ReferenceType(__name__, 'Cluster.NodeInfo')),
            'node2': type.OptionalType(type.ReferenceType(__name__, 'Cluster.NodeInfo')),
            'witness': type.OptionalType(type.ReferenceType(__name__, 'Cluster.WitnessInfo')),
            'mode': type.OptionalType(type.ReferenceType(__name__, 'Cluster.ClusterMode')),
            'health_state': type.OptionalType(type.ReferenceType(__name__, 'Cluster.ClusterState')),
            'health_exception': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'))),
            'health_warnings': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Cluster.ErrorCondition'))),
            'manual_failover_allowed': type.OptionalType(type.BooleanType()),
            'auto_failover_allowed': type.OptionalType(type.BooleanType()),
        },
        Info,
        False,
        None))


    class NodeVmInfo(VapiStruct):
        """
        The ``Cluster.NodeVmInfo`` class contains information to describe the
        Virtual Machine of a node of a VCHA cluster. This class was added in
        vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vm=None,
                     bios_uuid=None,
                    ):
            """
            :type  vm: :class:`str`
            :param vm: The identifier of the virtual machine of the VCHA node. This
                attribute was added in vSphere API 6.7.1.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``VirtualMachine:VCenter``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``VirtualMachine:VCenter``.
            :type  bios_uuid: :class:`str`
            :param bios_uuid: BIOS UUID for the node. This attribute was added in vSphere API
                6.7.1.
            """
            self.vm = vm
            self.bios_uuid = bios_uuid
            VapiStruct.__init__(self)


    NodeVmInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.node_vm_info', {
            'vm': type.IdType(resource_types='VirtualMachine:VCenter'),
            'bios_uuid': type.StringType(),
        },
        NodeVmInfo,
        False,
        None))


    class VmInfo(VapiStruct):
        """
        The ``Cluster.VmInfo`` class contains information to describe the Virtual
        Machines of passive and witness nodes of a VCHA cluster. This class was
        added in vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     passive=None,
                     witness=None,
                    ):
            """
            :type  passive: :class:`Cluster.NodeVmInfo`
            :param passive: The virtual machine information of the passive node. This attribute
                was added in vSphere API 6.7.1.
            :type  witness: :class:`Cluster.NodeVmInfo`
            :param witness: The virtual machine information of the witness node. This attribute
                was added in vSphere API 6.7.1.
            """
            self.passive = passive
            self.witness = witness
            VapiStruct.__init__(self)


    VmInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.vm_info', {
            'passive': type.ReferenceType(__name__, 'Cluster.NodeVmInfo'),
            'witness': type.ReferenceType(__name__, 'Cluster.NodeVmInfo'),
        },
        VmInfo,
        False,
        None))


    class UndeploySpec(VapiStruct):
        """
        The ``Cluster.UndeploySpec`` class contains the undeploy specification for
        a VCHA cluster. This class was added in vSphere API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vc_spec=None,
                     force_delete=None,
                     vms=None,
                    ):
            """
            :type  vc_spec: :class:`CredentialsSpec` or ``None``
            :param vc_spec: Contains the active node's management vCenter server credentials.
                This attribute was added in vSphere API 6.7.1.
                If None, then the active vCenter Server instance is assumed to be
                either self-managed or else in enhanced linked mode and managed by
                a linked vCenter Server instance.
            :type  force_delete: :class:`bool` or ``None``
            :param force_delete: Flag controlling in what circumstances the virtual machines will be
                deleted. For this flag to take effect, the VCHA cluster should have
                been successfully configured using automatic deployment. 
                
                * If true, the :attr:`Cluster.UndeploySpec.vms` attribute will be
                  ignored, the VCHA cluster specific information is removed, and the
                  passive and witness virtual machines will be deleted.
                * If false, the :attr:`Cluster.UndeploySpec.vms` attribute contains
                  the information identifying the passive and witness virtual
                  machines.
                
                
                * If the :attr:`Cluster.UndeploySpec.vms` attribute is set, then it
                  will be validated prior to deleting the passive and witness virtual
                  machines and VCHA cluster specific information is removed.
                * If the :attr:`Cluster.UndeploySpec.vms` attribute is None, then
                  the passive and witness virtual machines will not be deleted. The
                  customer should delete them in order to cleanup completely. VCHA
                  cluster specific information is removed.
                
                 
                . This attribute was added in vSphere API 6.7.1.
                If None, the :attr:`Cluster.UndeploySpec.vms` attribute contains
                the information identifying the passive and witness virtual
                machines. 
                
                * If the :attr:`Cluster.UndeploySpec.vms` attribute is set, then it
                  will be validated prior to deleting the passive and witness virtual
                  machines. VCHA cluster specific information is removed.
                * If the :attr:`Cluster.UndeploySpec.vms` attribute is None, then
                  the passive and witness virtual machines will not be deleted. The
                  customer should delete them in order to cleanup completely. VCHA
                  cluster specific information is removed.
            :type  vms: :class:`Cluster.VmInfo` or ``None``
            :param vms: Contains virtual machine information for the passive and witness
                virtual machines. For this flag to take effect, the VCHA cluster
                should have been successfully configured using automatic
                deployment. 
                
                If set, the :attr:`Cluster.UndeploySpec.force_delete` attribute
                controls whether this information is validated. 
                
                * If the :attr:`Cluster.UndeploySpec.force_delete` attribute is
                  true, then this information is ignored, VCHA cluster specific
                  information is removed and the passive and witness virtual machines
                  will be deleted.
                * If the :attr:`Cluster.UndeploySpec.force_delete` attribute is
                  None or false, then this information is validated prior to deleting
                  the passive and witness virtual machines. VCHA cluster specific
                  information is removed.
                
                . This attribute was added in vSphere API 6.7.1.
                If None, the :attr:`Cluster.UndeploySpec.force_delete` attribute
                controls the deletion of the passive and witness virtual machines. 
                
                * If the :attr:`Cluster.UndeploySpec.force_delete` attribute is
                  true, then the passive and witness virtual machines will be
                  deleted. VCHA cluster specific information is removed.
                * If the :attr:`Cluster.UndeploySpec.force_delete` attribute is
                  None or false, then the passive and witness virtual machines will
                  not be deleted. The customer should delete them in order to cleanup
                  completely. VCHA cluster specific information is removed.
            """
            self.vc_spec = vc_spec
            self.force_delete = force_delete
            self.vms = vms
            VapiStruct.__init__(self)


    UndeploySpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.cluster.undeploy_spec', {
            'vc_spec': type.OptionalType(type.ReferenceType(__name__, 'CredentialsSpec')),
            'force_delete': type.OptionalType(type.BooleanType()),
            'vms': type.OptionalType(type.ReferenceType(__name__, 'Cluster.VmInfo')),
        },
        UndeploySpec,
        False,
        None))




    def deploy_task(self,
               spec,
               ):
        """
        Prepares, clones, and configures a VCHA cluster. This method was added
        in vSphere API 6.7.1.

        :type  spec: :class:`Cluster.DeploySpec`
        :param spec: Contains the deploy specification for all three nodes of a VCHA
            cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the credentials provided for authenticating with the active
            node's management vCenter server are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user has insufficient privilege to perform the operation.
            Operation execution requires the Global.VCServer privilege.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnverifiedPeer` 
            If the SSL certificate of the management vCenter server cannot be
            validated.
            The value of the data attribute of
            :class:`com.vmware.vapi.std.errors_client.Error` will be a class
            that contains all the attributes defined in
            :class:`CertificateInfo`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If any other error occurs.
        """
        task_id = self._invoke('deploy$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance


    def failover_task(self,
                 planned,
                 ):
        """
        Initiates failover from the active vCenter node to the passive node. 
        
        For forced failover, Active node immediately initiates a failover. This
        may result into a data loss after failover. 
        
        For planned failover, Active node flushes all the state to the Passive
        node, waits for the flush to complete before causing a failover. After
        the failover, Passive node starts without any data loss. 
        
         A failover is allowed only in the following cases: 
        
        #. Cluster's mode is enabled and all cluster members are present.
        #. Cluster's mode is maintenance and all cluster members are present.
        
        . This method was added in vSphere API 6.7.1.

        :type  planned: :class:`bool`
        :param planned: If false, a failover is initiated immediately and may result in
            data loss.
            If true, a failover is initated after the Active node flushes its
            state to Passive and there is no data loss.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user has insufficient privilege to perform the operation.
            Operation execution requires the Global.VCServer privilege.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If any other error occurs.
        """
        task_id = self._invoke('failover$task',
                                {
                                'planned': planned,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance

    def get(self,
            vc_spec=None,
            partial=None,
            ):
        """
        Retrieves the status of a VCHA cluster. This method was added in
        vSphere API 6.7.1.

        :type  vc_spec: :class:`CredentialsSpec` or ``None``
        :param vc_spec: Contains active node's management vCenter server credentials.
            If None, then the active vCenter Server instance is assumed to be
            either self-managed or else in enhanced linked mode and managed by
            a linked vCenter Server instance.
        :type  partial: :class:`bool` or ``None``
        :param partial: If true, then return only the information that does not require
            connecting to the Active vCenter Server.
             If false or unset, then return all the information.
            If None, then return all the information.
        :rtype: :class:`Cluster.Info`
        :return: Info structure containing the VCHA configuration and health
            information.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the credentials provided for authenticating with the active
            node's management vCenter server are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user has insufficient privilege to perform the operation. 
            
            * If ``partial`` is false or unset, then the operation execution
              requires the Global.VCServer privilege.
            * If ``partial`` is true, then the operation execution requires the
              System.Read privilege.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnverifiedPeer` 
            If the SSL certificate of the management vCenter server cannot be
            validated.
            The value of the data attribute of
            :class:`com.vmware.vapi.std.errors_client.Error` will be a class
            that contains all the attributes defined in
            :class:`CertificateInfo`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If any other error occurs.
        """
        return self._invoke('get',
                            {
                            'vc_spec': vc_spec,
                            'partial': partial,
                            })


    def undeploy_task(self,
                 spec,
                 ):
        """
        Destroys the VCHA cluster and removes all VCHA specific information
        from the VCVA appliance. Optionally, the passive and witness node
        virtual machines will be deleted only if VCHA was deployed using
        automatic deployment. The active node in the cluster continues to run
        as a standalone VCVA appliance after the destroy operation has been
        performed. 
        
        If the VCHA cluster is in a transition state and not configured, then
        the VCHA cluster specific information is removed.. This method was
        added in vSphere API 6.7.1.

        :type  spec: :class:`Cluster.UndeploySpec`
        :param spec: Contains the undeploy specification for a VCHA cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the credentials provided for authenticating with the active
            node's management vCenter server are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the passive virtual machine is not managed by the specified
            vCenter server.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the witness virtual machine is not managed by the specified
            vCenter server.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user has insufficient privilege to perform the operation.
            Operation execution requires the Global.VCServer privilege.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnverifiedPeer` 
            If the SSL certificate of the management vCenter server cannot be
            validated.
            The value of the data attribute of
            :class:`com.vmware.vapi.std.errors_client.Error` will be a class
            that contains all the attributes defined in
            :class:`CertificateInfo`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If any other error occurs.
        """
        task_id = self._invoke('undeploy$task',
                                {
                                'spec': spec,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance
class Operations(VapiInterface):
    """
    The ``Operations`` class provides methods to figure out the currently
    active operations and currently disabled operations in a vCenter High
    Availability (VCHA) cluster. This class was added in vSphere API 6.7.1.
    """
    CLUSTER_DEPLOY_OP = "com.vmware.vcenter.vcha.cluster.deploy"
    """
    Identifier of the cluster deploy operation. This class attribute was added in
    vSphere API 6.7.1.

    """
    CLUSTER_FAILOVER_OP = "com.vmware.vcenter.vcha.cluster.failover"
    """
    Identifier of the cluster failover operation. This class attribute was added in
    vSphere API 6.7.1.

    """
    CLUSTER_GET_OP = "com.vmware.vcenter.vcha.cluster.get"
    """
    Identifier of the cluster get operation. This class attribute was added in
    vSphere API 6.7.1.

    """
    PASSIVE_REDEPLOY_OP = "com.vmware.vcenter.vcha.cluster.passive.redeploy"
    """
    Identifier of the passive redeploy operation. This class attribute was added in
    vSphere API 6.7.1.

    """
    WITNESS_REDEPLOY_OP = "com.vmware.vcenter.vcha.cluster.witness.redeploy"
    """
    Identifier of the witness redeploy operation. This class attribute was added in
    vSphere API 6.7.1.

    """
    MODE_GET_OP = "com.vmware.vcenter.vcha.cluster.mode.get"
    """
    Identifier of the get mode operation. This class attribute was added in vSphere
    API 6.7.1.

    """
    MODE_SET_OP = "com.vmware.vcenter.vcha.cluster.mode.set"
    """
    Identifier of the set mode operation. This class attribute was added in vSphere
    API 6.7.1.

    """
    CLUSTER_UNDEPLOY_OP = "com.vmware.vcenter.vcha.cluster.undeploy"
    """
    Identifier of the cluster undeploy operation. This class attribute was added in
    vSphere API 6.7.1.

    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.vcha.operations'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _OperationsStub)

    class Info(VapiStruct):
        """
        The ``Operations.Info`` class contains information about which the VCHA
        operations cannot be invoked in the current state of the system and the
        list of currently active VCHA operations. This class was added in vSphere
        API 6.7.1.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     disabled=None,
                     active=None,
                    ):
            """
            :type  disabled: :class:`set` of :class:`str`
            :param disabled: Identifiers of the operations that are current disabled. These
                operation strings are one of :attr:`Operations.CLUSTER_DEPLOY_OP`,
                :attr:`Operations.CLUSTER_FAILOVER_OP`,
                :attr:`Operations.PASSIVE_REDEPLOY_OP`,
                :attr:`Operations.WITNESS_REDEPLOY_OP`,
                :attr:`Operations.MODE_SET_OP`,
                :attr:`Operations.CLUSTER_UNDEPLOY_OP` and
                :attr:`Operations.CLUSTER_GET_OP`. This attribute was added in
                vSphere API 6.7.1.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vapi.operation``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``com.vmware.vapi.operation``.
            :type  active: :class:`set` of :class:`str`
            :param active: Identifiers of the operations that are currently running. These
                operation strings are one of :attr:`Operations.CLUSTER_DEPLOY_OP`,
                :attr:`Operations.CLUSTER_FAILOVER_OP`,
                :attr:`Operations.PASSIVE_REDEPLOY_OP`,
                :attr:`Operations.WITNESS_REDEPLOY_OP`,
                :attr:`Operations.MODE_SET_OP`, and
                :attr:`Operations.CLUSTER_UNDEPLOY_OP`. This attribute was added in
                vSphere API 6.7.1.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vapi.operation``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``com.vmware.vapi.operation``.
            """
            self.disabled = disabled
            self.active = active
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vcha.operations.info', {
            'disabled': type.SetType(type.IdType()),
            'active': type.SetType(type.IdType()),
        },
        Info,
        False,
        None))



    def get(self):
        """
        Retrieves the current active and disabled operations of a VCHA cluster.
        This method was added in vSphere API 6.7.1.


        :rtype: :class:`Operations.Info`
        :return: Info structure containing the current running and disabled
            operations of a VCHA cluster.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user has insufficient privilege to perform the operation.
            Operation execution requires the System.Read privilege.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If any other error occurs.
        """
        return self._invoke('get', None)
class _ClusterStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for deploy operation
        deploy_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Cluster.DeploySpec'),
        })
        deploy_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unverified_peer':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnverifiedPeer'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        deploy_input_value_validator_list = [
        ]
        deploy_output_validator_list = [
        ]
        deploy_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vcha/cluster',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for failover operation
        failover_input_type = type.StructType('operation-input', {
            'planned': type.BooleanType(),
        })
        failover_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        failover_input_value_validator_list = [
        ]
        failover_output_validator_list = [
        ]
        failover_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vcha/cluster',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vc_spec': type.OptionalType(type.ReferenceType(__name__, 'CredentialsSpec')),
            'partial': type.OptionalType(type.BooleanType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unverified_peer':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnverifiedPeer'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vcha/cluster',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for undeploy operation
        undeploy_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Cluster.UndeploySpec'),
        })
        undeploy_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unverified_peer':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnverifiedPeer'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        undeploy_input_value_validator_list = [
        ]
        undeploy_output_validator_list = [
        ]
        undeploy_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vcha/cluster',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'deploy$task': {
                'input_type': deploy_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': deploy_error_dict,
                'input_value_validator_list': deploy_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'failover$task': {
                'input_type': failover_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': failover_error_dict,
                'input_value_validator_list': failover_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Cluster.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'undeploy$task': {
                'input_type': undeploy_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': undeploy_error_dict,
                'input_value_validator_list': undeploy_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'deploy': deploy_rest_metadata,
            'failover': failover_rest_metadata,
            'get': get_rest_metadata,
            'undeploy': undeploy_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vcha.cluster',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _OperationsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vcha/operations',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Operations.Info'),
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
            self, iface_name='com.vmware.vcenter.vcha.operations',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Cluster': Cluster,
        'Operations': Operations,
        'cluster': 'com.vmware.vcenter.vcha.cluster_client.StubFactory',
    }

