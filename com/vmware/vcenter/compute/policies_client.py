# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.compute.policies.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.compute.policies_client`` module provides classes for
managing compute policies.

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


class CreateSpec(VapiStruct):
    """
    The ``CreateSpec`` class contains common information used to create a new
    policy. **Warning:** This class is available as technical preview. It may
    be changed in a future release.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 description=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the policy. The name needs to be unique within this vCenter
            server. **Warning:** This attribute is available as technical
            preview. It may be changed in a future release.
        :type  description: :class:`str`
        :param description: Description of the policy. **Warning:** This attribute is available
            as technical preview. It may be changed in a future release.
        """
        self.name = name
        self.description = description
        VapiStruct.__init__(self)


CreateSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.compute.policies.create_spec', {
        'name': type.StringType(),
        'description': type.StringType(),
    },
    CreateSpec,
    False,
    None))



class Info(VapiStruct):
    """
    The ``Info`` class contains common information about a compute policy.
    **Warning:** This class is available as technical preview. It may be
    changed in a future release.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 description=None,
                 capability=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the policy. **Warning:** This attribute is available as
            technical preview. It may be changed in a future release.
        :type  description: :class:`str`
        :param description: Description of the policy. **Warning:** This attribute is available
            as technical preview. It may be changed in a future release.
        :type  capability: :class:`str`
        :param capability: Identifier of the capability this policy is based on. **Warning:**
            This attribute is available as technical preview. It may be changed
            in a future release.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vcenter.compute.policies.Capability``. When methods
            return a value of this class as a return value, the attribute will
            be an identifier for the resource type:
            ``com.vmware.vcenter.compute.policies.Capability``.
        """
        self.name = name
        self.description = description
        self.capability = capability
        VapiStruct.__init__(self)


Info._set_binding_type(type.StructType(
    'com.vmware.vcenter.compute.policies.info', {
        'name': type.StringType(),
        'description': type.StringType(),
        'capability': type.IdType(resource_types='com.vmware.vcenter.compute.policies.Capability'),
    },
    Info,
    False,
    None))



class Status(VapiStruct):
    """
    The ``Status`` class describes the current status of a compute policy.
    **Warning:** This class is available as technical preview. It may be
    changed in a future release.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 status=None,
                ):
        """
        :type  status: :class:`Status.Compliance`
        :param status: The compliance status of the policy on a specified object.
            **Warning:** This attribute is available as technical preview. It
            may be changed in a future release.
        """
        self.status = status
        VapiStruct.__init__(self)


    class Compliance(Enum):
        """
        The ``Status.Compliance`` class defines the compliance states a policy can
        be in on a particular object. **Warning:** This enumeration is available as
        technical preview. It may be changed in a future release.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        NOT_APPLICABLE = None
        """
        The object is in a state for which the policy does not apply. **Warning:**
        This class attribute is available as technical preview. It may be changed
        in a future release.

        """
        COMPLIANT = None
        """
        The policy is in compliance on the object. **Warning:** This class
        attribute is available as technical preview. It may be changed in a future
        release.

        """
        NOT_COMPLIANT = None
        """
        The policy is not in compliance on the object. **Warning:** This class
        attribute is available as technical preview. It may be changed in a future
        release.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Compliance` instance.
            """
            Enum.__init__(string)

    Compliance._set_values([
        Compliance('NOT_APPLICABLE'),
        Compliance('COMPLIANT'),
        Compliance('NOT_COMPLIANT'),
    ])
    Compliance._set_binding_type(type.EnumType(
        'com.vmware.vcenter.compute.policies.status.compliance',
        Compliance))

Status._set_binding_type(type.StructType(
    'com.vmware.vcenter.compute.policies.status', {
        'status': type.ReferenceType(__name__, 'Status.Compliance'),
    },
    Status,
    False,
    None))



class Capabilities(VapiInterface):
    """
    The ``Capabilities`` class provides methods to manage compute policy
    capabilities. The description of the capability provides information about
    the intent of a policy based on this capability. A capability provides a
    type to create a policy (see
    :func:`com.vmware.vcenter.compute_client.Policies.create`). A capability
    also provides a type that describes the information returned when
    retrieving information about a policy (see
    :func:`com.vmware.vcenter.compute_client.Policies.get`). **Warning:** This
    class is available as technical preview. It may be changed in a future
    release.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.compute.policies.Capability"
    """
    The resource type for the compute policy capability. **Warning:** This class
    attribute is available as technical preview. It may be changed in a future
    release.

    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.compute.policies.capabilities'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CapabilitiesStub)

    class Summary(VapiStruct):
        """
        The ``Capabilities.Summary`` class contains commonly used information about
        a compute policy capability. **Warning:** This class is available as
        technical preview. It may be changed in a future release.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     capability=None,
                     name=None,
                     description=None,
                    ):
            """
            :type  capability: :class:`str`
            :param capability: Identifier of the capability. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.compute.policies.Capability``. When methods
                return a value of this class as a return value, the attribute will
                be an identifier for the resource type:
                ``com.vmware.vcenter.compute.policies.Capability``.
            :type  name: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param name: Name of the capability. **Warning:** This attribute is available as
                technical preview. It may be changed in a future release.
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of the capability. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
            """
            self.capability = capability
            self.name = name
            self.description = description
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.compute.policies.capabilities.summary', {
            'capability': type.IdType(resource_types='com.vmware.vcenter.compute.policies.Capability'),
            'name': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        },
        Summary,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Capabilities.Info`` class contains information about a compute policy
        capability. **Warning:** This class is available as technical preview. It
        may be changed in a future release.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     description=None,
                     create_spec_type=None,
                     info_type=None,
                    ):
            """
            :type  name: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param name: Name of the capability. **Warning:** This attribute is available as
                technical preview. It may be changed in a future release.
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of the capability. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
            :type  create_spec_type: :class:`str`
            :param create_spec_type: Identifier of the class used to create a policy based on this
                capability. See
                :func:`com.vmware.vcenter.compute_client.Policies.create`.
                **Warning:** This attribute is available as technical preview. It
                may be changed in a future release.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.structure``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.structure``.
            :type  info_type: :class:`str`
            :param info_type: Identifier of the class returned when retrieving information about
                a policy based on this capability. See
                :func:`com.vmware.vcenter.compute_client.Policies.get`.
                **Warning:** This attribute is available as technical preview. It
                may be changed in a future release.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.structure``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.structure``.
            """
            self.name = name
            self.description = description
            self.create_spec_type = create_spec_type
            self.info_type = info_type
            VapiStruct.__init__(self)


    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.compute.policies.capabilities.info', {
            'name': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'create_spec_type': type.IdType(resource_types='com.vmware.vapi.structure'),
            'info_type': type.IdType(resource_types='com.vmware.vapi.structure'),
        },
        Info,
        False,
        None))



    def list(self):
        """
        Returns information about the compute policy capabilities available in
        this vCenter server. **Warning:** This method is available as technical
        preview. It may be changed in a future release.


        :rtype: :class:`list` of :class:`Capabilities.Summary`
        :return: The list of compute policy capabilities available on this vCenter
            server.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('list', None)

    def get(self,
            capability,
            ):
        """
        Returns information about a specific compute policy capability.
        **Warning:** This method is available as technical preview. It may be
        changed in a future release.

        :type  capability: :class:`str`
        :param capability: Identifier of the capability for which information should be
            retrieved.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.compute.policies.Capability``.
        :rtype: :class:`Capabilities.Info`
        :return: Detailed information about the capability.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a capability with this identifier does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'capability': capability,
                            })
class TagUsage(VapiInterface):
    """
    The ``TagUsage`` class provides methods to query which tags are used by
    policies. **Warning:** This class is available as technical preview. It may
    be changed in a future release.
    """

    _VAPI_SERVICE_ID = 'com.vmware.vcenter.compute.policies.tag_usage'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TagUsageStub)

    class Summary(VapiStruct):
        """
        The ``TagUsage.Summary`` class contains common information about a tag used
        by a policy. **Warning:** This class is available as technical preview. It
        may be changed in a future release.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     policy=None,
                     tag_type=None,
                     tag=None,
                     tag_name=None,
                     category_name=None,
                    ):
            """
            :type  policy: :class:`str`
            :param policy: Identifier of the policy that uses the tag indicated by
                :attr:`TagUsage.Summary.tag`. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.compute.Policy``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.compute.Policy``.
            :type  tag_type: :class:`str`
            :param tag_type: Identifier of the tag type used by the policy indicated by
                :attr:`TagUsage.Summary.policy`. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.resource``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.resource``.
            :type  tag: :class:`str`
            :param tag: Identifier of the tag used by the policy indicated by
                :attr:`TagUsage.Summary.policy`. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
                When clients pass a value of this class as a parameter, the
                attribute ``tagType`` must contain the actual resource type. When
                methods return a value of this class as a return value, the
                attribute ``tagType`` will contain the actual resource type.
            :type  tag_name: :class:`str`
            :param tag_name: Name of the tag used by the policy indicated by
                :attr:`TagUsage.Summary.policy`. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
            :type  category_name: :class:`str`
            :param category_name: Name of the category that has :attr:`TagUsage.Summary.tag`.
                **Warning:** This attribute is available as technical preview. It
                may be changed in a future release.
            """
            self.policy = policy
            self.tag_type = tag_type
            self.tag = tag
            self.tag_name = tag_name
            self.category_name = category_name
            VapiStruct.__init__(self)


    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.compute.policies.tag_usage.summary', {
            'policy': type.IdType(resource_types='com.vmware.vcenter.compute.Policy'),
            'tag_type': type.IdType(resource_types='com.vmware.vapi.resource'),
            'tag': type.IdType(resource_types=[], resource_type_field_name="tag_type"),
            'tag_name': type.StringType(),
            'category_name': type.StringType(),
        },
        Summary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``TagUsage.FilterSpec`` class contains attributes used to filter the
        results when listing the tags used by policies as available in this vCenter
        server (see :func:`TagUsage.list`). If multiple attributes are specified,
        only the tags used by policies that match an element of each attribute
        match the filter. **Warning:** This class is available as technical
        preview. It may be changed in a future release.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     policies=None,
                     tags=None,
                     tag_types=None,
                    ):
            """
            :type  policies: :class:`set` of :class:`str` or ``None``
            :param policies: Identifiers that compute policies must have to match the filter.
                **Warning:** This attribute is available as technical preview. It
                may be changed in a future release.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.compute.Policy``. When methods return a value
                of this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.vcenter.compute.Policy``.
                If None or empty, then tags used by any policy match this filter.
            :type  tags: :class:`set` of :class:`str` or ``None``
            :param tags: Identifiers that tags must have to match the filter. **Warning:**
                This attribute is available as technical preview. It may be changed
                in a future release.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.cis.tagging.Tag``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``com.vmware.cis.tagging.Tag``.
                If None or empty, then tags with any tag identifier match this
                filter.
            :type  tag_types: :class:`set` of :class:`str` or ``None``
            :param tag_types: Identifiers that tag types must have to match the filter.
                **Warning:** This attribute is available as technical preview. It
                may be changed in a future release.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vapi.resource``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``com.vmware.vapi.resource``.
                If None or empty, then tags of any type match this filter.
            """
            self.policies = policies
            self.tags = tags
            self.tag_types = tag_types
            VapiStruct.__init__(self)


    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.compute.policies.tag_usage.filter_spec', {
            'policies': type.OptionalType(type.SetType(type.IdType())),
            'tags': type.OptionalType(type.SetType(type.IdType())),
            'tag_types': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns information about the tags used by policies available in this
        vCenter server matching the :class:`TagUsage.FilterSpec`. **Warning:**
        This method is available as technical preview. It may be changed in a
        future release.

        :type  filter: :class:`TagUsage.FilterSpec` or ``None``
        :param filter: Specification for matching tags used by policies.
            If None, the behavior is equivalent to a
            :class:`TagUsage.FilterSpec` with all attributes None, which means
            all tags used by policies match the filter.
        :rtype: :class:`list` of :class:`TagUsage.Summary`
        :return: The list of tags used by policies available on this vCenter server
            matching the :class:`TagUsage.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })
class _CapabilitiesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/compute/policies/capabilities',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'capability': type.IdType(resource_types='com.vmware.vcenter.compute.policies.Capability'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/compute/policies/capabilities/{capability}',
            path_variables={
                'capability': 'capability',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Capabilities.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Capabilities.Info'),
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
            self, iface_name='com.vmware.vcenter.compute.policies.capabilities',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _TagUsageStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'TagUsage.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/compute/policies/tag-usage',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'TagUsage.Summary')),
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
            self, iface_name='com.vmware.vcenter.compute.policies.tag_usage',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Capabilities': Capabilities,
        'TagUsage': TagUsage,
        'capabilities': 'com.vmware.vcenter.compute.policies.capabilities_client.StubFactory',
    }

