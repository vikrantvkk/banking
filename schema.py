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
create_loan_account_existing_schema = {
    'type': 'object',
    'properties': {
        'loanAmount': {'type': 'number'},
        'interestRate': {'type': 'number'},
        'loanStartDate': {'type': 'string', 'format': 'date'}
    },
    'required': ['loanAmount', 'interestRate', 'loanStartDate']
}
make_payment_to_loan_account_schema = {
    'type': 'object',
    'properties': {
        'paymentAmount': {'type': 'number'},
        'paymentDate': {'type': 'string', 'format': 'date'}
    },
    'required': ['paymentAmount', 'paymentDate']
}
