import typing_extensions

from gotyai_client.apis.tags import TagValues
from gotyai_client.apis.tags.classify_api import ClassifyApi
from gotyai_client.apis.tags.admin_api import AdminApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CLASSIFY: ClassifyApi,
        TagValues.ADMIN: AdminApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CLASSIFY: ClassifyApi,
        TagValues.ADMIN: AdminApi,
    }
)
