# coding: utf-8

from tapioca import TapiocaAdapter, JSONAdapterMixin

from requests.auth import HTTPBasicAuth
from tapioca.tapioca import TapiocaInstantiator, TapiocaClient

from .resource_mapping import RESOURCE_MAPPING


def generate_wrapper_from_adapter(adapter_class):
    return FreshdeskTapiocaInstantiator(adapter_class)


class FreshdeskTapiocaInstantiator(TapiocaInstantiator):
    def __call__(self, serializer_class=None, session=None, api_root=None, **kwargs):
        refresh_token_default = kwargs.pop("refresh_token_by_default", False)
        return TapiocaClient(
            self.adapter_class(serializer_class=serializer_class, api_root=api_root),
            api_params=kwargs,
            refresh_token_by_default=refresh_token_default,
            session=session,
        )


class FreshdeskClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = None
    resource_mapping = RESOURCE_MAPPING

    def __init__(self, serializer_class=None, api_root=None, *args, **kwargs):
        self.api_root = api_root
        super(FreshdeskClientAdapter, self).__init__(serializer_class, *args, **kwargs)

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(FreshdeskClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs
        )

        params["auth"] = HTTPBasicAuth(
            api_params.get("user"), api_params.get("password", "")
        )

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(
        self, iterator_request_kwargs, response_data, response
    ):
        pass


Freshdesk = generate_wrapper_from_adapter(FreshdeskClientAdapter)
