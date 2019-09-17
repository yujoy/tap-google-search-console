# streams: API URL endpoints to be called
# properties:
#   <root node>: Plural stream name for the endpoint
#   path: API endpoint relative path, when added to the base URL, creates the full path
#   key_properties: Primary key fields for identifying an endpoint record.
#   replication_method: INCREMENTAL or FULL_TABLE
#   replication_keys: bookmark_field(s), typically a date-time, used for filtering the results
#        and setting the state
#   data_key: JSON element containing the records for the endpoint
#   api_method: GET or POST; default = 'GET'
#   params: Query, sort, and other endpoint specific parameters; default = {}
#   pagination: types are none, body, params; default = 'none'
#       none = no pagination
#       body = POST has startRow and rowLimit in body payload
#       params = GET has startRow and rowLimit in URL query params
#   sub_types: list of sub_types for endpoint looping; delfault = ['self']
#   bookmark_type: Data type for bookmark, integer or datetime

STREAMS = {
    'sites': {
        'key_properties': ['site_url'],
        'replication_method': 'FULL_TABLE',
        'path': 'sites/{}',
        'data_key': 'site_entry',
        'api_method': 'GET'
    },

    'sitemaps': {
        'key_properties': ['site_url', 'path', 'last_submitted'],
        'replication_method': 'FULL_TABLE',
        'path': 'sites/{}/sitemaps',
        'data_key': 'sitemap',
        'api_method': 'GET'
    },

    'performance_reports': {
        'key_properties': ['site_url', 'search_type', 'date', 'dimensions_hash_key'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['date'],
        'path': 'sites/{}/searchAnalytics/query',
        'data_key': 'rows',
        'api_method': 'POST',
        'bookmark_type': 'datetime',
        'pagination': 'body',
        'sub_types': ['web', 'image', 'video']
    }
}
