import json
import urllib.parse
import urllib.request
import config

def request(url):
    """
    Replaces default Python Header to avoid being tagged as bot/scraper :)
    :param url: str Object | ex: 'https://example.com'
    :return: HTTPSResponse Object
    """
    return urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

def clean_json_response(dirty_json):
    '''
    Takes the HTTPResponse that is actually JSON and makes it to a string
    so that it can be decoded by json.loads()
    :param dirty_json: HTTPResponse Object
    :return: json string
    '''
    # set encoding
    encoding = dirty_json.info().get_content_charset('utf-8')
    return dirty_json.read().decode(encoding)

def get_data():
    '''
    Prints a list of posts and IDs in format 'ID: title: author ID'
    :return: list
    '''
    try:
        clean_json = clean_json_response(
            urllib.request.urlopen(request(config.API_URL))
        )
        data = json.loads(clean_json)
        return data

    except urllib.error.HTTPError as e:
        print('FAILURE: ' + e.code)

    except urllib.error.URLError as e:
        print('FAILURE: ' + e.reason.strerror)