def password_strength(password):
    score=0

#declaring flags
    has_upper=False
    has_lower=False
    has_digit=False
    has_special=False
    has_repeat=False

    for char in password:

        if char.isupper() :
            has_upper=True

        if char.islower() :
            has_lower=True

        if char.isdigit() :
            has_digit=True

        if not char.isalpha() and not char.isdigit() :
            has_special=True

        for i in range(1,len(password)):
            if password[i]==password[i-1]:
                has_repeat=True
                break

        if len(password)>=8:
            score+=1

        if has_upper:
            score+=1

        if has_lower:
            score+=1

        if has_digit:
            score+=1

        if has_special:
            score+=1

        if score<=2:
            strength="Weak"

        elif score<=4:
            strength="Medium"

        else:
            strength="Strong"

        if has_repeat:
            if strength=="Strong":
                strength="Medium"
            elif strength=="Medium":
                strength="Weak"

        return strength


password=input("Enter your password :")
print(password_strength(password))
