import datetime

from account import Account


class AccountsManager:
    def __init__(self):
        self.accounts_manager = dict()

    def create_account(self, user_data):
        """
        This function accepts user_data dictionary containing following attributes:
        "firstName": "Vikrant",
        "lastName": "Vishwakarma",
        "emailId": "vikrant.vishwakarma07@gmail.com",
        "contact": "9591297013",
        "loanAmount" : 100
        "interestRate": 7.3
        "loanStartDate": 2022-06-30
        :param user_data: dictionary
        :return: None
        """
        new_ac = Account(user_data["firstName"], user_data["lastName"], user_data["emailId"], user_data["contact"])
        new_ac.create_loan_account(user_data["loanAmount"], user_data["interestRate"],
                                   datetime.datetime.strptime(user_data["loanStartDate"], "%Y-%m-%d"))
        self.accounts_manager[str(new_ac.id)] = new_ac
        user_data["accountId"] = str(new_ac.id)
        return user_data

    def get_loan_balance(self, account_id, to_date):
        account_obj = self.accounts_manager[account_id]
        try:
            loan_bal = account_obj.get_loan_balance(datetime.datetime.strptime(to_date, "%Y-%m-%d"))
        except Exception as e:
            return {"message": str(e) + " on this account"}
        # {"principal": self.principal_balance, "interest_accumulated": self.interest_accumulated}
        if "principal" in loan_bal:
            return {
                "accountId": account_id,
                "principal": loan_bal["principal"],
                "interestAccumulated": loan_bal["interest_accumulated"],
                "balanceLoanAmount": float(format(loan_bal["principal"] + loan_bal["interest_accumulated"], ".2f"))
            }

    def add_payment_to_account(self, account_id, payment_details):
        account_obj = self.accounts_manager[account_id]
        payment_date = datetime.datetime.strptime(payment_details["paymentDate"], "%Y-%m-%d")
        try:
            loan_bal = account_obj.update_loan_account(payment_details["paymentAmount"], payment_date)
        except Exception as e:
            return e
        if "principal" in loan_bal:
            return {
                "accountId": account_id,
                "principal": loan_bal["principal"],
                "interest_accumulated": loan_bal["interest_accumulated"]
            }

    def create_account_existing(self, acc_id, user_data):
        """
        This function accepts user_data dictionary containing following attributes:
        "loanAmount" : 100
        "interestRate": 7.3
        "loanStartDate": 2022-06-30
        :param acc_id: string
        :param user_data: dictionary
        :return: None
        """
        existing_ac = self.accounts_manager[acc_id]
        existing_ac.create_loan_account(user_data["loanAmount"], user_data["interestRate"],
                                        datetime.datetime.strptime(user_data["loanStartDate"], "%Y-%m-%d"))
        resp_data = existing_ac.get_basic_info()
        resp_data["accountId"] = acc_id
        return resp_data
