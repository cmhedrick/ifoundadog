import os
import sys
import argparse
from bottle import route, run, template, static_file, post, request, error
import api_helpers

# Get current location, set as current location, and append to path
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
sys.path.append(current_dir)

#Allows CSS, JS, and Images to be stored in the '/static/' directory and be
#rendered using paths like "/static/css/example.css".
@route('/static/<filename:path>')
def server_static(filename):
    """
    allows the static files to be found.
    :param filename:
    :return:
    """
    return static_file(filename, root=os.path.join(current_dir, "static"))

#'/' is the root of the site in most cases
@route('/')
def index():
    """
    renders home page
    :return:
    """
    return template('templates/index.tpl')

@post('/lookup')
def lookup():
    """
    performs the search for the dog license and returns it
    :return:
    """
    license_id = request.forms.get('inputLicense').upper()
    data = api_helpers.get_data()
    match = [r for r in data['result'] if license_id in r]
    return template('templates/result.tpl', result=match[0])

def get_port():
    description = 'Set port for the bottle server to run on.'
    parser = argparse.ArgumentParser(description)
    parser.add_argument(
        '-p',
        '--port',
        type=int,
        help="The port number the server will run on"
    )
    args = parser.parse_args()

    return args.port if args.port else 8080

@route('/keybase.txt')
def verify_keybase():
    """
    Allows for proper routing of Lets Encrypt if you're using ACME
    :param filename:
    :return:
    """
    return static_file('keybase.txt',
        root=os.path.join(current_dir, 'static')
    )

@route('/.well-known/acme-challenge/<filename:path>')
def verify_lets_encrypt(filename):
    """
    Allows for proper routing of Lets Encrypt if you're using ACME
    :param filename:
    :return:
    """
    return static_file(
        filename,
        root=os.path.join(current_dir, ".well-known/acme-challenge")
    )

# HTTP Error Handling Functions
@error(404)
def error404(error):
    return 'You\'re looking in the wrong place :P'

@error(500)
def error500(error):
    return 'Beep boop, no snoop for you dog.'

@error(505)
def error505(error):
    return 'How about you take a paws and go back to home?'


if __name__ == "__main__":
    run(host="0.0.0.0", port=get_port(), reloader='True', debug='True')
