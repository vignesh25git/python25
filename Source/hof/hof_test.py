#higher order function

def gmail_method(email):
    return email+"@gmail.com"

def yahoo_method(email):
    return email+"@yahoo.com"

print(gmail_method("vicky"))

def generate_email(email,email_method):
    return email_method(email)

def email_builder(domain):
    def build_email(email):
        return email + "@" + domain + ".com"
    return build_email

print(generate_email("vicky",yahoo_method))

func = email_builder("gmail")

print(func("vicky1122"))
