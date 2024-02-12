import re # Import the regular expression module

def validate_email(email):
    # Regular expression pattern for basic email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
# The regular expression pattern is a string that represents the pattern of the email address.