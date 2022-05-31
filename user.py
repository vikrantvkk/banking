class User:
    def __init__(self, f_name, l_name, email_id, contact_num):
        self.f_name = f_name
        self.l_name = l_name
        self.email_id = email_id
        self.contact_num = contact_num

    def get_basic_info(self):
        return dict({
            "firstName": self.f_name,
            "lastName": self.l_name,
            "emailId": self.email_id,
            "contact": self.contact_num
        }
        )
