# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.topology.
#---------------------------------------------------------------------------

"""


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


class Nodes(VapiInterface):
    """
    The ``Nodes`` interface provides methods to retrieve vCenter and Platform
    Services Controller nodes information in the topology. This class was added
    in vSphere API 6.7.2.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.topology.nodes'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NodesStub)

    class ApplianceType(Enum):
        """
        The ``Nodes.ApplianceType`` class defines values for valid appliance types
        for the vCenter and Platform Services Controller node. See
        :class:`Nodes.Info`. This enumeration was added in vSphere API 6.7.2.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        VCSA_EMBEDDED = None
        """
        vCenter Server Appliance with an embedded Platform Services Controller.
        This class attribute was added in vSphere API 6.7.2.

        """
        VCSA_EXTERNAL = None
        """
        vCenter Server Appliance with an external Platform Services Controller.
        This class attribute was added in vSphere API 6.7.2.

        """
        PSC_EXTERNAL = None
        """
        An external Platform Services Controller. This class attribute was added in
        vSphere API 6.7.2.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ApplianceType` instance.
            """
            Enum.__init__(string)

    ApplianceType._set_values([
        ApplianceType('VCSA_EMBEDDED'),
        ApplianceType('VCSA_EXTERNAL'),
        ApplianceType('PSC_EXTERNAL'),
    ])
    ApplianceType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.topology.nodes.appliance_type',
        ApplianceType))


    class Info(VapiStruct):
        """
        The ``Nodes.Info`` class contains vCenter or Platform Services Controller
        node details. This class was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'VCSA_EMBEDDED' : [('replication_partners', True)],
                    'PSC_EXTERNAL' : [('replication_partners', True)],
                    'VCSA_EXTERNAL' : [('client_affinity', True)],
                }
            ),
        ]



        def __init__(self,
                     domain=None,
                     type=None,
                     replication_partners=None,
                     client_affinity=None,
                    ):
            """
            :type  domain: :class:`str`
            :param domain: Domain name of the node. This attribute was added in vSphere API
                6.7.2.
            :type  type: :class:`Nodes.ApplianceType`
            :param type: Appliance type of the node. This attribute was added in vSphere API
                6.7.2.
            :type  replication_partners: :class:`list` of :class:`str`
            :param replication_partners: List of replication partners' node identifiers. Identifiers can be
                either IP address or DNS resolvable name of the partner node. This
                attribute was added in vSphere API 6.7.2.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.VCenter.name``. When methods return a value of
                this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.vcenter.VCenter.name``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`Nodes.ApplianceType.VCSA_EMBEDDED` or
                :attr:`Nodes.ApplianceType.PSC_EXTERNAL`.
            :type  client_affinity: :class:`str`
            :param client_affinity: Identifier of the affinitized Platform Services Controller node.
                Identifier can be either IP address or DNS resolvable name of the
                affinitized node. This attribute was added in vSphere API 6.7.2.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.VCenter.name``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.vcenter.VCenter.name``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Nodes.ApplianceType.VCSA_EXTERNAL`.
            """
            self.domain = domain
            self.type = type
            self.replication_partners = replication_partners
            self.client_affinity = client_affinity
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.topology.nodes.info', {
            'domain': type.StringType(),
            'type': type.ReferenceType(__name__, 'Nodes.ApplianceType'),
            'replication_partners': type.OptionalType(type.ListType(type.IdType())),
            'client_affinity': type.OptionalType(type.IdType()),
        },
        Info,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Nodes.Summary`` class contains commonly used information of vCenter
        or Platform Services Controller node. This class was added in vSphere API
        6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'VCSA_EMBEDDED' : [('replication_partners', True)],
                    'PSC_EXTERNAL' : [('replication_partners', True)],
                    'VCSA_EXTERNAL' : [('client_affinity', True)],
                }
            ),
        ]



        def __init__(self,
                     node=None,
                     type=None,
                     replication_partners=None,
                     client_affinity=None,
                    ):
            """
            :type  node: :class:`str`
            :param node: Identifier for the vCenter or Platform Services Controller node.
                Identifier can be either IP address or DNS resolvable name of the
                node. This attribute was added in vSphere API 6.7.2.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.VCenter.name``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.vcenter.VCenter.name``.
            :type  type: :class:`Nodes.ApplianceType`
            :param type: Appliance type of the node. This attribute was added in vSphere API
                6.7.2.
            :type  replication_partners: :class:`list` of :class:`str`
            :param replication_partners: List of replication partners' node identifiers. Identifiers can be
                either IP address or DNS resolvable name of the partner node. This
                attribute was added in vSphere API 6.7.2.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.VCenter.name``. When methods return a value of
                this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.vcenter.VCenter.name``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`Nodes.ApplianceType.VCSA_EMBEDDED` or
                :attr:`Nodes.ApplianceType.PSC_EXTERNAL`.
            :type  client_affinity: :class:`str`
            :param client_affinity: Identifier of the affinitized Platform Services Controller node.
                Identifier can be either IP address or DNS resolvable name of the
                affinitized node. This attribute was added in vSphere API 6.7.2.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.VCenter.name``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.vcenter.VCenter.name``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Nodes.ApplianceType.VCSA_EXTERNAL`.
            """
            self.node = node
            self.type = type
            self.replication_partners = replication_partners
            self.client_affinity = client_affinity
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.topology.nodes.summary', {
            'node': type.IdType(resource_types='com.vmware.vcenter.VCenter.name'),
            'type': type.ReferenceType(__name__, 'Nodes.ApplianceType'),
            'replication_partners': type.OptionalType(type.ListType(type.IdType())),
            'client_affinity': type.OptionalType(type.IdType()),
        },
        Summary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Nodes.FilterSpec`` class contains attribute used to filter the
        results when listing vCenter and Platform Services Controller nodes (see
        :func:`Nodes.list`). This class was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     types=None,
                    ):
            """
            :type  types: :class:`set` of :class:`Nodes.ApplianceType` or ``None``
            :param types: Types of the appliance that a vCenter and Platform Services
                Controller node must be to match the filter (see
                :class:`Nodes.ApplianceType`. This attribute was added in vSphere
                API 6.7.2.
                If None or empty, node of any ApplianceType match the filter.
            """
            self.types = types
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.topology.nodes.filter_spec', {
            'types': type.OptionalType(type.SetType(type.ReferenceType(__name__, 'Nodes.ApplianceType'))),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns information about all vCenter and Platform Services Controller
        nodes matching the :class:`Nodes.FilterSpec`. This method was added in
        vSphere API 6.7.2.

        :type  filter: :class:`Nodes.FilterSpec` or ``None``
        :param filter: Specification of matching vCenter and Platform Services Controller
            nodes for which information should be returned.
            If None, the behavior is equivalent to a :class:`Nodes.FilterSpec`
            with all attributes None which means all nodes match the filter.
        :rtype: :class:`list` of :class:`Nodes.Summary`
        :return: commonly used information for all vCenter and Platform Services
            Controller nodes matching the :class:`Nodes.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`Nodes.FilterSpec.types` attribute contains a value
            that is not supported.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })

    def get(self,
            node,
            ):
        """
        Retrieve details for a given identifier of the vCenter or Platform
        Services Controller node. This method was added in vSphere API 6.7.2.

        :type  node: :class:`str`
        :param node: Identifier of the vCenter or Platform Services Controller node.
            Identifier can be either IP address or DNS resolvable name of the
            node.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.VCenter.name``.
        :rtype: :class:`Nodes.Info`
        :return: vCenter or Platform Services Controller node details with
            replication partners and client affinity information as applicable.
            See :class:`Nodes.Info`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if a node doesn't exist for given node identifier.
        """
        return self._invoke('get',
                            {
                            'node': node,
                            })
class ReplicationStatus(VapiInterface):
    """
    The ``ReplicationStatus`` interface provides methods to retrieve
    replication status information of vCenter and Platform Services Controller
    nodes of type VCSA_EMBEDDED/PSC_EXTERNAL (see :attr:`Nodes.Info.type`).
    This class was added in vSphere API 6.7.2.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.topology.replication_status'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ReplicationStatusStub)

    class Summary(VapiStruct):
        """
        The ``ReplicationStatus.Summary`` class contains replication information of
        partner vCenter or Platform Services Controller node of type
        VCSA_EMBEDDED/PSC_EXTERNAL (see :attr:`Nodes.Info.type`). This class was
        added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     node=None,
                     replication_partner=None,
                     partner_available=None,
                     status_available=None,
                     replicating=None,
                     change_lag=None,
                    ):
            """
            :type  node: :class:`str`
            :param node: Identifier for the vCenter or Platform Services Controller node.
                Identifier can be either IP address or DNS resolvable name of the
                node. This attribute was added in vSphere API 6.7.2.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.VCenter.name``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.vcenter.VCenter.name``.
            :type  replication_partner: :class:`str`
            :param replication_partner: Identifier for the vCenter or Platform Services Controller
                replication partner. Identifier can be either IP address or DNS
                resolvable name of the replication partner. This attribute was
                added in vSphere API 6.7.2.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.VCenter.name``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.vcenter.VCenter.name``.
            :type  partner_available: :class:`bool`
            :param partner_available: Indicates if the VMware Directory Service on partner is reachable
                or not. This attribute was added in vSphere API 6.7.2.
            :type  status_available: :class:`bool`
            :param status_available: Indicates if the replication status for the node with respect to
                replication partner can be retrieved or not. This attribute was
                added in vSphere API 6.7.2.
            :type  replicating: :class:`bool` or ``None``
            :param replicating: Indicates if node is processing replication changes from the
                replication partner. This attribute was added in vSphere API 6.7.2.
                This attribute will be None if the partner host or replication
                status is not available, i.e, if
                :attr:`ReplicationStatus.Summary.partner_available` or
                :attr:`ReplicationStatus.Summary.status_available` is false.
            :type  change_lag: :class:`long` or ``None``
            :param change_lag: Number of replication changes node is behind the replication
                partner. This attribute was added in vSphere API 6.7.2.
                This attribute will be None if the partner host or replication
                status is not available, i.e, if
                :attr:`ReplicationStatus.Summary.partner_available` or
                :attr:`ReplicationStatus.Summary.status_available` is false.
            """
            self.node = node
            self.replication_partner = replication_partner
            self.partner_available = partner_available
            self.status_available = status_available
            self.replicating = replicating
            self.change_lag = change_lag
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.topology.replication_status.summary', {
            'node': type.IdType(resource_types='com.vmware.vcenter.VCenter.name'),
            'replication_partner': type.IdType(resource_types='com.vmware.vcenter.VCenter.name'),
            'partner_available': type.BooleanType(),
            'status_available': type.BooleanType(),
            'replicating': type.OptionalType(type.BooleanType()),
            'change_lag': type.OptionalType(type.IntegerType()),
        },
        Summary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``ReplicationStatus.FilterSpec`` class contains attribute used to
        filter the results when listing replication status for the vCenter and
        Platform Services Controller nodes (see :func:`ReplicationStatus.list`) of
        type VCSA_EMBEDDED/PSC_EXTERNAL (see :attr:`Nodes.Info.type`). This class
        was added in vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     nodes=None,
                    ):
            """
            :type  nodes: :class:`set` of :class:`str` or ``None``
            :param nodes: Identifier that a vCenter and Platform Services Controller node
                must have to match the filter. (see
                :attr:`ReplicationStatus.Summary.node`). This attribute was added
                in vSphere API 6.7.2.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.VCenter.name``. When methods return a value of
                this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.vcenter.VCenter.name``.
                If None or empty, all vCenter and Platform Services Controller
                nodes of type VCSA_EMBEDDED/PSC_EXTERNAL match the filter.
            """
            self.nodes = nodes
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.topology.replication_status.filter_spec', {
            'nodes': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns the replication information of vCenter and Platform Services
        Controller nodes of type VCSA_EMBEDDED/PSC_EXTERNAL (see
        :attr:`Nodes.Info.type`) matching the
        :class:`ReplicationStatus.FilterSpec`. This method was added in vSphere
        API 6.7.2.

        :type  filter: :class:`ReplicationStatus.FilterSpec` or ``None``
        :param filter: Specification of matching vCenter and Platform Services Controller
            nodes for which information should be returned.
            If None, the behavior is equivalent to a
            :class:`ReplicationStatus.FilterSpec` with all attributes None
            which means all vCenter and Platform Services Controller nodes of
            type VCSA_EMBEDDED/PSC_EXTERNAL match the filter.
        :rtype: :class:`list` of :class:`ReplicationStatus.Summary`
        :return: Commonly used replication information about vCenter and Platform
            Services Controller nodes matching the
            :class:`ReplicationStatus.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`ReplicationStatus.FilterSpec.nodes` attribute
            contains a invalid value.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })
class Pscs(VapiInterface):
    """
    The ``Pscs`` class provides methods to decommission the external Platform
    Services Controller node. This class was added in vSphere API 6.7.2.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.topology.pscs'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PscsStub)

    class DecommissionSpec(VapiStruct):
        """
        The ``Pscs.DecommissionSpec`` class contains information about the Platform
        Services Controller node to be decommissioned. This class was added in
        vSphere API 6.7.2.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     sso_admin_username=None,
                     sso_admin_password=None,
                     ssl_thumbprint=None,
                     ssl_verify=None,
                    ):
            """
            :type  sso_admin_username: :class:`str`
            :param sso_admin_username: The SSO administrator username for example
                "administrator\\\\@vsphere.local". This attribute was added in
                vSphere API 6.7.2.
            :type  sso_admin_password: :class:`str`
            :param sso_admin_password: The SSO administrator account password. This attribute was added in
                vSphere API 6.7.2.
            :type  ssl_thumbprint: :class:`str` or ``None``
            :param ssl_thumbprint: SHA1 thumbprint of the external Platform Services Controller node
                to be decommissioned that will be used for verification. This
                attribute was added in vSphere API 6.7.2.
                This attribute is only relevant if ``sslVerify`` is :class:`set` or
                has the value true. No verification will be performed if
                ``sslVerify`` value is set to false.
            :type  ssl_verify: :class:`bool` or ``None``
            :param ssl_verify: SSL verification should be enabled or disabled. This attribute was
                added in vSphere API 6.7.2.
                If None, ssl_verify false will be used.
            """
            self.sso_admin_username = sso_admin_username
            self.sso_admin_password = sso_admin_password
            self.ssl_thumbprint = ssl_thumbprint
            self.ssl_verify = ssl_verify
            VapiStruct.__init__(self)


    DecommissionSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.topology.pscs.decommission_spec', {
            'sso_admin_username': type.StringType(),
            'sso_admin_password': type.SecretType(),
            'ssl_thumbprint': type.OptionalType(type.StringType()),
            'ssl_verify': type.OptionalType(type.BooleanType()),
        },
        DecommissionSpec,
        False,
        None))




    def decommission_task(self,
                     hostname,
                     spec,
                     only_precheck=None,
                     ):
        """
        Decommission the external Platform Services Controller node. This
        method was added in vSphere API 6.7.2.

        :type  hostname: :class:`str`
        :param hostname: FQDN or IP address of external Platform Services Controller node to
            be decommissioned.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.VCenter.name``.
        :type  spec: :class:`Pscs.DecommissionSpec`
        :param spec: Information needed to decommission the external Platform Services
            Controller node.
        :type  only_precheck: :class:`bool` or ``None``
        :param only_precheck: Flag indicating whether only a pre-check should be performed.
            If None the full decommission will be performed.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the appliance is in not a management node.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed arguments are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnverifiedPeer` 
            If the SSL certificate of the foreign external Platform Services
            Controller node cannot be validated. 
            The value of the data attribute of null will be a class that
            contains all the attributes defined in null.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the provided Platform Services Controller node doesn't qualify
            for decommission due to some reasons like it has some other nodes
            connected to it.
        """
        task_id = self._invoke('decommission$task',
                                {
                                'hostname': hostname,
                                'spec': spec,
                                'only_precheck': only_precheck,
                                })
        task_svc = Tasks(self._config)
        task_instance = Task(task_id, task_svc, type.VoidType())
        return task_instance
class _NodesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Nodes.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/topology/nodes',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'node': type.IdType(resource_types='com.vmware.vcenter.VCenter.name'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
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
            url_template='/vcenter/topology/nodes/{node}',
            path_variables={
                'node': 'node',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Nodes.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Nodes.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.topology.nodes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ReplicationStatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'ReplicationStatus.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/topology/replication-status',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'ReplicationStatus.Summary')),
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
            self, iface_name='com.vmware.vcenter.topology.replication_status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _PscsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for decommission operation
        decommission_input_type = type.StructType('operation-input', {
            'hostname': type.IdType(resource_types='com.vmware.vcenter.VCenter.name'),
            'spec': type.ReferenceType(__name__, 'Pscs.DecommissionSpec'),
            'only_precheck': type.OptionalType(type.BooleanType()),
        })
        decommission_error_dict = {
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unverified_peer':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnverifiedPeer'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        decommission_input_value_validator_list = [
        ]
        decommission_output_validator_list = [
        ]
        decommission_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/topology/pscs/{hostname}?action=decommission',
            path_variables={
                'hostname': 'hostname',
            },
            query_parameters={
            }
        )

        operations = {
            'decommission$task': {
                'input_type': decommission_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.TASK'),
                'errors': decommission_error_dict,
                'input_value_validator_list': decommission_input_value_validator_list,
                'output_validator_list': [],
                'task_type': TaskType.TASK_ONLY,
            },
        }
        rest_metadata = {
            'decommission': decommission_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.topology.pscs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Nodes': Nodes,
        'ReplicationStatus': ReplicationStatus,
        'Pscs': Pscs,
    }

