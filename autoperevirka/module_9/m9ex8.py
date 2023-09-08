def get_emails(list_contacts):
    return list(map(lambda x: x["email"], list_contacts))