# Tapioca Freshdesk

A Python API client for Freshdesk API v2

Freshdesk's API docs are here: https://developers.freshdesk.com/api/

As of now, it supports the following:
- contacts

It's very easy to implement the other endpoints. Just have a look at ```tapioca_freshdesk/resource_mapping.py```


## Installation
```
pip install git+https://github.com/tobiase/tapioca-freshdesk
```

## Instantiate client
```python
from tapioca_freshdesk import Freshdesk


api = Freshdesk(
    api_root="{https://example.freshdesk.com/api/v2/}", user="{your-user}", password="{your-password}"
)

```

or

```python
from tapioca_freshdesk import Freshdesk


api = Freshdesk(api_root="{https://example.freshdesk.com}", user='{your-api-key}')
```
Notice: The api_root URL must be entered with it's schema, ```https://``` or ```http://```.

## Implemented Endpoints

### Contacts

A contact is a customer or a potential customer who has raised a support ticket through any channel.


#### Create a contact 

*POST /api/v2/contacts*

```python
user = {
    "name": "Super Man",
    "email": "superman@freshdesk.com",
    "other_emails": ["lex@freshdesk.com", "louis@freshdesk.com"],
}
api.contacts().post(data=user)
```

https://developers.freshdesk.com/api/#create_contact

#### View a contact 

*GET /api/v2/contacts/[id]*

```python
api.contact(id=434).get()
```

https://developers.freshdesk.com/api/#view_contact


#### List all contacts  

*GET /api/v2/contacts*

```python
# Get all contacts
api.contacts().get()

# Filter contacts by state
api.contacts().get(params={"state": "unverified"})

# Get soft deleted contacts
api.contacts().get(params={"state": "deleted"})
```

https://developers.freshdesk.com/api/#list_all_contacts


#### Filter contacts

*GET /api/v2/search/contacts?query=[query]*

```python
api.contacts_filter().get(params={"query": '"active:true"'})
```

https://developers.freshdesk.com/api/#filter_contacts


#### Update a contact

*PUT /api/v2/contacts/[id]*

```python
api.contact(id=432).put(
    data={
        "name": "Clark Kent",
        "job_title": "Journalist",
        "other_emails": ["louis@freshdesk.com", "jonathan.kent@freshdesk.com"],
    }
)
```

https://developers.freshdesk.com/api/#update_contact


#### Soft delete a contact

*DELETE /api/v2/contacts/[id]*

```python
api.contact(id=432).delete()
```

https://developers.freshdesk.com/api/#delete_contact


#### Restore a contact

*PUT api/v2/contacts/[id]/restore*

```python
api.contact_restore(id=432).put()
```

https://developers.freshdesk.com/api/#restore_contact


#### Permanently delete a contact

*DELETE /api/v2/contacts/[id]/hard_delete*

```python
api.contact_delete(id=432).delete()

# Force delete a contact that is not soft deleted already.
api.contact_delete(id=432).delete(params={"force": "true"})
```

https://developers.freshdesk.com/api/#hard_delete_contact


#### Make agent

*PUT /api/v2/contacts/[id]/make_agent*

```python
api.contact_make_agent(id=432).put()

# Make occasional agent
api.contact_make_agent(id=432).put(data={"occasional": "true"})
```

https://developers.freshdesk.com/api/#make_agent


#### List all contact fields

*GET /api/v2/contact_fields*

```python
api.contact_fields().get()
```

https://developers.freshdesk.com/api/#list_all_contact_fields


#### Send invite to a contact

*PUT api/v2/contacts/[id]/send_invite*

```python
api.contact_send_invite(id=432).put()
```

https://developers.freshdesk.com/api/#send_invite


#### Merge contacts

*POST api/v2/contacts/merge*

```python
api.contacts_merge().post(
    data={"primary_contact_id": 432, "secondary_contact_ids": [433]}
)
````

https://developers.freshdesk.com/api/#merge_contact

---

- Learn how Tapioca works [here](http://tapioca-wrapper.readthedocs.org/en/stable/quickstart.html)
- Explore this package using iPython
- Have fun!
