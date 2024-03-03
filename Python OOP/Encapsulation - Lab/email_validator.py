
class EmailValidator:

    def __init__(self, min_length: int, mails: list, domains: list) -> None:
        self.min_length = min_length
        self.mails = mails
        self.domains = domains
        
    def __is_name_valid(self, name):
        if len(name) >= self.min_length:
            return True
        return False 

    def __is_mail_valid(self, mail):
        if mail in self.mails:
            return True
        return False

    def __is_domain_valid(self, domain):
        if domain in self.domains:
            return True
        return False
    
    def validate(self,email):
        name = email.split("@")[0]
        mail = email.split("@")[1]
        mail, domain = mail.split(".")
        if self.__is_mail_valid(mail) and self.__is_domain_valid(domain) and self.__is_name_valid(name):
            return True
        return False


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
