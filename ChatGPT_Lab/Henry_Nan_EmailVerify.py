def validate_email(email):
    if '@' in email: # Check if '@' is in the email
        if '.' in email: # Check if '.' is in the email
            if email.count('@') == 1 and email.count('.') >= 1:
                return True # If the email has only one '@' and at least one '.'
            else:
                return False
        else:
            return False
    else:
        return False