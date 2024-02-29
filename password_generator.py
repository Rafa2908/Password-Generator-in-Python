import random
import string


password = []

pass_upper_letters = string.ascii_uppercase
pass_lower_letters = string.ascii_lowercase
pass_digits = string.digits
special_character = "!@#$%^&*<>?"

password.append(random.choice(pass_upper_letters))
password.append(random.choice(pass_lower_letters))
password.append(random.choice(pass_digits))
password.append(random.choice(special_character))


password_length = 10

while len(password) < password_length:
    password_generator = (
        pass_upper_letters + pass_lower_letters + pass_digits + special_character
    )
    password.append(random.choice(password_generator))


random.shuffle(password)

password = "".join(password)

print(f"Temporary random password: {password}")
