import json

from flask import Flask, request, make_response

from accounts_service import AccountsManager

banking_service = Flask(__name__)
accounts_service = None


@banking_service.route('/account/<account_id>/', methods=['GET'])
def get_loan_account_balance(account_id):
    to_date = request.args.get('date')
    try:
        response_data = accounts_service.get_loan_balance(account_id, to_date)
    except KeyError:
        return make_response(json.dumps({'status': 'ERROR'}), 404)
    return make_response(json.dumps({'status': 'SUCCESS', 'data': response_data}), 200)


@banking_service.route('/account/', methods=['POST'])
def create_loan_account():
    request_data = request.data
    request_data = json.loads(request_data)
    response_data = accounts_service.create_account(request_data)
    return make_response(json.dumps({'status': 'SUCCESS', 'data': response_data}), 201)


@banking_service.route('/account/<account_id>/', methods=['PUT'])
def make_payment_to_loan_account(account_id):
    request_data = request.data
    request_data = json.loads(request_data)
    try:
        response_data = accounts_service.add_payment_to_account(account_id, request_data)
    except KeyError:
        return make_response(json.dumps({'status': 'ERROR'}), 404)
    return make_response(json.dumps({'status': 'SUCCESS', 'data': response_data}), 201)


if __name__ == '__main__':
    accounts_service = AccountsManager()
    banking_service.run(host="0.0.0.0", port=5000, debug=True)
