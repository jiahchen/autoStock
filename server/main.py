import shioaji as sj
import sys
import logging
import json
import base64
import logging_utility
from flask import Flask, request, jsonify, abort, make_response, g

APP = Flask(__name__)
logging_utility.basicConfig(
    filename='server.log',
    format='%(levelname)-8s %(asctime)s %(name)s:%(lineno)d| %(message)s',
    level=logging.INFO,
)

sj_api = sj.Shioaji(backend='http', simulation=False)

@APP.route('/accountinfo/<auth_token>', methods=['GET'])
def get_server_info(auth_token=None):

    if auth_token is None:
        logging.error('Missing Auth Token')
        abort(make_response('Missing Auth Token', 404))

    person_id, person_pass = auth_decode(auth_token)
    sj_api.login(person_id=person_id, passwd=person_pass)
    accounts = sj_api.list_accounts()

    account_list = []
    for acc in accounts:
        account_list.append(acc.__dict__)

    data = {
        'Account List': account_list
    }

    logging.info('Get account information')
    return jsonify(data)

def auth_decode(auth_token):
    decodedBytes = base64.urlsafe_b64decode(auth_token)
    decodedStr = str(decodedBytes, "utf-8")
    person_id = decodedStr.split('\n')[0]
    person_pass = decodedStr.split('\n')[1]
    return person_id, person_pass

def main():
    logging.info('Auto Stock Server is starting')
    APP.run(host='0.0.0.0', port=3000, threaded=False)
    logging.info('Server is closing')
    sys.exit(0)

if __name__ == '__main__':
    main()

