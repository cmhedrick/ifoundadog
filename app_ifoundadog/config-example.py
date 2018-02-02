# Prefix for URL (shouldn't need to be changed)
API_URL_PREFIX = 'https://api.data.arlingtonva.us/api/v2/datastreams/'
# Suffix for URL (shouldn't need to be changed)
API_URL_SUFFIX = '/data.ajson/?auth_key='
# API Key obtained from https://data.arlingtonva.us/developers/
API_KEY = 'YOUR API KEY HERE'
# DATA SET NAME
DATASET = 'CURRE-DOG-LICEN'
# Complete Callable URL
API_URL = API_URL_PREFIX + DATASET + API_URL_SUFFIX + API_KEY