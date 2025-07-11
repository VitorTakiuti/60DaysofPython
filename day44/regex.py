import re

def validate_email(email):
    """
    Function validates emails
    """
    
    # Validate in regexr.com
    regex = r'ˆ[a-zA-z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-z0-9_.]+$'
    if re.match(regex, email):
        print(f"{email} - Valid email")
    else:
        print(f"{email} -Invalid email")
        
# ˆ indicates the beggining of the text
# [a-zA-z0-9_.+-]
# @ needs to be in a email
# +\.
# $ end the text

validate_email("blablabla@business.com")
validate_email("blablablablabla")
