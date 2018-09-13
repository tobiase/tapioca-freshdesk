# coding: utf-8

RESOURCE_MAPPING = {
    "contact": {
        "resource": "contacts/{id}",
        "docs": [
            "https://developers.freshdesk.com/api/#contacts",
            "https://developers.freshdesk.com/api/#update_contact",
            "https://developers.freshdesk.com/api/#delete_contact",
        ],
        "methods": ["GET", "PUT", "DELETE"],
    },
    "contacts": {
        "resource": "contacts",
        "docs": [
            "https://developers.freshdesk.com/api/#contacts",
            "https://developers.freshdesk.com/api/#create_contact",
        ],
        "methods": ["GET", "POST"],
    },
    "contacts_filter": {
        "resource": "search/contacts",
        "docs": "https://developers.freshdesk.com/api/#filter_contacts",
        "methods": ["GET"],
    },
    "contact_delete": {
        "resource": "contacts/{id}/hard_delete",
        "docs": "https://developers.freshdesk.com/api/#hard_delete_contact",
        "methods": ["DELETE"],
    },
    "contact_restore": {
        "resource": "contacts/{id}/restore",
        "docs": "https://developers.freshdesk.com/api/#restore_contact",
        "methods": ["PUT"],
    },
    "contact_fields": {
        "resource": "contact_fields",
        "docs": "https://developers.freshdesk.com/api/#list_all_contact_fields",
        "methods": ["GET"],
    },
    "contact_make_agent": {
        "resource": "contacts/{id}/make_agent",
        "docs": "https://developers.freshdesk.com/api/#make_agent",
        "methods": ["PUT"],
    },
    "contact_send_invite": {
        "resource": "contacts/{id}/send_invite",
        "docs": "https://developers.freshdesk.com/api/#send_invite",
        "methods": ["PUT"]
    },
    "contacts_merge": {
        "resource": "contacts/merge",
        "docs": "https://developers.freshdesk.com/api/#merge_contact",
        "methods": ["POST"]
    }
}
