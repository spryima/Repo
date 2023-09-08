def format_phone_number(func):
    def inner(phone):
        result = func(phone)
        new_phone = "".join(["+38", result.removeprefix("38")])
        return new_phone
    return inner
        
        


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone