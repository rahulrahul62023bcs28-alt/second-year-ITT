import re

def is_valid_gmail(email):
    banned_words = [
        "king", "boss", "cool", "official", "real",
        "legend", "hacker", "admin", "support"
    ]

    # Must end with @gmail.com
    if not email.endswith("@gmail.com"):
        return False, "Email must end with @gmail.com"

    username = email[:-10]  # remove '@gmail.com'

    # Length check
    if len(username) < 6 or len(username) > 30:
        return False, "Username length must be between 6 and 30 characters"

    # Only lowercase letters, numbers, dot
    if not re.fullmatch(r"[a-z0-9.]+", username):
        return False, "Only lowercase letters, numbers, and and dots allowed"

    # Must start and end with a letter
    if not (username[0].isalpha() and username[-1].isalpha()):
        return False, "Username must start and end with a letter"

    # No consecutive dots
    if ".." in username:
        return False, "Consecutive dots are not allowed"

    # Numbers only allowed at the end
    if re.search(r"[0-9]+[a-z]", username):
        return False, "Numbers must appear only at the end"

    # Banned words check
    for word in banned_words:
        if word in username:
            return False, f"Username contains banned word: '{word}'"

    return True, "Valid professional Gmail ID"


# Main Program
email = input("Enter a Gmail ID: ").strip()

valid, message = is_valid_gmail(email)

if valid:
   print("ACCEPTED:", message)
else:
   print("REJECTED:", message)
