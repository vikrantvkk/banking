"""
This is the main app which will run the flask REST service on given port and host.

This module will call account management service
"""
import json

from flask import Flask, request, make_response
from flask_expects_json import expects_json

from accounts_service import AccountsManager

banking_service = Flask(__name__)
accounts_service = None

create_loan_account_schema = {
    'type': 'object',
    'properties': {
        'firstName': {'type': 'string'},
        'lastName': {'type': 'string'},
        'emailId': {'type': 'string', "pattern": "[^@]+@[^@]+\.[^@]"},
        'contact': {'type': 'string'},
        'loanAmount': {'type': 'number'},
        'interestRate': {'type': 'number'},
        'loanStartDate': {'type': 'string', 'format': 'date'}
    },
    'required': ['firstName', 'lastName', 'emailId', 'loanAmount', 'interestRate', 'loanStartDate']
}

make_payment_to_loan_account_schema = {
    'type': 'object',
    'properties': {
        'paymentAmount': {'type': 'number'},
        'paymentDate': {'type': 'string', 'format': 'date'}
    },
    'required': ['paymentAmount', 'paymentDate']
}


@banking_service.route('/account/<account_id>/', methods=['GET'])
def get_loan_account_balance(account_id):
    """
    API to get loan details. Takes a date as an argument and returns the total balance as of that date.
    :param account_id:
    :return:
    """
    to_date = request.args.get('date')
    try:
        response_data = accounts_service.get_loan_balance(account_id, to_date)
    except KeyError:
        return make_response(json.dumps({'status': 'ERROR'}), 404)
    return make_response(json.dumps({'status': 'SUCCESS', 'data': response_data}), 200)


@banking_service.route('/account/', methods=['POST'])
@expects_json(create_loan_account_schema)
def create_loan_account():
    """
    Initiate loan: with arguments for initial amount, annual interest rate, and start date.
    :return:
    """
    request_data = request.data
    request_data = json.loads(request_data)
    response_data = accounts_service.create_account(request_data)
    return make_response(json.dumps({'status': 'SUCCESS', 'data': response_data}), 201)


@banking_service.route('/account/<account_id>/', methods=['PUT'])
def make_payment_to_loan_account(account_id):
    """
    Add payment: with arguments for amount and date.
    :param account_id:
    :return:
    """
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
