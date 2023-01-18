# Check if password is strong enough

# length is over 8
# has number
# has special digit


def is_password_strong(password):

    if type(password)!=str:
        raise ValueError("Password variable is not a string")

    if len(password) < 8:
        return False

    if not has_both_letters_and_numbers(password):
        return False

    if not has_special_character(password):
        return False

    return True

