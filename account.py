import uuid

from loan import LoanAccount
from user import User


class Account(User):

    def __init__(self, f_name, l_name, email_id, contact_num):
        super().__init__(f_name, l_name, email_id, contact_num)
        self.id = uuid.uuid4()
        self.loan_account = None

    def create_loan_account(self, principal, interest_rate, loan_start_date):
        self.loan_account = LoanAccount(self.f_name, self.l_name, self.email_id, self.contact_num)
        self.loan_account.create_loan_account(principal, interest_rate, loan_start_date)

    def get_loan_balance(self, date):
        if self.loan_account is None:
            raise "No active Loan"
        return self.loan_account.get_loan_balance(date)

    def update_loan_account(self, payment_amount, payment_date):
        self.loan_account.add_payment(payment_amount, payment_date)
        return self.get_loan_balance(payment_date)
