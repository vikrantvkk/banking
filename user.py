class User:
    def __init__(self, f_name, l_name, email_id, contact_num):
        self.f_name = f_name
        self.l_name = l_name
        self.email_id = email_id
        self.contact_num = contact_num

    def get_basic_info(self):
        return dict({
            "first_name": self.f_name,
            "last_name": self.l_name,
            "email_id": self.email_id,
            "contact_number": self.contact_num
        }
        )