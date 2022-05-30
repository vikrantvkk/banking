import uuid

from user import User


class LoanAccount(User):

    def __init__(self, f_name, l_name, email_id, contact_num):
        super().__init__(f_name, l_name, email_id, contact_num)
        self.id = uuid.uuid4()
        self.init_date = None
        self.init_interest_rate = None
        self.init_principal = None
        self.interest_accumulated = None
        self.principal_due = None
        self.last_payment_date = None

    def create_loan_account(self, principal, interest_rate, loan_start_date):
        self.init_principal = principal
        self.init_interest_rate = interest_rate
        self.init_date = loan_start_date
        self.interest_accumulated = 0
        self.principal_due = self.init_principal
        self.last_payment_date = self.init_date

    def get_loan_balance(self, date):
        if self.last_payment_date > date:
            raise ("Requested date cannot be greater than last requested date {}".format(self.last_payment_date))
        duration = date - self.last_payment_date
        interest_on_duration = self.principal_due * self.init_interest_rate / 100 / 365 * duration.days
        return {
            "principal": float(format(self.principal_due, ".2f")),
            "interest_accumulated": float(format(self.interest_accumulated + interest_on_duration, ".2f"))
        }

    def add_payment(self, payment_amount, payment_date):
        """
        Adds payment to the loan amount by updating the interest accumulated and principal due on the account
        case1: payment amount exceeds principal plus interest accumulated (then raise exception)
        case2: payment amount is less than interest accumulated (then update only interest accumulated)
        case3: payment amount exceeds interest accumulated (then update both interest accumulated and principal due)

        :param payment_amount:
        :param payment_date:
        :return:
        """
        loan_balance = self.get_loan_balance(payment_date)
        # case1
        if payment_amount > loan_balance["interest_accumulated"] + loan_balance["principal"]:
            raise ("Payment amount exceeds total balance amount {}".
                   format(loan_balance["interest_accumulated"] + loan_balance["principal"]))
        # case3
        interest_due = loan_balance["interest_accumulated"] - payment_amount
        if interest_due < 0:
            self.interest_accumulated = 0
            self.principal_due += float(format(interest_due, ".2f"))
        # case2
        else:
            self.interest_accumulated = float(format(interest_due, ".2f"))
        self.last_payment_date = payment_date
