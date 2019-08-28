# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2019 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx.firewall.
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


class Excludelist(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.firewall.excludelist'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ExcludelistStub)


    def addmember(self,
                  resource_reference,
                  ):
        """
        Add a new object in the exclude list

        :type  resource_reference: :class:`com.vmware.nsx.model_client.ResourceReference`
        :param resource_reference: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ResourceReference`
        :return: com.vmware.nsx.model.ResourceReference
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
        return self._invoke('addmember',
                            {
                            'resource_reference': resource_reference,
                            })

    def checkifexists(self,
                      object_id,
                      ):
        """
        Check if the object a member of the exclude list

        :type  object_id: :class:`str`
        :param object_id: identifier of the object (required)
        :rtype: :class:`com.vmware.nsx.model_client.ResourceReference`
        :return: com.vmware.nsx.model.ResourceReference
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
        return self._invoke('checkifexists',
                            {
                            'object_id': object_id,
                            })

    def get(self):
        """
        Get list of entities in exclude list


        :rtype: :class:`com.vmware.nsx.model_client.ExcludeList`
        :return: com.vmware.nsx.model.ExcludeList
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

    def removemember(self,
                     object_id,
                     ):
        """
        Remove an existing object from the exclude list

        :type  object_id: :class:`str`
        :param object_id: identifier of the object (required)
        :rtype: :class:`com.vmware.nsx.model_client.ResourceReference`
        :return: com.vmware.nsx.model.ResourceReference
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
        return self._invoke('removemember',
                            {
                            'object_id': object_id,
                            })

    def update(self,
               exclude_list,
               ):
        """
        Modify exclude list

        :type  exclude_list: :class:`com.vmware.nsx.model_client.ExcludeList`
        :param exclude_list: (required)
        :rtype: :class:`com.vmware.nsx.model_client.ExcludeList`
        :return: com.vmware.nsx.model.ExcludeList
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
                            'exclude_list': exclude_list,
                            })
class Rules(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.firewall.rules'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RulesStub)


    def get(self,
            rule_id,
            ):
        """
        Return existing firewall rule information.

        :type  rule_id: :class:`str`
        :param rule_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallRule`
        :return: com.vmware.nsx.model.FirewallRule
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
                            'rule_id': rule_id,
                            })
class Sections(VapiInterface):
    """
    
    """
    CREATE_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Sections.create`.

    """
    CREATE_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Sections.create`.

    """
    CREATE_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Sections.create`.

    """
    CREATE_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Sections.create`.

    """
    CREATEWITHRULES_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Sections.createwithrules`.

    """
    CREATEWITHRULES_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Sections.createwithrules`.

    """
    CREATEWITHRULES_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Sections.createwithrules`.

    """
    CREATEWITHRULES_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Sections.createwithrules`.

    """
    LIST_ENFORCED_ON_VIF = "VIF"
    """
    Possible value for ``enforcedOn`` of method :func:`Sections.list`.

    """
    LIST_ENFORCED_ON_LOGICALROUTER = "LOGICALROUTER"
    """
    Possible value for ``enforcedOn`` of method :func:`Sections.list`.

    """
    LIST_ENFORCED_ON_BRIDGEENDPOINT = "BRIDGEENDPOINT"
    """
    Possible value for ``enforcedOn`` of method :func:`Sections.list`.

    """
    LIST_ENFORCED_ON_DHCP_SERVICE = "DHCP_SERVICE"
    """
    Possible value for ``enforcedOn`` of method :func:`Sections.list`.

    """
    LIST_ENFORCED_ON_METADATA_PROXY = "METADATA_PROXY"
    """
    Possible value for ``enforcedOn`` of method :func:`Sections.list`.

    """
    LIST_ENFORCED_ON_L2VPN_SESSION = "L2VPN_SESSION"
    """
    Possible value for ``enforcedOn`` of method :func:`Sections.list`.

    """
    LIST_ENFORCED_ON_NONE = "NONE"
    """
    Possible value for ``enforcedOn`` of method :func:`Sections.list`.

    """
    LIST_EXCLUDE_APPLIED_TO_TYPE_NSGROUP = "NSGroup"
    """
    Possible value for ``excludeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_EXCLUDE_APPLIED_TO_TYPE_LOGICALSWITCH = "LogicalSwitch"
    """
    Possible value for ``excludeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_EXCLUDE_APPLIED_TO_TYPE_LOGICALROUTER = "LogicalRouter"
    """
    Possible value for ``excludeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_EXCLUDE_APPLIED_TO_TYPE_LOGICALPORT = "LogicalPort"
    """
    Possible value for ``excludeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_FILTER_TYPE_FILTER = "FILTER"
    """
    Possible value for ``filterType`` of method :func:`Sections.list`.

    """
    LIST_FILTER_TYPE_SEARCH = "SEARCH"
    """
    Possible value for ``filterType`` of method :func:`Sections.list`.

    """
    LIST_INCLUDE_APPLIED_TO_TYPE_NSGROUP = "NSGroup"
    """
    Possible value for ``includeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_INCLUDE_APPLIED_TO_TYPE_LOGICALSWITCH = "LogicalSwitch"
    """
    Possible value for ``includeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_INCLUDE_APPLIED_TO_TYPE_LOGICALROUTER = "LogicalRouter"
    """
    Possible value for ``includeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_INCLUDE_APPLIED_TO_TYPE_LOGICALPORT = "LogicalPort"
    """
    Possible value for ``includeAppliedToType`` of method :func:`Sections.list`.

    """
    LIST_TYPE_LAYER2 = "LAYER2"
    """
    Possible value for ``type`` of method :func:`Sections.list`.

    """
    LIST_TYPE_LAYER3 = "LAYER3"
    """
    Possible value for ``type`` of method :func:`Sections.list`.

    """
    REVISE_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Sections.revise`.

    """
    REVISE_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Sections.revise`.

    """
    REVISE_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Sections.revise`.

    """
    REVISE_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Sections.revise`.

    """
    REVISEWITHRULES_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`Sections.revisewithrules`.

    """
    REVISEWITHRULES_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`Sections.revisewithrules`.

    """
    REVISEWITHRULES_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`Sections.revisewithrules`.

    """
    REVISEWITHRULES_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`Sections.revisewithrules`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.firewall.sections'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SectionsStub)


    def create(self,
               firewall_section,
               id=None,
               operation=None,
               ):
        """
        Creates new empty firewall section in the system.

        :type  firewall_section: :class:`com.vmware.nsx.model_client.FirewallSection`
        :param firewall_section: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSection`
        :return: com.vmware.nsx.model.FirewallSection
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
        return self._invoke('create',
                            {
                            'firewall_section': firewall_section,
                            'id': id,
                            'operation': operation,
                            })

    def createwithrules(self,
                        firewall_section_rule_list,
                        id=None,
                        operation=None,
                        ):
        """
        Creates a new firewall section with rules. The limit on the number of
        rules is defined by maxItems in collection types for FirewallRule
        (FirewallRuleXXXList types). When invoked on a section with a large
        number of rules, this API is supported only at low rates of invocation
        (not more than 4-5 times per minute). The typical latency of this API
        with about 1024 rules is about 4-5 seconds. This API should not be
        invoked with large payloads at automation speeds. More than 50 rules
        with a large number of rule references is not supported. Instead, to
        create sections, use: POST /api/v1/firewall/sections To create rules,
        use: POST /api/v1/firewall/sections/<section-id>/rules

        :type  firewall_section_rule_list: :class:`com.vmware.nsx.model_client.FirewallSectionRuleList`
        :param firewall_section_rule_list: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSectionRuleList`
        :return: com.vmware.nsx.model.FirewallSectionRuleList
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
        return self._invoke('createwithrules',
                            {
                            'firewall_section_rule_list': firewall_section_rule_list,
                            'id': id,
                            'operation': operation,
                            })

    def delete(self,
               section_id,
               cascade=None,
               ):
        """
        Removes firewall section from the system. Firewall section with rules
        can only be deleted by passing \"cascade=true\" parameter.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  cascade: :class:`bool` or ``None``
        :param cascade: Flag to cascade delete of this object to all it's child objects.
            (optional, default to false)
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
        return self._invoke('delete',
                            {
                            'section_id': section_id,
                            'cascade': cascade,
                            })

    def get(self,
            section_id,
            ):
        """
        Returns information about firewall section for the identifier.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSection`
        :return: com.vmware.nsx.model.FirewallSection
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
                            'section_id': section_id,
                            })

    def list(self,
             applied_tos=None,
             cursor=None,
             destinations=None,
             enforced_on=None,
             exclude_applied_to_type=None,
             filter_type=None,
             include_applied_to_type=None,
             included_fields=None,
             locked=None,
             page_size=None,
             search_invalid_references=None,
             search_scope=None,
             services=None,
             sort_ascending=None,
             sort_by=None,
             sources=None,
             type=None,
             ):
        """
        List all firewall section in paginated form. A default page size is
        limited to 1000 firewall sections. By default list of section is
        filtered by LAYER3 type.

        :type  applied_tos: :class:`str` or ``None``
        :param applied_tos: AppliedTo's referenced by this section or section's Distributed
            Service Rules . (optional)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  destinations: :class:`str` or ``None``
        :param destinations: Destinations referenced by this section's Distributed Service Rules
            . (optional)
        :type  enforced_on: :class:`str` or ``None``
        :param enforced_on: Type of attachment for logical port; for query only. (optional)
        :type  exclude_applied_to_type: :class:`str` or ``None``
        :param exclude_applied_to_type: Resource type valid for use as AppliedTo filter in section API
            (optional)
        :type  filter_type: :class:`str` or ``None``
        :param filter_type: Filter type (optional, default to FILTER)
        :type  include_applied_to_type: :class:`str` or ``None``
        :param include_applied_to_type: Resource type valid for use as AppliedTo filter in section API
            (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  locked: :class:`bool` or ``None``
        :param locked: Limit results to sections which are locked/unlocked (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  search_invalid_references: :class:`bool` or ``None``
        :param search_invalid_references: Return invalid references in results. (optional, default to false)
        :type  search_scope: :class:`str` or ``None``
        :param search_scope: Limit result to sections of a specific enforcement point (optional)
        :type  services: :class:`str` or ``None``
        :param services: NSService referenced by this section's Distributed Service Rules .
            (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :type  sources: :class:`str` or ``None``
        :param sources: Sources referenced by this section's Distributed Service Rules .
            (optional)
        :type  type: :class:`str` or ``None``
        :param type: Section Type (optional, default to LAYER3)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSectionListResult`
        :return: com.vmware.nsx.model.FirewallSectionListResult
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
                            'applied_tos': applied_tos,
                            'cursor': cursor,
                            'destinations': destinations,
                            'enforced_on': enforced_on,
                            'exclude_applied_to_type': exclude_applied_to_type,
                            'filter_type': filter_type,
                            'include_applied_to_type': include_applied_to_type,
                            'included_fields': included_fields,
                            'locked': locked,
                            'page_size': page_size,
                            'search_invalid_references': search_invalid_references,
                            'search_scope': search_scope,
                            'services': services,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            'sources': sources,
                            'type': type,
                            })

    def listwithrules(self,
                      section_id,
                      ):
        """
        Returns firewall section information with rules for a section
        identifier. When invoked on a section with a large number of rules,
        this API is supported only at low rates of invocation (not more than
        4-5 times per minute). The typical latency of this API with about 1024
        rules is about 4-5 seconds. This API should not be invoked with large
        payloads at automation speeds. More than 50 rules with a large number
        rule references is not supported. Instead, to read firewall rules, use:
        GET /api/v1/firewall/sections/<section-id>/rules with the appropriate
        page_size.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSectionRuleList`
        :return: com.vmware.nsx.model.FirewallSectionRuleList
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
        return self._invoke('listwithrules',
                            {
                            'section_id': section_id,
                            })

    def lock(self,
             section_id,
             firewall_section_lock,
             ):
        """
        Lock a section

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  firewall_section_lock: :class:`com.vmware.nsx.model_client.FirewallSectionLock`
        :param firewall_section_lock: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSection`
        :return: com.vmware.nsx.model.FirewallSection
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
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
             Locked
        """
        return self._invoke('lock',
                            {
                            'section_id': section_id,
                            'firewall_section_lock': firewall_section_lock,
                            })

    def revise(self,
               section_id,
               firewall_section,
               id=None,
               operation=None,
               ):
        """
        Modifies an existing firewall section along with its relative position
        among other firewall sections in the system. Simultaneous update
        (modify) operations on same section are not allowed to prevent
        overwriting stale contents to firewall section. If a concurrent update
        is performed, HTTP response code 409 will be returned to the client
        operating on stale data. That client should retrieve the firewall
        section again and re-apply its update.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  firewall_section: :class:`com.vmware.nsx.model_client.FirewallSection`
        :param firewall_section: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSection`
        :return: com.vmware.nsx.model.FirewallSection
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
        return self._invoke('revise',
                            {
                            'section_id': section_id,
                            'firewall_section': firewall_section,
                            'id': id,
                            'operation': operation,
                            })

    def revisewithrules(self,
                        section_id,
                        firewall_section_rule_list,
                        id=None,
                        operation=None,
                        ):
        """
        Modifies an existing firewall section along with its relative position
        among other firewall sections with rules. When invoked on a large
        number of rules, this API is supported only at low rates of invocation
        (not more than 2 times per minute). The typical latency of this API
        with about 1024 rules is about 15 seconds in a cluster setup. This API
        should not be invoked with large payloads at automation speeds.
        Instead, to move a section above or below another section, use: POST
        /api/v1/firewall/sections/<section-id>?action=revise To modify rules,
        use: PUT /api/v1/firewall/sections/<section-id>/rules/<rule-id>
        Simultaneous update (modify) operations on same section are not allowed
        to prevent overwriting stale contents to firewall section. If a
        concurrent update is performed, HTTP response code 409 will be returned
        to the client operating on stale data. That client should retrieve the
        firewall section again and re-apply its update.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  firewall_section_rule_list: :class:`com.vmware.nsx.model_client.FirewallSectionRuleList`
        :param firewall_section_rule_list: (required)
        :type  id: :class:`str` or ``None``
        :param id: Identifier of the anchor rule or section. This is a required field
            in case operation like 'insert_before' and 'insert_after'.
            (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSectionRuleList`
        :return: com.vmware.nsx.model.FirewallSectionRuleList
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
        return self._invoke('revisewithrules',
                            {
                            'section_id': section_id,
                            'firewall_section_rule_list': firewall_section_rule_list,
                            'id': id,
                            'operation': operation,
                            })

    def unlock(self,
               section_id,
               firewall_section_lock,
               ):
        """
        Unlock a section

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  firewall_section_lock: :class:`com.vmware.nsx.model_client.FirewallSectionLock`
        :param firewall_section_lock: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSection`
        :return: com.vmware.nsx.model.FirewallSection
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
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
             Locked
        """
        return self._invoke('unlock',
                            {
                            'section_id': section_id,
                            'firewall_section_lock': firewall_section_lock,
                            })

    def update(self,
               section_id,
               firewall_section,
               ):
        """
        Modifies the specified section, but does not modify the section's
        associated rules. Simultaneous update (modify) operations on same
        section are not allowed to prevent overwriting stale contents to
        firewall section. If a concurrent update is performed, HTTP response
        code 409 will be returned to the client operating on stale data. That
        client should retrieve the firewall section again and re-apply its
        update.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  firewall_section: :class:`com.vmware.nsx.model_client.FirewallSection`
        :param firewall_section: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSection`
        :return: com.vmware.nsx.model.FirewallSection
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
                            'section_id': section_id,
                            'firewall_section': firewall_section,
                            })

    def updatewithrules(self,
                        section_id,
                        firewall_section_rule_list,
                        ):
        """
        Modifies existing firewall section along with its association with
        rules. When invoked on a large number of rules, this API is supported
        only at low rates of invocation (not more than 2 times per minute). The
        typical latency of this API with about 1024 rules is about 15 seconds
        in a cluster setup. This API should not be invoked with large payloads
        at automation speeds. Instead, to update rule content, use: PUT
        /api/v1/firewall/sections/<section-id>/rules/<rule-id> Simultaneous
        update (modify) operations on same section are not allowed to prevent
        overwriting stale contents to firewall section. If a concurrent update
        is performed, HTTP response code 409 will be returned to the client
        operating on stale data. That client should retrieve the firewall
        section again and re-apply its update.

        :type  section_id: :class:`str`
        :param section_id: (required)
        :type  firewall_section_rule_list: :class:`com.vmware.nsx.model_client.FirewallSectionRuleList`
        :param firewall_section_rule_list: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallSectionRuleList`
        :return: com.vmware.nsx.model.FirewallSectionRuleList
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
        return self._invoke('updatewithrules',
                            {
                            'section_id': section_id,
                            'firewall_section_rule_list': firewall_section_rule_list,
                            })
class Stats(VapiInterface):
    """
    
    """
    RESET_CATEGORY_L3DFW = "L3DFW"
    """
    Possible value for ``category`` of method :func:`Stats.reset`.

    """
    RESET_CATEGORY_L3EDGE = "L3EDGE"
    """
    Possible value for ``category`` of method :func:`Stats.reset`.

    """
    RESET_CATEGORY_L3BRIDGEPORT = "L3BRIDGEPORT"
    """
    Possible value for ``category`` of method :func:`Stats.reset`.

    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.firewall.stats'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatsStub)


    def reset(self,
              category,
              ):
        """
        Sets firewall rule statistics counter to zero. This operation is
        supported for given category, for example: L3DFW i.e. for all layer3
        firewall (transport nodes only) rules or L3EDGE i.e. for all layer3
        edge firewall (edge nodes only) rules or L3BRIDGEPORT i.e. for all
        layer3 bridge port firewall (bridge ports only) rules.

        :type  category: :class:`str`
        :param category: Aggregation Statistic Category (required)
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
        return self._invoke('reset',
                            {
                            'category': category,
                            })
class Status(VapiInterface):
    """
    
    """

    _VAPI_SERVICE_ID = 'com.vmware.nsx.firewall.status'
    """
    Identifier of the service in canonical form.
    """
    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatusStub)


    def disablefirewall(self,
                        context_type,
                        id,
                        ):
        """
        Disable firewall on target resource in dfw context

        :type  context_type: :class:`str`
        :param context_type: (required)
        :type  id: :class:`str`
        :param id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TargetResourceStatus`
        :return: com.vmware.nsx.model.TargetResourceStatus
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
        return self._invoke('disablefirewall',
                            {
                            'context_type': context_type,
                            'id': id,
                            })

    def enablefirewall(self,
                       context_type,
                       id,
                       ):
        """
        Enable firewall on target resource in dfw context

        :type  context_type: :class:`str`
        :param context_type: (required)
        :type  id: :class:`str`
        :param id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TargetResourceStatus`
        :return: com.vmware.nsx.model.TargetResourceStatus
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
        return self._invoke('enablefirewall',
                            {
                            'context_type': context_type,
                            'id': id,
                            })

    def get(self,
            context_type,
            ):
        """
        Get firewall global status for dfw context

        :type  context_type: :class:`str`
        :param context_type: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallStatus`
        :return: com.vmware.nsx.model.FirewallStatus
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
                            'context_type': context_type,
                            })

    def get_0(self,
              context_type,
              id,
              ):
        """
        Get firewall status for target resource in dfw context

        :type  context_type: :class:`str`
        :param context_type: (required)
        :type  id: :class:`str`
        :param id: (required)
        :rtype: :class:`com.vmware.nsx.model_client.TargetResourceStatus`
        :return: com.vmware.nsx.model.TargetResourceStatus
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
                            'context_type': context_type,
                            'id': id,
                            })

    def list(self):
        """
        List all firewall status for supported contexts


        :rtype: :class:`com.vmware.nsx.model_client.FirewallStatusListResult`
        :return: com.vmware.nsx.model.FirewallStatusListResult
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
        return self._invoke('list', None)

    def update(self,
               context_type,
               firewall_status,
               ):
        """
        Update global firewall status for dfw context

        :type  context_type: :class:`str`
        :param context_type: (required)
        :type  firewall_status: :class:`com.vmware.nsx.model_client.FirewallStatus`
        :param firewall_status: (required)
        :rtype: :class:`com.vmware.nsx.model_client.FirewallStatus`
        :return: com.vmware.nsx.model.FirewallStatus
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
                            'context_type': context_type,
                            'firewall_status': firewall_status,
                            })
class _ExcludelistStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for addmember operation
        addmember_input_type = type.StructType('operation-input', {
            'resource_reference': type.ReferenceType('com.vmware.nsx.model_client', 'ResourceReference'),
        })
        addmember_error_dict = {
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
        addmember_input_value_validator_list = [
        ]
        addmember_output_validator_list = [
        ]
        addmember_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/excludelist?action=add_member',
            request_body_parameter='resource_reference',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for checkifexists operation
        checkifexists_input_type = type.StructType('operation-input', {
            'object_id': type.StringType(),
        })
        checkifexists_error_dict = {
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
        checkifexists_input_value_validator_list = [
        ]
        checkifexists_output_validator_list = [
        ]
        checkifexists_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/excludelist?action=check_if_exists',
            path_variables={
            },
            query_parameters={
                'object_id': 'object_id',
            },
            content_type='application/json'
        )

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
            url_template='/api/v1/firewall/excludelist',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for removemember operation
        removemember_input_type = type.StructType('operation-input', {
            'object_id': type.StringType(),
        })
        removemember_error_dict = {
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
        removemember_input_value_validator_list = [
        ]
        removemember_output_validator_list = [
        ]
        removemember_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/excludelist?action=remove_member',
            path_variables={
            },
            query_parameters={
                'object_id': 'object_id',
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'exclude_list': type.ReferenceType('com.vmware.nsx.model_client', 'ExcludeList'),
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
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/firewall/excludelist',
            request_body_parameter='exclude_list',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'addmember': {
                'input_type': addmember_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ResourceReference'),
                'errors': addmember_error_dict,
                'input_value_validator_list': addmember_input_value_validator_list,
                'output_validator_list': addmember_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'checkifexists': {
                'input_type': checkifexists_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ResourceReference'),
                'errors': checkifexists_error_dict,
                'input_value_validator_list': checkifexists_input_value_validator_list,
                'output_validator_list': checkifexists_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ExcludeList'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'removemember': {
                'input_type': removemember_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ResourceReference'),
                'errors': removemember_error_dict,
                'input_value_validator_list': removemember_input_value_validator_list,
                'output_validator_list': removemember_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'ExcludeList'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'addmember': addmember_rest_metadata,
            'checkifexists': checkifexists_rest_metadata,
            'get': get_rest_metadata,
            'removemember': removemember_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.firewall.excludelist',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _RulesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'rule_id': type.StringType(),
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
            url_template='/api/v1/firewall/rules/{rule-id}',
            path_variables={
                'rule_id': 'rule-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallRule'),
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
            self, iface_name='com.vmware.nsx.firewall.rules',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SectionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'firewall_section': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSection'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        create_error_dict = {
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
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/sections',
            request_body_parameter='firewall_section',
            path_variables={
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for createwithrules operation
        createwithrules_input_type = type.StructType('operation-input', {
            'firewall_section_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionRuleList'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        createwithrules_error_dict = {
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
        createwithrules_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        createwithrules_output_validator_list = [
            HasFieldsOfValidator()
        ]
        createwithrules_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/sections?action=create_with_rules',
            request_body_parameter='firewall_section_rule_list',
            path_variables={
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'cascade': type.OptionalType(type.BooleanType()),
        })
        delete_error_dict = {
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
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/api/v1/firewall/sections/{section-id}',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'cascade': 'cascade',
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
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
            url_template='/api/v1/firewall/sections/{section-id}',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'applied_tos': type.OptionalType(type.StringType()),
            'cursor': type.OptionalType(type.StringType()),
            'destinations': type.OptionalType(type.StringType()),
            'enforced_on': type.OptionalType(type.StringType()),
            'exclude_applied_to_type': type.OptionalType(type.StringType()),
            'filter_type': type.OptionalType(type.StringType()),
            'include_applied_to_type': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'locked': type.OptionalType(type.BooleanType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'search_invalid_references': type.OptionalType(type.BooleanType()),
            'search_scope': type.OptionalType(type.StringType()),
            'services': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'sources': type.OptionalType(type.StringType()),
            'type': type.OptionalType(type.StringType()),
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
            url_template='/api/v1/firewall/sections',
            path_variables={
            },
            query_parameters={
                'applied_tos': 'applied_tos',
                'cursor': 'cursor',
                'destinations': 'destinations',
                'enforced_on': 'enforced_on',
                'exclude_applied_to_type': 'exclude_applied_to_type',
                'filter_type': 'filter_type',
                'include_applied_to_type': 'include_applied_to_type',
                'included_fields': 'included_fields',
                'locked': 'locked',
                'page_size': 'page_size',
                'search_invalid_references': 'search_invalid_references',
                'search_scope': 'search_scope',
                'services': 'services',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
                'sources': 'sources',
                'type': 'type',
            },
            content_type='application/json'
        )

        # properties for listwithrules operation
        listwithrules_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
        })
        listwithrules_error_dict = {
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
        listwithrules_input_value_validator_list = [
        ]
        listwithrules_output_validator_list = [
            HasFieldsOfValidator()
        ]
        listwithrules_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/sections/{section-id}?action=list_with_rules',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for lock operation
        lock_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'firewall_section_lock': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionLock'),
        })
        lock_error_dict = {
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
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),

        }
        lock_input_value_validator_list = [
        ]
        lock_output_validator_list = [
        ]
        lock_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/sections/{section-id}?action=lock',
            request_body_parameter='firewall_section_lock',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for revise operation
        revise_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'firewall_section': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSection'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        revise_error_dict = {
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
        revise_input_value_validator_list = [
        ]
        revise_output_validator_list = [
        ]
        revise_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/sections/{section-id}?action=revise',
            request_body_parameter='firewall_section',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for revisewithrules operation
        revisewithrules_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'firewall_section_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionRuleList'),
            'id': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        revisewithrules_error_dict = {
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
        revisewithrules_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        revisewithrules_output_validator_list = [
            HasFieldsOfValidator()
        ]
        revisewithrules_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/sections/{section-id}?action=revise_with_rules',
            request_body_parameter='firewall_section_rule_list',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
                'id': 'id',
                'operation': 'operation',
            },
            content_type='application/json'
        )

        # properties for unlock operation
        unlock_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'firewall_section_lock': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionLock'),
        })
        unlock_error_dict = {
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
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),

        }
        unlock_input_value_validator_list = [
        ]
        unlock_output_validator_list = [
        ]
        unlock_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/sections/{section-id}?action=unlock',
            request_body_parameter='firewall_section_lock',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'firewall_section': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSection'),
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
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/firewall/sections/{section-id}',
            request_body_parameter='firewall_section',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for updatewithrules operation
        updatewithrules_input_type = type.StructType('operation-input', {
            'section_id': type.StringType(),
            'firewall_section_rule_list': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionRuleList'),
        })
        updatewithrules_error_dict = {
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
        updatewithrules_input_value_validator_list = [
            HasFieldsOfValidator()
        ]
        updatewithrules_output_validator_list = [
            HasFieldsOfValidator()
        ]
        updatewithrules_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/sections/{section-id}?action=update_with_rules',
            request_body_parameter='firewall_section_rule_list',
            path_variables={
                'section_id': 'section-id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSection'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'createwithrules': {
                'input_type': createwithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionRuleList'),
                'errors': createwithrules_error_dict,
                'input_value_validator_list': createwithrules_input_value_validator_list,
                'output_validator_list': createwithrules_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSection'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'listwithrules': {
                'input_type': listwithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionRuleList'),
                'errors': listwithrules_error_dict,
                'input_value_validator_list': listwithrules_input_value_validator_list,
                'output_validator_list': listwithrules_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'lock': {
                'input_type': lock_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSection'),
                'errors': lock_error_dict,
                'input_value_validator_list': lock_input_value_validator_list,
                'output_validator_list': lock_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revise': {
                'input_type': revise_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSection'),
                'errors': revise_error_dict,
                'input_value_validator_list': revise_input_value_validator_list,
                'output_validator_list': revise_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revisewithrules': {
                'input_type': revisewithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionRuleList'),
                'errors': revisewithrules_error_dict,
                'input_value_validator_list': revisewithrules_input_value_validator_list,
                'output_validator_list': revisewithrules_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'unlock': {
                'input_type': unlock_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSection'),
                'errors': unlock_error_dict,
                'input_value_validator_list': unlock_input_value_validator_list,
                'output_validator_list': unlock_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSection'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'updatewithrules': {
                'input_type': updatewithrules_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallSectionRuleList'),
                'errors': updatewithrules_error_dict,
                'input_value_validator_list': updatewithrules_input_value_validator_list,
                'output_validator_list': updatewithrules_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'createwithrules': createwithrules_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'listwithrules': listwithrules_rest_metadata,
            'lock': lock_rest_metadata,
            'revise': revise_rest_metadata,
            'revisewithrules': revisewithrules_rest_metadata,
            'unlock': unlock_rest_metadata,
            'update': update_rest_metadata,
            'updatewithrules': updatewithrules_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.firewall.sections',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for reset operation
        reset_input_type = type.StructType('operation-input', {
            'category': type.StringType(),
        })
        reset_error_dict = {
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
        reset_input_value_validator_list = [
        ]
        reset_output_validator_list = [
        ]
        reset_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/stats?action=reset',
            path_variables={
            },
            query_parameters={
                'category': 'category',
            },
            content_type='application/json'
        )

        operations = {
            'reset': {
                'input_type': reset_input_type,
                'output_type': type.VoidType(),
                'errors': reset_error_dict,
                'input_value_validator_list': reset_input_value_validator_list,
                'output_validator_list': reset_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'reset': reset_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.firewall.stats',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for disablefirewall operation
        disablefirewall_input_type = type.StructType('operation-input', {
            'context_type': type.StringType(),
            'id': type.StringType(),
        })
        disablefirewall_error_dict = {
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
        disablefirewall_input_value_validator_list = [
        ]
        disablefirewall_output_validator_list = [
        ]
        disablefirewall_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/status/{context-type}/{id}?action=disable_firewall',
            path_variables={
                'context_type': 'context-type',
                'id': 'id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for enablefirewall operation
        enablefirewall_input_type = type.StructType('operation-input', {
            'context_type': type.StringType(),
            'id': type.StringType(),
        })
        enablefirewall_error_dict = {
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
        enablefirewall_input_value_validator_list = [
        ]
        enablefirewall_output_validator_list = [
        ]
        enablefirewall_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/api/v1/firewall/status/{context-type}/{id}?action=enable_firewall',
            path_variables={
                'context_type': 'context-type',
                'id': 'id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'context_type': type.StringType(),
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
            url_template='/api/v1/firewall/status/{context-type}',
            path_variables={
                'context_type': 'context-type',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'context_type': type.StringType(),
            'id': type.StringType(),
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
            url_template='/api/v1/firewall/status/{context-type}/{id}',
            path_variables={
                'context_type': 'context-type',
                'id': 'id',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/api/v1/firewall/status',
            path_variables={
            },
            query_parameters={
            },
            content_type='application/json'
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'context_type': type.StringType(),
            'firewall_status': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallStatus'),
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
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/api/v1/firewall/status/{context-type}',
            request_body_parameter='firewall_status',
            path_variables={
                'context_type': 'context-type',
            },
            query_parameters={
            },
            content_type='application/json'
        )

        operations = {
            'disablefirewall': {
                'input_type': disablefirewall_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TargetResourceStatus'),
                'errors': disablefirewall_error_dict,
                'input_value_validator_list': disablefirewall_input_value_validator_list,
                'output_validator_list': disablefirewall_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'enablefirewall': {
                'input_type': enablefirewall_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TargetResourceStatus'),
                'errors': enablefirewall_error_dict,
                'input_value_validator_list': enablefirewall_input_value_validator_list,
                'output_validator_list': enablefirewall_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallStatus'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'TargetResourceStatus'),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallStatusListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx.model_client', 'FirewallStatus'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'disablefirewall': disablefirewall_rest_metadata,
            'enablefirewall': enablefirewall_rest_metadata,
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx.firewall.status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Excludelist': Excludelist,
        'Rules': Rules,
        'Sections': Sections,
        'Stats': Stats,
        'Status': Status,
        'rules': 'com.vmware.nsx.firewall.rules_client.StubFactory',
        'sections': 'com.vmware.nsx.firewall.sections_client.StubFactory',
    }

