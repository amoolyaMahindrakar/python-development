def email_validator(email):

    allowed_characters=True

    for char in email:
        if not (char.isalpha() or char.isdigit() or char=="_.@"):
            allowed_characters=False

    if(email.count("@")==1
       and not email.startswith("@")
       and not email.endswith("@")
       and email.endswith((".com",".in"))
       and " " not in email
       and allowed_characters):
        return "Valid Email"
    
    else:
        return "Invalid Email"

email=input("Enter your email:")
print(email_validator(email))

